<template>
    <footer class="footer">
        <div class="footer-content">
            <div class="phone">+7 (999) 123-45-67</div>
            <div class="address">г. Москва, ул. Строителей, д. 15</div>
        </div>
    </footer>
</template>

<script setup>
</script>

<style scoped>
.footer {
    background: #583031;
    height: 80px;
    width: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0; /* Предотвращает сжатие */
}

.footer-content {
    width: 100%;
    max-width: 1200px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0 20px;
}

.phone,
.address {
    color: #EAEAEA;
    font-size: 20px;
}
</style>