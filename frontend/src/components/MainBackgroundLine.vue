<template>
  <div class="container">
    <div class="content-center">
      <div class="svg-container">
        <img src="@/assets/background2.svg" alt="Background SVG" class="centered-svg">
      </div>
      <div class="customFont" v-html="recommendation"></div>
      <div class="button-container">
        <button v-if="!showBottomButtons" class="top-button" @click="handleTopButtonClick">吃什么?
        </button>
        <div v-if="showBottomButtons" class="bottom-buttons">
          <button class="bottom-button" @click="handleRecordClick()">就这个！</button>
          <button class="bottom-button" @click="handleRenewClick()">换一个</button>
          <button class="bottom-button" @click="handlePlazaClick">去广场看看</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import apiClient from '../axios';
import {ElMessage} from 'element-plus';

export default {
  name: 'CenteredSvgAndTitle',

  data() {
    return {
      showBottomButtons: false,
      recommendation: '今天在BUAA吃什么？', // 默认显示的内容
      dish: '',
      place: '',
    };
  },
  methods: {
    handleTopButtonClick() {
      this.showBottomButtons = true;
      console.log('吃什么?');
      this.get_recommendation();
    },
    handleRenewClick() {
      this.get_recommendation();
    },
    handleRecordClick() {
      if (this.dish === '' || this.place === '') {
        ElMessage({
          message: '菜还没有选择哦',
          type: 'error',
          duration: 3000,
          showClose: true,
          customClass: 'large-message-font'
        });
      } else {
        ElMessage({
          message: '成功添加记录',
          type: 'success',
          duration: 3000,
          showClose: true,
          customClass: 'large-message-font'
        });

        apiClient.post(`http://127.0.0.1:8000/users/add-record/`, {
          "time": '打算去吃！',
          "dish_name": this.dish,
          "restaurant_name": this.place,
          "price": 0,
        })
          .then(() => {
            apiClient.get(`http://127.0.0.1:8000/users/get-records/`)
              .then(() => {
              })
              .catch(error => {
                console.error('Error add records:', error);
              });
          })
          .catch(error => {
            console.error('Error save records:', error);
          });
      }
    },
    handlePlazaClick() {
      console.log('跳转到广场');
      this.$router.push('/plaza');
    },
    get_recommendation() {
      apiClient.get('http://127.0.0.1:8000/dish/get-dish-recommend')
        .then(response => {
          const {place, dish} = response.data;
          this.recommendation = `在<span style="color: #5E17EB;">${place}</span>吃<span style="color: #5E17EB;">${dish}</span>`;
          this.place = place;
          this.dish = dish;
        })
        .catch(error => {
          console.error('Error fetching data: ', error);
        });
    },
    check_login_status() {
      apiClient.get('http://127.0.0.1:8000/users/check-login-status')
        .then(response => {
          response.data.login_status;
          console.log("已登录")
        })
        .catch(error => {
          console.error('Error fetching data: ', error);
          this.$router.push('/login');
        });
    },
  },
  mounted() {
    this.check_login_status();
  }
};
</script>

<style scoped>
.container {
  position: relative;
  width: 100vw;
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  overflow: hidden; /* 防止出现滚动条 */
}

.content-center {
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  position: relative;
  z-index: 2; /* 确保内容在SVG上方 */
  overflow: hidden; /* 防止内部滚动条 */
}

.svg-container {
  position: absolute;
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1; /* 确保SVG在内容下方 */
  overflow: hidden;
}

.centered-svg {
  max-width: 100%;
  max-height: 100%;
}

.customFont {
  font-family: 'Lato';
  font-weight: bold;
  font-size: 5rem;
  text-align: center;
  width: 80%;
  margin: 0; /* 移除可能引起溢出的负边距 */
  z-index: 3; /* 确保字体在SVG上方 */
  position: relative;
}

.button-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-top: 20px; /* 调整这个值来设置按钮容器的垂直位置 */
  z-index: 3; /* 确保按钮在SVG上方 */
  position: relative;
}

.top-button {
  font-size: 28px;
  padding: 15px 30px; /* 统一按钮大小 */
  margin: 10px;
  background-color: black;
  color: white;
  border: none;
  cursor: pointer;
  white-space: nowrap;
  text-align: center;
  width: 200px; /* 统一按钮宽度 */
}

.bottom-buttons {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: row; /* 确保新按钮水平排列 */
}

.bottom-button {
  font-size: 28px;
  padding: 15px 30px; /* 统一按钮大小 */
  margin: 10px;
  background-color: black;
  color: white;
  border: none;
  cursor: pointer;
  white-space: nowrap;
  text-align: center;
  width: 200px; /* 统一按钮宽度 */
}

</style>
