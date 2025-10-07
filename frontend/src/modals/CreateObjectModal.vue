<template>
    <div class="modal-overlay" v-if="show">
        <div class="modal-window">
            <h2>Добавить дефект</h2>

            <div class="modal-content">
                <div class="form-section">
                    <label>Адрес:</label>
                    <input type="text" v-model="form.address" />

                    <label>Описание:</label>
                    <textarea rows="4" v-model="form.description"></textarea>
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
    address: "",
    description: "",
});

function save() {
    emit("save", { ...form.value });
}
</script>

<style scoped>
/* Общие стили */
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
    width: 600px;
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

/* Контент */
.modal-content {
    display: flex;
    flex-direction: column;
    gap: 15px;
}

.form-section {
    display: flex;
    flex-direction: column;
    gap: 12px;
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

/* Кнопки */
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
