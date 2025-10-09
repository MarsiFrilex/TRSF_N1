<script setup>
import { ref } from "vue";
import { useRouter } from "vue-router";
import Header from "@/components/Header.vue";
import Footer from "@/components/Footer.vue";
import { loginUser } from "@/api/index.js";

const login = ref("");
const password = ref("");

const router = useRouter();

async function handleLogin() {
    try {
        let tokens = await loginUser({email: login.value, password: password.value});
        localStorage.setItem("accessToken", tokens.access_token);
        localStorage.setItem("refreshToken", tokens.refresh_token);
        await router.push("/");
    }
    catch (error) {
        console.log(error);
    }
}
</script>

<template>
    <div class="app">
        <Header />

        <main class="main">
            <div class="overlay"></div>

            <!-- Форма входа -->
            <div class="login-box">
                <form @submit.prevent="handleLogin" class="login-form">
                    <label for="login">Логин</label>
                    <input
                        id="login"
                        v-model="login"
                        type="text"
                        required
                        class="login-input"
                    />

                    <label for="password">Пароль</label>
                    <input
                        id="password"
                        v-model="password"
                        type="password"
                        required
                        class="login-input"
                    />

                    <button type="submit" class="login-button">Войти</button>
                </form>
            </div>
        </main>

        <Footer />
    </div>
</template>

<style scoped>
.app {
    display: flex;
    flex-direction: column;
    min-height: 100vh;
}

.main {
    position: relative;
    flex: 1;
    background: url("@/assets/background.jpg") no-repeat center center;
    background-size: cover;
    display: flex;
    align-items: flex-start;
    justify-content: flex-start;
    padding: 60px 100px;
}

.overlay {
    position: absolute;
    inset: 0;
    background: rgba(0, 0, 0, 0.2);
    z-index: 1;
}

.login-box {
    position: relative;
    z-index: 2;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
}

.login-form {
    display: flex;
    flex-direction: column;
}

.login-form label {
    margin-top: 24px;
    font-size: 18px;
    color: #000;
}

.login-input {
    width: 280px;
    padding: 8px 10px;
    border: 1px solid black;
    border-radius: 6px;
    background: #f3f3f3;
    font-size: 15px;
    outline: none;
}

.login-input:focus {
    border-color: #222;
    background: #fff;
}

.login-button {
    width: 150px;
    padding: 10px;
    font-size: 18px;
    border-radius: 8px;
    border: 1px solid black;
    background: #f0f0f0;
    cursor: pointer;
    transition: all 0.2s;
    align-self: center;
    margin-top: 32px;
}

.login-button:hover {
    background: #e4e4e4;
}
</style>
