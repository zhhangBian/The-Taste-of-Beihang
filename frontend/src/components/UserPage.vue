<template>  
  <div class="user-container">  
    <div class="user-info">  
      <!-- 使用本地图标或图标库 -->  
      <img src="@/assets/user.svg" alt="User Icon" class="user-icon">  
      <span class="username">{{ userInfo.name }}</span>  
      <span class="uid">UID: {{ userInfo.uid }}</span>  
    </div>  
    <div class="profile">  
      <div class="iro">个人简介</div>
      <div class="info-container">  
  <div class="info-item">  
    <label>性别</label>  
    <span>{{ userInfo.gender }}</span>  
  </div>  
  <div class="info-item">  
    <label>学院</label>  
    <span>{{ userInfo.college }}</span>  
  </div>  
  <div class="info-item">  
    <label>个性签名</label>  
    <span>{{ userInfo.signature }}</span>  
  </div>  
  <button class="open-button">修改个人信息</button> 
</div>  
      </div> 
      <div class="meal-records">  
         <div class="record">最近用餐记录</div>
        <button class="close-button">修改用餐记录</button>  
        <ul>  
          <li v-for="record in mealRecords" :key="record.id">  
            {{ record.date }}  {{ record.meal }}@{{ record.local }} {{ record.money }}  
          </li>  
        </ul> 
        <div class="pagination-container">  
<a href="#" class="prev-page">&laquo; 上一页</a>  
<a href="#" class="next-page">下一页 &raquo;</a>  
</div>
      </div>  
      <div class="favorites">  
         <div class="record">我的收藏</div>
        <button class="close2-button">修改收藏</button>  
        <ul>  
          <li v-for="record in favorites" :key="record.id">  
            {{ record.date }}  {{ record.meal }}@{{ record.local }} {{ record.money }}  
          </li>  
        </ul>
        <div class="pagination-container">  
<a href="#" class="prev-page">&laquo; 上一页</a>  
<a href="#" class="next-page">下一页 &raquo;</a>  
</div>
      </div>
  </div>
  <div class="horizontal-line"></div>  
  <div class="statistics">  
      <div class="iroo">统计</div>
      <div class="info-container">  
  <div class="info-item2">  
    <label>点亮菜品</label>  
    <span>{{ statistics.meal }}</span>  
  </div>  
  <div class="info-item2">  
    <label>累计就餐</label>  
    <span>{{ statistics.eat }}</span>  
  </div>  
  <div class="info-item2">  
    <label>累计消费</label>  
    <span>{{ statistics.consume }}</span>  
  </div>  
  <div class="info-item2">  
    <label>累计收藏</label>  
    <span>{{ statistics.collection }}</span>  
  </div> 
  <div class="info-item2">  
    <label>累计喜欢</label>  
    <span>{{ statistics.like }}</span>  
  </div> 
</div>  
      </div> 
      <div class="Location"> 
      <div class="location">就餐地点统计</div>
      </div>
      <div class="Location2"> 
      <div class="location">就餐消费统计</div>
      </div>
</template>  
  
<script setup>  
import { ref } from 'vue'; 
// 模拟的用户信息  
const userInfo = ref({  
  name: 'Loading...',  
  uid: 'Loading...',  
  gender: 'Loading...',  
  college: 'Loading...',  
  signature: 'Loading...'  
});  
const statistics = ref({
  meal : 'Loading...',
  eat : 'Loading...',
  consume: 'Loading...',
  collection: 'Loading...',
  like : 'Loading...'
})
  
// 模拟的用餐记录  
const mealRecords = ref([  
  { id: 1, date: '2023-04-01', meal: '汉堡薯条套餐牛肉面', money:'10元',local:'新北食堂'},  
  { id: 2, date: '2023-04-02', meal: '汉堡薯条套餐寿司' , money:'20元',local:'新北'},  
]);  
  
