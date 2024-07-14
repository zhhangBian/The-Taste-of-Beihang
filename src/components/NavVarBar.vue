<template>  
    <nav class="navbar">  
      <div class="navbar-logo">
      <img src="@/assets/1.jpg" alt="Logo" />
    </div>
      <ul class="navbar-links">  
        <li><router-link to="/recipes">菜谱</router-link></li>  
        <li><router-link to="/reviews">评论</router-link></li>  
        <li><router-link to="/reviews">推荐</router-link></li>  
      </ul>   
    <!-- 其他导航栏内容 -->  
  
    <div class="search-bar">
    <input
      type="text"
      v-model="searchQuery"
      placeholder="搜索..."
      @input="handleInput"
      class="search-input"
    />
    <button class="search-button" @click="handleSubmit">
      <!-- SVG放大镜图标 -->
      <svg class="search-icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
        <circle cx="11" cy="10" r="8"></circle>
        <path d="M16 16 L22 22"></path>
      </svg>
    </button>
  </div>
      <div class="navbar-actions">  
        <button @click="toggleLoginModal">登录/注册</button>  
        <!-- 这里可以添加登录/注册模态框的逻辑，但为了简化，我们只展示按钮 -->  
      </div>  
    </nav>  
    <div style="width: 150%; ">
    <img  src="@/assets/map.jpg" alt="">
  </div>

  </template>  
    
  <script>  
  export default {  
    name: 'Navbar',  
    methods: {  
      toggleLoginModal() {  
        // 这里可以添加打开登录/注册模态框的逻辑  
        console.log('打开登录/注册模态框');  
      },  
    },  
  };  
  </script>  
    
    <style scoped>  
    .navbar {  
      display: flex;  
      align-items: center;  
      justify-content: center;
      padding: 0px 0px;  
      background-color: #333;  
      color: #fff;  
      position: fixed; /* 将导航栏固定在页面顶端 */  
      top: 0;  
      left: 0;  
      width: 100%; /* 确保导航栏宽度占满整个屏幕 */  
      z-index: 1000; /* 确保导航栏在其他内容之上 */  
      box-shadow: 0 2px 4px rgba(0,0,0,0.1); /* 可选：添加一些阴影效果，让导航栏看起来更立体 */  
    }  
      
    .navbar-logo {
  /* 调整Logo容器的左右边距来增加与菜单项的距离 */
   margin-right: 70px; /* 增加了右侧边距 */
  /* ... 其他样式保持不变 ... */
}
    .navbar-logo img {  
      height: 50px; /* Logo图片的高度，根据需要调整 */  
      width: 200px;
      display: block;
    }  
      
    .navbar-links {  
      list-style: none;  
      display: flex;  
      margin: 0;  
      padding: 0;  
      font-size: 20px;
      gap: 70px; /* 使用gap属性来增加列表项之间的间距 */  
      margin-right: 70px;
    }  
      
    /* 如果你的浏览器不支持gap属性，可以使用margin-right代替，但最后一个元素需要特殊处理 */  
    /*  
    .navbar-links li {  
      margin-right: 20px;  
    }  
    .navbar-links li:last-child {  
      margin-right: 0;  
    }  
    */  
      
    .navbar-links li a {  
      color: #fff;  
      text-decoration: none;  
    }  
      
    .navbar-search input {  
      padding: 8px;  
      border: none;  
      border-radius: 4px;  
      background-color: #555;  
      color: #fff;  
    }  
      
    .navbar-actions button {  
      padding: 8px 16px;  
      background-color: #007bff;  
      color: #fff;  
      border: none;  
      border-radius: 4px;  
      cursor: pointer;  
    }  
      
    .navbar-actions button:hover {  
      background-color: #0056b3;  
    }  
      
    /* 可能需要添加一些额外的样式来确保内容在导航栏下方显示 */  
    /* 例如，给App.vue中的<router-view>或其他内容容器添加一个上边距 */  
    /*  
    #app {  
      padding-top: 60px; /* 根据导航栏的高度调整  
    */  
      
    /* 但由于导航栏是固定的，通常你需要在全局样式中或根组件中添加这个padding-top */  

    .search-bar {
  display: flex;
  align-items: center;
  background: #fff;
  padding: 5px;
  border-radius: 24px;
  margin-top: 5px; 
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  margin-bottom: 5px; 
  margin-right: 70px;
}

.search-input {
  border: none; /* 去除边框 */
  outline: none; /* 去除聚焦时的轮廓 */
  padding: 10px;
  flex-grow: 1;
  margin-right: 5px; /* 与搜索按钮保持一定间距 */
  background: #f5f5f5; /* 轻微的背景色 */
  border-radius: 24px; /* 圆角边框 */
  color: #333; /* 字体颜色 */
  font-size: 16px; /* 字体大小 */
}

.search-button {
  border: none;
  background: none;
  cursor: pointer;
  padding: 5px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.search-icon {
  width: 20px;
  height: 30px;
  fill: white;
  transition: fill 0.3s ease;
}

.search-input::placeholder {
  color: #bbb; /* 占位符文字颜色 */
  font-size: 16px; /* 占位符文字大小 */
}

.search-input:focus + .search-button .search-icon {
  fill: white;
}/* ... 其他样式保持不变 ... */

.container {
  display: inline;
  justify-content: center;
  vertical-align: sub;
  align-items: center;
  height: 100vh; /* 使用视窗高度来使容器填满整个屏幕 */
}
 
.centered-image {
  max-width: 100%; /* 确保图片不会超出容器宽度 */
  height: auto; /* 保持图片的宽高比 */
}
    </style>