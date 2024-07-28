<template>
    <div class="menu-wrapper">
      <div class="content">
        <div class="person-info">
          <img src="../assets/kobe.jpg" alt="" />
          <div class="person-name">
            <div class="name">时间的彷徨</div>
            <span class="detail">我是sb</span>
          </div>
        </div>
        <div class="menu-content">
          <div class="menu-list">
            <div class="menu-list-item" v-for="item in menuData" :key="item.id">
              <div class="block"></div>
              <span class="iconfont" :class="item.iconFont"></span>
              <div class="item-name">{{ item.menuName }}</div>
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
        menuData: [
          {
            id: 1,
            menuName: "首页",
            iconFont: "icon-caidan",
          },
          {
            id: 2,
            menuName: "美食广场",
            iconFont: "icon-weizhi",
          },
        //   {
        //     id: 2,
        //     menuName: "Products",
        //     iconFont: "icon-gouwu",
        //   },
          {
            id: 3,
            menuName: "我的收藏",
            iconFont: "icon-category",
          },
          {
            id: 4,
            menuName: "用餐记录",
            iconFont: "icon-bingtu",
          },
        //   {
        //     id: 4,
        //     menuName: "Orders",
        //     iconFont: "icon-order-fill",
        //   },
        //   {
        //     id: 5,
        //     menuName: "Customers",
        //     iconFont: "icon-denglu-yonghuzu",
        //   },
        //   {
        //     id: 6,
        //     menuName: "Sales Offers",
        //     iconFont: "icon-liwu",
        //   },
          {
            id: 5,
            menuName: "个人中心",
            iconFont: "icon-shezhi",
          },
          {
            id: 6,
            menuName: "登出",
            iconFont: "icon-jinru",
          },
        ],
        themeDark: false,
      };
    },
    mounted() {
      document.body.setAttribute("theme-color", "light");
    },
    methods: {
      changeDark() {
        if (!this.theme) {
          document.body.setAttribute("theme-color", "dark");
          this.theme = !this.theme;
        } else {
          document.body.setAttribute("theme-color", "light");
          this.theme = !this.theme;
        }
      },
    },
  };
  </script>
  
  <style lang="scss" scoped>
  @import url(../assets/iconfont/iconfont.css);
  @import url(../assets/themecss/theme.scss);
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
    width: 90px;
    border-radius: 20px;
    background-color: #e6e3e3;
    padding: 20px;
    box-sizing: border-box;
    transition: 0.6s;
    overflow: hidden;
    .menu-title {
      padding-bottom: 20px;
      box-sizing: border-box;
      border-bottom: 1px solid rgb(229, 233, 236);
      margin-bottom: 20px;
      .title-text {
        margin-left: 10px;
        font-family: "BasketBall";
        font-size: 30px;
        vertical-align: middle;
        opacity: 0;
        transition: 0.6s;
        color: var(--theme-info-text-color);
      }
      .icon-24gf-bag {
        font-size: 30px;
        padding-left: 10px;
        color: rgb(103, 56, 223);
      }
    }
    .content {
      // text-align: center;
      .person-info {
        margin-top: 20px;
        white-space: nowrap;
        text-align: left;
        img {
          width: 50px;
          height: 50px;
          border-radius: 50%;
          border: 2px solid #fff;
          box-shadow: 0px 0px 10px 0px rgba(0, 0, 0, 0.2);
          vertical-align: middle;
        }
        .person-name {
          margin-left: 15px;
          vertical-align: middle;
          opacity: 0;
          transition: 0.6s;
          overflow: hidden;
          color: var(--theme-info-text-color);
          display: inline-block;
          .name {
            font-size: 20px;
            font-weight: 600;
          }
          .detail {
            font-size: 12px;
          }
        }
      }
      .menu-content {
        margin-top: 20px;
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
              transition: 0.5s;
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
              transition: 0.6s;
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
            .btn {
              position: absolute;
              top: 50%;
              transform: translateY(-50%);
              display: inline-block;
              opacity: 0;
              margin-left: 10px;
              .check-ipt {
                display: none;
              }
              .check-lable {
                display: inline-block;
                width: 40px;
                height: 20px;
                border-radius: 20px;
                background: rgb(101, 58, 223);
                /* border: 1px solid #eee; */
                cursor: pointer;
                position: relative;
                overflow: hidden;
              }
              .check-lable::before {
                display: inline-block;
                content: "";
                width: 15px;
                height: 15px;
                border-radius: 50%;
                background: white;
                position: absolute;
                left: 3px;
                top: 50%;
                transform: translateY(-50%);
                transition: all 0.3s;
              }
  
              .check-ipt:checked + .check-lable::before {
                left: 20px;
                background: rgb(32, 30, 43);
              }
              .check-ipt:checked + .check-lable::after {
                width: 100%;
              }
            }
          }
        }
      }
    }
    &:hover {
      width: 220px;
      .menu-title {
        .title-text {
          opacity: 1;
        }
      }
  
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
            .btn {
              opacity: 1;
            }
          }
        }
      }
    }
  }
  </style>