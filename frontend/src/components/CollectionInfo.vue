<template>
  <div style="padding: 10px">
    <h1 class="main-title">我的收藏</h1>
    <hr class="divider"/>

    <div class="columns-container">
      <div class="left-column">
        <div class="search-bar">
          <el-input
            style="width: 300px"
            placeholder="请输入食堂名称..."
            v-model="restaurantSearchQuery"
            clearable
          ></el-input>
          <el-button type="primary" @click="searchCanteen" style="margin-left: 5px">查询</el-button>
        </div>
        <h2>收藏的食堂</h2>
        <el-button type="primary" @click="add_collect_restaurant" style="margin-bottom: 10px">新增食堂
        </el-button>
        <el-table :data="pagedCanteenData" border style="width: 100%">
          <el-table-column prop="restaurant" label="食堂"/>
          <el-table-column label="操作">
            <template #default="scope">
              <el-button link type="danger" size="small"
                         @click.prevent="delete_collect_restaurant(scope.row,scope.$index)">删除
              </el-button>
            </template>
          </el-table-column>
        </el-table>
        <div class="pagination-container">
          <el-pagination
            background
            layout="total, prev, pager, next, jumper"
            :total="totalCanteen"
            v-model:current-page="currentCanteenPage"
            :page-size="restaurantPageSize"
          ></el-pagination>
        </div>
      </div>

      <div class="divider-vertical"></div>

      <div class="right-column">
        <div class="search-bar">
          <el-input
            style="width: 300px"
            placeholder="请输入菜品名称..."
            v-model="dishSearchQuery"
            clearable
          ></el-input>
          <el-button type="primary" @click="searchDish" style="margin-left: 5px">查询</el-button>
        </div>
        <h2>收藏的菜品</h2>
        <el-button type="primary" @click="add_collect_dish" style="margin-bottom: 10px">新增菜品
        </el-button>
        <el-table :data="pagedDishData" border style="width: 100%">
          <el-table-column prop="restaurant" label="食堂"/>
          <el-table-column prop="dish" label="菜品"/>
          <el-table-column label="操作">
            <template #default="scope">
              <el-button link type="danger" size="small"
                         @click.prevent="delete_collect_dish(scope.$index)">
                删除
              </el-button>
            </template>
          </el-table-column>
        </el-table>
        <div class="pagination-container">
          <el-pagination
            background
            layout="total, prev, pager, next, jumper"
            :total="totalDish"
            v-model:current-page="currentDishPage"
            :page-size="dishPageSize"
          ></el-pagination>
        </div>
      </div>
    </div>

    <el-dialog v-model="dialogFormVisible" title="添加收藏" width="60%">
      <el-form :model="form" label-width="100px" style="padding-right: 30px">
        <el-form-item label="食堂">
          <el-select v-model="form.restaurant" placeholder="请选择食堂">
            <el-option label="学一食堂" value="学一食堂"></el-option>
            <el-option label="学二食堂" value="学二食堂"></el-option>
            <el-option label="学三食堂" value="学三食堂"></el-option>
            <el-option label="学四食堂" value="学四食堂"></el-option>
            <el-option label="学五食堂" value="学五食堂"></el-option>
            <el-option label="学六食堂" value="学六食堂"></el-option>
            <el-option label="教工食堂" value="教工食堂"></el-option>
            <el-option label="清真食堂" value="清真食堂"></el-option>
            <el-option label="合一厅" value="合一厅"></el-option>
            <el-option label="东区第一食堂" value="东区第一食堂"></el-option>
            <el-option label="鼓瑟轩" value="鼓瑟轩"></el-option>
            <el-option label="西区清真食堂" value="西区清真食堂"></el-option>
            <el-option label="西区第一食堂" value="西区第一食堂"></el-option>
            <el-option label="西区第二食堂" value="西区第二食堂"></el-option>
            <el-option label="西区第三食堂" value="西区第三食堂"></el-option>
          </el-select>
        </el-form-item>
        <el-form-item v-if="!isCanteenForm" label="菜品">
          <el-input v-model="form.dish" autocomplete="off"/>
        </el-form-item>
      </el-form>
      <template #footer>
          <span class="dialog-footer">
            <el-button @click="dialogFormVisible = false">取消</el-button>
            <el-button type="primary" @click="save">确认</el-button>
          </span>
      </template>
    </el-dialog>
  </div>
</template>

<script setup>
import {reactive, ref, computed, onMounted} from "vue";
import apiClient from "@/axios";
import { ElMessage } from 'element-plus';

let collected_restaurants = ref([
  {restaurant: "学二食堂"},
  {restaurant: "学四食堂"},
  // 更多数据...
]);

let collected_dishes = ref([
  {restaurant: "学二食堂", dish: "麻婆豆腐"},
  {restaurant: "学四食堂", dish: "宫保鸡丁"},
  // 更多数据...
]);

