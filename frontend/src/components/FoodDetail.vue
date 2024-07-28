<template>
  <div class="bg-white text-black">
    <div class="container">
      <div class="col-span-1">
        <h1 class="text-8xl font-mashan border-b border-gray pb-1 mb-1">{{ dish.name }}</h1>
        <p class="text-2xl font-noto mb-9">{{ dish.address }}</p>
        <div class="mt-4">
          <h2 class="text-4xl font-noto border-b border-gray pb-1 mb-1">总体评价</h2>
          <p :class="getColor(dish.overallRating)" class="text-7xl font-serif">
            {{ dish.overallRating.toFixed(1) }}</p>
        </div>
        <div class="mt-4">
          <h2 class="text-4xl font-noto border-b border-gray pb-1 mb-1">口味</h2>
          <p :class="getColor(dish.flavorRating)" class="text-7xl font-noto">
            {{ dish.flavorRating.toFixed(1) }}</p>
        </div>
        <div class="mt-4">
          <h2 class="text-4xl font-noto border-b border-gray pb-1 mb-1">价格</h2>
          <p :class="getColor(dish.priceRating)" class="text-7xl font-noto">
            {{ dish.priceRating.toFixed(1) }}</p>
        </div>
        <div class="mt-4">
          <h2 class="text-4xl font-noto border-b border-gray pb-1 mb-1">排队时长</h2>
          <p :class="getColor(dish.timeRating)" class="text-7xl font-noto">
            {{ dish.timeRating.toFixed(1) }}</p>
        </div>
      </div>
      <div class="col-span-2">
        <img :src="dish.image" alt="Delicious dish" class="w-full h-auto rounded-lg decreased-height">
        <h2 class="mt-4 text-3xl font-man font-bold border-b border-gray pb-1 mb-1">吃过的怎么说？</h2>
        <div class="mt-4 reviews-container">
          <div v-for="(comment, index) in comments" :key="index">
            <div class="review-item">
              <div class="flex items-center space-x-4">
                <img :src="comment.avatar" alt="User avatar" class="w-12 h-12 rounded-full">
                <div class="review-content flex-1">
                  <div class="flex items-center justify-between">
                    <p class="font-man font-bold">{{ comment.name }} &ensp;<span class="font-man text-zinc-400">{{ formatDate(comment.date) }}吃过&ensp;</span></p>
                    <div class="flex space-x-2 ml-auto">
                      <button @click="toggleLike(comment.id)" class="icon-button">
                        <img :src="likedComments.includes(comment.id) ? require('@/assets/like.svg') : require('@/assets/unlike.svg')" alt="Like/Unlike" class="icon">
                      </button>
                    </div>
                  </div>
                  <p class="font-man text-zinc-500">{{ getCommentTitle(comment) }}</p>
                  <p class="font-man font-medium">{{ comment.content }}</p>
                </div>
              </div>
            </div>
            <hr class="my-2 hr-gray" v-if="index < comments.length - 1">
          </div>
        </div>
      </div>
      <div class="col-span-2">
        <img src="https://placehold.co/400x300" alt="Hotpot dish" class="w-full h-auto rounded-lg decreased-height">
        <h2 class="mt-4 text-3xl font-man font-bold border-b border-gray pb-1 mb-1">写下你的评论！</h2>
        <div class="mt-4">
          <div class="flex items-center space-x-4 rating-container" v-for="(rating, index) in ratings" :key="index">
            <span class="font-man rating-label">{{ rating.label }}</span>
            <input type="range" class="range" :value="rating.value" min="0" max="5" step="0.1" @input="updateRating(index, $event)">
            <span>{{ parseFloat(rating.value).toFixed(1) }}</span>
          </div>
          <textarea class="w-full increased-height mt-4 padding-2 rounded-lg font-man resize-none" placeholder="帮助大家了解这道菜吧！" v-model="newReview.comment"></textarea>
          <button class="mt-4 bg-black text-white py-2 px-4 rounded-lg font-man" @click="submitReview">提交</button>
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
      dish: {
        name: '麻辣香锅',
        address: '学四食堂南侧',
        overallRating: 4.5,
        flavorRating: 4.9,
        priceRating: 2.5,
        timeRating: 3.5,
        image: 'https://placehold.co/400x300'
      },
      comments: [
        {
          id: 1,
          name: 'Jew',
          date: '2024-05-18 09:15:00',
          avatar: 'https://placehold.co/50x50',
          overallRating: 4.0,
          flavorRating: 4.0,
          priceRating: 2.0,
          timeRating: 3.0,
          content: '感觉不如新北二楼的麻辣香锅'
        },
        {
          id: 2,
          name: '时间的彷徨',
          date: '2024-06-18 12:20:00',
          avatar: 'https://placehold.co/50x50',
          overallRating: 4.0,
          flavorRating: 4.0,
          priceRating: 4.0,
          timeRating: 4.0,
          content: '觉得这家不好吃的都是sb'
        },
        {
          id: 3,
          name: '传奇co助教myk',
          date: '2024-07-27 16:45:00',
          avatar: 'https://placehold.co/50x50',
          overallRating: 4.9,
          flavorRating: 4.0,
          priceRating: 3.5,
          timeRating: 3.2,
          content: '少年，代码你要亲自写，屎你要亲自去吃；未来可期，拼尽全力。当你为未来付出踏踏实实努力的时候，那些你觉得看不到的人，和遇不到的风景，都终将在你生命里出现。'
        },
        {
          id: 4,
          name: '张三',
          date: '2024-05-18 09:15:00',
          avatar: 'https://placehold.co/50x50',
          overallRating: 3.8,
          flavorRating: 4.2,
          priceRating: 3.0,
          timeRating: 2.5,
          content: '味道还不错，但是排队时间有点长。'
        },
        {
          id: 5,
          name: '李四',
          date: '2024-04-22 11:45:00',
          avatar: 'https://placehold.co/50x50',
          overallRating: 2.5,
          flavorRating: 3.0,
          priceRating: 1.5,
          timeRating: 2.0,
          content: '价格有点贵，性价比不高。'
        },
        {
          id: 6,
          name: '王五',
          date: '2024-07-10 19:30:00',
          avatar: 'https://placehold.co/50x50',
          overallRating: 4.7,
          flavorRating: 4.8,
          priceRating: 3.5,
          timeRating: 3.7,
          content: '总体感觉很好，推荐大家尝试！'
        }
      ],
      likedComments: [],
      ratings: [
        { label: '总体评价', value: 0 },
        { label: '口味', value: 0 },
        { label: '价格', value: 0 },
        { label: '排队时长', value: 0 }
      ],
      newReview: {
        content: ''
      }
    };
  },
  methods: {
    submitReview() {
      // 提交评论的逻辑
      console.log('New Review Submitted:', this.newReview);
    },
    fetchComments() {
      axios.get(`http://127.0.0.1:8000/dish/get-dish-comments`, {
        params: {
          "dish_address": this.dish.address,
          "dish_name": this.dish.name
        }
      })
        .then(response => {
          this.dish.overallRating = response.data.overallRating;
          this.dish.flavorRating = response.data.flavorRating;
          this.dish.priceRating = response.data.priceRating;
          this.dish.timeRating = response.data.timeRating;
          this.comments = response.data.comments_list;
        })
        .catch(error => {
          console.error('Error fetching comments:', error);
        });
    },
    formatDate(dateString) {
      const date = new Date(dateString);
      const now = new Date();
      const diffInSeconds = Math.floor((now - date) / 1000);

      const intervals = {
        年: 31536000,
        个月: 2592000,
        天: 86400,
        小时: 3600,
        分钟: 60,
        秒: 1
      };

      let counter;
      for (const [key, value] of Object.entries(intervals)) {
        counter = Math.floor(diffInSeconds / value);
        if (counter > 0) {
          return `${counter} ${key}前`;
        }
      }

      return '刚刚';
    },
    getColor(score) {
      if (score >= 4.0) {
        return 'text-green-500';
      } else if (score >= 3.0) {
        return 'text-yellow-500';
      } else {
        return 'text-red-500';
      }
    },
    getCommentTitle(comment) {
      return `总体评价 ${comment.overallRating.toFixed(1)} | 口味 ${comment.flavorRating.toFixed(1)} | 价格 ${comment.priceRating.toFixed(1)} | 排队时长 ${comment.timeRating.toFixed(1)}`;
    },
    toggleLike(commentId) {
      const index = this.likedComments.indexOf(commentId);
      if (index !== -1) {
        this.likedComments.splice(index, 1);
        console.log(`取消喜欢评论${commentId}`);
      } else {
        this.likedComments.push(commentId);
        console.log(`已喜欢评论${commentId}`);
      }
    },
    updateRating(index, event) {
      this.ratings[index].value = parseFloat(event.target.value);
    }
  },
  mounted() {
    this.fetchComments();
    document.title = `详情 - ${this.dish.name}`;
  }
};
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Noto+Serif+SC:wght@200..900&family=ZCOOL+KuaiLe&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Ma+Shan+Zheng&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Ma+Shan+Zheng&family=Noto+Sans+SC:wght@100..900&display=swap');

