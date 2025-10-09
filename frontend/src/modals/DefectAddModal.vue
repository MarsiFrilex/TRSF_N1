<script setup>
import { onMounted, ref, watch } from "vue";
import { getTags } from "@/api/index.js";

const props = defineProps({
    show: Boolean,
});

const emit = defineEmits(["save", "cancel"]);

const form = ref({
    title: "",
    description: "",
    tag: "",
    photo: null,
});

const previewUrl = ref(null);
const tags = ref([]);
const errors = ref({}); // объект ошибок

function handleFileUpload(event) {
    const file = event.target.files[0];
    if (file) {
        form.value.photo = file;
        previewUrl.value = URL.createObjectURL(file);
    }
}

// 🔍 Проверка обязательных полей
function validateForm() {
    errors.value = {};

    if (!form.value.title.trim()) errors.value.title = "Введите название";
    if (!form.value.description.trim()) errors.value.description = "Введите описание";
    if (!form.value.tag) errors.value.tag = "Выберите тег";
    if (!form.value.photo) errors.value.photo = "Загрузите фотографию";

    return Object.keys(errors.value).length === 0;
}

function save() {
    if (validateForm()) {
        emit("save", { ...form.value });
    }
}

// Очистка формы при закрытии
watch(
    () => props.show,
    (val) => {
        if (!val) {
            form.value = {
                title: "",
                description: "",
                tag: "",
                photo: null,
            };
            previewUrl.value = null;
            errors.value = {};
        }
    }
);

onMounted(async () => {
    tags.value = await getTags();
});
</script>

<template>
    <div class="modal-overlay" v-if="show">
        <div class="modal-window">
            <h2>Добавить дефект</h2>

            <div class="modal-content">
                <div class="form-section">
                    <label>Название:</label>
                    <input
                        type="text"
                        v-model="form.title"
                        :class="{ 'input-error': errors.title }"
                    />
                    <span v-if="errors.title" class="error-text">{{ errors.title }}</span>

                    <label>Описание:</label>
                    <textarea
                        rows="3"
                        v-model="form.description"
                        :class="{ 'input-error': errors.description }"
                    ></textarea>
                    <span v-if="errors.description" class="error-text">{{ errors.description }}</span>

                    <label>Тег:</label>
                    <select
                        v-model="form.tag"
                        :class="{ 'input-error': errors.tag }"
                    >
                        <option disabled value="">Выберите тег</option>
                        <option
                            v-for="tag in tags"
                            :key="tag.id"
                            :value="tag.id"
                        >
                            {{ tag.title }}
                        </option>
                    </select>
                    <span v-if="errors.tag" class="error-text">{{ errors.tag }}</span>

                    <label>Фотография:</label>
                    <input
                        type="file"
                        @change="handleFileUpload"
                        :class="{ 'input-error': errors.photo }"
                    />
                    <span v-if="errors.photo" class="error-text">{{ errors.photo }}</span>
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
.form-section textarea,
.form-section select {
    background: #eee;
    color: #000;
    border: none;
    border-radius: 5px;
    padding: 8px;
    font-size: 16px;
    width: 100%;
    box-sizing: border-box;
}

.form-section textarea {
    resize: none;
}

.input-error {
    border: 2px solid #ff6666;
    background: #ffeaea;
}

.error-text {
    color: #ff9999;
    font-size: 14px;
    margin-top: -5px;
    margin-bottom: 5px;
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
