<template>
    <header class="header">
        <div class="header-content">
            <a class="logo" href="/">строй.ру</a>

            <div v-if="!!userName" class="user-section" @click="toggleMenu">
                <span class="user-name">{{ userName }}</span>
                <span class="arrow" :class="{ open: showMenu }">▼</span>

                <div v-if="showMenu" class="dropdown">
                    <button class="logout-btn" @click.stop="handleLogout">Выйти</button>
                </div>
            </div>
        </div>
    </header>
</template>

<script setup>
import { onMounted, ref } from "vue";
import { useRouter } from "vue-router";
import { getCurrentUser } from "@/api/index.js";

const router = useRouter();

const userName = ref("");
const showMenu = ref(false);

function toggleMenu() {
    showMenu.value = !showMenu.value;
}

async function handleLogout() {
    showMenu.value = false;
    localStorage.removeItem("accessToken");
    localStorage.removeItem("refreshToken");
    await router.push("/login");
}

onMounted(async () => {
    let user = await getCurrentUser();
    userName.value = user.user_name;
})
</script>

<style scoped>
.header {
    background: #583031;
    height: 80px;
    width: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
}

.header-content {
    width: 90%;
    max-width: 1200px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0 20px;
}

.logo {
    text-decoration: none;
    font-size: 48px;
    font-weight: bold;
    color: white;
}

.user-section {
    position: relative;
    color: #eaeaea;
    font-size: 22px;
    cursor: pointer;
    display: flex;
    align-items: center;
    gap: 8px;
    user-select: none;
}

.user-name:hover {
    color: #ccc;
}

.arrow {
    font-size: 14px;
    transition: transform 0.2s ease;
}

.arrow.open {
    transform: rotate(180deg);
}

.dropdown {
    position: absolute;
    top: 120%;
    right: 0;
    background: #fff;
    border-radius: 6px;
    box-shadow: 0 2px 6px rgba(0, 0, 0, 0.25);
    display: flex;
    flex-direction: column;
    z-index: 100;
}

.logout-btn {
    background: none;
    border: none;
    padding: 10px 20px;
    text-align: left;
    font-size: 18px;
    cursor: pointer;
    color: #583031;
    transition: background 0.2s;
    width: 100%;
}
</style>
