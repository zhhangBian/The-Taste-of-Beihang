<template>
  <div style="padding: 10px">
    <h1 class="main-title">就餐记录</h1>
    <hr class="divider">

    <el-input style="width: 300px" placeholder="请输入菜品名称..." v-model="dish_name"
              clearable></el-input>
    <el-button type="primary" @click="search" style="margin-left: 5px">查询数据</el-button>

    <el-button type="primary" @click="get_record_form">新增数据</el-button>

    <div class="table-container">
      <el-table :data="data_paged" border style="width: 100%">
        <el-table-column prop="time" label="时间" width="300"/>
        <el-table-column prop="restaurant_name" label="地点" width="200"/>
        <el-table-column prop="dish_name" label="菜品名称" width="300"/>
        <el-table-column prop="price" label="花费（元）" width="200"/>
        <el-table-column label="">
          <template #default="scope">
            <el-button link type="primary" size="small"
                       @click="handleEdit(scope.row, scope.$index)">编辑
            </el-button>
            <el-button link type="danger" size="small"
                       @click.prevent="delete_record(scope.row, scope.$index)">删除
            </el-button>
          </template>
        </el-table-column>
      </el-table>
    </div>

    <!-- 分页组件 -->
    <div class="pagination-container">
      <el-pagination
        background
        layout="total, prev, pager, next, jumper"
        :total="page_count"
        v-model:current-page="current_page"
        :page-size="page_size">
      </el-pagination>
    </div>

    <!--新增和编辑都复用这个弹窗-->
    <el-dialog v-model="dialogFormVisible" title="更改就餐记录" width="60%">
      <el-form :model="record" label-width="100px" style="padding-right:30px">
        <el-form-item label="时间">
          <el-row :gutter="10">
            <el-col :span="4">
              <el-input v-model="record.year" placeholder="年" type="number" autocomplete="off">
                <template #append>年</template>
              </el-input>
            </el-col>
            <el-col :span="4">
              <el-input v-model="record.month" placeholder="月" type="number" autocomplete="off">
                <template #append>月</template>
              </el-input>
            </el-col>
            <el-col :span="4">
              <el-input v-model="record.day" placeholder="日" type="number" autocomplete="off">
                <template #append>日</template>
              </el-input>
            </el-col>
            <el-col :span="4">
              <el-input v-model="record.hour" placeholder="时" type="number" autocomplete="off">
                <template #append>时</template>
              </el-input>
            </el-col>
            <el-col :span="4">
              <el-input v-model="record.minute" placeholder="分" type="number" autocomplete="off">
                <template #append>分</template>
              </el-input>
            </el-col>
          </el-row>
        </el-form-item>
        <el-form-item label="地点">
          <el-input v-model="record.restaurant_name" autocomplete="off"/>
        </el-form-item>
        <el-form-item label="菜品名称">
          <el-input v-model="record.dish_name" autocomplete="off"/>
        </el-form-item>
        <el-form-item label="花费">
          <el-input v-model="record.price" type="number" autocomplete="off"/>
        </el-form-item>
      </el-form>
      <template #footer>
                <span class="dialog-footer">
                    <el-button @click="dialogFormVisible = false">取消</el-button>
                    <el-button type="primary" @click="save_record">确认</el-button>
                </span>
      </template>
    </el-dialog>
  </div>
</template>

<script setup>
import {reactive, ref, computed, onMounted} from "vue";
import apiClient from "@/axios";

let records = ref([
  {
    id: 1,
    time: '2023-07-29 12:30',
    restaurant_name: '学二食堂',
    dish_name: '麻婆豆腐',
    price: 25
  },
  {
    id: 2,
    time: '2023-07-28 18:00',
    restaurant_name: '学四食堂',
    dish_name: '宫保鸡丁',
    price: 30
  },
]);

let dialogFormVisible = ref(false);
let record = reactive({
  year: '',
  month: '',
  day: '',
  hour: '',
  minute: '',

  dish_name: '',
  restaurant_name: '',
  price: '',
  id: '',
});

const record_index = ref(-1);
const dish_name = ref('');

// 分页相关的状态
const current_page = ref(1);
// 每页显示的数据条数
const page_size = ref(10);
// 计算总页数
const page_count = computed(() => records.value.length);