// 模拟的收藏列表  
const favorites = ref([  
{ id: 1, date: '2023-04-01', meal: '汉堡薯条套餐牛肉面', money:'10元',local:'新北食堂'},  
  { id: 2, date: '2023-04-02', meal: '汉堡薯条套餐寿司' , money:'20元',local:'新北'},  
  { id: 3, date: '2023-04-02', meal: '汉堡薯条套餐' , money:'20元',local:'新北'},
  { id: 3, date: '2023-04-02', meal: '汉堡薯条套餐' , money:'20元',local:'新北'},
  { id: 5, date: '2023-04-02', meal: '寿司' , money:'20元',local:'新北'},
]);  
  
// 模拟从后端获取用户数据  
function fetchStatisticsData() {  
  setTimeout(() => {  
    statistics.value = {  
      meal : '92.4%',
      eat : '65',
      consume: '98.7元',
      collection: '32',
      like : '35'
    };  
  }, 1000); // 假设请求需要1秒  
}  
function fetchUserData() {  
  setTimeout(() => {  
    userInfo.value = {  
      name: '时间的彷徨',  
      uid: '123413413342456',  
      gender: '男',  
      college: '计算机科学与技术学院',  
      signature: '牛子王牛子王牛子王牛子王'  
    };  
  }, 1000); // 假设请求需要1秒  
}  
  
// 假设的编辑个人信息的方法  
function editProfile() {  
  alert('编辑个人信息功能尚未实现');  
}  
  
// 假设的编辑用餐记录的方法  
function editMealRecords() {  
  alert('修改用餐记录功能尚未实现');  
}  
  
// 组件加载时获取用户数据  
fetchUserData();  
fetchStatisticsData();
</script>  
  
<style scoped>  
.user-container {  
  display: flex;  
  flex-direction: column;  
}  
  
.user-info {  
  display: flex;  
  position: fixed;
  top: 20px; /* 根据需要调整 */  
  left: 20px; 
  width: 5%;
}  
  
.user-icon {  
  position: fixed; 
  top: 1%; 
  left: 1%; 
  width: 5%;
}  
.username {
  position: fixed;
  display: flex; 
  top: 2.5%; 
  left: 6.5%; 
  width: 100%;
  font-weight: bold;
  font-family:Impact, Haettenschweiler, 'Arial Narrow Bold', sans-serif;
  color: black;
}
.uid {
  position: fixed; 
  display: flex;
  justify-content:flex-start;
  top: 7%; 
  left: 6.5%; 
  width: 100%; 
  font-weight: bold;
  font-family:'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif;
  max-width: 200px;
  color: black;
}
.profile {  
position: fixed; /* 使用固定定位 */  
top: 15%; /* 距离顶部10% */  
left: 2%; /* 先左移50%，然后通过transform左移自身宽度的50%，实现居中（如果您想要居中显示的话） */  
width: 20%; /* 宽度为屏幕宽度的1/4 */  
min-height: 33.3%; /* 高度大致为屏幕高度的1/3，但这里使用min-height以防内容溢出 */  
box-sizing: border-box; /* 确保padding和border不会增加元素的额外宽度和高度 */  
background-color: #f9f9f9; /* 背景色，可根据需要调整 */  
box-shadow: 0 4px 8px rgba(0,0,0,0.1); /* 可选：添加一些阴影以增强视觉效果 */  
overflow-y: auto; /* 如果内容超出高度，允许垂直滚动 */  
}  
  
.iro {  
/* 将字体放在容器的左上方 */  
margin-top: 0; /* 移除默认的margin-top，确保它紧贴容器顶部 */  
display: flex;
justify-content: flex-start;
font-weight: bold; /* 加粗字体 */  
font-size: 2rem; /* 放大字体，您可以根据需要调整这个值 */  
/* 其他样式，如颜色、字体家族等 */  
color: #333; /* 字体颜色 */  
font-family: Arial, sans-serif; /* 字体家族 */  
margin-bottom: 4%;
}
.info-container {  
display: flex;  
justify-content: flex-start;
flex-direction: column; /* 垂直排列字段 */  
color: #333; /* 字体颜色 */  
font-family: Arial, sans-serif; /* 字体家族 */
font-weight: bold; /* 加粗字体 */   
gap: 3vh; /* 字段之间的垂直间距 */  
/* 注意：这里不需要特别的对齐设置，因为flex子项默认就是靠左对齐的 */  
}  

