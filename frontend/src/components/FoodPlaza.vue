<template>
  <div class="container black">
    <div class="sidebar">
      <h5 class="title">美食广场</h5>
      <select v-model="selectedCanteen" @change="filterResults">
        <option value="全选">所有食堂</option>
        <option value="学一食堂">学一食堂</option>
        <option value="学二食堂">学二食堂</option>
        <option value="学三食堂">学三食堂</option>
        <option value="学四食堂">学四食堂</option>
        <option value="学五食堂">学五食堂</option>
        <option value="学六食堂">学六食堂</option>
        <option value="教工食堂">教工食堂</option>
        <option value="清真食堂">清真食堂</option>
        <option value="合一厅">合一厅</option>
        <option value="东区第一食堂">东区第一食堂</option>
        <option value="鼓瑟轩">鼓瑟轩</option>
        <option value="西区清真食堂">西区清真食堂</option>
        <option value="西区第一食堂">西区第一食堂</option>
        <option value="西区第二食堂">西区第二食堂</option>
        <option value="西区第三食堂">西区第三食堂</option>
      </select>
      <select v-model="selectedDish" @change="filterResults">
        <option value="所有菜品">所有菜品</option>
        <option value="鸡">鸡</option>
        <option value="猪">猪</option>
        <option value="羊">羊</option>
        <option value="香锅">香锅</option>
        <option value="汉堡">汉堡</option>
      </select>
      <div v-if="selectedCanteen !== '全选'" class="favorite">
        <p>收藏{{ selectedCanteen }}</p>
        <img
          :src="isSubscribed ? require('@/assets/sub.svg') : require('@/assets/unsub.svg')"
          class="favorite-icon"
          @click="toggleSubscription"
          :alt="isSubscribed ? 'Subscribed' : 'Unsubscribed'"
        />
      </div>
      <p class="recommend-title">或者......</p>
      <p class="recommend-subtitle">输入你的需求，<br/>让我们为你推荐！</p>
      <textarea class="textarea" placeholder="今天想吃什么？" v-model="inputText"></textarea>
      <textarea class="textarea2" placeholder="llm_answer" v-model="llm_answer" disabled
                readonly></textarea>
      <button class="search-button" @click="searchResults">查询</button>
    </div>
    <div class="content">
      <div class="results-header">
        <span class="results-title">共{{ filteredComments.length }}条搜索结果</span>
      </div>
      <div class="results-container">
        <div class="grid">
          <div class="card" v-for="comment in filteredComments" :key="comment.id"
               @click="goToDetail(comment.dish_id)">
            <img :src="getImage(comment.image)" :alt="comment.title" class="card-img">
            <h2 class="card-title">{{ comment.title }}</h2>
            <p class="card-text">
              {{
                `${comment.restaurant_name} | ${comment.grade.toFixed(1)}分 | 平均${comment.price.toFixed(2)}元`
              }}</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import apiClient from '../axios';
import {ElMessage} from 'element-plus';

