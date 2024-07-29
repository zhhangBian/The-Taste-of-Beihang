<template>
  <div class="container">
    <h1 class="main-title">{{ greeting }}，{{ user.name }}</h1>
    <hr class="divider" />
    <div class="content">
      <div class="profile-section">
        <div class="card">
          <h2 class="subtitle">个人信息</h2>
          <hr class="card-divider" />
          <div class="input-group">
            <label for="name"><strong>昵称</strong></label>
            <input type="text" id="name" v-model="user.name" />
          </div>
          <div class="input-group">
            <label for="uid"><strong>账号（UID）</strong></label>
            <input type="text" id="uid" v-model="user.uid" disabled />
          </div>
          <div class="input-group">
            <label for="college"><strong>学院</strong></label>
            <input type="text" id="college" v-model="user.college" />
          </div>
          <div class="input-group">
            <label for="signature"><strong>个性签名</strong></label>
            <input type="text" id="signature" v-model="user.signature" />
          </div>
          <div class="input-group">
            <label><strong>头像</strong></label>
            <img :src="user.avatar" alt="user-avatar" class="avatar" />
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
          <hr class="card-divider" />
          <div class="stats-content">
            <div class="stats-left">
              <p><strong>点亮菜品:</strong> {{ stats.orderRate }}%</p>
              <p><strong>累计就餐:</strong> {{ stats.totalMeals }}</p>
              <p><strong>累计消费:</strong> {{ stats.totalSpend }}元</p>
              <p><strong>累计收藏:</strong> {{ stats.totalFavorites }}</p>
            </div>
            <div class="stats-right">
              <p><strong>已点赞的评论数:</strong> {{ stats.totalLikes }}</p>
              <p><strong>最高消费:</strong> {{ stats.highestSpend }}元（{{ stats.highestSpendMeal }}）</p>
              <p><strong>最低消费:</strong> {{ stats.lowestSpend }}元（{{ stats.lowestSpendMeal }}）</p>
            </div>
          </div>
        </div>
        <div class="chart-card">
          <div class="charts">
            <div class="chart-container">
              <h3 class="chart-title">就餐地点统计</h3>
              <img :src="stats.locationChart" alt="pie-chart" class="chart-image" />
            </div>
            <div class="chart-container">
              <h3 class="chart-title">就餐消费统计</h3>
              <img :src="stats.expenseChart" alt="pie-chart" class="chart-image" />
            </div>
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
      user: {
        name: '时间的彷徨',
        uid: 'zxwswd114514',
        college: '计算机学院',
        signature: '我是sb我是sb我是sb我是sb',
        avatar: 'https://placehold.co/100x100'
      },
      stats: {
        orderRate: 92.4,
        totalMeals: 65,
        totalSpend: 98.7,
        totalFavorites: 32,
        totalLikes: 35,
        highestSpend: 35,
        highestSpendMeal: '麻辣香锅/六食堂',
        lowestSpend: 2,
        lowestSpendMeal: '汉堡/四食堂',
        locationChart: 'https://placehold.co/200x200',
        expenseChart: 'https://placehold.co/200x200'
      }
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
  mounted() {
    document.title = `个人中心 - ${this.user.name}`;
  },
  methods: {
    editProfile() {
      alert('点击了修改个人信息');
    },
    triggerFileUpload() {
      this.$refs.fileInput.click();
    },
    onFileChange(event) {
      const file = event.target.files[0];
      if (file) {
        const reader = new FileReader();
        reader.onload = e => {
          this.user.avatar = e.target.result;
        };
        reader.readAsDataURL(file);
      }
    }
  }
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
  margin:0 0 0;
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
align-items: flex-start;  /* 垂直方向从容器的开头开始排列 */
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
  padding :0 0;
}

.chart-title {
  margin-top:10px;
  font-weight: 600;
}

.chart-image {
  margin-top: 1px;
  width: 200px;
  height: 200px;
  border-radius: 50%;
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
