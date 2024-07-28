<template>
    <div class="container">
      <h1 class="main-title">{{ greeting }}，{{ user.name }}</h1>
      <hr class="divider" />
      <div class="content">
        <div class="profile-section">
          <div class="card">
            <h2 class="subtitle">个人信息</h2>
            <hr class="card-divider" />
            <p><strong>昵称:</strong> {{ user.name }}</p>
            <p><strong>账号（UID）:</strong> {{ user.uid }}</p>
            <p><strong>性别:</strong> {{ user.gender }}</p>
            <p><strong>学院:</strong> {{ user.college }}</p>
            <p><strong>个性签名:</strong> {{ user.signature }}</p>
            <p><strong>头像:</strong> <img :src="user.avatar" alt="user-avatar" class="avatar" /></p>
            <button class="edit-button" @click="editProfile">修改个人信息</button>
          </div>
        </div>
        <div class="stats-section">
          <div class="card">
            <h2 class="subtitle">统计</h2>
            <hr class="card-divider" />
            <div class="stats-content">
              <div class="stats-left">
                <p><strong>点菜率:</strong> {{ stats.orderRate }}%</p>
                <p><strong>累计就餐:</strong> {{ stats.totalMeals }}</p>
                <p><strong>累计消费:</strong> {{ stats.totalSpend }}元</p>
                <p><strong>累计收藏:</strong> {{ stats.totalFavorites }}</p>
              </div>
              <div class="stats-right">
                <p><strong>点赞评论数:</strong> {{ stats.totalLikes }}</p>
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
          gender: '男',
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
        } else if (hour >= 14 && hour < 21) {
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
      }
    }
  }
  </script>
  
  <style scoped>
  .container {
    display: flex;
    flex-direction: column;
    padding: 24px;
    background-color: var(--background, #fff);
    color: var(--foreground, #1a1a1a);
  }
  
  .main-title {
    font-size: 3.5rem;
    font-weight: bold;
    margin-bottom: 8px;
    text-align: left;
  }
  
  .divider {
    border: none;
    border-top: 2px solid #000;
    margin-bottom: 16px;
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
    flex: 1;
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
    font-size: 2rem;
    font-weight: 700;
    margin-top: 4px;
    margin-bottom: 4px;
    text-align: left;
  }
  
  .card, .chart-card {
    background-color: var(--card, #fff);
    padding: 20px;
    border-radius: 0.5rem;
    border: 1px solid #ccc;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    margin-bottom: 24px;
    flex: 1;
    text-align: left;
    font-size: 1.1rem;
  }
  
  .stats-content {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
  }
  
  .stats-left, .stats-right {
    width: 48%; /* Slightly less than half to account for gap */
  }
  
  .card-divider {
    margin: 8px 0;
    border: none;
    border-top: 2px solid #ccc;
  }
  
  .avatar {
    border-radius: 50%;
    width: 100px;
    height: 100px;
  }
  
  .edit-button {
    margin-top: 16px;
    background-color: var(--secondary, #e0e0e0);
    color: var(--secondary-foreground, #1a1a1a);
    padding: 8px 16px;
    border-radius: 0.25rem;
    cursor: pointer;
    border: none;
    transition: background-color 0.3s;
  }
  
  .edit-button:hover {
    background-color: var(--secondary-hover, #cfcfcf);
  }
  
  .charts {
    display: flex;
    justify-content: space-between;
    margin-top: auto;
  }
  
  .chart-container {
    text-align: center;
  }
  
  .chart-title {
    font-weight: 600;
  }
  
  .chart-image {
    margin-top: 8px;
    width: 200px;
    height: 200px;
    border-radius: 50%;
  }
  </style>
  