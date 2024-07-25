<template>  
<div class="home">  
    <MainBackground />
    <MainBackgroundLine />
</div>  
</template>  
<script>
import MainBackground from './components/MainBackground.vue';
import MainBackgroundLine from './components/MainBackgroundLine.vue';

export default {  
name: 'HomePage',
components: {
    MainBackground,
    MainBackgroundLine,
}
}; 
</script>

<style scoped>
.home {
position: relative;
width: 100vw;
height: 100vh;
display: flex;
justify-content: center;
align-items: center;
overflow: hidden;
}
</style>
  