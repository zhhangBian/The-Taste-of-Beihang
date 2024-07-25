<template>  
<div class="home">  
    <MainBackground />
    <MainLogo />
    <UserFavicon />
    <MainLogin />
    <MainBackgroundLine />
</div>  
</template>  
<script>
import MainBackground from './components/MainBackground.vue';
import MainBackgroundLine from './components/MainBackgroundLine.vue';
import MainLogo from './components/MainLogo.vue'
import UserFavicon from './components/UserFavicon.vue'
import MainLogin from './components/MainLogin.vue'

export default {  
name: 'HomePage',
components: {
    MainBackground,
    MainBackgroundLine,
    MainLogo,
    UserFavicon,
    MainLogin,
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
  