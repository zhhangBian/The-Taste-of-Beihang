<template>
    <div :class="{'dark': isDarkMode}" class="page-container">
      <NavBar :isSidebarClosed="isSidebarClosed" :toggleSidebar="toggleSidebar" :isDarkMode="isDarkMode" :toggleDarkMode="toggleDarkMode"/>
      <div class="content-wrapper">
        <FoodPlaza />
      </div>
    </div>
  </template>
  
  <script>
  import NavBar from './NavBar.vue';
  import FoodPlaza from './FoodPlaza.vue';
  
  export default {
    components: {
      NavBar,
      FoodPlaza
    },
    data() {
      return {
        isSidebarClosed: true,
        isDarkMode: false
      };
    },
    methods: {
      toggleSidebar() {
        this.isSidebarClosed = !this.isSidebarClosed;
      },
      toggleDarkMode() {
        this.isDarkMode = !this.isDarkMode;
      }
    }
  };
  </script>
  
  <style scoped>
  .page-container {
    background-image: url('@/assets/background.png');
    background-size: cover;
    background-position: center;
    min-height: 100vh;
  }
  .content-wrapper {
    margin-left: 250px;
    padding: 20px;
    transition: margin-left 0.3s;
  }
  .dark .content-wrapper {
    background-color: var(--body-color);
  }
  </style>
  