.info-item {  
display: flex; /* 使用flex布局来并排显示label和span */  
justify-content: flex-start;
color: #333; /* 字体颜色 */  
font-family: Arial, sans-serif; /* 字体家族 */
font-weight: bold; /* 加粗字体 */    
gap: 8%; /* label和span之间的水平间距 */  
/* align-items: flex-start; 实际上是默认的，但显式写出也无妨 */  
}  

.info-item2 {  
margin :0 0;
display: flex; /* 使用flex布局来并排显示label和span */  
justify-content: flex-start;
color: #333; /* 字体颜色 */  
font-family: Arial, sans-serif; /* 字体家族 */
font-weight: bold; /* 加粗字体 */    
gap: 6%; /* label和span之间的水平间距 */  
 align-items: flex-start; 
}  

/* label和span的宽度可以根据需要设置，但通常label会有一个最小宽度，而span则根据内容自动调整 */  
.info-item label,.info-item2 label {  
min-width: 60px; /* 确保label有足够的宽度 */  
}  
.open-button {  
/* 定位到容器的底部中心（但在这个例子中，我们不需要定位，因为按钮是profile的直接子元素） */  
/* 宽度可以根据需要设置，或者让它根据内容自动调整 */  
width: 100px; /* 示例宽度 */  
/* 为了让按钮居中，我们可以使用margin: auto来自动分配左右外边距 */  
margin: 0 20%; /* 上下外边距为0，左右外边距自动分配，实现水平居中 */  
/* 也可以添加一些内边距、边框、背景色等样式来美化按钮 */  
padding: 10px;  
border: none;  
background-color: black; 
color: white;  
cursor: pointer;  
}  
.close-button {  
/* 定位到容器的底部中心（但在这个例子中，我们不需要定位，因为按钮是profile的直接子元素） */  
/* 宽度可以根据需要设置，或者让它根据内容自动调整 */  
width: 100px; /* 示例宽度 */  
/* 为了让按钮居中，我们可以使用margin: auto来自动分配左右外边距 */  
margin: 0 0; /* 上下外边距为0，左右外边距自动分配，实现水平居中 */  
/* 也可以添加一些内边距、边框、背景色等样式来美化按钮 */  
padding: 10px;  
border: none;  
font-weight: bold;
background-color: black; 
display: flex;
color: white;  
left :0;
cursor: pointer;   margin-bottom: 1%;
}  

.meal-records{  
  position: fixed; /* 使用固定定位 */  
top: 10%; /* 距离顶部10% */  
left: 25%; /* 先左移50%，然后通过transform左移自身宽度的50%，实现居中（如果您想要居中显示的话） */  
width: 35%; /* 宽度为屏幕宽度的1/4 */  
height: 40%; /* 高度大致为屏幕高度的1/3，但这里使用min-height以防内容溢出 */  
box-sizing: border-box; /* 确保padding和border不会增加元素的额外宽度和高度 */  
background-color: #f9f9f9; /* 背景色，可根据需要调整 */  
box-shadow: 0 4px 8px rgba(0,0,0,0.1); /* 可选：添加一些阴影以增强视觉效果 */  
overflow-y: auto; /* 如果内容超出高度，允许垂直滚动 */  
}  
.record {  
/* 将字体放在容器的左上方 */  
margin-top: 0; /* 移除默认的margin-top，确保它紧贴容器顶部 */  
display: flex;
justify-content: flex-start;
font-weight: bold; /* 加粗字体 */  
font-size: 2.5rem; /* 放大字体，您可以根据需要调整这个值 */  
/* 其他样式，如颜色、字体家族等 */  
color: #333; /* 字体颜色 */  
font-family: Arial, sans-serif; /* 字体家族 */  
margin-bottom: 1%;
}
/* 其他样式可以根据需要添加 */  
.meal-records ul {  
padding: 0; /* 移除 <ul> 的内边距，确保 <li> 紧贴左侧 */  
margin: 0; /* 移除 <ul> 的外边距，确保 <ul> 紧贴其父容器的边缘 */  
list-style-type: none; /* 可选：移除列表项前的默认标记 */  
text-align: left;
font-size: 1.1rem;
font-weight: bold;
color: #333;
}  
.favorites ul{
  padding: 0; /* 移除 <ul> 的内边距，确保 <li> 紧贴左侧 */  
margin: 0; /* 移除 <ul> 的外边距，确保 <ul> 紧贴其父容器的边缘 */  
list-style-type: none; /* 可选：移除列表项前的默认标记 */  
text-align: left;
font-size: 1.1rem;
font-weight: bold;
color: #333;
}

