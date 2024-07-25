<template>  
    <div class="user-container">  
      <img src="@/assets/user.svg" alt="User Profile" class="user-image">  
    </div>  
  </template>  
    
  <script>  
  export default {  
    name: 'UserFavicon',  
    // 如果需要，可以在这里添加props或data来动态控制图片或其他属性  
  }  
  </script>  
    
  <style scoped>  
  .user-container {  
    position: absolute; /* 使用绝对定位将图片固定在右上角 */  
    top: 20px; /* 根据需要调整距离顶部的距离 */  
    right: 220px; /* 根据需要调整距离右侧的距离 */  
    /* 注意：如果user-container不是直接子元素于具有相对定位的父元素，  
       则可能需要将position设置为fixed，并调整样式以确保它固定在视口的右上角 */  
  }  
    
  .user-image {  
    width: 70px; /* 根据图片的实际大小和需求调整宽度 */  
    height: auto; /* 保持图片宽高比 */  
    /* 如果需要，可以添加其他样式，如边框、阴影等 */  
  }  
  </style>