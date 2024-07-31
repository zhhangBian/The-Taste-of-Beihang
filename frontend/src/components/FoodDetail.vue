<template>
  <div class="bg-white text-black">
    <div class="container">
      <div class="col-span-1">
        <h1 class="text-8xl font-mashan border-b border-gray pb-1 mb-1 flex items-center">
          {{ dish.name }}
          <button @click="toggleSubscription" class="icon-button ml-4">
            <img :src="isSubscribed ? require('@/assets/sub.svg') : require('@/assets/unsub.svg')"
                 alt="Subscription status" class="icon enlarged-icon">
          </button>
        </h1>
        <p class="text-2xl font-noto mb-9">{{ dish.address }}</p>
        <div class="mt-4">
          <h2 class="text-4xl font-noto border-b border-gray pb-1 mb-1">总体评价</h2>
          <p :class="getColor(dish.overall_rating)" class="text-7xl font-serif">
            {{ dish.overall_rating.toFixed(1) }}</p>
        </div>
        <div class="mt-4">
          <h2 class="text-4xl font-noto border-b border-gray pb-1 mb-1">口味</h2>
          <p :class="getColor(dish.flavor_rating)" class="text-7xl font-noto">
            {{ dish.flavor_rating.toFixed(1) }}</p>
        </div>
        <div class="mt-4">
          <h2 class="text-4xl font-noto border-b border-gray pb-1 mb-1">价格</h2>
          <p :class="getColor(dish.prices)" class="text-7xl font-noto">
            {{ dish.prices.toFixed(1) }}</p>
        </div>
        <div class="mt-4">
          <h2 class="text-4xl font-noto border-b border-gray pb-1 mb-1">排队时长</h2>
          <p :class="getColor(dish.waiting_time)" class="text-7xl font-noto">
            {{ dish.waiting_time.toFixed(1) }}</p>
        </div>
      </div>
      <div class="col-span-4">
        <div class="top-container">
          <img :src="currentImage" alt="Delicious dish"
               class="w-full h-auto rounded-lg decreased-height">
        </div>
        <div class="bottom-container mt-4">
          <div class="reviews-container">
            <h2 class="mt-4 text-3xl font-man font-bold border-b border-gray pb-1 mb-1">
              吃过的怎么说？</h2>
            <div class="reviews-inner-container mt-4">
              <div v-for="(comment, index) in comments" :key="index" class="review-item">
                <div class="flex items-center space-x-4">
                  <div class="avatar-container">
                    <img :src="comment.avatar" alt="User avatar" class="user-avatar">
                  </div>
                  <div class="review-description flex-1">
                    <div class="flex items-center justify-between">
                      <p class="font-man font-bold">{{ comment.title }} &ensp;<span
                        class="font-man text-zinc-400">{{
                          formatDate(comment.date)
                        }}吃过&ensp;</span>
                      </p>
                      <div class="flex space-x-2 ml-auto">
                        <button @click="toggleLike(comment.id)" class="icon-button">
                          <img
                            :src="likedComments.includes(comment.id) ? require('@/assets/like.svg') : require('@/assets/unlike.svg')"
                            alt="Like/Unlike" class="icon">
                        </button>
                      </div>
                    </div>
                    <p class="font-man text-zinc-500">{{ getCommentTitle(comment) }}</p>
                    <p class="font-man font-medium">{{ comment.content }}</p>
                  </div>
                </div>
                <hr class="my-2 hr-gray" v-if="index < comments.length - 1">
              </div>
            </div>
          </div>
          <div class="write-review-container ">
            <div class="flex-container mt-4 font-man font-bold border-b border-gray pb-1 mb-1">
  <h2 class="mt-4 font-man font-bold border-b border-gray pb-1 mb-1 text-3xl inline-block">写下你的评论！</h2>
  <div class="btn bg-black text-white text-xl inline-block ml-auto">
    <label for="image-upload">
      上传图片
      <input
        id="image-upload"
        type="file"
        accept="image/*"
        @change="handleImageUpload"
        style="display: none;"
      />
    </label>
  </div>
</div>
            <div class="mt-4">
              <div class="flex items-center space-x-4 rating-container"
                   v-for="(rating, index) in ratings" :key="index">
                <span class="font-man rating-label">{{ rating.label }}</span>
                <input type="range" class="range" :value="rating.value" min="0" max="5" step="0.1"
                       @input="updateRating(index, $event)">
                <span>{{ parseFloat(rating.value).toFixed(1) }}</span>
              </div>
              <textarea
                class="w-full increased-height mt-4 padding-2 rounded-lg font-man resize-none"
                placeholder="帮助大家了解这道菜吧！" v-model="newReview.comment"></textarea>
              <button class="mt-4 bg-black text-white py-2 px-4 rounded-lg font-man"
                      @click="submitReview">提交
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import apiClient from '../axios'; // 导入 Axios 实例
import { ElMessage } from 'element-plus';

