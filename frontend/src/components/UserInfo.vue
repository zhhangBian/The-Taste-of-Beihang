<template>
  <div class="container">
    <h1 class="main-title">{{ greeting }}，{{ user.name }}</h1>
    <hr class="divider"/>
    <div class="content">
      <div class="profile-section">
        <div class="card">
          <h2 class="subtitle">个人信息</h2>
          <hr class="card-divider"/>
          <div class="input-group">
            <label for="name"><strong>昵称</strong></label>
            <input type="text" id="name" v-model="user.name"/>
          </div>
          <div class="input-group">
            <label for="username"><strong>账号</strong></label>
            <input type="text" id="username" v-model="user.username" disabled/>
          </div>
          <div class="input-group">
            <label for="college"><strong>学院</strong></label>
            <input type="text" id="college" v-model="user.college"/>
          </div>
          <div class="input-group">
            <label for="signature"><strong>个性签名</strong></label>
            <input type="text" id="signature" v-model="user.signature"/>
          </div>
          <div class="input-group">
            <label><strong>头像</strong></label>
            <img :src="user.avatar" alt="user-avatar" class="avatar"/>
          </div>
          <div class="button-group">
            <input type="file" @change="onFileChange" style="display: none;" ref="fileInput">
            <button class="upload-button" @click="triggerFileUpload">上传头像</button>
            <button class="edit-button" @click="editProfile">完成信息修改</button>
          </div>
        </div>
      </div>
      <div class="stats-section">
        <div class="card">
          <h2 class="subtitle">统计</h2>
          <hr class="card-divider"/>
          <div class="stats-content">
            <div class="stats-left">
              <!--              <p><strong>点亮菜品:</strong> {{ stats.orderRate }}%</p>-->
              <p><strong>累计就餐:</strong> {{ stats.meal_count }}次</p>
              <p><strong>累计消费:</strong> {{ stats.price_sum }}元</p>
              <p><strong>累计收藏:</strong> {{ stats.collect_sum }}次</p>
            </div>
            <div class="stats-right">
              <!--              <p><strong>已点赞的评论数:</strong> {{ stats.like_sum }}</p>-->
              <p><strong>最高消费:</strong> {{ stats.price_highest }}元（{{
                  stats.price_highest_place
                }}）
              </p>
              <p><strong>最低消费:</strong> {{ stats.price_lowest }}元（{{
                  stats.price_lowest_place
                }}）
              </p>
              <p><strong>平均消费:</strong> {{ stats.price_mean }}元
              </p>
            </div>
          </div>
        </div>
        <div class="chart-card">
          <div class="charts">
            <div class="chart-container">
              <h3 class="chart-title">就餐地点统计</h3>
              <div id="locationChart" class="chart-image"></div>
            </div>
            <div class="chart-container">
              <h3 class="chart-title">就餐消费统计</h3>
              <div id="expenseChart" class="chart-image"></div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import * as echarts from 'echarts';
import apiClient from '../axios';
import {ElMessage} from 'element-plus';

