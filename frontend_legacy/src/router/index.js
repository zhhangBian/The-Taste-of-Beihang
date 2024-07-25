import { createRouter, createWebHistory } from "vue-router";
import {defineAsyncComponent} from 'vue'

//路由设置

const router = createRouter({
    // history: createWebHashHistory(process.env.BASE_URL),  // hash 模式
    history: createWebHistory(),  // history 模式
    routes: [

        {
            path: '/home',
            name: 'home',
            component: defineAsyncComponent(() => import(`../Home.vue`)),
            meta: {
                title: '主页',
            },
        },
        {
            path: '/login',
            name: 'login',
            component: defineAsyncComponent(() => import(`../components/PaLogin.vue`)),
            meta: {
                title: '主页',
            },
        }
    ]
})


export default router
