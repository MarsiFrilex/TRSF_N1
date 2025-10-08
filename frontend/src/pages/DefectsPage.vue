<script setup>
import { ref } from "vue";
import { useRoute } from "vue-router";
import Header from "@/components/Header.vue";
import Footer from "@/components/Footer.vue";
import DefectAddModal from "@/modals/DefectAddModal.vue";
import DefectViewModal from "@/modals/DefectViewModal.vue";
import CreateAccountModal from "@/modals/CreateAccountModal.vue";

const defects = [
    { id: 1, title: "Трещина в плитке", status: "В работе", description: "Описание: длинное описание дефекта..." },
    { id: 2, title: "Неровность стены", status: "Новый", description: "Описание: требуется штукатурка..." },
    { id: 3, title: "Протечка", status: "Завершён", description: "Описание: устранено, но нужно наблюдать..." },
];

const route = useRoute();
const projectId = route.params.id;

// состояния модальных окон
const showAdd = ref(false);
const showView = ref(false);
const showAccount = ref(false);

// выбранный id дефекта
const selectedId = ref(null);

// открытие разных модалок
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

// закрытие
function closeAddModal() {
    showAdd.value = false;
}

function closeViewModal() {
    showView.value = false;
}

function closeAccountModal() {
    showAccount.value = false;
}

// сохранение
function handleSaveDefect(data) {
    console.log("Сохранён новый дефект:", data);
    closeAddModal();
}

function handleStatusChange({ id, status }) {
    const defect = defects.find((d) => d.id === id);
    if (defect) defect.status = status;
    console.log("Статус изменён:", id, status);
}

function handleAccountSave(data) {
    console.log("Создан аккаунт:", data);
    closeAccountModal();
}

const isAdmin = true;
</script>

<template>
    <div class="app">
        <Header />

        <main class="main-content">
            <div class="main">
                <div class="container">
                    <!-- Левая колонка -->
                    <div class="content-column">
                        <!-- Фильтры -->
                        <div class="filters">
                            <label>Фильтры:</label>
                            <button class="filter-btn">Проект</button>
                            <button class="filter-btn">Статус</button>
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
                            @close="closeViewModal"
                            @statusChange="handleStatusChange"
                        />

                        <CreateAccountModal
                            :show="showAccount"
                            @cancel="closeAccountModal"
                            @save="handleAccountSave"
                        />

                        <!-- Список дефектов -->
                        <div
                            class="defect-card"
                            v-for="defect in defects"
                            :key="defect.id"
                            @click="openViewModal(defect.id)"
                        >
                            <div class="defect-header">
                                <span class="defect-title">{{ defect.title }}</span>
                                <span class="defect-status">Статус: {{ defect.status }}</span>
                            </div>
                            <div class="defect-description">
                                {{ defect.description }}
                            </div>
                        </div>
                    </div>

                    <!-- Правая колонка -->
                    <div v-if="isAdmin" class="buttons-column">
                        <button @click="openAddModal" class="action-btn">Добавить</button>
                        <button class="action-btn">Скачать отчёт</button>
                        <button @click="openAccountModal" class="action-btn">Создать аккаунт</button>
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
    background: url('@/assets/background.jpg') no-repeat center center;
    background-size: cover;
    width: 100%;
    min-height: calc(100vh - 160px);
    position: relative;
}

.main::before {
    content: '';
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

/* Фильтры */
.filters {
    display: flex;
    align-items: center;
    margin-bottom: 20px;
}
.filters label {
    margin-right: 10px;
    font-size: 18px;
    font-weight: bold;
}
.filter-btn {
    margin-right: 10px;
    padding: 8px 14px;
    border-radius: 6px;
    border: 1px solid #aaa;
    background: #fff;
    cursor: pointer;
}

/* Карточки дефектов */
.defect-card {
    background: #EAEAEA;
    padding: 14px;
    font-family: Inter, system-ui;
    margin-bottom: 20px;
    border-radius: 10px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    cursor: pointer;
    transition: background 0.3s;
}
.defect-card:hover {
    background: #CCC;
}
.defect-header {
    display: flex;
    justify-content: space-between;
    font-size: 18px;
    margin-bottom: 8px;
}
.defect-title {
    font-weight: bold;
}
.defect-status {
    font-style: italic;
}
.defect-description {
    font-size: 16px;
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
    background: #EAEAEA;
    cursor: pointer;
    transition: background 0.3s;
}
.action-btn:hover {
    background: #CCC;
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