body {
  font-family: 'Noto Sans SC', sans-serif;
  background-color: #ffffff;
  color: #000000;
  padding: 24px;
  margin: 0;
  text-align: left; /* 全局左对齐 */
}

.container {
  display: grid;
  grid-template-columns: 1fr;
  gap: 12px;
  background-color: #ffffff;
}

@media (min-width: 768px) {
  .container {
    grid-template-columns: repeat(5, 1fr);
  }
}

.col-span-1 {
  grid-column: span 1;
}

.col-span-2 {
  grid-column: span 2;
}

.border-b {
  border-bottom: 2px solid #e2e8f0;
}

.p-6 {
  padding: 24px;
}

.rounded-lg {
  border-radius: 12px;
}

.text-8xl {
  font-size: 4rem;
  line-height: 0.9;
  text-align: left; /* 左对齐 */
}

.text-7xl {
  font-size: 4rem;
  line-height: 0.1;
  text-align: left; /* 左对齐 */
}

.text-4xl {
  font-size: 2.25rem;
  line-height: 1.1;
  text-align: left; /* 左对齐 */
}

.text-3xl {
  font-size: 1.875rem;
  line-height: 1.1;
  text-align: left; /* 左对齐 */
}

.text-2xl {
  font-size: 1.5rem;
  line-height: 1.1;
  text-align: left; /* 左对齐 */
}

