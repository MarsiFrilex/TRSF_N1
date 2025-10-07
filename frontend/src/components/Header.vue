<template>
    <header class="header">
        <div class="header-content">
            <a class="logo" href="/">строй.ру</a>
            <nav class="navigation">
                <a href="/" class="nav-link">Объекты</a>
            </nav>
        </div>
    </header>
</template>

<script setup>
</script>

<style scoped>
.header {
    background: #583031;
    height: 80px;
    width: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0; /* Предотвращает сжатие */
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

.navigation {
    display: flex;
    gap: 30px;
}

.nav-link {
    color: #EAEAEA;
    text-decoration: none;
    font-size: 24px;
    transition: color 0.3s;
}

.nav-link:hover {
    color: #CCC;
}
</style>