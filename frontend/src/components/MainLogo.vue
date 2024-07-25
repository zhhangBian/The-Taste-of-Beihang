<template>  
<div class="logo-container">  
    <img src="@/assets/logo.svg" alt="Logo" class="logo-image" />  
</div>  
</template>  

<script>  
export default {  
name: 'MainLogo',  
// 如果需要，可以在这里添加props或data来动态控制logo  
}  
</script>  

<style scoped>  
.logo-container {  
position: absolute; /* 或者使用 fixed，取决于您希望logo如何定位 */  
top: -20px; /* 根据需要调整 */  
left: 30px; /* 根据需要调整 */  
/* 如果logo应该相对于整个页面定位，并且您希望它固定在那里，  
    即使页面滚动也不移动，那么请使用 position: fixed; */  
}  

.logo-image {  
width: 300px; /* 根据logo图片的实际大小和需求调整 */  
height: auto; /* 保持图片宽高比 */  
/* 如果logo图片有透明背景，它将与父元素或页面的背景色融合 */  
}  
</style>