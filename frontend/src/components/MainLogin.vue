<template>  
    <div class="top-right-buttons">  
      <button class="register-login-button" @click="testLogin">登录</button>  
      <span class="vertical-divider">|</span>  
      <button class="register-login-button" @click="testRegister">注册</button>  
    </div>  
  </template>  
  
  <script>  
  export default {  
    name: 'MainLogin',  
    methods: {  
      testLogin() {  
        console.log('登录按钮被点击');
        this.$router.push('/login');
      },  
      testRegister() {  
        console.log('注册按钮被点击');
        this.$router.push('/login');
      },  
    },  
  };  
  </script>
  

<style scoped>  
.top-right-buttons {  
position: fixed;  
top: 38px;  
right: 80px;  
display: flex;  
align-items: center;  
z-index: 1000;
}  

.register-login-button {  
background-color: transparent; /* 透明背景 */  
border: none; /* 无边框 */  
color: black; /* 黑色文字 */  
font-size: 18px; /* 字体大小 */  
cursor: pointer; /* 鼠标悬停时显示指针 */  
outline: none; /* 去除点击时的轮廓线 */  
padding: 5px 10px; /* 内边距，根据需要调整 */  
/* 如果你想让按钮看起来更像是链接，可以添加下面的样式 */  
text-decoration: none; /* 去除下划线 */  
font-family: inherit; /* 继承父元素的字体 */ 
z-index: 1000; 
/* 注意：这里没有添加hover样式，你可以根据需要添加 */  
}  

.vertical-divider {  
margin: 0 0px; /* 两边添加一些外边距以分隔按钮 */  
color: black; /* 分割线颜色 */  
font-size: 18px; /* 分割线大小，可能需要根据实际调整以匹配按钮大小 */  
line-height: 0; /* 去除分割线的垂直空间 */  
/* 注意：这里使用font-size和line-height来模拟分割线，因为纯CSS中没有直接创建垂直线的简便方法 */  
}  

.bottom-button {
  font-size: 28px;
  padding: 15px 30px; /* 统一按钮大小 */
  margin: 10px;
  background-color: black;
  color: white;
  border: none;
  cursor: pointer;
  white-space: nowrap;
  text-align: center;
  width: 200px; /* 统一按钮宽度 */
}
</style>