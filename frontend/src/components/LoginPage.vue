<template>
  <div class="box">
    <div class="content" :class="{ 'add-class-content': !isLogin }">
      <img class="login-img images" src="@/assets/login.jpg" alt="登录" :class="{ 'add-class-login-img': !isLogin, 'add-class-login-img-show': isLogin }">
      <img class="register-img images" src="@/assets/register.jpg" alt="注册" :class="{ 'add-class-register-img': !isLogin }">
      <div class="login-wrapper" :style="{ height: isLogin ? '70vh' : '80vh' }">
        <div class="top-tips">
          <span class="cat-text">CAT IS LITTLE #FFF</span>
        </div>
        <h1 class="h1-text">{{ isLogin ? '登录' : '注册' }}</h1>
        <div class="form-container">
          <div class="login-form" v-show="isLogin">
            <div class="user-form form-item">
              <div class="text-tips">
                <span>账号</span>
              </div>
              <input type="text">
            </div>
            <div class="password-form form-item">
              <div class="text-tips">
                <span>密码</span>
              </div>
              <input type="password">
            </div>
            <button class="btn">登录</button>
            <button class="toggle-btn" @click="toggleForm">没有账户？</button>
          </div>
          <div class="register-form" v-show="!isLogin">
            <div class="user-form form-item">
              <div class="text-tips">
                <span>账号</span>
              </div>
              <input type="text">
            </div>
            <div class="password-form form-item">
              <div class="text-tips">
                <span>密码</span>
              </div>
              <input type="password">
            </div>
            <div class="password-form form-item">
              <div class="text-tips">
                <span>确认密码</span>
              </div>
              <input type="password">
            </div>
            <button class="btn">注册</button>
            <button class="toggle-btn" @click="toggleForm">已有账户？</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      isLogin: true
    };
  },
  methods: {
    toggleForm() {
      this.isLogin = !this.isLogin;
    }
  }
};
</script>

<style scoped>
* {
  margin: 0;
  padding: 0;
}

.box {
  background-color: rgb(51, 32, 108);
  width: 100vw;
  height: 100vh;
}
.box .content {
  width: 90vw;
  height: 85vh;
  background-color: rgb(228, 218, 232);
  border-radius: 40px;
  position: absolute;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
  display: flex;
  justify-content: center;
  align-items: center;
  overflow: hidden;
  transition: 1s;
}
.box .content .images {
  margin-left: -150px;
  margin-right: 100px;
  position: absolute;
  left: 15%;
}
.box .content .login-img {
  width: 45%;
  height: 90%;
  border-radius: 15%;
}
.box .content .register-img {
  width: 45%;
  opacity: 0;
  border-radius: 15%;
}
.box .content .login-wrapper {
  width: 30vw;
  height: 70vh;
  border-radius: 40px;
  -webkit-backdrop-filter: blur(1px);
          backdrop-filter: blur(1px);
  background: rgba(244, 240, 245, 0.6);
  padding: 60px;
  box-sizing: border-box;
  position: absolute;
  right: 10%;
  transition: 1s;
}
.box .content .login-wrapper .top-tips {
  display: flex;
  justify-content: flex-start;
  align-items: center;
  margin-bottom: 20px;
}
.box .content .login-wrapper .top-tips .cat-text {
  font-size: 25px;
  font-weight: 600;
}
.box .content .login-wrapper h1 {
  font-size: 45px;
  margin: 20px 0;
  text-align: left;
}
.box .content .login-wrapper .login-form,
.box .content .login-wrapper .register-form {
  width: 100%;
}
.box .content .login-wrapper .login-form .form-item .text-tips,
.box .content .login-wrapper .register-form .form-item .text-tips {
  color: rgb(123, 122, 123);
  margin: 5px;
  text-align: left;
}
.box .content .login-wrapper .login-form .form-item input,
.box .content .login-wrapper .register-form .form-item input {
  width: 100%;
  height: 50px;
  margin: 5px 0;
  border-radius: 5px;
  border: 0;
  font-size: 17px;
  padding: 0 20px;
  box-sizing: border-box;
}
.box .content .login-wrapper .login-form .form-item input:focus,
.box .content .login-wrapper .register-form .form-item input:focus {
  outline: none;
  border: 1px solid rgb(79, 133, 226);
}
.box .content .login-wrapper .login-form .btn,
.box .content .login-wrapper .register-form .btn {
  width: 100%;
  height: 50px;
  margin: 20px 0;
  background-color: rgb(59, 58, 59);
  border: 0;
  border-radius: 5px;
  color: #fff;
  font-size: 20px;
  cursor: pointer;
  text-align: center;
}
.box .content .login-wrapper .login-form .toggle-btn,
.box .content .login-wrapper .register-form .toggle-btn {
  width: 100%;
  height: 50px;
  margin: 10px 0;
  background-color: transparent;
  border: 0;
  color: rgb(79, 133, 226);
  font-size: 15px;
  cursor: pointer;
  text-align: center;
}
.form-container {
  display: block;
}

.add-class-content {
  background-color: rgb(156, 148, 208) !important;
  transition: 0.1s;
}

.add-class-login-img {
  -webkit-animation: disappear 0.3s forwards;
          animation: disappear 0.3s forwards;
  -webkit-animation-timing-function: ease;
          animation-timing-function: ease;
}

.add-class-login-img-show {
  -webkit-animation-delay: 1s;
          animation-delay: 1s;
  -webkit-animation: appear 1s forwards;
          animation: appear 1s forwards;
  -webkit-animation-timing-function: ease;
          animation-timing-function: ease;
}

.add-class-register-img {
  -webkit-animation: appear 1s forwards;
          animation: appear 1s forwards;
  -webkit-animation-timing-function: ease;
          animation-timing-function: ease;
  -webkit-animation-delay: 0.2s;
          animation-delay: 0.2s;
}

@-webkit-keyframes appear {
  from {
    border-radius: 15%;
    opacity: 0;
  }
  to {
    border-radius: 0%;
    opacity: 1;
  }
}

@keyframes appear {
  from {
    border-radius: 15%;
    opacity: 0;
  }
  to {
    border-radius: 0%;
    opacity: 1;
  }
}
@-webkit-keyframes disappear {
  from {
    opacity: 1;
  }
  to {
    opacity: 0;
  }
}
@keyframes disappear {
  from {
    opacity: 1;
  }
  to {
    opacity: 0;
  }
}
</style>