.meal-records li,.favorites li {  
/* 这里通常不需要特别的样式来使 <li> 换行和左对齐，  
   因为 <li> 默认就是块级元素并左对齐。  
   但是，您可以添加一些内边距来改善可读性。  
*/  
/* 其他样式... */  
margin:0;
}
.favorites li {  
  margin-bottom:0;
}
.pagination-container {  
display: flex;  
justify-content: space-between; /* 让上一页和下一页按钮分别靠左右两侧 */  
align-items: flex-end; /* 这会将子项对齐到容器的底部，但注意它要求容器有足够的高度 */  
padding: 10px; /* 容器内边距，根据需要调整 */  
height: 0px; /* 假设的高度，根据实际需求设置 */  
/* 其他样式 */  
}  

.pagination-container a {  
text-decoration: none;  
color: black;  
display: block; /* 如果需要的话，将链接转换为块级元素以更好地控制布局 */  
/* 其他样式，如字体大小、鼠标悬停效果等 */  
}  

/* 上一页和下一页按钮的特定样式 */  
.prev-page {  
/* 这里可以添加一些特定于分页按钮的样式，比如内边距、边框等 */  
padding: 5px 10px;  
border: 1px solid #ccc;  
border-radius: 4px;  
display: flex;
position: absolute;
bottom : 0;
left:0;
}  
.next-page {  
/* 这里可以添加一些特定于分页按钮的样式，比如内边距、边框等 */  
padding: 5px 10px;  
border: 1px solid #ccc;  
border-radius: 4px;  
display: flex;
position: absolute;
bottom : 0;
right:0;
}  

