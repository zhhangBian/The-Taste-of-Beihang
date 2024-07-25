<template>  
<div class="home">  
    <MainBackground />
    <MainLogo />
    <MainBackgroundLine />
</div>  
</template>  
<script>
import MainBackground from './components/MainBackground.vue';
import MainBackgroundLine from './components/MainBackgroundLine.vue';
import MainLogo from './components/MainLogo.vue'

export default {  
name: 'HomePage',
components: {
    MainBackground,
    MainBackgroundLine,
    MainLogo,
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
  