export default {
  props: {
    id: {
      type: Number,
      required: true,
    },
  },
  data() {
    return {
      user: {
        id: Number(this.$route.params.id),
        name: '时间的彷徨',
        username: 'zxwswd114514',
        college: '计算机学院',
        signature: '我是sb我是sb我是sb我是sb',
        avatar: 'https://placehold.co/100x100'
      },
      stats: {

        meal_count: 65,
        price_sum: 98.7,
        collect_sum: 32,
        like_sum: 35,
        price_highest: 35,
        price_highest_place: '麻辣香锅/六食堂',
        price_lowest: 2,
        price_lowest_place: '汉堡/四食堂',
        price_mean: 92.4,
      },
      place_dict: [
        {value: 1048, name: '六食堂'},
        {value: 735, name: '四食堂'},
        {value: 580, name: '三食堂'},
        {value: 484, name: '二食堂'},
        {value: 300, name: '一食堂'}
      ],
      time_dict: [
        {value: 1048, name: '早餐'},
        {value: 735, name: '午餐'},
        {value: 580, name: '晚餐'},
        {value: 484, name: '夜宵'},
        {value: 300, name: '其他'}
      ]
    };
  },
  computed: {
    greeting() {
      const hour = new Date().getHours();
      if (hour >= 6 && hour < 11) {
        return '早上好';
      } else if (hour >= 11 && hour < 14) {
        return '中午好';
      } else if (hour >= 14 && hour < 19) {
        return '下午好';
      } else if (hour >= 19 && hour < 23) {
        return '晚上好';
      } else {
        return '晚安';
      }
    }
  },
  methods: {
    getStatics() {
      apiClient.get(`http://127.0.0.1:8000/users/get-statics/`, {})
        .then(response => {
          this.stats.meal_count = response.data.meal_count;
          this.stats.price_sum = response.data.price_sum;
          this.stats.collect_sum = response.data.collect_sum;
          this.stats.price_highest = response.data.price_highest;
          this.stats.price_highest_place = response.data.price_highest_place;
          this.stats.price_lowest = response.data.price_lowest;
          this.stats.price_lowest = response.data.price_lowest_place;
          this.stats.price_mean = response.data.price_mean;

          this.time_dict = response.data.time_dict;
          this.place_dict = response.data.place_dict;
        })
        .catch(error => {
          console.error('Error fetching comments:', error);
        });
    },
    editProfile() {
      ElMessage({
        message: '个人信息修改完成，请刷新页面应用修改',
        type: 'success',
        duration: 3000,
        showClose: true,
        customClass: 'large-message-font'
      });
      apiClient.post(`http://127.0.0.1:8000/users/update-user/`, {
        "name": this.user.name,
        "school": this.user.college,
        "motto": this.user.signature,
      })
        .then(() => {
          this.get_user_info()
        })
        .catch(error => {
          console.error('Error fetching comments:', error);
        });
    },
    triggerFileUpload() {
      this.$refs.fileInput.click();
    },
    onFileChange(event) {
      const file = event.target.files[0];
      if (file) {
        const formData = new FormData();
        formData.append('img', file);

        // 上传文件到服务器
        apiClient.post('http://127.0.0.1:8000/users/update-avatar/', formData)
          .then(response => {
            this.user.avatar = response.data.avatar;
            alert("头像更新成功");
          })
          .catch(error => {
            console.error('Error uploading file:', error);
          });
      }
    },
    get_user_info() {
      apiClient.get(`http://127.0.0.1:8000/users/get-user-detail/`)
        .then(response => {
          this.user.name = response.data.name;
          this.user.username = response.data.username;
          this.user.college = response.data.school;
          this.user.signature = response.data.motto;
          this.user.avatar = response.data.avatar;
          document.title = `个人中心 - ${this.user.name}`;
        })
        .catch(error => {
          console.error('Error fetching dish details:', error);
        });
    },
    initCharts() {
      // Initialize the location chart
      var locationChart = echarts.init(document.getElementById('locationChart'));
      var locationOption = {
        legend: {
          orient: 'vertical',
          left: 'right',
          top: 'middle'
        },
        tooltip: {
          trigger: 'item'
        },
        series: [
          {
            name: 'Location',
            type: 'pie',
            radius: ['50%'],
            center: ['40%', '50%'],
            avoidLabelOverlap: false,
            label: {
              show: false,
              position: 'center'
            },
            labelLine: {
              show: false
            },
            data: this.place_dict,
            emphasis: {
              itemStyle: {
                shadowBlur: 10,
                shadowOffsetX: 0,
                shadowColor: 'rgba(0, 0, 0, 0.5)'
              }
            }
          }
        ]
      };
      locationChart.setOption(locationOption);

      // Initialize the expense chart
      var expenseChart = echarts.init(document.getElementById('expenseChart'));
      var expenseOption = {
        legend: {
          orient: 'vertical',
          left: 'right',
          top: 'middle'
        },
        tooltip: {
          trigger: 'item'
        },
        series: [
          {
            name: 'Expense',
            type: 'pie',
            radius: ['50%'],
            center: ['40%', '50%'],
            avoidLabelOverlap: false,
            label: {
              show: false,
              position: 'center'
            },
            labelLine: {
              show: false
            },
            data: this.time_dict,
            emphasis: {
              itemStyle: {
                shadowBlur: 10,
                shadowOffsetX: 0,
                shadowColor: 'rgba(0, 0, 0, 0.5)'
              }
            }
          }
        ]
      };
      expenseChart.setOption(expenseOption);
    }
  },
  mounted() {
    this.getStatics();
    this.initCharts();
    this.get_user_info();
  },
}

