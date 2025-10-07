<template>
    <div class="modal-overlay" v-if="show">
        <div class="modal-window">
            <h2>Добавить дефект</h2>
            <div class="modal-content">
                <div class="form-section">
                    <label>Название:</label>
                    <input type="text" v-model="form.title" />

                    <label>Описание:</label>
                    <textarea rows="3" v-model="form.description"></textarea>

                    <label>Классификация:</label>
                    <input type="text" v-model="form.classification" />

                    <label>Фотография:</label>
                    <input type="file" @change="handleFileUpload" />
                </div>

                <div class="photo-section">
                    <img
                        v-if="previewUrl"
                        :src="previewUrl"
                        alt="Фото дефекта"
                    />
                    <div v-else class="placeholder">Нет изображения</div>
                </div>
            </div>

            <div class="modal-buttons">
                <button @click="$emit('cancel')">Отмена</button>
                <button class="save" @click="save">Сохранить</button>
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref, watch } from "vue";

const props = defineProps({
    show: Boolean,
});

const emit = defineEmits(["save", "cancel"]);

const form = ref({
    title: "",
    description: "",
    classification: "",
    photo: null,
});

const previewUrl = ref(null);

function handleFileUpload(event) {
    const file = event.target.files[0];
    if (file) {
        form.value.photo = file;
        previewUrl.value = URL.createObjectURL(file);
    }
}

function save() {
    emit("save", { ...form.value });
}
</script>

<style scoped>
.modal-overlay {
    position: fixed;
    inset: 0;
    background: rgba(0, 0, 0, 0.6);
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

.form-section {
    flex: 1;
    display: flex;
    flex-direction: column;
    gap: 10px;
}

.form-section label {
    font-size: 18px;
}

.form-section input,
.form-section textarea {
    background: #eee;
    color: #000;
    border: none;
    border-radius: 5px;
    padding: 8px;
    font-size: 16px;
    width: 100%;
    box-sizing: border-box;
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

.placeholder {
    color: #ccc;
    font-size: 18px;
}

.modal-buttons {
    display: flex;
    justify-content: flex-end;
    gap: 15px;
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

.modal-buttons .save:hover {
    background: #f0f0f0;
}
</style>
