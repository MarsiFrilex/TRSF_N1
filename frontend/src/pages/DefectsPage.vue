<script setup>
import { onMounted, ref, computed, watch } from "vue";
import { useRoute } from "vue-router";
import Header from "@/components/Header.vue";
import Footer from "@/components/Footer.vue";
import DefectAddModal from "@/modals/DefectAddModal.vue";
import DefectViewModal from "@/modals/DefectViewModal.vue";
import CreateAccountModal from "@/modals/CreateAccountModal.vue";
import {
    downloadExcel,
    getDefectsByObjectId, getRoles, getStatuses, getUsers,
    registerDefect, registerUser, updateDefect,
    uploadImage,
} from "@/api/index.js";

const props = defineProps({
    id: Number,
    role_id: Number,
    user_id: Number,
});
const isAdmin = (props.role_id === 2 || props.role_id === 3);

const route = useRoute();
const objectId = route.params.id;

const defects = ref([]);
const selectedId = ref(null);
const statuses = ref([]);
const users = ref([]);
const roles = ref([]);

// состояния модальных окон
const showAdd = ref(false);
const showView = ref(false);
const showAccount = ref(false);

// сортировка
const sortField = ref(null);
const sortOrder = ref("asc");

async function loadStatuses() {
    statuses.value = await getStatuses();
}

function toggleSort(field) {
    if (sortField.value === field) {
        sortOrder.value = sortOrder.value === "asc" ? "desc" : "asc";
    } else {
        sortField.value = field;
        sortOrder.value = "asc";
    }
}

function resetSort() {
    sortField.value = null;
    sortOrder.value = "asc";
}

const sortedDefects = computed(() => {
    if (!sortField.value) return defects.value;
    const list = [...defects.value];
    list.sort((a, b) => {
        const getValue = (d) =>
            sortField.value === "tag"
                ? (d.tag?.title || d.tag || "")
                : (d.status || "");
        const valA = getValue(a).toString().toLowerCase();
        const valB = getValue(b).toString().toLowerCase();
        if (valA < valB) return sortOrder.value === "asc" ? -1 : 1;
        if (valA > valB) return sortOrder.value === "asc" ? 1 : -1;
        return 0;
    });
    return list;
});

function openAddModal() {
    showAdd.value = true;
}

function openViewModal(id) {
    selectedId.value = id;
    showView.value = true;
}

function openAccountModal() {
    showAccount.value = true;
}

function closeAddModal() {
    showAdd.value = false;
}

function closeViewModal() {
    showView.value = false;
}

function closeAccountModal() {
    showAccount.value = false;
}

async function handleSaveDefect(data) {
    const fileUrl = await uploadImage(data.photo);

    await registerDefect(
        data.title,
        data.description,
        fileUrl.strict_url,
        data.tag,
        objectId,
        props.user_id,
    );

    closeAddModal();
    await loadDefects();
}

async function handleDefectChange(data) {
    const defect = defects.value.find((d) => d.id === data.id);
    if (defect) {
        defect.status = data.status.title;
        defect.deadline = data.deadline;
        defect.engineer = data.engineer_id;

        await updateDefect(data.id, data.status.id, data.deadline, data.engineer_id);
    }
}

async function handleAccountSave(data) {
    await registerUser(data.name, data.email, data.password, data.role_id);
    await loadUsers();
    closeAccountModal();
}

async function loadDefects() {
    defects.value = await getDefectsByObjectId(objectId);
}

async function loadUsers() {
    users.value = await getUsers();
}

async function loadRoles() {
    roles.value = await getRoles(props.role_id);
}

async function downloadStats() {
    try {
        const response = await downloadExcel(objectId);

        // Создаём blob-объект
        const blob = new Blob([response], {
            type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        });

        // Делаем временный URL
        const url = window.URL.createObjectURL(blob);

        // Создаём ссылку <a> и триггерим клик
        const link = document.createElement("a");
        link.href = url;
        link.setAttribute("download", "report.xlsx"); // имя сохраняемого файла
        document.body.appendChild(link);
        link.click();

        // Чистим
        link.remove();
        window.URL.revokeObjectURL(url);
    } catch (error) {
        console.error("Ошибка при скачивании файла:", error);
    }
}

onMounted(async () => {
    await loadDefects();
    await loadStatuses();
    await loadUsers();

    if (isAdmin) {
        await loadRoles();
    }
});
</script>

