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
        // {
        //     path: '/login',
        //     name: 'login',
        //     component: defineAsyncComponent(() => import(`../components/PaLogin.vue`)),
        //     meta: {
        //         title: '主页',
        //     },
        // }
    ]
})
export default router