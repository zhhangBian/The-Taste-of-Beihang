<template>
  <div class="bg-white text-black">
    <div class="container">
      <div class="col-span-1">
        <h1 class="text-8xl font-mashan border-b border-gray pb-1 mb-1">{{ dish.title }}</h1>
        <p class="text-2xl font-noto mb-9">{{ dish.location }}</p>
        <div class="mt-4">
          <h2 class="text-4xl font-noto border-b border-gray pb-1 mb-1">总体评价</h2>
          <p class="text-7xl text-green-500 font-serif">{{ dish.overallRating }}</p>
        </div>
        <div class="mt-4" v-for="(rating, key) in dish.ratings" :key="key">
          <h2 class="text-4xl font-noto border-b border-gray pb-1 mb-1">{{ rating.label }}</h2>
          <p class="text-7xl font-noto" :class="rating.color">{{ rating.score }}</p>
        </div>
      </div>
      <div class="col-span-2">
        <img :src="dish.image" alt="Delicious dish"
             class="w-full h-auto rounded-lg decreased-height">
        <h2 class="mt-4 text-3xl font-man font-bold border-b border-gray pb-1 mb-1">
          吃过的怎么说？
        </h2>
        <div class="mt-4 reviews-container">
          <div v-for="comment in comments" :key="comment.id">
            <div class="review-item">
              <div class="flex items-center space-x-4">
                <img :src="comment.avatar" alt="User avatar" class="w-12 h-12 rounded-full">
                <div class="review-content">
                  <p class="font-man font-bold">{{ comment.name }} <span
                      class="font-man text-zinc-400">{{ comment.date }}</span></p>
                  <p class="font-man text-zinc-500">{{ comment.title }}</p>
                  <p class="font-man font-medium">{{ comment.context }}</p>
                </div>
              </div>
            </div>
            <!--            <hr class="my-2 hr-gray" v-if="index < comments.length - 1">-->
          </div>
        </div>
      </div>
      <div class="col-span-2">
        <img src="https://placehold.co/400x300" alt="Hotpot dish"
             class="w-full h-auto rounded-lg decreased-height">
        <h2 class="mt-4 text-3xl font-man font-bold border-b border-gray pb-1 mb-1">
          写下你的评论！
        </h2>
        <div class="mt-4">
          <div class="flex items-center space-x-2" v-for="(rating, index) in ratings" :key="index">
            <span class="font-man">{{ rating.label }}</span>
            <span>⭐⭐⭐⭐⭐</span>
          </div>
          <textarea class="w-full increased-height mt-4 padding-2 rounded-lg font-man resize-none"
                    placeholder="帮助大家了解这道菜吧！" v-model="newReview.comment"></textarea>
          <button class="mt-4 bg-black text-white py-2 px-4 rounded-lg font-man"
                  @click="submitReview">提交
          </button>
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
        title: '麻辣香锅',
        location: '合一楼/学四食堂南侧',
        overallRating: 4.5,
        ratings: [
          {label: '口味', score: 4.9, color: 'text-green-500'},
          {label: '价格', score: 2.5, color: 'text-red-500'},
          {label: '排队时长', score: 3.5, color: 'text-yellow-500'}
        ],

        grade: 4.9,
        price: 114,
        flavor: 3.5,
        waiting_time: 514,

        image: 'https://placehold.co/400x300'
      },
      comments: [
        {
          name: 'Jew',
          date: '昨天吃过',
          avatar: 'https://placehold.co/50x50',
          title: '总体评价 4.0 | 口味 4.0 | 价格 3.0 | 排队时长 3.0',
          context: '感觉不如新北二楼的麻辣香锅'
        },
        {
          name: '时间的彷徨',
          date: '前天吃过',
          avatar: 'https://placehold.co/50x50',
          title: '总体评价 4.0 | 口味 4.0 | 价格 4.0 | 排队时长 4.0',
          context: '觉得这家不好吃的都是sb'
        },
        {
          name: '传奇co助教myk',
          date: '10天前吃过',
          avatar: 'https://placehold.co/50x50',
          title: '总体评价 4.9 | 口味 4.0 | 价格 3.5 | 排队时长 3.2',
          context: '少年，代码你要亲自写，屎你要亲自去吃；未来可期，拼尽全力。当你为未来付出踏踏实实努力的时候，那些你觉得看不到的人，和遇不到的风景，都终将在你生命里出现。'
        },
        {
          name: '时间的彷徨',
          date: '前天吃过',
          avatar: 'https://placehold.co/50x50',
          title: '总体评价 4.0 | 口味 4.0 | 价格 4.0 | 排队时长 4.0',
          context: '觉得这家不好吃的都是sb'
        },
        {
          name: '时间的彷徨',
          date: '前天吃过',
          avatar: 'https://placehold.co/50x50',
          title: '总体评价 4.0 | 口味 4.0 | 价格 4.0 | 排队时长 4.0',
          context: '觉得这家不好吃的都是sb'
        },
        {
          name: '时间的彷徨',
          date: '前天吃过',
          avatar: 'https://placehold.co/50x50',
          title: '总体评价 4.0 | 口味 4.0 | 价格 4.0 | 排队时长 4.0',
          context: '觉得这家不好吃的都是sb'
        },
        {
          name: '时间的彷徨',
          date: '前天吃过',
          avatar: 'https://placehold.co/50x50',
          title: '总体评价 4.0 | 口味 4.0 | 价格 4.0 | 排队时长 4.0',
          context: '觉得这家不好吃的都是sb'
        },
        {
          name: '时间的彷徨',
          date: '前天吃过',
          avatar: 'https://placehold.co/50x50',
          title: '总体评价 4.0 | 口味 4.0 | 价格 4.0 | 排队时长 4.0',
          context: '觉得这家不好吃的都是sb'
        },
        {
          name: '时间的彷徨',
          date: '前天吃过',
          avatar: 'https://placehold.co/50x50',
          title: '总体评价 4.0 | 口味 4.0 | 价格 4.0 | 排队时长 4.0',
          context: '觉得这家不好吃的都是sb'
        }
      ],
      ratings: [
        {label: '总体评价'},
        {label: '口味'},
        {label: '价格'},
        {label: '排队时长'}
      ],
      newReview: {
        context: ''
      }
    };
  },
  methods: {
    submitReview() {
      // 提交评论的逻辑
      console.log('New Review Submitted:', this.newReview);
    },
    fetchComments() {
      const address = this.dish.location;
      const name = this.dish.title;

      axios.post('http://127.0.0.1:8000/dish/get-dish-comments', {query: this.query})
          .then(response => {
            this.grade = response.data.grade;
            this.price = response.data.price;
            this.flavor = response.data.flavor;
            this.waiting_time = response.data.waiting_time;

            this.this.comments = response.data.comments_list;
          })
          .catch(error => {
            console.error('Error fetching comments:', error);
          });
    }
  },
  mounted() {
    this.fetchComments();
  },
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
</style>