export default {
  props: {
    id: {
      type: Number,
      required: true,
    },
  },
  data() {
    return {
      imageFiles: [], //新加
      dish: {
        id: 114514,
        name: '麻辣香锅',
        address: '学四食堂南侧',
        overall_rating: 4.5,
        flavor_rating: 4.9,
        prices: 2.5,
        waiting_time: 3.5,
        image: 'https://placehold.co/400x300'
      },
      currentImageIndex: 0,
      images: [
        'https://placehold.co/400x300', // 示例图片
        'https://placehold.co/400x300?text=Image2' // 示例图片
      ],
      comments: [
        {
          id: 1,
          author_name: 'Jew',
          date: '2024-05-18 09:15:00',
          avatar: 'https://placehold.co/50x50',
          grade: 4.0,
          flavour: 4.0,
          price: 2.0,
          waiting_time: 3.0,
          content: '感觉不如新北二楼的麻辣香锅'
        },
        {
          id: 2,
          author_name: '时间的彷徨',
          date: '2024-06-18 12:20:00',
          avatar: 'https://placehold.co/50x50',
          grade: 4.0,
          flavour: 4.0,
          price: 4.0,
          waiting_time: 4.0,
          content: '觉得这家不好吃的都是sb'
        },
        {
          id: 3,
          author_name: '传奇co助教myk',
          date: '2024-07-27 16:45:00',
          avatar: 'https://placehold.co/50x50',
          grade: 4.9,
          flavour: 4.0,
          price: 3.5,
          waiting_time: 3.2,
          content: '少年，代码你要亲自写，屎你要亲自去吃；未来可期，拼尽全力。当你为未来付出踏踏实实努力的时候，那些你觉得看不到的人，和遇不到的风景，都终将在你生命里出现。'
        },
        {
          id: 4,
          author_name: '张三',
          date: '2024-05-18 09:15:00',
          avatar: 'https://placehold.co/50x50',
          grade: 3.8,
          flavour: 4.2,
          price: 3.0,
          waiting_time: 2.5,
          content: '味道还不错，但是排队时间有点长。'
        },
        {
          id: 5,
          author_name: '李四',
          date: '2024-04-22 11:45:00',
          avatar: 'https://placehold.co/50x50',
          grade: 2.5,
          flavour: 3.0,
          price: 1.5,
          waiting_time: 2.0,
          content: '价格有点贵，性价比不高。'
        },
        {
          id: 6,
          author_name: '王五',
          date: '2024-07-10 19:30:00',
          avatar: 'https://placehold.co/50x50',
          grade: 4.7,
          flavour: 4.8,
          price: 3.5,
          waiting_time: 3.7,
          content: '总体感觉很好，推荐大家尝试！'
        }
      ],
      likedComments: [],
      isSubscribed: false,  // 初始化订阅状态为未订阅
      ratings: [
        {label: '总体评价', value: 0},
        {label: '价格', value: 0},
        {label: '口味', value: 0},
        {label: '排队时长', value: 0}
      ],
      newReview: {
        comment: ''
      }
    };
  },
  computed: {
    currentImage() {
      return this.images[this.currentImageIndex];
    }
  },
  methods: {
    handleImageUpload(event) { //新加
      const files = event.target.files;
      if (!files.length) return;
      this.imageFiles = Array.from(files); 
      console.log(this.imageFiles); 
    },
    getCookie(name) {
      let cookieValue = null;
      if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
          const cookie = cookies[i].trim();
          if (cookie.substring(0, name.length + 1) === (name + '=')) {
            cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
            break;
          }
        }
      }
      return cookieValue;
    },
    get_dish_detail() {

      apiClient.get(`http://127.0.0.1:8000/dish/detail/${this.id}/`)
        .then(response => {
          this.dish.name = response.data.name;
          this.dish.image = response.data.image;

          this.dish.address = response.data.restaurant_name;
          this.dish.overall_rating = response.data.overall_rating;
          this.dish.flavor_rating = response.data.flavor_rating;
          this.dish.prices = response.data.prices;
          this.dish.waiting_time = response.data.waiting_time;
          this.comments = response.data.comments;

          this.images = response.data.images;
        })
        .catch(error => {
          console.error('Error fetching dish details:', error);
        });
    },
    submitReview() {
      // 提交评论的逻辑
      console.log('New Review Submitted:', this.newReview);
      apiClient.post(`http://127.0.0.1:8000/users/create-comment/`, {
        "title": this.dish.name + "好吃！",
        "content": this.newReview.comment,
        "dish_name": this.dish.name,

        "restaurant_name": this.dish.address,

        "grade": this.ratings[0].value,
        "price": this.ratings[1].value,
        "flavour": this.ratings[2].value,
        "waiting_time": this.ratings[3].value,
      })
        .then(() => {
          this.get_dish_detail();
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
      return `总体评价 ${comment.grade.toFixed(1)} |
      口味 ${comment.flavour.toFixed(1)} |
      价格 ${comment.price.toFixed(1)} |
      排队时长 ${comment.waiting_time.toFixed(1)}`;
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
    toggleSubscription() {
      this.isSubscribed = !this.isSubscribed;
      const message = this.isSubscribed ? `已收藏 ${this.dish.name}` : `取消收藏 ${this.dish.name}`;
      console.log(message);
      ElMessage({
            message: message,
            type: 'info',
            duration: 3000,
            showClose: true,
            customClass: 'large-message-font'
          });

      apiClient.post(`http://127.0.0.1:8000/users/collect-dish/`, {
        "restaurant_name": this.dish.address,
        "dish_name": this.dish.name,
      })
        .then(() => {
        })
        .catch(error => {
          alert("没有这个菜品哦");
        });
    },
    updateRating(index, event) {
      this.ratings[index].value = parseFloat(event.target.value);
      console.log(this.ratings[index].value);
    },
    startImageSlider() {
      setInterval(() => {
        this.currentImageIndex = (this.currentImageIndex + 1) % this.images.length;
      }, 3000); // 每3秒切换一次图片
    }
  },
  watch: {
    'dish.name': function (newName) {
      document.title = `详情 - ${newName}`;
    }
  },
  mounted() {
    this.get_dish_detail();
    document.title = `详情 - ${this.dish.name}`;
    console.log('FoodDetail mounted with ID:', this.id);
    this.startImageSlider();
  },
};
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Noto+Serif+SC:wght@200..900&family=ZCOOL+KuaiLe&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Ma+Shan+Zheng&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Ma+Shan+Zheng&family=Noto+Sans+SC:wght@100..900&display=swap');
.inline-block {  
    display: inline-block;  
}  
.flex-container {
  display: flex;
  align-items: flex-start; /* 垂直方向上不改变对齐方式 */
  justify-content: space-between; /* 水平方向上在容器两端留白 */
}

.btn {
  /* 按钮的基础样式 */
  padding: 0.5em 1em; /* 根据需要调整内边距 */
  margin-right: 10%;
  margin-top: 1%;
  white-space: nowrap; /* 防止文本换行 */
  cursor: pointer; /* 鼠标悬停时显示手型图标 */
}

.text-xl {
  line-height: 1.5;
  font-size: 1rem; /* 根据需要调整字体大小 */
}

.ml-auto {
  margin-left: auto; /* 推到右侧 */
}
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
  overflow: hidden;
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

.col-span-4 {
  grid-column: span 4;
}

.border-b {
  border-bottom: 1px solid #e2e8f0;
}

.p-6 {
  padding: 24px;
}

.rounded-lg {
  border-radius: 12px;
}

.text-8xl {
  font-size: 3rem;
  line-height: 0.9;
  text-align: left; /* 左对齐 */
}

.text-7xl {
  font-size: 2.5rem;
  line-height: 0.1;
  margin-top: 25px;
  text-align: left; /* 左对齐 */
}

.text-4xl {
  font-size: 2rem;
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
  width: 95%;
}

.h-auto {
  height: auto;
}

.rounded-full {
  border-radius: 50%;
}

.mt-4 {
  margin-top: 10px;
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

.review-description {
  text-align: left; /* 确保reviews部分左对齐 */
}

.review-item .font-man {
  margin: 0; /* 确保单个review中没有行距 */
}

.reviews-container {
  max-height: 280px; /* 设置reviews容器的最大高度 */
}

.reviews-inner-container {
  max-height: 280px; /* 设置reviews容器的最大高度 */
  overflow-y: auto; /* 添加垂直滚动条 */
}

.decreased-height {
  max-height: 400px; /* 降低图片的高度 */
  object-fit: cover;
}

.increased-height {
  height: 7rem; /* 增大文本框的高度 */
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
  height: 1rem; /* 调整大小 */
  width: 1rem; /* 调整大小 */
  vertical-align: bottom; /* 保持图标底部与文字底部对齐 */
}

.enlarged-icon {
  height: 1.5rem; /* 调整图标放大后的高度 */
  width: 1.5rem; /* 调整图标放大后的宽度 */
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
  width: 120px; /* 调整这个宽度来对齐文字 */
}

.avatar-container {
  flex-shrink: 0;
  width: 8%;
}

.user-avatar {
  width: 100%;
  height: auto;
  border-radius: 50%;
  object-fit: cover;
}

.top-container {
  display: flex;
  justify-content: space-between; /* 调整为左右排列 */
}

.bottom-container {
  display: flex;
  justify-content: space-between; /* 调整为左右排列 */
}

.reviews-container, .write-review-container {
  width: 48%; /* 每个容器占一半宽度 */
}
</style>
