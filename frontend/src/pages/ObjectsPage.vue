<script setup>
import Header from "@/components/Header.vue";
import Footer from "@/components/Footer.vue";

const items = [
    {id: 1, name: 'Стройка 1'},
    {id: 2, name: 'Стройка 2'},
    {id: 3, name: 'Стройка 3'},
    {id: 4, name: 'Стройка 4'},
    {id: 5, name: 'Стройка 5'},
];

const isAdmin = true;
</script>

<template>
    <div class="app">
        <Header />

        <main class="main-content">
            <div class="main">
                <div class="container">
                    <!-- Левая колонка - основной контент -->
                    <div class="content-column">
                        <div class="content-item" v-for="item in items" :key="item.id">
                            {{ item.name }}
                        </div>
                    </div>

                    <!-- Правая колонка - кнопки -->
                    <div v-if="isAdmin" class="buttons-column">
                        <button class="action-btn">
                            Добавить
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

body {
    height: 100%;
    margin: 0;
}

.main {
    display: flex;
    align-items: center;
    justify-content: center;
    background: url('@/assets/background.jpg') no-repeat center center;
    background-size: cover;
    width: 100%;
    min-height: calc(100vh - 160px); /* Вычитаем высоту хедера и футера */
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
}

/* Левая колонка - основная */
.content-column {
    flex: 1;
    padding-right: 0;
    padding-top: 20px;
    max-height: 70vh;
    overflow-y: auto;
}

.content-item {
    background: #EAEAEA;
    padding: 18px;
    font-size: 20px;
    font-family: Inter, system-ui;
    margin-bottom: 30px;
    border-radius: 10px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.content-item:hover {
    background: #CCC;
}

/* Правая колонка - кнопки */
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
    font-size: 18px;
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

    .content-column {
        padding-right: 0;
    }
}
</style>