</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Ma+Shan+Zheng&family=Noto+Sans+SC:wght@100..900&display=swap');

.container {
  display: flex;
  height: auto;
  width: auto;
  flex-direction: column;
  background-color: var(--background, #fff);
  color: var(--foreground, #1a1a1a);
  font-family: 'Noto Sans SC', sans-serif; /* 应用全局字体 */
}

.main-title {
  font-size: 2.4rem;
  font-weight: bold;
  text-align: left !important;
  margin: 0 0 0;
}

.divider {
  border: none;
  border-top: 2px solid #000;
  width: 100%;
  background-color: black;
}

.content {
  display: flex;
  flex-direction: row;
  gap: 16px;
  align-items: stretch;
}

.profile-section {
  padding: 16px;
  display: flex;
  flex-direction: column;
}

.stats-section {
  flex: 2;
  padding: 16px;
  display: flex;
  flex-direction: column;
}

.subtitle {
  display: flex;
  justify-content: flex-start; /* 水平方向从容器的开头开始排列 */
  align-items: flex-start; /* 垂直方向从容器的开头开始排列 */
  font-size: 2rem;
  font-weight: 700;
  text-align: left !important;
}

.card, .chart-card {
  background-color: var(--card, #fff);
  padding: 0 20px;
  border-radius: 0.5rem;
  border: 1px solid #ccc;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  margin-bottom: 24px;
  flex: 0;
  text-align: left !important;
  font-size: 1.1rem;
}

.card-divider {
  margin: 8px 0;
  border: none;
  border-top: 2px solid #ccc;
}

.avatar {
  border-radius: 50%;
  width: 125px;
  height: 125px;
  display: inline-block;
  vertical-align: middle;
  margin-right: 16px;
}

.button-group {
  display: flex;
  justify-content: center;
  gap: 8px;
  margin-top: 16px;
}

.edit-button, .upload-button {
  background-color: #000;
  color: #fff;
  padding: 8px 16px;
  border-radius: 0;
  cursor: pointer;
  border: none;
  transition: background-color 0.3s;
  display: inline-block;
  margin-bottom: 10px;
  font-family: 'Noto Sans SC', sans-serif; /* 设置按钮的字体 */
}

.edit-button:hover, .upload-button:hover {
  background-color: #333;
}

.stats-content {
  box-sizing: border-box;
  display: flex;
  flex-direction: row;
  padding: 0 0 0 0;
  justify-content: space-between;
}

.stats-left, .stats-right {
  padding: 0 0 0 0;
  width: 48%;
}

.charts {
  display: flex;
  justify-content: space-between;
}

.chart-container {
  text-align: center;
  padding: 0 0 0 0;
}

.chart-title {
  margin-top: 10px;
  margin-bottom: 0px;
  margin-left: 0px;
  font-weight: 600;
}

.chart-image {
  width: 220px;
  height: 220px;
}

.input-group {
  display: flex;
  align-items: center;
  margin: 8px 0;
}

.input-group label {
  display: inline-block;
  width: 120px;
}

.input-group input {
  flex: 1;
  padding: 8px;
  border: 1px solid #ccc;
  border-radius: 0.25rem;
  font-size: 1rem;
  font-family: 'Noto Sans SC', sans-serif; /* 设置输入框的字体 */
}

.input-group input[disabled] {
  background-color: #f5f5f5;
  color: #aaa;
}

</style>
