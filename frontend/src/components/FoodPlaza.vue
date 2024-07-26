<template>
  <div class="container">
    <div class="sidebar">
      <h1 class="title">美食广场</h1>
      <p class="subtitle">按食堂搜索</p>
      <button class="filter-button" @click="filterResults">筛选</button>
      <p class="recommend-title">或者......</p>
      <p class="recommend-subtitle">输入你的需求，<br/>让我们为你推荐！</p>
      <textarea class="textarea" placeholder="今天想吃什么？" v-model="query"></textarea>
      <button class="search-button" @click="searchResults">查询</button>
    </div>
    <div class="content">
      <div class="results-header">
        <span class="results-title">共{{ comments_count }}条搜索结果</span>
      </div>
      <div class="results-container">
        <div class="grid">
          <div class="card" v-for="comment in comments_list" :key="comment.id">
            <img :src="comment.image" :alt="comment.title" class="card-img">
            <h2 class="card-title">{{ comment.title }}</h2>
            <p class="card-text">{{ comment.details }}</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      query: '',
      comments_count: 114514,
      comments_list: [
        // 保留之前的搜索结果数据
        {
          id: 1,
          image: 'https://placehold.co/400x300',
          title: '麻辣香锅',
          details: '学六食堂 | 4.5分 | 平均20元'
        },
        {
          id: 2,
          image: 'https://placehold.co/400x300',
          title: '宫保鸡丁',
          details: '学五食堂 | 4.7分 | 平均25元'
        },
        {
          id: 3,
          image: 'https://placehold.co/400x300',
          title: '红烧排骨',
          details: '学一食堂 | 4.8分 | 平均30元'
        },
        {
          id: 4,
          image: 'https://placehold.co/400x300',
          title: '鱼香肉丝',
          details: '学四食堂 | 4.6分 | 平均22元'
        },
        {
          id: 5,
          image: 'https://placehold.co/400x300',
          title: '青椒炒肉',
          details: '学二食堂 | 4.3分 | 平均18元'
        },
        {
          id: 6,
          image: 'https://placehold.co/400x300',
          title: '香菇鸡丁',
          details: '学三食堂 | 4.4分 | 平均20元'
        },
        {
          id: 7,
          image: 'https://placehold.co/400x300',
          title: '糖醋里脊',
          details: '学五食堂 | 4.5分 | 平均24元'
        },
        {
          id: 8,
          image: 'https://placehold.co/400x300',
          title: '蒜蓉炒虾',
          details: '学六食堂 | 4.7分 | 平均28元'
        },
        {
          id: 9,
          image: 'https://placehold.co/400x300',
          title: '酸菜鱼',
          details: '学一食堂 | 4.9分 | 平均35元'
        },
        {
          id: 10,
          image: 'https://placehold.co/400x300',
          title: '红烧狮子头',
          details: '学四食堂 | 4.6分 | 平均26元'
        },
        {
          id: 11,
          image: 'https://placehold.co/400x300',
          title: '干锅花菜',
          details: '学二食堂 | 4.4分 | 平均20元'
        },
        {
          id: 12,
          image: 'https://placehold.co/400x300',
          title: '蒜苔炒肉',
          details: '学三食堂 | 4.3分 | 平均19元'
        },
        {
          id: 13,
          image: 'https://placehold.co/400x300',
          title: '辣子鸡丁',
          details: '学五食堂 | 4.7分 | 平均27元'
        },
        {
          id: 14,
          image: 'https://placehold.co/400x300',
          title: '红烧茄子',
          details: '学六食堂 | 4.5分 | 平均21元'
        },
        {
          id: 15,
          image: 'https://placehold.co/400x300',
          title: '番茄炒蛋',
          details: '学一食堂 | 4.8分 | 平均15元'
        },
        {
          id: 16,
          image: 'https://placehold.co/400x300',
          title: '梅菜扣肉',
          details: '学四食堂 | 4.9分 | 平均32元'
        },
        {
          id: 17,
          image: 'https://placehold.co/400x300',
          title: '土豆牛肉',
          details: '学二食堂 | 4.6分 | 平均25元'
        },
      ],
    };
  },
  methods: {
    filterResults() {
      // 筛选逻辑
    },
    searchResults() {
      axios.post('http://127.0.0.1:8000/comment/search-comment', {query: this.query})
          .then(response => {
            this.comments_count = response.data.comments_count;
            this.comments_list = response.data.comments;
          })
          .catch(error => {
            console.error('Error fetching data: ', error);
          });
    }
  }
};
</script>

