<template>
    <div :class="{'dark': isDarkMode}">
      <nav class="sidebar" :class="{'close': isSidebarClosed}">
        <header>
          <div class="image-text">
            <span class="image">
              <img src="@/assets/kobe.jpg" alt="Profile Image">
            </span>
            <div class="text logo-text">
              <span class="name">Phoenix</span>
              <span class="profession">Web Developer</span>
            </div>
          </div>
          <i class="bx bx-chevron-right toggle" @click="toggleSidebar"></i>
        </header>
        <div class="menu-bar">
          <div class="menu">
            <ul class="menu-links">
              <li class="nav-link">
                <a href="#">
                  <i class="bx bx-home-alt icon"></i>
                  <span class="text nav-text">Dashboard</span>
                </a>
              </li>
              <li class="nav-link">
                <a href="#">
                  <i class='bx bx-bar-chart-alt-2 icon'></i>
                  <span class="text nav-text">Revenue</span>
                </a>
              </li>
              <li class="nav-link">
                <a href="#">
                  <i class='bx bx-bell icon'></i>
                  <span class="text nav-text">Notifications</span>
                </a>
              </li>
              <li class="nav-link">
                <a href="#">
                  <i class='bx bx-pie-chart-alt icon'></i>
                  <span class="text nav-text">Analytics</span>
                </a>
              </li>
              <li class="nav-link">
                <a href="#">
                  <i class='bx bx-heart icon'></i>
                  <span class="text nav-text">Likes</span>
                </a>
              </li>
              <li class="nav-link">
                <a href="#">
                  <i class='bx bx-wallet icon'></i>
                  <span class="text nav-text">Wallets</span>
                </a>
              </li>
            </ul>
          </div>
          <div class="bottom-content">
            <li>
              <a href="#">
                <i class="bx bx-log-out icon"></i>
                <span class="text nav-text">Logout</span>
              </a>
            </li>
          </div>
        </div>
      </nav>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        isSidebarClosed: false,
        isDarkMode: false,
      };
    },
    methods: {
      toggleSidebar() {
        this.isSidebarClosed = !this.isSidebarClosed;
      },
      toggleDarkMode() {
        this.isDarkMode = !this.isDarkMode;
      },
    },
  };
  </script>
  
  <style>
  @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');
  
  * {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: "Poppins", sans-serif;
  }
  
  :root {
    --body-color: #e4e9f7;
    --sidebar-color: #fff;
    --primary-color: #695cfe;
    --primary-color-light: #f6f5ff;
    --toggle-color: #ddd;
    --text-color: #707070;
    --tran-02: all 0.2s ease;
    --tran-03: all 0.3s ease;
  }
  
  body {
    min-height: 100vh;
    background-color: var(--body-color);
    transition: var(--tran-03);
  }
  
  ::selection {
    background-color: var(--primary-color);
    color: #fff;
  }
  
  .dark {
    --body-color: #18191a;
    --sidebar-color: #242526;
    --primary-color: #3a3b3c;
    --primary-color-light: #3a3b3c;
    --toggle-color: #fff;
    --text-color: #ccc;
  }
  
  .sidebar {
    position: absolute;
    top: 0;
    left: 0;
    height: 100%;
    width: 250px;
    padding: 10px 14px;
    background: var(--sidebar-color);
    transition: var(--tran-03);
    z-index: 100;
  }
  
  .sidebar.close {
    width: 88px;
  }
  
  .sidebar li {
    height: 50px;
    list-style: none;
    display: flex;
    align-items: center;
    margin-top: 10px;
  }
  
  .sidebar header .image, .sidebar .icon {
    min-width: 60px;
    border-radius: 6px;
  }
  
  .sidebar .icon {
    min-width: 60px;
    border-radius: 6px;
    height: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 20px;
  }
  
  .sidebar .text, .sidebar .icon {
    color: var(--text-color);
    transition: var(--tran-03);
  }
  
  .sidebar .text {
    font-size: 17px;
    font-weight: 500;
    white-space: nowrap;
    opacity: 1;
  }
  
  .sidebar.close .text {
    opacity: 0;
  }
  
  .sidebar header {
    position: relative;
  }
  
  .sidebar header .image-text {
    display: flex;
    align-items: center;
  }
  
  .sidebar header .logo-text {
    display: flex;
    flex-direction: column;
  }
  
  header .image-text .name {
    margin-top: 2px;
    font-size: 18px;
    font-weight: 600;
  }
  
  header .image-text .profession {
    font-size: 16px;
    margin-top: -2px;
    display: block;
  }
  
  .sidebar header .image {
    display: flex;
    align-items: center;
    justify-content: center;
  }
  
  .sidebar header .image img {
    width: 40px;
    border-radius: 6px;
  }
  
  .sidebar header .toggle {
    position: absolute;
    top: 50%;
    right: -25px;
    transform: translateY(-50%) rotate(180deg);
    height: 25px;
    width: 25px;
    background-color: var(--primary-color);
    color: var(--sidebar-color);
    display: flex;
    border-radius: 50%;
    align-items: center;
    justify-content: center;
    font-size: 22px;
    cursor: pointer;
    transition: var(--tran-03);
  }
  
  .dark .sidebar header .toggle {
    color: var(--text-color);
  }
  
  .sidebar.close .toggle {
    transform: translateY(-50%) rotate(0deg);
  }
  
  .sidebar .menu {
    margin-top: 40px;
  }
  
  .sidebar li.search-box {
    border-radius: 6px;
    background-color: var(--primary-color-light);
    cursor: pointer;
    transition: var(--tran-03);
  }
  
  .sidebar li.search-box input {
    height: 100%;
    width: 100%;
    outline: none;
    border: none;
    background-color: var(--primary-color-light);
    color: var(--text-color);
    border-radius: 6px;
    font-size: 17px;
    font-weight: 500;
    transition: var(--tran-03);
  }
  
  .sidebar li a {
    list-style: none;
    height: 100%;
    background-color: transparent;
    display: flex;
    align-items: center;
    height: 100%;
    width: 100%;
    border-radius: 6px;
    text-decoration: none;
    transition: var(--tran-03);
  }
  
  .sidebar li a:hover {
    background-color: var(--primary-color);
  }
  
  .sidebar li a:hover .icon, .sidebar li a:hover .text {
    color: var(--sidebar-color);
  }
  
  .dark .sidebar li a:hover .icon,
  .dark .sidebar li a:hover .text {
    color: var(--text-color);
  }
  
  .sidebar .menu-bar {
    height: calc(100% - 55px);
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    overflow-y: scroll;
  }
  
  .menu-bar::-webkit-scrollbar {
    display: none;
  }
  
  .sidebar .menu-bar .mode {
    border-radius: 6px;
    background-color: var(--primary-color-light);
    position: relative;
    transition-timing-function: var(--tran-03);
  }
  
  .menu-bar .mode .sun-moon {
    height: 50px;
    width: 60px;
  }
  
  .mode .sun-moon .icon {
    position: absolute;
    top: 50%;
    left: 0;
    transform: translateY(-50%);
    font-size: 20px;
  }
  
  .mode .sun-moon .icon.moon {
    color: var(--text-color);
  }
  
  .mode .sun-moon .icon.sun {
    color: var(--text-color);
  }
  
  .mode .toggle-switch {
    position: absolute;
    top: 50%;
    left: 50px;
    transform: translateY(-50%);
    height: 20px;
    width: 50px;
    background-color: var(--toggle-color);
    border-radius: 20px;
    cursor: pointer;
  }
  
  .mode .toggle-switch .switch {
    position: absolute;
    top: 0;
    left: 0;
    height: 20px;
    width: 20px;
    background-color: var(--primary-color);
    border-radius: 20px;
    transition: var(--tran-03);
  }
  
  .mode .toggle-switch .switch.active {
    transform: translateX(30px);
  }
  
  .home {
    margin-left: 250px;
    padding: 20px;
  }
  
  .home .text {
    font-size: 25px;
    font-weight: 600;
    color: var(--text-color);
  }
  </style>
  
  <!-- 添加下面的链接到 public/index.html 文件 -->
  <link href='https://unpkg.com/boxicons@2.1.1/css/boxicons.min.css' rel='stylesheet'>
  