<template>
    <div class="container">
      <div class="content-center">
        <div class="svg-container">
          <img src="@/assets/background2.svg" alt="Background SVG" class="centered-svg">
        </div>
        <div :class="{ customFont: true }">在BUAA吃什么？</div>  
        
        <!--div class="title-container">
          <h1 class="artistic-title">今天在BUAA吃什么？</h1>
        </div-->
        <div class="button-container">
          <button class="top-button">吃什么?</button>
          <div class="bottom-buttons">
            <button class="bottom-button">就这个！</button>
            <button class="bottom-button">重新建议</button>
            <button class="bottom-button">去广场看看</button>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'CenteredSvgAndTitle'
  };
  </script>
  
  <style scoped>
  .container {
    position : relative;
    width: 75vw;
    height: 80vh;
  }
  
  .content-center {
    width: 100%;
    height: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
  }
  
  .svg-container {
    position: absolute;
    width: 100%;
    height: 100%;
  }
  
  .centered-svg {
    width: 100%;
    height: 100%;
  }/*
  
  .title-container {
    top: 14%;
    left: 50%;
    transform: translate(-50%, -50%);
    z-index: 2; 
  }
  
  .artistic-title {
    font-family: 'Arial', sans-serif;
    font-size: 58px;
    color: #333;
    text-align: center;
    margin-bottom: 45px; 
  }
    */
  .customFont {
    font-family: 'Lato';
    font-weight: bold;
    font-size: 5rem;
    height: 30px;
    margin-top: -650px;
    text-align: center;
    width: 80%;
  }
  
  .button-container {  
  position: absolute;  
  left: 50%;  
  transform: translateX(-50%);  
  z-index: 3;  
  /* 如果需要限制容器宽度，可以添加以下样式 */  
  width: calc(100% - 40px); /* 假设左右各有20px的间距或边距 */  
  /*max-width: 600px; /* 可选：设置最大宽度 */  
  /* 如果需要限制高度或添加其他样式，请在这里添加 */  
}  
  
.top-button {  
  font-size: 28px;  
  padding: 20px 30px;  
  margin-bottom: 40px;  
  transform: translateX(-8%);  
  background-color: black;  
  color: white;  
  border: none;  
  cursor: pointer;  
  white-space: nowrap;  
  text-align: center;  
  /* 如果需要，可以添加border-radius等样式 */  
}  
  
.bottom-buttons {  
  display: flex;  
  justify-content: center; /* 使底部按钮水平居中 */  
  margin-top: 150px;  
  /* 如果需要，可以添加padding来在容器边缘和按钮之间创建空间 */  
}  
  
.bottom-button {  
  font-size: 28px;  
  padding: 10px 20px; /* 默认内边距 */  
  margin: 0 70px; /* 左右边距，用于在按钮之间创建空间 */  
  background-color: black;  
  color: white;  
  border: none;  
  cursor: pointer;  
  white-space: nowrap;  
  text-align: center;  
}  
  
/* 特别注意：.bottom-button.medium 类应该只应用于需要特殊内边距的按钮 */  
.bottom-button.medium {  
  padding: 1px 30px; /* 增加中间按钮的内边距以与顶部按钮对齐（如果必要） */  
  /* 如果需要，还可以调整其他样式 */  
}
  </style>