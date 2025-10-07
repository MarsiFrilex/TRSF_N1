<template>
    <div class="modal-overlay" v-if="show">
        <div class="modal-window">
            <h2>{{ defectData.title }}</h2>

            <div class="modal-content">
                <div class="info-section">
                    <div class="status-block">
                        <label>Статус:</label>
                        <select v-model="defectData.status" @change="updateStatus">
                            <option value="Новый">Новый</option>
                            <option value="В работе">В работе</option>
                            <option value="Завершён">Завершён</option>
                        </select>
                    </div>

                    <p><strong>До {{ defectData.deadline }}</strong></p>
                    <p>{{ defectData.author }}</p>
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

<script setup>
import { ref, watch, onMounted } from "vue";

const props = defineProps({
    show: Boolean,
    id: Number,
});
const emit = defineEmits(["close", "statusChange"]);

const DEFECTS = [
    {
        id: 1,
        title: "Трещина в плитке",
        status: "В работе",
        deadline: "31.12.2025",
        author: "Василий Петрович",
        description:
            "Очень длинное описание проблемы, которая изображена на фотографии.",
        image: "https://via.placeholder.com/400x300?text=Трещина+в+плитке",
    },
    {
        id: 2,
        title: "Неровность стены",
        status: "Новый",
        deadline: "20.11.2025",
        author: "Мария Ивановна",
        description: "Требуется штукатурка и выравнивание стены.",
        image: "https://via.placeholder.com/400x300?text=Неровность+стены",
    },
    {
        id: 3,
        title: "Протечка",
        status: "Завершён",
        deadline: "05.09.2025",
        author: "Иван Сергеевич",
        description: "Протечка устранена, требуется контроль состояния.",
        image: "https://via.placeholder.com/400x300?text=Протечка",
    },
];

const DEFAULT_DEFECT = {
    id: 0,
    title: "Неизвестный дефект",
    status: "Новый",
    deadline: "-",
    author: "Неизвестно",
    description: "Информация о дефекте не найдена.",
    image: "https://via.placeholder.com/400x300?text=Нет+данных",
};

const defectData = ref({ ...DEFAULT_DEFECT });

function loadDefectData() {
    const found = DEFECTS.find((d) => d.id === props.id);
    defectData.value = found ? { ...found } : { ...DEFAULT_DEFECT };
}

onMounted(loadDefectData);
watch(() => props.id, loadDefectData);

function updateStatus() {
    emit("statusChange", { id: props.id, status: defectData.value.status });
}
</script>

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

.status-block {
    display: flex;
    flex-direction: column;
    gap: 5px;
}

.status-block select {
    background: #eee;
    color: #000;
    border: none;
    border-radius: 5px;
    padding: 5px 8px;
    font-size: 16px;
    width: fit-content;
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
