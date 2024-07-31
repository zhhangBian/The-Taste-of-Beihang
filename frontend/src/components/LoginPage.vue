<template>
  <div class="box">
    <div class="content" :class="{ 'add-class-content': !isLogin }">
      <img class="login-img images" src="@/assets/login2.png" alt="登录"
           :class="{ 'add-class-login-img': !isLogin, 'add-class-login-img-show': isLogin }">
      <img class="register-img images" src="@/assets/reg2.png" alt="注册"
           :class="{ 'add-class-register-img': !isLogin }">
      <div class="login-wrapper" :style="{ height: isLogin ? '75vh' : '85vh' }">
        <div class="top-tips">
          <span class="cat-text">食在北航，<br/>带你解锁北航味道。</span>
          <hr/>
        </div>
        <h1 class="h1-text">{{ isLogin ? '欢迎回来。' : '加入我们！' }}</h1>
        <div class="form-container">
          <div class="login-form" v-show="isLogin">
            <div class="inputBox">
              <input type="text" v-model="username" required="required">
              <label>账号</label>
              <i></i>
            </div>
            <div class="inputBox">
              <input type="password" v-model="password" required="required">
              <label>密码</label>
              <i></i>
            </div>
            <button class="btn" @click="login">登录</button>
            <button class="toggle-btn" @click="toggleForm">没有账户？注册</button>
          </div>
          <div class="register-form" v-show="!isLogin">
            <div class="inputBox">
              <input type="text" v-model="username" required="required">
              <label>账号</label>
              <i></i>
            </div>
            <div class="inputBox">
              <input type="text" v-model="email" required="required">
              <label>邮箱</label>
              <i></i>
            </div>
            <div class="inputBox">
              <input type="password" v-model="password" required="required">
              <label>密码</label>
              <i></i>
            </div>
            <div class="inputBox">
              <input type="password" v-model="confirmPassword" required="required">
              <label>确认密码</label>
              <i></i>
            </div>
            <button class="btn" @click="signup">注册</button>
            <button class="toggle-btn" @click="toggleForm">已有账户？登录</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import apiClient from '../axios';
import { ElMessage } from 'element-plus';

export default {
  data() {
    return {
      isLogin: true,
      username: '',
      password: '',
      confirmPassword: '',
      email: ''
    };
  },
  watch: {
    isLogin(newVal) {
      document.title = newVal ? '欢迎回来' : '加入我们';
    }
  },
  created() {
    document.title = this.isLogin ? '欢迎回来' : '加入我们';
  },
  methods: {
    toggleForm() {
      this.isLogin = !this.isLogin;
    },
    login() {
      apiClient.post('http://127.0.0.1:8000/users/login/', {
        username: this.username,
        password: this.password,
      })
        .then(() => {
          this.$router.push('/');
        })
        .catch(error => {
          console.error(error);
          ElMessage({
            message: '账户或密码错误',
            type: 'error',
            duration: 3000,
            showClose: true,
            customClass: 'large-message-font'
          });
        });
    },
    signup() {
      if (this.password !== this.confirmPassword) {
        ElMessage({
            message: '密码不匹配',
            type: 'error',
            duration: 3000,
            showClose: true,
            customClass: 'large-message-font'
          });
        return;
      }
      apiClient.post('http://127.0.0.1:8000/users/signup/', {
        username: this.username,
        password: this.password,
        email: this.email,
      })
        .then(response => {
          console.log(response.data);
          ElMessage({
            message: '注册成功',
            type: 'success',
            duration: 3000,
            showClose: true,
            customClass: 'large-message-font'
          });
        })
        .catch(error => {
          console.error(error);
          ElMessage({
            message: '注册发生错误',
            type: 'error',
            duration: 3000,
            showClose: true,
            customClass: 'large-message-font'
          });
        });
    }
  }
};
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Ma+Shan+Zheng&family=Noto+Sans+SC:wght@100..900&display=swap');

* {
  margin: 0;
  padding: 0;
  font-family: 'Noto Sans SC', sans-serif;
}

.box {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-image: url('@/assets/background.png');
  background-size: cover;
  background-repeat: no-repeat;
  background-attachment: fixed;
  background-color: white;
  overflow: hidden;
  z-index: 1;
}

.box .content {
  width: 90vw;
  height: 85vh;
  background-color: white;
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
  width: 33vw;
  height: 70vh;
  border-radius: 40px;
  -webkit-backdrop-filter: blur(1px);
  backdrop-filter: blur(1px);
  background: white;
  padding: 60px;
  box-sizing: border-box;
  position: absolute;
  right: 10%;
  transition: 1s;
}

.box .content .login-wrapper .top-tips {
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: flex-start;
  text-align: left;
  margin-bottom: 0px;
}

.box .content .login-wrapper .top-tips .cat-text {
  font-family: 'Noto Sans SC', sans-serif;
  font-size: 42px;
  font-weight: 700;
}

.box .content .login-wrapper .top-tips hr {
  width: 100%;
  border: none;
  border-top: 3px solid #ccc;
  margin-top: 10px;
}

.box .content .login-wrapper h1 {
  font-size: 30px;
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
  margin: 10px 0;
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
  background-color: white !important;
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

/* 新增样式 */
.inputBox {
  position: relative;
  width: 100%;
  margin: 20px 0;
}

.inputBox input {
  width: 100%;
  padding: 15px 0 10px; /* 增加上下内边距来提高输入框高度 */
  background: transparent;
  outline: none;
  box-shadow: none;
  border: none;
  color: #000;
  font-size: 1em;
  letter-spacing: 0.1em;
  transition: 0.5s;
  border-bottom: 1px solid rgba(0, 0, 0, 0.5);
}

.inputBox label {
  position: absolute;
  left: 0;
  top: 10px; /* 初始位置 */
  padding: 10px 0 5px;
  pointer-events: none;
  font-size: 1em;
  color: rgba(0, 0, 0, 0.5);
  text-transform: uppercase;
  letter-spacing: 0.1em;
  transition: 0.5s;
}

.inputBox input:valid ~ label,
.inputBox input:focus ~ label {
  color: #b0a4e3;
  transform: translateY(-30px); /* 向上移动 */
  font-size: 0.65em;
}

.inputBox i {
  position: absolute;
  left: 0;
  bottom: 0;
  width: 100%;
  height: 2px;
  background: #000;
  overflow: hidden;
}

.inputBox i::before {
  content: '';
  position: absolute;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(90deg, #EEBD89, #D13ABD, #C973FF, #6CC6CB, #9FA5D5, #EAD6EE);
  animation: runing 1s linear infinite;
  transition: 0.5s;
}

.inputBox input:valid ~ i::before,
.inputBox input:focus ~ i::before {
  left: 0;
}

@keyframes runing {
  0% {
    background-position-x: 0;
  }
  100% {
    background-position-x: 250px;
  }
}
</style>
