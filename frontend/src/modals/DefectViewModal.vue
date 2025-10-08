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
    isAdmin: {
        type: Boolean,
        default: false,
    },
});

const emit = defineEmits(["close", "statusChange"]);

const defectData = ref({
    id: 0,
    title: "",
    status: "Новый",
    deadline: "",
    author: "",
    responsible: "",
    description: "",
    tag: "",
    image: "",
});

function loadDefectData() {
    const found = props.defects.find((d) => d.id === props.id);
    if (found) {
        defectData.value = { ...found };
    } else {
        defectData.value = {
            id: 0,
            title: "Неизвестный дефект",
            status: "Новый",
            deadline: "",
            author: "",
            responsible: "",
            description: "Информация о дефекте не найдена.",
            tag: "",
            image: "https://via.placeholder.com/400x300?text=Нет+данных",
        };
    }
}

onMounted(loadDefectData);
watch(() => props.id, loadDefectData);

function updateStatus() {
    emit("statusChange", { id: props.id, status: defectData.value.status });
}
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
                            v-model="defectData.status"
                            @change="updateStatus"
                            :disabled="!isAdmin"
                        >
                            <option value="Новый">Новый</option>
                            <option value="В работе">В работе</option>
                            <option value="Завершён">Завершён</option>
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
                            v-model="defectData.responsible"
                            :disabled="!isAdmin"
                        >
                            <option
                                v-for="employee in employees"
                                :key="employee"
                                :value="employee"
                            >
                                {{ employee }}
                            </option>
                        </select>
                    </div>

                    <div class="tag-block">
                        <label>Тег:</label>
                        <span class="tag-text">{{ defectData.tag }}</span>
                    </div>

                    <div class="author-block">
                        <label>Зарегистрировал:</label>
                        <span class="author-text">{{ defectData.author }}</span>
                    </div>

                    <p class="description">{{ defectData.description }}</p>
                </div>

                <div class="photo-section">
                    <img :src="defectData.image" alt="Фото дефекта" />
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
