<template>  
    <!--div class="title-container"-->  
      <!--h1 class="artistic-title">今天在BUAA吃什么？</h1-->
      <div :class="{ customFont: true }">软工教学论坛</div>  
    <!--/div-->  
  </template>  
    
  <script>  
  export default {  
    name: 'Title'  
  }  
  </script>  
    
  <style scoped>  
  /*
  .title-container {  
    justify-content: center;
    align-items: center; 
    width: 75vw; 
    height: 90vh; 
    padding: 0 0;
  }  
    
  .artistic-title {  
    font-family: 'Arial', sans-serif;  
    font-size: 60px; 
    color: #333;
    margin: 0 auto; 
  }  
  */
  .customFont {
    font-family: 'consolas', sans-serif;
    font-weight: bold;
    font-size: 20px;
    text-align: center;
    width: 80%;
}
  </style>