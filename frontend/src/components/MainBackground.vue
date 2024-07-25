<template>  
    <div class="full-screen-background"></div>  
</template>  
<script>  
  export default {  
    name: 'MainBackground',  
  }  
</script>  
<style scoped>  
.full-screen-background {  
    /* 确保元素占据整个屏幕 */  
    position: fixed;   
    top: 0;   
    left: 0;   
    right: 0;   
    bottom: 0;  
    
    /* 设置背景图片 */  
    background-image: url('@/assets/background.png');  
    
    /* 确保背景图片覆盖整个容器 */  
    background-size: cover;  
    
    /* 防止背景图片重复 */  
    background-repeat: no-repeat;  
    
    /* 使得背景图片始终固定在容器内 */  
    background-attachment: fixed;  
    
    /* 可选：设置背景色，当图片加载失败时显示 */  
    background-color: #f0f0f0;  
    
    /* 隐藏溢出部分，确保图片不会溢出容器 */  
    overflow: hidden;  
    
    /* 可选：添加z-index确保背景在其他元素之下 */  
    z-index: -1;  
}  
</style>