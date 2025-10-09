import { createRouter, createWebHistory } from 'vue-router';

import LoginPage from "@/pages/LoginPage.vue";
import ObjectsPage from "@/pages/ObjectsPage.vue";
import DefectsPage from "@/pages/DefectsPage.vue";
import { getCurrentUser } from "@/api/index.js";

let role_id = 1;
let user_id = 1;

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path: '/',
            name: 'Objects',
            component: ObjectsPage,
            props: () => ({
                role_id: role_id,
            }),
        },
        {
            path: '/login',
            name: 'Login',
            component: LoginPage,
        },
        {
            path: '/defects/:id',
            name: 'Defects',
            component: DefectsPage,
            props: (route) => ({
                id: Number(route.params.id),
                role_id: role_id,
                user_id: user_id,
            }),
        }
    ],
});

router.beforeEach(async (to, from, next) => {
    let user;

    try { user = await getCurrentUser(); role_id = user.role_id; user_id = user.id; }
    catch (error) { console.log(error); }

    if (!user && to.name !== 'Login') {
        next({ name: 'Login' });
    }
    else {
        next();
    }
});

export default router;