<style scoped>
  @import url('https://fonts.googleapis.com/css2?family=Noto+Serif+SC:wght@200..900&family=ZCOOL+KuaiLe&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Ma+Shan+Zheng&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Ma+Shan+Zheng&family=Noto+Sans+SC:wght@100..900&display=swap');

body {
  font-family: 'Noto Sans SC', sans-serif;
  margin: 0;
  padding: 0;
  display: flex;
  flex-direction: column;
  background-color: hsl(0, 0%, 100%);
  color: hsl(240, 10%, 3.9%);
}

.container {
  display: flex;
  height: 100vh; /* 设置高度为视口高度 */
  padding: 1rem;
}

.sidebar {
  width: 20%;
  padding: 1rem;
  text-align: left; /* 确保内容左对齐 */
}

.content {
  width: 80%;
  padding: 1rem;
  display: flex;
  flex-direction: column;
}

.title {
  font-family: 'Ma Shan Zheng', sans-serif;
  font-size: 4.5rem;
  border-bottom: 2px solid #f5f5f5;
  padding-bottom: 0.25rem;
  margin-bottom: 0.25rem;
}

.subtitle {
  font-size: 1.5rem;
}

.filter-button {
  margin-top: 0.5rem;
  background-color: hsl(240, 4.8%, 95.9%);
  color: hsl(240, 5.9%, 10%);
  padding: 0.25rem 0.75rem;
  border-radius: 9999px;
  font-family: 'Noto Sans SC', sans-serif;
  border: none;
  cursor: pointer;
  font-size: 1.25rem;
}

.recommend-title {
  margin-top: 2rem;
  font-size: 3rem;
  font-weight: 600;
  margin-bottom: 0.5rem;
}

.recommend-subtitle {
  font-size: 1.875rem;
  margin-top: 0;
}

.textarea {
  width: 100%;
  height: 20rem;
  margin-top: 1rem;
  padding: 0.5rem;
  border-radius: 0.5rem;
  resize: none;
  font-family: 'Noto Sans SC', sans-serif;
  border: 1px solid #ccc;
}

.search-button {
  margin-top: 1rem;
  background-color: black;
  color: white;
  padding: 0.5rem 1rem;
  border-radius: 0.5rem;
  font-family: 'Noto Sans SC', sans-serif;
  border: none;
  cursor: pointer;
}

.results-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.results-title {
  font-size: 1.875rem;
  font-family: 'Noto Sans SC', sans-serif;
}

.results-container {
  flex: 1;
  overflow: auto; /* 当内容超过高度时出现滚动条 */
  margin-top: 1rem;
}

.grid {
  display: grid;
  grid-template-columns: repeat(1, minmax(0, 1fr));
  gap: 1rem;
}

@media (min-width: 640px) {
  .grid {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }
}

@media (min-width: 1024px) {
  .grid {
    grid-template-columns: repeat(3, minmax(0, 1fr));
  }
}

.card {
  background-color: hsl(240, 4.8%, 95.9%);
  padding: 1rem;
  border-radius: 0.5rem;
}

.card img {
  width: 100%;
  height: 8rem;
  object-fit: cover;
  border-radius: 0.5rem;
}

.card-title {
  margin-top: 0.5rem;
  font-size: 1.25rem;
  font-weight: 700;
  font-family: 'Noto Sans SC', sans-serif;
}

.card-text {
  font-size: 1rem;
  font-family: 'Noto Sans SC', sans-serif;
}

.pagination {
  display: none; /* 隐藏分页按钮 */
}
</style>