<template>
    <div class="app">
        <Header />

        <main class="main-content">
            <div class="main">
                <div class="container">
                    <!-- Левая колонка -->
                    <div class="content-column">
                        <!-- Панель сортировки -->
                        <div class="sort-controls">
                            <label>Сортировать по:</label>

                            <button
                                class="sort-btn"
                                :class="{ active: sortField === 'tag' }"
                                @click="toggleSort('tag')"
                            >
                                Тег
                                <span v-if="sortField === 'tag'">
                                    {{ sortOrder === 'asc' ? '↑' : '↓' }}
                                </span>
                            </button>

                            <button
                                class="sort-btn"
                                :class="{ active: sortField === 'status' }"
                                @click="toggleSort('status')"
                            >
                                Статус
                                <span v-if="sortField === 'status'">
                                    {{ sortOrder === 'asc' ? '↑' : '↓' }}
                                </span>
                            </button>

                            <button
                                class="sort-btn reset"
                                @click="resetSort"
                                :disabled="!sortField"
                            >
                                Сбросить
                            </button>
                        </div>

                        <!-- Модальные окна -->
                        <DefectAddModal
                            :show="showAdd"
                            @cancel="closeAddModal"
                            @save="handleSaveDefect"
                        />

                        <DefectViewModal
                            v-if="showView"
                            :show="showView"
                            :id="selectedId"
                            :defects="defects"
                            :statuses="statuses"
                            :employees="users"
                            :isAdmin="isAdmin"
                            @close="closeViewModal"
                            @change="handleDefectChange"
                        />

                        <CreateAccountModal
                            :show="showAccount"
                            :roles="roles"
                            @cancel="closeAccountModal"
                            @save="handleAccountSave"
                        />

                        <!-- Список дефектов -->
                        <div
                            class="defect-card"
                            v-for="defect in sortedDefects"
                            :key="defect.id"
                            @click="openViewModal(defect.id)"
                        >
                            <div class="defect-header">
                                <span class="defect-title">{{ defect.title }}</span>
                                <span class="defect-tag">
                                    {{ defect.tag?.title || defect.tag }}
                                </span>
                                <span
                                    class="defect-status"
                                >
                                    {{ defect.status }}
                                </span>
                            </div>

                            <div class="defect-description">
                                {{ defect.description }}
                            </div>
                        </div>
                    </div>

                    <!-- Правая колонка -->
                    <div class="buttons-column">
                        <button @click="openAddModal" class="action-btn">
                            Добавить
                        </button>
                        <button v-if="isAdmin" @click="downloadStats" class="action-btn">
                            Скачать отчёт
                        </button>
                        <button v-if="isAdmin" @click="openAccountModal" class="action-btn">
                            Создать аккаунт
                        </button>
                    </div>
                </div>
            </div>
        </main>

        <Footer />
    </div>
</template>

<style scoped>
.app {
    min-height: 100vh;
    display: flex;
    flex-direction: column;
}

.main-content {
    flex: 1;
    display: flex;
    align-items: center;
    justify-content: center;
}

.main {
    display: flex;
    align-items: center;
    justify-content: center;
    background: url("@/assets/background.jpg") no-repeat center center;
    background-size: cover;
    width: 100%;
    min-height: calc(100vh - 160px);
    position: relative;
}

.main::before {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: rgba(0, 0, 0, 0.3);
    z-index: 1;
}

.container {
    display: flex;
    width: 90%;
    height: 70%;
    max-width: 1200px;
    position: relative;
    z-index: 2;
    flex-direction: row;
}

/* Левая колонка */
.content-column {
    flex: 1;
    padding-top: 20px;
    max-height: 70vh;
    overflow-y: auto;
}

/* Панель сортировки */
.sort-controls {
    display: flex;
    align-items: center;
    margin-bottom: 20px;
    gap: 10px;
}
.sort-controls label {
    font-size: 18px;
    font-weight: bold;
}
.sort-btn {
    padding: 8px 14px;
    border-radius: 6px;
    border: 1px solid #aaa;
    background: #fff;
    cursor: pointer;
    font-size: 15px;
    transition: all 0.2s;
}
.sort-btn:hover {
    background: #f2f2f2;
}
.sort-btn.active {
    background: #ddd;
    font-weight: 600;
}
.sort-btn.reset {
    background: #f7f7f7;
    border: 1px solid #bbb;
}
.sort-btn.reset:disabled {
    opacity: 0.6;
    cursor: not-allowed;
}

/* Карточки дефектов */
.defect-card {
    background: #eaeaea;
    padding: 14px;
    font-family: Inter, system-ui;
    margin-bottom: 20px;
    border-radius: 10px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    cursor: pointer;
    transition: background 0.3s;
}
.defect-card:hover {
    background: #dcdcdc;
}
.defect-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-size: 18px;
    margin-bottom: 8px;
    gap: 10px;
}
.defect-title {
    font-weight: bold;
    flex: 1;
}
.defect-tag {
    background: #4b5fc1;
    color: #fff;
    padding: 3px 10px;
    border-radius: 6px;
    font-size: 14px;
    white-space: nowrap;
}
.defect-status {
    font-style: italic;
    font-weight: 600;
    font-size: 15px;
}
.defect-status.open {
    color: #e53935;
}
.defect-status.closed {
    color: #2e7d32;
}
.defect-status.pending {
    color: #f9a825;
}
.defect-description {
    font-size: 16px;
    color: #222;
}

/* Правая колонка */
.buttons-column {
    width: 180px;
    padding-left: 20px;
    padding-top: 20px;
    display: flex;
    flex-direction: column;
}
.action-btn {
    padding: 14px 18px;
    margin-bottom: 20px;
    font-size: 16px;
    border: none;
    border-radius: 6px;
    background: #eaeaea;
    cursor: pointer;
    transition: background 0.3s;
}
.action-btn:hover {
    background: #ccc;
}

/* Адаптивность */
@media (max-width: 768px) {
    .container {
        flex-direction: column;
        height: auto;
    }
    .buttons-column {
        width: 100%;
        padding-left: 0;
        flex-direction: row;
        justify-content: space-around;
        margin-top: 20px;
    }
    .action-btn {
        flex: 1;
        margin-left: 5px;
    }
}
</style>
