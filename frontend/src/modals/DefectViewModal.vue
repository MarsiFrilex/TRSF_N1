<script setup>
import { ref, watch, onMounted } from "vue";

const props = defineProps({
    show: Boolean,
    id: Number,
    defects: {
        type: Array,
        required: true,
    },
    employees: {
        type: Array,
        required: true,
    },
    statuses: {
        type: Array,
        required: true,
    },
    isAdmin: {
        type: Boolean,
        default: false,
    },
});

const emit = defineEmits(["close", "change"]);

const defectData = ref({
    id: 0,
    title: "",
    description: "",
    status_id: null,
    tag: "",
    deadline: "",
    registrator: "",
    engineer: null, // теперь храним id сотрудника
    photo_url: "",
});

// helper: попытаться извлечь status_id из found.status
function extractStatusId(foundStatus) {
    if (!foundStatus) return null;
    if (typeof foundStatus === "number") return foundStatus;
    if (typeof foundStatus === "object" && "id" in foundStatus) return foundStatus.id;
    if (typeof foundStatus === "string") {
        const match = props.statuses?.find((s) => s.title === foundStatus);
        return match ? match.id : null;
    }
    return null;
}

// helper: попытаться извлечь id инженера
function extractEngineerId(engineerValue) {
    if (!engineerValue) return null;
    // если уже id
    if (typeof engineerValue === "number") return engineerValue;

    // если это объект пользователя
    if (typeof engineerValue === "object" && "id" in engineerValue) {
        return engineerValue.id;
    }

    // если строка — ищем по имени
    if (typeof engineerValue === "string") {
        const found = props.employees?.find(
            (u) => u.user_name === engineerValue
        );
        return found ? found.id : null;
    }

    return null;
}

function loadDefectData() {
    if (props.id == null) {
        defectData.value = {
            id: 0, title: "", description: "", status_id: null, tag: "",
            deadline: "", registrator: "", engineer: null, photo_url: ""
        };
        return;
    }

    const found = props.defects.find((d) => d.id === props.id);
    if (!found) {
        defectData.value = {
            id: 0, title: "", description: "", status_id: null, tag: "",
            deadline: "", registrator: "", engineer: null, photo_url: ""
        };
        return;
    }

    // Заполняем данные
    defectData.value.id = found.id;
    defectData.value.title = found.title ?? "";
    defectData.value.description = found.description ?? "";
    defectData.value.tag = found.tag ?? "";
    defectData.value.deadline = found.deadline ?? "";
    defectData.value.registrator = found.registrator ?? "";
    defectData.value.photo_url = found.photo_url ?? "";

    // Определяем статус и инженера
    defectData.value.status_id = extractStatusId(found.status);
    defectData.value.engineer = extractEngineerId(found.engineer);
}

// следим за изменением списка статусов или сотрудников
watch(
    [() => props.statuses, () => props.employees],
    () => {
        if (props.id != null) {
            loadDefectData();
        }
    },
    { immediate: true }
);

// следим за сменой выбранного дефекта
watch(
    () => props.id,
    () => loadDefectData(),
    { immediate: true }
);

// при изменениях отправляем событие в родителя
watch(
    () => ({
        status_id: defectData.value.status_id,
        deadline: defectData.value.deadline,
        engineer: defectData.value.engineer,
    }),
    (newValues) => {
        const statusObj = props.statuses?.find(
            (s) => s.id === newValues.status_id
        ) ?? null;

        const engineerObj = props.employees?.find(
            (e) => e.id === newValues.engineer
        ) ?? null;

        emit("change", {
            id: props.id,
            status_id: newValues.status_id,
            status: statusObj,
            deadline: newValues.deadline,
            engineer_id: newValues.engineer,
            engineer: engineerObj?.user_name ?? "",
        });
    },
    { deep: true }
);

onMounted(loadDefectData);
</script>

<template>
    <div class="modal-overlay" v-if="show">
        <div class="modal-window">
            <h2>{{ defectData.title }}</h2>

            <div class="modal-content">
                <div class="info-section">
                    <div class="status-block">
                        <label>Статус:</label>
                        <select
                            v-model="defectData.status_id"
                            :disabled="!isAdmin"
                        >
                            <option
                                v-for="status in props.statuses"
                                :key="status.id"
                                :value="status.id"
                            >
                                {{ status.title }}
                            </option>
                        </select>
                    </div>

                    <div class="deadline-block">
                        <label>Дедлайн:</label>
                        <input
                            type="date"
                            v-model="defectData.deadline"
                            :disabled="!isAdmin"
                        />
                    </div>

                    <div class="responsible-block">
                        <label>Ответственный:</label>
                        <select
                            v-model="defectData.engineer"
                            :disabled="!isAdmin"
                        >
                            <option
                                v-for="user in employees"
                                :key="user.id"
                                :value="user.id"
                            >
                                {{ user.user_name }}
                            </option>
                        </select>
                    </div>

                    <div class="tag-block">
                        <label>Тег:</label>
                        <span class="tag-text">{{ defectData.tag }}</span>
                    </div>

                    <div class="author-block">
                        <label>Зарегистрировал:</label>
                        <span class="author-text">{{ defectData.registrator }}</span>
                    </div>

                    <p class="description">
                        {{ defectData.description ? `Описание: ${defectData.description}` : '' }}
                    </p>
                </div>

                <div class="photo-section">
                    <img :src="defectData.photo_url" alt="Фото дефекта" />
                </div>
            </div>

            <div class="modal-buttons">
                <button @click="$emit('close')">OK</button>
            </div>
        </div>
    </div>
</template>

<style scoped>
.modal-overlay {
    position: fixed;
    inset: 0;
    background: rgba(0, 0, 0, 0.5);
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: 1000;
}

.modal-window {
    background: #532a2b;
    color: #fff;
    border-radius: 10px;
    padding: 30px;
    width: 800px;
    display: flex;
    flex-direction: column;
    gap: 20px;
    font-family: "Segoe UI", sans-serif;
}

.modal-window h2 {
    text-align: center;
    font-size: 28px;
    margin-bottom: 10px;
}

.modal-content {
    display: flex;
    justify-content: space-between;
    gap: 20px;
}

.info-section {
    flex: 1;
    display: flex;
    flex-direction: column;
    gap: 10px;
    font-size: 18px;
}

.status-block,
.deadline-block,
.responsible-block,
.tag-block,
.author-block {
    display: flex;
    flex-direction: column;
    gap: 5px;
}

.status-block select,
.deadline-block input,
.responsible-block select {
    background: #eee;
    color: #000;
    border: none;
    border-radius: 5px;
    padding: 5px 8px;
    font-size: 16px;
    width: fit-content;
}

.tag-text,
.author-text {
    background: #3e2021;
    padding: 6px 10px;
    border-radius: 6px;
    width: fit-content;
    color: #fff;
}

.description {
    margin-top: 10px;
    color: #ddd;
    line-height: 1.4;
}

.photo-section {
    flex: 1;
    display: flex;
    align-items: center;
    justify-content: center;
    background: #3e2021;
    border-radius: 8px;
    overflow: hidden;
}

.photo-section img {
    width: 100%;
    height: auto;
    border-radius: 8px;
}

.modal-buttons {
    display: flex;
    justify-content: flex-end;
}

.modal-buttons button {
    background: #eee;
    color: #000;
    border: none;
    padding: 10px 25px;
    font-size: 16px;
    border-radius: 6px;
    cursor: pointer;
    transition: background 0.2s ease;
}

.modal-buttons button:hover {
    background: #ddd;
}
</style>