.text-green-500 {
  color: #48bb78;
}

.text-red-500 {
  color: #f56565;
}

.text-yellow-500 {
  color: #ecc94b;
}

.text-zinc-400 {
  color: #cbd5e0;
}

.text-zinc-500 {
  color: #a0aec0;
}

.font-mashan {
  font-family: 'Ma Shan Zheng', sans-serif;
}

.font-noto {
  font-family: 'Noto Serif SC', serif;
}

.font-man {
  font-family: 'Noto Sans SC', sans-serif;
}

.font-serif {
  font-family: 'Noto Serif SC', serif;
}

.font-bold {
  font-weight: bold;
}

.font-medium {
  font-weight: 500;
}

.grid {
  display: grid;
  gap: 12px;
}

.flex {
  display: flex;
}

.items-start {
  align-items: flex-start;
}

.items-center {
  align-items: center;
}

.space-x-4 {
  gap: 16px;
}

.space-x-2 {
  gap: 8px;
}

.w-full {
  width: 100%;
}

.h-auto {
  height: auto;
}

.rounded-full {
  border-radius: 50%;
}

.mt-4 {
  margin-top: 16px;
}

.mb-1 {
  margin-bottom: 4px;
}

.pb-1 {
  padding-bottom: 4px;
}

.pb-4 {
  padding-bottom: 16px;
}

.pt-4 {
  padding-top: 16px;
}

.resize-none {
  resize: none;
}

.bg-black {
  background-color: #000000;
}

.bg-white {
  background-color: #ffffff;
}

.text-white {
  color: white;
}

.py-2 {
  padding-top: 8px;
  padding-bottom: 8px;
}

.px-4 {
  padding-left: 16px;
  padding-right: 16px;
}

.border-gray {
  border-color: #e2e8f0;
}

.hr-gray {
  border-top: 1px solid #e2e8f0;
  margin-left: 0;
  margin-right: 0;
}

.review-content {
  text-align: left; /* 确保reviews部分左对齐 */
}

.review-item .font-man {
  margin: 0; /* 确保单个review中没有行距 */
}

.reviews-container {
  max-height: 425px; /* 设置reviews容器的最大高度 */
  overflow-y: auto; /* 添加垂直滚动条 */
}

.decreased-height {
  max-height: 400px; /* 降低图片的高度 */
  object-fit: cover;
}

.increased-height {
  height: 12rem; /* 增大文本框的高度 */
}

.padding-2 {
  padding: 0.1rem; /* 增加内边距 */
}

.icon-button {
  background: transparent;
  border: none;
  padding: 0;
  margin: 0;
  cursor: pointer;
}

.icon {
  height: 1rem; /* Adjust the size as needed */
  width: 1rem;  /* Adjust the size as needed */
}

.range {
  width: 300px;
  height: 5px;
  -webkit-appearance: none;
  appearance: none;
  background: #ddd;
  outline: none;
  border-radius: 5px;
  overflow: hidden;
}

.range::-webkit-slider-thumb {
  -webkit-appearance: none;
  appearance: none;
  width: 20px;
  height: 20px;
  background: #4CAF50;
  border-radius: 50%;
  cursor: pointer;
}

.range::-moz-range-thumb {
  width: 20px;
  height: 20px;
  background: #4CAF50;
  border-radius: 50%;
  cursor: pointer;
}

.rating-container {
  align-items: center;
}

.rating-label {
  width: 80px; /* 调整这个宽度来对齐文字 */
}
</style>
