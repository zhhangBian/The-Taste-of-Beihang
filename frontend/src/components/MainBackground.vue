<template>
  <div class="full-screen-background"></div>
</template>
<script>
export default {
  name: 'MainBackground',
}
</script>
<style scoped>
.full-screen-background {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-image: url('@/assets/background.png');
  background-size: cover;
  background-repeat: no-repeat;
  background-attachment: fixed;
  background-color: #f0f0f0;
  overflow: hidden;
  z-index: -1;
}
</style>
