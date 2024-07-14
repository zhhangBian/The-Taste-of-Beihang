<template>  
  <div id="app">  
    <NavVarBar /> 
    <!-- 其他页面内容 -->  
    <!--router-view /-->  
  </div>  
</template>  
  
<script>  
import NavVarBar from './components/NavVarBar.vue';  
  
export default {  
  name: 'App',  
  components: {  
    NavVarBar
  },  
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