// 计算当前页显示的数据
const data_paged = computed(() => {
  const start = (current_page.value - 1) * page_size.value;
  const end = start + page_size.value;
  return records.value.slice(start, end);
});


const get_record_form = () => {
  // 获取当前时间并设置为默认值
  const now = new Date();
  record.year = now.getFullYear().toString();
  record.month = (now.getMonth() + 1).toString().padStart(2, '0'); // 月份从0开始，因此+1
  record.day = now.getDate().toString().padStart(2, '0');
  record.hour = now.getHours().toString().padStart(2, '0');
  record.minute = now.getMinutes().toString().padStart(2, '0');

  record.dish_name = '';
  record.restaurant_name = '';
  record.price = '';
  record.id = '';

  record_index.value = -1;
  dialogFormVisible.value = true;
};

// 保存，需要区分是新增还是更改
const save_record = () => {
  // 将分散的时间字段组合成一个完整的时间字符串
  record.time = `${record.year}-${record.month}-${record.day} ${record.hour}:${record.minute}`;

  // 更改
  if (record_index.value >= 0) {
    record_index.value = -1;
    // 更改一条记录
    apiClient.post(`http://127.0.0.1:8000/users/modify-record/`, {
      "record_id": record.id,
      "time": record.time,
      "dish_name": record.dish_name,
      "restaurant_name": record.restaurant_name,
      "price": record.price,
    })
      .then(() => {
        apiClient.get(`http://127.0.0.1:8000/users/get-records/`)
          .then(response => {
            records.value = response.data.records;
          })
          .catch(error => {
            console.error('Error get records:', error);
          });
      })
      .catch(error => {
        console.error('Error save records:', error);
      });
  }
  // 新增
  else {
    // 更改一条记录
    apiClient.post(`http://127.0.0.1:8000/users/add-record/`, {
      "time": record.time,
      "dish_name": record.dish_name,
      "restaurant_name": record.restaurant_name,
      "price": record.price,
    })
      .then(() => {
        apiClient.get(`http://127.0.0.1:8000/users/get-records/`)
          .then(response => {
            records.value = response.data.records;
          })
          .catch(error => {
            console.error('Error get records:', error);
          });
      })
      .catch(error => {
        console.error('Error save records:', error);
      });
  }
  // 隐藏填写窗口
  dialogFormVisible.value = false;
};

const handleEdit = (row, index) => {
  const [date, time] = row.time.split(' ');
  const [year, month, day] = date.split('-');
  const [hour, minute] = time.split(':');

  record.year = year;
  record.month = month;
  record.day = day;
  record.hour = hour;
  record.minute = minute;

  record.dish_name = row.dish_name;
  record.restaurant_name = row.restaurant_name;
  record.price = row.price;
  record.id = row.id;

  record_index.value = index;
  dialogFormVisible.value = true;
};

const delete_record = (row, index) => {
  record.id = row.id
  apiClient.post(`http://127.0.0.1:8000/users/delete-record/`, {
    "record_id": record.id,
  })
    .then(() => {
      apiClient.get(`http://127.0.0.1:8000/users/get-records/`)
        .then(response => {
          records.value = response.data.records;
        })
        .catch(error => {
          console.error('Error get records:', error);
        });
    })
    .catch(error => {
      console.error('Error save records:', error);
    });
};

const search = () => {
  records.value = records.value.filter(v => v.dishName.includes(dish_name.value));
};

onMounted(() => {
  apiClient.get('http://127.0.0.1:8000/users/get-records/')
    .then(response => {
      records.value = response.data.records;
    })
    .catch(error => {
      console.error('Error fetching records:', error);
    });
});
</script>

<style scoped>
.main-title {
  font-size: 2.5rem;
  font-weight: bold;
  margin-bottom: 8px;
  text-align: left !important;
  color: black;
}

.divider {
  border: none;
  border-top: 2px solid #000;
  margin-bottom: 16px;
  width: 100%;
  background-color: black;
}

.table-container {
  margin-top: 20px;
  overflow-y: auto;
}

/* 分页组件的容器，添加距离 */
.pagination-container {
  margin-top: 20px;
  display: flex;
  justify-content: left;
}
</style>
