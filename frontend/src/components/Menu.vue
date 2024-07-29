<template>
  <div class="menu-wrapper">
    <div class="content">
      <div class="person-info" @click="navigateToUserCenter(this.id)">
        <img :src="avatar" alt=""/>
        <div class="person-name">
          <div class="name">{{ this.username }}</div>
          <span class="detail">{{ this.moto }}</span>
        </div>
      </div>
      <div class="menu-content">
        <div class="menu-list">
          <div
            class="menu-list-item"
            v-for="item in menuData"
            :key="item.id"
            @click="navigateTo(item.path)"
          >
            <div class="block"></div>
            <span class="iconfont" :class="item.iconFont"></span>
            <div class="item-name">{{ item.menuName }}</div>
          </div>
        </div>
      </div>
      <div class="logout" @click="navigateTo('/login')">
        <div class="menu-list-item">
          <div class="block"></div>
          <span class="iconfont icon-jinru"></span>
          <div class="item-name">退出登录</div>
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
      id: 0,
      username: "时间的彷徨",
      moto: "i am sb!",
      avatar: "https://pigkiller-011955-1319328397.cos.ap-beijing.myqcloud.com/img/202407241830349.avif",
      menuData: [
        {id: 1, menuName: '首页', iconFont: 'icon-caidan', path: '/'},
        {id: 2, menuName: '美食广场', iconFont: 'icon-weizhi', path: '/plaza'},
        {id: 3, menuName: '我的收藏', iconFont: 'icon-category', path: '/collection'},
        {id: 4, menuName: '就餐记录', iconFont: 'icon-bingtu', path: '/record'},
        {id: 5, menuName: '个人中心', iconFont: 'icon-shezhi', path: '/user'},
      ],
    };
  },
  methods: {
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
    navigateTo(path) {
      this.$router.push(path);
    },
    navigateToUserCenter(id) {
      this.$router.push({name: 'user', params: {id}});
    },
    log_out() {
      axios.get('http://127.0.0.1:8000/users/logout/')
        .then(() => {
          this.$router.push('/login');
        })
        .catch(error => {
          console.error('Error fetching data: ', error);
        });
    },
    getAvatarUrl() {
      console.log(this.avatar)
      return this.avatar;
    },
    get_user_info() {
      axios.get('http://127.0.0.1:8000/users/get-user-info/')
        .then(response => {
          this.id = response.data.id;
          this.username = response.data.username;
          this.moto = response.data.moto;
          this.avatar = response.data.avatar;
        })
        .catch(error => {
          console.error('Error fetching data: ', error);
        });
      console.log(this.id);
    }
  },
  mounted() {
    setInterval(this.get_user_info, 500);
  }
};
</script>

<style lang="scss" scoped>
@import url(../assets/iconfont/iconfont.css);
@import url(../assets/themecss/theme.scss);
@import url('https://fonts.googleapis.com/css2?family=Ma+Shan+Zheng&family=Noto+Sans+SC:wght@100..900&display=swap');

.iconfont {
  font-family: "iconfont" !important;
  font-style: normal;
  font-size: 25px;
  color: var(--theme-text-color);
  vertical-align: middle;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

.menu-wrapper {
  display: flex;
  flex-direction: column;
  height: 100vh;
  width: 90px;
  border-radius: 0 0 0 0;
  background-color: #e6e3e3;
  padding: 20px;
  box-sizing: border-box;
  transition: width 0.6s;
  overflow: hidden;

  &:hover {
    width: 250px; /* 调整这个宽度 */
  }

  .content {
    display: flex;
    flex-direction: column;
    flex-grow: 1;

    .person-info {
      margin-top: 20px;
      white-space: nowrap;
      text-align: left;
      cursor: pointer;

      img {
        width: 50px;
        height: 50px;
        border-radius: 50%;
        border: 2px solid #fff;
        box-shadow: 0px 0px 10px 0px rgba(0, 0, 0, 0.2);
        vertical-align: middle;
      }

      .person-name {
        margin-left: 10px;
        vertical-align: middle;
        opacity: 0;
        transition: opacity 0.6s;
        overflow: hidden;
        color: var(--theme-info-text-color);
        display: inline-block;
        font-family: 'Noto Sans SC';

        .name {
          font-size: 24px;
          font-weight: 800;
        }

        .detail {
          font-size: 12px;
          font-weight: 500;
        }
      }
    }

    .menu-content {
      margin-top: 20px;
      flex-grow: 1;

      .menu-list {
        .menu-list-item {
          cursor: pointer;
          width: 100%;
          height: 50px;
          font-size: 18px;
          position: relative;
          text-align: left;
          border-radius: 10px;
          padding-left: 10px;
          white-space: nowrap;

          .block {
            width: 6px;
            height: 25px;
            background: rgb(101, 57, 225);
            position: absolute;
            right: -10px;
            top: 13px;
            transition: opacity 0.5s;
            border-top-left-radius: 4px;
            border-bottom-left-radius: 4px;
            opacity: 0;
          }

          .item-name {
            line-height: 50px;
            display: inline-block;
            margin-left: 10px;
            font-size: 18px;
            color: var(--theme-text-color);
            font-weight: 100;
            transition: opacity 0.6s;
            opacity: 0;
            text-align: left;
          }

          &:hover {
            background-color: var(--theme-hover-menu-color);

            .item-name {
              color: var(--theme-hover-color);
            }

            .iconfont {
              color: var(--theme-hover-color);
            }

            .block {
              opacity: 1;
            }
          }
        }
      }
    }

    .logout {
      margin-top: auto;

      .menu-list-item {
        cursor: pointer;
        width: 100%;
        height: 50px;
        font-size: 18px;
        position: relative;
        text-align: left;
        border-radius: 10px;
        padding-left: 10px;
        white-space: nowrap;

        .block {
          width: 6px;
          height: 25px;
          background: rgb(101, 57, 225);
          position: absolute;
          right: -10px;
          top: 13px;
          transition: opacity 0.5s;
          border-top-left-radius: 4px;
          border-bottom-left-radius: 4px;
          opacity: 0;
        }

        .item-name {
          line-height: 50px;
          display: inline-block;
          margin-left: 10px;
          font-size: 18px;
          color: var(--theme-text-color);
          font-weight: 100;
          transition: opacity 0.6s;
          opacity: 0;
          text-align: left;
        }

        &:hover {
          background-color: var(--theme-hover-menu-color);

          .item-name {
            color: var(--theme-hover-color);
          }

          .iconfont {
            color: var(--theme-hover-color);
          }

          .block {
            opacity: 1;
          }
        }
      }
    }
  }

  &:hover {
    .content {
      .person-info {
        .person-name {
          opacity: 1;
        }
      }

      .menu-content {
        .menu-list {
          .menu-list-item {
            .item-name {
              opacity: 1;
            }
          }
        }
      }

      .logout {
        .menu-list-item {
          .item-name {
            opacity: 1;
          }
        }
      }
    }
  }
}
</style>
