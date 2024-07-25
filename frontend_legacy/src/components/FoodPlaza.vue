<template>
  <div class="container">
    <div class="sidebar">
      <h1 class="title">美食广场</h1>
      <p class="subtitle">按食堂搜索</p>
      <button class="filter-button" @click="filterResults">筛选</button>
      <p class="recommend-title">或者......</p>
      <p class="recommend-subtitle">输入你的需求，<br />让我们为你推荐！</p>
      <textarea class="textarea" placeholder="今天想吃什么？" v-model="query"></textarea>
      <button class="search-button" @click="searchResults">查询</button>
    </div>
    <div class="content">
      <div class="results-header">
        <span class="results-title">共114条搜索结果</span>
      </div>
      <div class="grid">
        <div class="card" v-for="item in items" :key="item.id">
          <img :src="item.image" :alt="item.title" class="card-img">
          <h2 class="card-title">{{ item.title }}</h2>
          <p class="card-text">{{ item.details }}</p>
        </div>
      </div>
      <div class="pagination">
        <button class="pagination-button" @click="prevPage">
          <span>«</span>
          <span>上一页</span>
        </button>
        <button class="pagination-button" @click="nextPage">
          <span>下一页</span>
          <span>»</span>
        </button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      query: '',
      items: [
        {
          id: 1,
          image: 'https://placehold.co/400x300',
          title: '麻辣香锅',
          details: '学六食堂 | 4.5分 | 平均20元'
        },
        // 更多项目
      ],
    };
  },
  methods: {
    filterResults() {
      // 筛选逻辑
    },
    searchResults() {
      // 查询逻辑
    },
    prevPage() {
      // 上一页逻辑
    },
    nextPage() {
      // 下一页逻辑
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
  flex-direction: column;
  padding: 1rem;
}

@media (min-width: 768px) {
  .container {
    flex-direction: row;
  }
}

.sidebar {
  width: 100%;
  padding: 1rem;
  text-align: left; /* 确保内容左对齐 */
}

@media (min-width: 768px) {
  .sidebar {
    width: 20%;
  }
}

.content {
  width: 100%;
  padding: 1rem;
}

@media (min-width: 768px) {
  .content {
    width: 80%;
  }
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

.grid {
  display: grid;
  grid-template-columns: repeat(1, minmax(0, 1fr));
  gap: 1rem;
  margin-top: 1rem;
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
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-top: 1rem;
}

.pagination-button {
  display: flex;
  align-items: center;
  color: hsl(240, 5.9%, 10%);
  font-size: 1rem;
  cursor: pointer;
}

.pagination-button span {
  font-size: 1.25rem;
}
</style>
