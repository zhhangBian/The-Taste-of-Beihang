<template>
  <div class="app-container">
    <Menu />
    <FoodDetail />
  </div>
</template>

<script>
import Menu from './Menu.vue';
import FoodDetail from './FoodDetail.vue';

export default {
  components: {
    Menu,
    FoodDetail,
  },
};
</script>

<style>
.app-container {
  display: flex;
  height: 100vh;
}

.menu-wrapper {
  flex-shrink: 0;
  transition: width 0.6s;
  margin-right: 20px;
}

.food-detail {
  flex-grow: 1;
  padding: 20px;
  overflow-y: auto;
}
</style>
