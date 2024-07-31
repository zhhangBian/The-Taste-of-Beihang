<template>
  <div class="user-actions-container">
    <div class="user-container">
      <img src="@/assets/user.svg" alt="User Profile" class="user-image">
    </div>
    <div class="top-right-buttons">
      <button class="register-login-button" @click="testLogin">登录</button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'UserActions',
  methods: {
    testLogin() {
      console.log('登录按钮点击');
      this.$router.push('/login');
    },
  },
};
</script>

<style scoped>
.user-actions-container {
  position: absolute; /* 使用absolute定位确保它们相对于父元素定位 */
  top: 20px;
  right: 80px;
  display: flex;
  align-items: center;
  z-index: 1000;
}

.user-container {
  margin-right: 10px; /* 在头像和按钮之间添加一些间距 */
}

.user-image {
  width: 70px; /* 根据图片的实际大小和需求调整宽度 */
  height: auto; /* 保持图片宽高比 */
  /* 如果需要，可以添加其他样式，如边框、阴影等 */
}

.top-right-buttons {
  display: flex;
  align-items: center;
}

.register-login-button {
  background-color: transparent; /* 透明背景 */
  border: none; /* 无边框 */
  color: black; /* 黑色文字 */
  font-size: 18px; /* 字体大小 */
  cursor: pointer; /* 鼠标悬停时显示指针 */
  outline: none; /* 去除点击时的轮廓线 */
  padding: 5px 10px; /* 内边距，根据需要调整 */
  text-decoration: none; /* 去除下划线 */
  font-family: inherit; /* 继承父元素的字体 */
}

.vertical-divider {
  margin: 0 5px; /* 两边添加一些外边距以分隔按钮 */
  color: black; /* 分割线颜色 */
  font-size: 18px; /* 分割线大小，可能需要根据实际调整以匹配按钮大小 */
  line-height: 0; /* 去除分割线的垂直空间 */
}
</style>
