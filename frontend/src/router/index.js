import { createRouter, createWebHistory } from "vue-router";
import { defineAsyncComponent } from 'vue';

// 路由设置
const router = createRouter({
    // history 模式
    history: createWebHistory(),
    routes: [
        {
            path: '/',
            name: 'home',
            component: defineAsyncComponent(() => import(`../HomePage.vue`)),
            meta: {
                title: '今天在BUAA吃什么？',
            },
        },
        {
            path: '/login',
            name: 'login',
            component: defineAsyncComponent(() => import(`../components/LoginPage.vue`)),
            meta: {
                title: '欢迎回来',
            },
        },
        {
            path: '/plaza',
            name: 'plaza',
            component: defineAsyncComponent(() => import(`../components/FoodPlaza.vue`)),
            meta: {
                title: '美食广场',
            },
        },
        {
            path: '/detail',
            name: 'detail',
            component: defineAsyncComponent(() => import(`../components/FoodDetail.vue`)),
            meta: {
                title: '详情',
            },
        },
        {
            path: '/user',
            name: 'user',
            component: defineAsyncComponent(() => import(`../components/UserPage.vue`)),
            meta: {
                title: '详情',
            },
        }
    ]
});

// 添加 beforeEach 导航守卫来设置页面标题
router.beforeEach((to, from, next) => {
    document.title = to.meta.title || '默认标题';
    next();
});

export default router;
