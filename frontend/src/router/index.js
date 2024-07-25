import { createRouter, createWebHistory } from "vue-router";
import {defineAsyncComponent} from 'vue'

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
                title: '主页',
            },
        },
        {
            path: '/login',
            name: 'login',
            component: defineAsyncComponent(() => import(`../components/LoginPage.vue`)),
            meta: {
                title: '登录注册',
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
        }
    ]
})
export default router