/* 鼠标悬停效果 */  
.pagination-container a:hover {  
background-color: grey;  
}
.favorites{  
  position: fixed; /* 使用固定定位 */  
top: 10%; /* 距离顶部10% */  
left: 62%; /* 先左移50%，然后通过transform左移自身宽度的50%，实现居中（如果您想要居中显示的话） */  
width: 35%; /* 宽度为屏幕宽度的1/4 */  
height: 40%; /* 高度大致为屏幕高度的1/3，但这里使用min-height以防内容溢出 */  
box-sizing: border-box; /* 确保padding和border不会增加元素的额外宽度和高度 */  
background-color: #f9f9f9; /* 背景色，可根据需要调整 */  
box-shadow: 0 4px 8px rgba(0,0,0,0.1); /* 可选：添加一些阴影以增强视觉效果 */  
overflow-y: auto; /* 如果内容超出高度，允许垂直滚动 */  
}  
.close2-button {  
width: 80p; /* 示例宽度 */  
/* 为了让按钮居中，我们可以使用margin: auto来自动分配左右外边距 */  
margin: 0 0; /* 上下外边距为0，左右外边距自动分配，实现水平居中 */  
/* 也可以添加一些内边距、边框、背景色等样式来美化按钮 */  
padding: 10px;  
border: none;  
font-weight: bold;
background-color: black; 
display: flex;
color: white;  
cursor: pointer;   margin-bottom: 1%;
}  
.horizontal-line {  
/* 绘制水平直线 */  
width: 100%; /* 占据整个容器的宽度 */  
height: 2px; /* 直线的高度 */  
background-color: #000; /* 直线的颜色 */  
position: absolute; /* 绝对定位 */  
bottom: 48%; /* 距离容器底部的距离，实现偏下效果 */  
left: 0; /* 从左侧开始 */  
/* 如果你不希望这条线影响到其
他元素的布局，确保父元素有position: relative; */  
} 
.statistics {  
position: fixed; /* 使用固定定位 */  
top: 55%; /* 距离顶部10% */  
left: 2%; /* 先左移50%，然后通过transform左移自身宽度的50%，实现居中（如果您想要居中显示的话） */  
width: 20%; /* 宽度为屏幕宽度的1/4 */  
min-height: 33.3%; /* 高度大致为屏幕高度的1/3，但这里使用min-height以防内容溢出 */  
box-sizing: border-box; /* 确保padding和border不会增加元素的额外宽度和高度 */  
background-color: #f9f9f9; /* 背景色，可根据需要调整 */  
box-shadow: 0 4px 8px rgba(0,0,0,0.1); /* 可选：添加一些阴影以增强视觉效果 */  
overflow-y: auto; /* 如果内容超出高度，允许垂直滚动 */  
}   
.iroo {  
/* 将字体放在容器的左上方 */  
margin-top: 0; /* 移除默认的margin-top，确保它紧贴容器顶部 */  
display: flex;
justify-content: flex-start;
font-weight: bold; /* 加粗字体 */  
font-size: 2.5rem; /* 放大字体，您可以根据需要调整这个值 */  
/* 其他样式，如颜色、字体家族等 */  
color: #333; /* 字体颜色 */  
font-family: Arial, sans-serif; /* 字体家族 */  
margin-bottom: 4%;
}
.Location{  
  position: fixed; /* 使用固定定位 */  
top: 56%; /* 距离顶部10% */  
left: 25%; /* 先左移50%，然后通过transform左移自身宽度的50%，实现居中（如果您想要居中显示的话） */  
width: 35%; /* 宽度为屏幕宽度的1/4 */  
height: 40%; /* 高度大致为屏幕高度的1/3，但这里使用min-height以防内容溢出 */  
box-sizing: border-box; /* 确保padding和border不会增加元素的额外宽度和高度 */  
background-color: #f9f9f9; /* 背景色，可根据需要调整 */  
box-shadow: 0 4px 8px rgba(0,0,0,0.1); /* 可选：添加一些阴影以增强视觉效果 */  
overflow-y: auto; /* 如果内容超出高度，允许垂直滚动 */  
}  
.Location2{  
  position: fixed; /* 使用固定定位 */  
top: 56%; /* 距离顶部10% */  
left: 60%; /* 先左移50%，然后通过transform左移自身宽度的50%，实现居中（如果您想要居中显示的话） */  
width: 35%; /* 宽度为屏幕宽度的1/4 */  
height: 40%; /* 高度大致为屏幕高度的1/3，但这里使用min-height以防内容溢出 */  
box-sizing: border-box; /* 确保padding和border不会增加元素的额外宽度和高度 */  
background-color: #f9f9f9; /* 背景色，可根据需要调整 */  
box-shadow: 0 4px 8px rgba(0,0,0,0.1); /* 可选：添加一些阴影以增强视觉效果 */  
overflow-y: auto; /* 如果内容超出高度，允许垂直滚动 */  
}  
.location {  
/* 将字体放在容器的左上方 */  
margin-top: 0; /* 移除默认的margin-top，确保它紧贴容器顶部 */  
display: flex;
justify-content: flex-start;
font-weight: bold; /* 加粗字体 */  
font-size: 1.5rem; /* 放大字体，您可以根据需要调整这个值 */  
/* 其他样式，如颜色、字体家族等 */  
color: #333; /* 字体颜色 */  
font-family: Arial, sans-serif; /* 字体家族 */  
margin-bottom: 1%;
}
</style>