<template>
    <div class="container">
      <Menu class="menu" />
      <FoodPlaza class="food-plaza" />
    </div>
  </template>
  
  <script>
  import Menu from './Menu.vue';
  import FoodPlaza from './FoodPlaza.vue';
  
  export default {
    components: {
      Menu,
      FoodPlaza,
    },
  };
  </script>
  
  <style scoped>
  .container {
    display: flex;
    height: 100vh;
  }
  
  .menu {
    width: 90px;
    transition: width 0.6s;
    flex-shrink: 0;
  }
  
  .menu:hover {
    width: 220px;
  }
  
  .food-plaza {
    flex-grow: 1;
    overflow-y: auto;
  }
  </style>
  