export default {
  data() {
    return {
      inputText: '',
      selectedCanteen: '全选',
      selectedDish: '所有菜品',
      comments_list: [],
      isFavorite: false,
      isSubscribed: false,
      llm_answer: '大模型等待你的询问',
    };
  },
  computed: {
    filteredComments() {
      let filtered = this.comments_list;

      if (this.selectedCanteen !== '全选') {
        filtered = filtered.filter(comment => comment.restaurant_name.includes(this.selectedCanteen));
      }

      if (this.selectedDish !== '所有菜品') {
        filtered = filtered.filter(comment => comment.title.includes(this.selectedDish));
      }

      return filtered;
    }
  },
  methods: {
    getImage(url) {
      return url
    },
    filterResults() {
      // 筛选逻辑不需要额外处理，因为筛选在computed中已经实现
    },
    // 收藏
    toggleSubscription() {
      this.isSubscribed = !this.isSubscribed;
      const action = this.isSubscribed ? 'subscribed to' : 'unsubscribed from';
      console.log(`${action} ${this.selectedCanteen}`);
      const message = this.isSubscribed ? `已收藏 ${this.selectedCanteen}` : `取消收藏 ${this.selectedCanteen}`;
      ElMessage({
        message: message,
        type: 'info',
        duration: 3000,
        showClose: true,
        customClass: 'large-message-font'
      });
      apiClient.post(`http://127.0.0.1:8000/users/collect-restaurant/`, {
        "restaurant_name": this.selectedCanteen,
      })
        .then(() => {
        })
        .catch(error => {
          ElMessage({
            message: '没有这个食堂',
            type: 'error',
            duration: 3000,
            showClose: true,
            customClass: 'large-message-font'
          });
        });
    },
    getList() {
      apiClient.post('http://127.0.0.1:8000/comment/search-comment', {
        restaurant_name: this.selectedCanteen,
        dish_name: this.selectedDish
      })
        .then(response => {
          this.comments_list = response.data.comments;
          this.filterResults(); // 调用筛选方法
        })
        .catch(error => {
          console.error('Error fetching data: ', error);
        });
    },
    searchResults() {
      console.log('Selected Canteen:', this.selectedCanteen);
      console.log('Selected Dish:', this.selectedDish);

      apiClient.post('http://127.0.0.1:8000/comment/search-comment', {
        search: this.inputText,
        restaurant_name: this.selectedCanteen,
        dish_name: this.selectedDish
      })
        .then(response => {
          this.comments_list = response.data.comments;
          this.filterResults(); // 调用筛选方法
        })
        .catch(error => {
          console.error('Error fetching data: ', error);
        });

      this.llm_answer = '结果加载中';
      apiClient.post('http://127.0.0.1:8000/comment/get-llm-answer', {
        search: this.inputText,
      })
        .then(response => {
          this.llm_answer = response.data.llm_answer;
        })
        .catch(error => {
          console.error('Error fetching data: ', error);
        });
    },
    goToDetail(id) {
      this.$router.push({name: 'detail', params: {id}});
    },
  },
  mounted() {
    // 页面加载时自动查询
    this.getList();
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
  background-color: hsl(0, 0%, 100%);
  color: hsl(240, 10%, 3.9%);
}

.black {
  overflow: hidden;
  color : black;
}
.container {
  display: flex;
  height: 100vh; /* 设置高度为视口高度 */
}

.sidebar {
  width: 20%;
  height: 100vh;
  margin: 0;
  padding: 0;
  overflow-y: auto; /* 当内容超过高度时出现滚动条 */
  overflow-x: hidden; /* 隐藏水平滚动条 */
  box-sizing: border-box; /* 包括padding在内的高度 */
  text-align: left; /* 确保文字左对齐 */
}

.content {
  width: 80%;
  padding: 1rem;
  height: 100vh;
  overflow-y: auto; /* 当内容超过高度时出现滚动条 */
  box-sizing: border-box; /* 包括padding在内的高度 */
  display: flex;
  flex-direction: column;
}

.title {
  font-family: 'Ma Shan Zheng', sans-serif;
  font-size: 3.4rem;
  border-bottom: 2px solid #f5f5f5;
  padding-bottom: 0.25rem;
  margin-bottom: 1rem; /* 增加与下拉选择表单的距离 */
}

select {
  font-size: 1.25rem; /* 调整字体大小 */
  margin-top: 1rem; /* 增加与上面的距离 */
}

.subtitle {
  font-size: 1.25rem;
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
  font-size: 1.8rem;
  font-weight: 600;
  margin-bottom: 0.5rem;
}

.recommend-subtitle {
  font-size: 1.4rem;
  margin-top: 0;
}

.textarea {
  width: 100%;
  box-sizing: border-box; /* 确保宽度包括padding和border */
  height: 3rem;
  padding: 0.5rem;
  border-radius: 0.5rem;
  font-size: 1.2rem;
  resize: none;
  font-family: 'Noto Sans SC', sans-serif;
  border: 1px solid #ccc;
}

.textarea2 {
  width: 100%;
  box-sizing: border-box; /* 确保宽度包括padding和border */
  height: 15rem;
  padding: 0.5rem;
  border-radius: 0.5rem;
  font-size: 1.2rem;
  resize: none;
  font-family: 'Noto Sans SC', sans-serif;
  border: 1px solid #ccc;
  color: black;
}

.search-button {
  margin-top: 1rem;
  width: 100%; /* 确保按钮宽度适应sidebar */
  background-color: black;
  color: white;
  padding: 0.5rem 1rem;
  border-radius: 0.5rem;
  font-family: 'Noto Sans SC', sans-serif;
  border: none;
  cursor: pointer;
}

.favorite {
  display: flex;
  align-items: center;
  font-size: 1rem;
  margin-top: 0.5rem;
}

.favorite p {
  margin: 0;
}

.favorite-icon {
  margin-left: 1rem;
  cursor: pointer;
  width: 24px;
  height: 24px;
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
  overflow-y: auto; /* 当内容超过高度时出现滚动条 */
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
  margin-bottom: 0.25rem; /* 减少与详情文本的间距 */
  font-size: 2.25rem;
  font-weight: 700;
  text-align: left;
  font-family: 'Noto Sans SC', sans-serif;
}

.card-text {
  margin-top: 0.25rem; /* 减少与标题的间距 */
  font-size: 100%;
  text-align: left;
  font-family: 'Noto Sans SC', sans-serif;
}

.pagination {
  display: none; /* 隐藏分页按钮 */
}
</style>
