import { createRouter, createWebHistory } from 'vue-router';

import LoginPage from "@/pages/LoginPage.vue";
import ObjectsPage from "@/pages/ObjectsPage.vue";
import DefectsPage from "@/pages/DefectsPage.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
      {
          path: '/',
          name: 'Objects',
          component: ObjectsPage,
      },
      {
          path: '/login',
          name: 'Login',
          component: LoginPage,
      },
      {
          path: '/defects',
          name: 'Defects',
          component: DefectsPage,
      }
  ],
});

router.beforeEach((to, from, next) => {
    // Тут будет логика переброса на страницу входа, если не зареган
    next();
});

export default router;