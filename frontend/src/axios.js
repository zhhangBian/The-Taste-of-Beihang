import axios from 'axios';

// 创建 Axios 实例
const apiClient = axios.create({
    baseURL: 'http://127.0.0.1:8000', // 你的 API 基础 URL
    withCredentials: true, // 启用凭证
});

// 导出 Axios 实例
export default apiClient;
