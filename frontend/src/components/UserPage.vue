<template>
    <div class="container">
      <!-- 侧边栏组件 -->
      <Menu class="menu" />
      
      <!-- 主内容区域组件 -->
      <UserInfo class="main-content" />
    </div>
  </template>
  
  <script>
  import Menu from './Menu.vue';
  import UserInfo from './UserInfo.vue';
  
  export default {
    components: {
      Menu,
      UserInfo,
    },
  };
  </script>
  
  <style scoped>
  .container {
    display: flex;
    height: 100vh;
  }
  
  /* 侧边栏样式 */
  .menu {
    width: 90px;
    transition: width 0.6s;
    flex-shrink: 0;
  }
  
  .menu:hover {
    width: 220px;
  }
  
  /* 主内容区样式 */
  .main-content {
    flex-grow: 1;
    overflow-y: auto;
    padding: 20px;
    background-color: white;
  }
  </style>
  