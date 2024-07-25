<template>  
  <div class="home">  
    <background /> 
    <logo />
    <user />
    <logins />
    <background2 />  
    <router-view />  
  </div>  
</template>  
<script>
import background from './components/background.vue';  
import background2 from './components/background2.vue';  
import logo from './components/logo.vue';  
import user from './components/user.vue';  
import logins from './components/logins.vue';  
export default {  
  name: 'Home',  
  components: {  
    background,
    background2,
    logo,
    user,
    logins
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
