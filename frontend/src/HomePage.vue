<template>
  <div class="home">
    <Menu/>
    <MainBackground/>
<!--    <MainUser/>-->
    <MainBackgroundLine/>
  </div>
</template>
<script>
import MainBackground from './components/MainBackground.vue';
import MainBackgroundLine from './components/MainBackgroundLine.vue';
import MainLogo from './components/MainLogo.vue'
import MainUser from './components/MainUser.vue'
import Menu from './components/Menu.vue';
export default {
  name: 'HomePage',
  components: {
    MainBackground,
    MainBackgroundLine,
    MainUser,
    Menu,
  }
};
</script>

<style scoped>
.home {
  position: fixed;
  width: 100vw;
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  overflow: hidden;
}
</style>