let dialogFormVisible = ref(false);
let form = reactive({restaurant: "", dish: ""});
const globalIndex = ref(-1);
const isCanteenForm = ref(true);
const restaurantSearchQuery = ref("");
const dishSearchQuery = ref("");

// 分页相关的状态
const currentCanteenPage = ref(1);
const restaurantPageSize = ref(10); // 每页显示的数据条数

const currentDishPage = ref(1);
const dishPageSize = ref(10); // 每页显示的数据条数

// 计算当前页显示的数据
const pagedCanteenData = computed(() => {
  const start = (currentCanteenPage.value - 1) * restaurantPageSize.value;
  return collected_restaurants.value.slice(start, start + restaurantPageSize.value);
});

const pagedDishData = computed(() => {
  const start = (currentDishPage.value - 1) * dishPageSize.value;
  return collected_dishes.value.slice(start, start + dishPageSize.value);
});

// 计算总页数
const totalCanteen = computed(() => collected_restaurants.value.length);
const totalDish = computed(() => collected_dishes.value.length);

const add_collect_restaurant = () => {
  form.restaurant = "";
  form.dish = "";
  globalIndex.value = -1;
  isCanteenForm.value = true;
  dialogFormVisible.value = true;
};

const add_collect_dish = () => {
  form.restaurant = "";
  form.dish = "";
  globalIndex.value = -1;
  isCanteenForm.value = false;
  dialogFormVisible.value = true;
};

const save = () => {
  if (isCanteenForm.value) {
    apiClient.post(`http://127.0.0.1:8000/users/collect-restaurant/`, {
      "restaurant_name": form.restaurant,
    })
      .then(() => {
        apiClient.get(`http://127.0.0.1:8000/users/get-collected-restaurants/`)
          .then(response => {
            collected_restaurants.value = response.data.collected_restaurants;
          })
          .catch(error => {
            console.error('Error get records:', error);
          });
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
  } else {
    apiClient.post(`http://127.0.0.1:8000/users/collect-dish/`, {
      "restaurant_name": form.restaurant,
      "dish_name": form.dish,
    })
      .then(() => {
        apiClient.get(`http://127.0.0.1:8000/users/get-collected-dishes/`)
          .then(response => {
            collected_dishes.value = response.data.collected_dishes;
          })
          .catch(error => {
            console.error('Error get records:', error);
          });
      })
      .catch(error => {
        ElMessage({
              message: '没有这个菜品',
              type: 'error',
              duration: 3000,
              showClose: true,
              customClass: 'large-message-font'
            });
      });
  }

  dialogFormVisible.value = false;
};

const delete_collect_restaurant = (row, index) => {
  apiClient.post(`http://127.0.0.1:8000/users/discollect-restaurant/`, {
    "restaurant_name": row.restaurant,
  })
    .then(() => {
      apiClient.get(`http://127.0.0.1:8000/users/get-collected-restaurants/`)
        .then((response) => {
          collected_restaurants.value = response.data.collected_restaurants;
        })
        .catch(error => {
          console.error('Error get records:', error);
        });
    })
    .catch(error => {
      console.error('Error save records:', error);
    });
};

const delete_collect_dish = (row, index) => {
  apiClient.post(`http://127.0.0.1:8000/users/discollect-dish/`, {
    "restaurant_name": row.restaurant,
    "dish_name": row.dish,
  })
    .then(() => {
      apiClient.get(`http://127.0.0.1:8000/users/get-collected-dishes/`)
        .then((response) => {
          collected_dishes.value = response.data.collected_dishes;
        })
        .catch(error => {
          console.error('Error get records:', error);
        });
    })
    .catch(error => {
      console.error('Error save records:', error);
    });
};

const searchCanteen = () => {
  collected_restaurants.value = collected_restaurants.value.filter((v) =>
    v.restaurant.includes(restaurantSearchQuery.value)
  );
};

const searchDish = () => {
  collected_dishes.value = collected_dishes.value.filter((v) =>
    v.dish.includes(dishSearchQuery.value)
  );
};

onMounted(() => {
  apiClient.get(`http://127.0.0.1:8000/users/get-collected-restaurants/`)
    .then(response => {
      collected_restaurants.value = response.data.collected_restaurants;
    })
    .catch(error => {
      console.error('Error get records:', error);
    });

  apiClient.get(`http://127.0.0.1:8000/users/get-collected-dishes/`)
    .then(response => {
      collected_dishes.value = response.data.collected_dishes;
    })
    .catch(error => {
      console.error('Error get records:', error);
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

.divider-vertical {
  width: 2px;
  background-color: #ddd;
  margin: 0 20px;
}

.columns-container {
  display: flex;
  justify-content: space-between;
}

.left-column,
.right-column {
  flex: 1;
}

.table-container {
  margin-top: 20px;
  overflow-y: auto;
}

.pagination-container {
  margin-top: 20px;
  display: flex;
  justify-content: left;
}

.search-bar {
  display: flex;
  align-items: center;
  margin-bottom: 10px;
}
</style>
