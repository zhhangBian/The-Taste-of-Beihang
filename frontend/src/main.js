import {createApp} from 'vue'
import router from './router'
import App from './App.vue'
import "./assets/common.css";

import ElementPlus from 'element-plus';
import 'element-plus/dist/index.css';

const debounce = (fn, delay) => {
    let timer = null;
    return function () {
      let context = this;
      let args = arguments;
      clearTimeout(timer);
      timer = setTimeout(function () {
        fn.apply(context, args);
      }, delay);
    }
  }
  
  const _ResizeObserver = window.ResizeObserver;
  window.ResizeObserver = class ResizeObserver extends _ResizeObserver {
    constructor(callback) {
      callback = debounce(callback, 16);
      super(callback);
    }
  }
  

const app = createApp(App)
app.use(router)
app.use(ElementPlus)
app.mount('#app')
