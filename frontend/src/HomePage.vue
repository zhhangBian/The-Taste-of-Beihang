<template>  
<div class="home">  
    <MainBackground />
</div>  
</template>  
<script>
import MainBackground from './components/MainBackground.vue';
export default {  
    name: 'HomePage',
    components: {
        MainBackground,
    }
}; 
</script>


<style>  
#app {  
font-family: Avenir, Helvetica, Arial, sans-serif;  
-webkit-font-smoothing: antialiased;  
-moz-osx-font-smoothing: grayscale;  
text-align: center;  
color: #2c3e50;  
margin-top: 60px;
}  
</style>
  