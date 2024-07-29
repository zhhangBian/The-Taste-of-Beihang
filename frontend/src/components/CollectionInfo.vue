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
            v-model="canteenSearchQuery"
            clearable
          ></el-input>
          <el-button type="primary" @click="searchCanteen" style="margin-left: 5px">查询</el-button>
        </div>
        <h2>收藏的食堂</h2>
        <el-button type="primary" @click="handleAddCanteen" style="margin-bottom: 10px">新增食堂
        </el-button>
        <el-table :data="pagedCanteenData" border style="width: 100%">
          <el-table-column prop="time" label="时间"/>
          <el-table-column prop="canteen" label="食堂"/>
          <el-table-column label="操作">
            <template #default="scope">
              <el-button link type="primary" size="small"
                         @click="handleEditCanteen(scope.row, scope.$index)">编辑
              </el-button>
              <el-button link type="danger" size="small"
                         @click.prevent="removeCanteen(scope.$index)">删除
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
            :page-size="canteenPageSize"
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
        <el-button type="primary" @click="handleAddDish" style="margin-bottom: 10px">新增菜品
        </el-button>
        <el-table :data="pagedDishData" border style="width: 100%">
          <el-table-column prop="time" label="时间"/>
          <el-table-column prop="canteen" label="食堂"/>
          <el-table-column prop="dish" label="菜品"/>
          <el-table-column label="操作">
            <template #default="scope">
              <el-button link type="primary" size="small"
                         @click="handleEditDish(scope.row, scope.$index)">编辑
              </el-button>
              <el-button link type="danger" size="small" @click.prevent="removeDish(scope.$index)">
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
          <el-select v-model="form.canteen" placeholder="请选择食堂">
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
import {reactive, ref, computed} from "vue";

let canteenData = ref([
  {time: "2023-07-29 12:30", canteen: "学二食堂"},
  {time: "2023-07-28 18:00", canteen: "学四食堂"},
  // 更多数据...
]);

let dishData = ref([
  {time: "2023-07-29 12:30", canteen: "学二食堂", dish: "麻婆豆腐"},
  {time: "2023-07-28 18:00", canteen: "学四食堂", dish: "宫保鸡丁"},
  // 更多数据...
]);

let dialogFormVisible = ref(false);
let form = reactive({canteen: "", dish: ""});
const globalIndex = ref(-1);
const isCanteenForm = ref(true);
const canteenSearchQuery = ref("");
const dishSearchQuery = ref("");

// 分页相关的状态
const currentCanteenPage = ref(1);
const canteenPageSize = ref(10); // 每页显示的数据条数

const currentDishPage = ref(1);
const dishPageSize = ref(10); // 每页显示的数据条数

// 计算当前页显示的数据
const pagedCanteenData = computed(() => {
  const start = (currentCanteenPage.value - 1) * canteenPageSize.value;
  return canteenData.value.slice(start, start + canteenPageSize.value);
});

const pagedDishData = computed(() => {
  const start = (currentDishPage.value - 1) * dishPageSize.value;
  return dishData.value.slice(start, start + dishPageSize.value);
});

// 计算总页数
const totalCanteen = computed(() => canteenData.value.length);
const totalDish = computed(() => dishData.value.length);

const handleAddCanteen = () => {
  form.canteen = "";
  form.dish = "";
  globalIndex.value = -1;
  isCanteenForm.value = true;
  dialogFormVisible.value = true;
};

const handleAddDish = () => {
  form.canteen = "";
  form.dish = "";
  globalIndex.value = -1;
  isCanteenForm.value = false;
  dialogFormVisible.value = true;
};

const save = () => {
  // 自动生成当前时间
  const now = new Date();
  const timeString = `${now.getFullYear()}-${(now.getMonth() + 1)
    .toString()
    .padStart(2, "0")}-${now
    .getDate()
    .toString()
    .padStart(2, "0")} ${now
    .getHours()
    .toString()
    .padStart(2, "0")}:${now.getMinutes().toString().padStart(2, "0")}`;

  if (globalIndex.value >= 0) {
    if (isCanteenForm.value) {
      canteenData.value[globalIndex.value] = {...form, time: timeString};
    } else {
      dishData.value[globalIndex.value] = {...form, time: timeString};
    }
    globalIndex.value = -1;
  } else {
    if (isCanteenForm.value) {
      canteenData.value.push({...form, time: timeString});
    } else {
      dishData.value.push({...form, time: timeString});
    }
  }
  dialogFormVisible.value = false;
};

const handleEditCanteen = (row, index) => {
  form.canteen = row.canteen;
  form.dish = "";
  globalIndex.value = index;
  isCanteenForm.value = true;
  dialogFormVisible.value = true;
};

const handleEditDish = (row, index) => {
  form.canteen = row.canteen;
  form.dish = row.dish;
  globalIndex.value = index;
  isCanteenForm.value = false;
  dialogFormVisible.value = true;
};

const removeCanteen = (index) => {
  const actualIndex = (currentCanteenPage.value - 1) * canteenPageSize.value + index;
  canteenData.value.splice(actualIndex, 1);
};

const removeDish = (index) => {
  const actualIndex = (currentDishPage.value - 1) * dishPageSize.value + index;
  dishData.value.splice(actualIndex, 1);
};

const searchCanteen = () => {
  canteenData.value = canteenData.value.filter((v) =>
    v.canteen.includes(canteenSearchQuery.value)
  );
};

const searchDish = () => {
  dishData.value = dishData.value.filter((v) =>
    v.dish.includes(dishSearchQuery.value)
  );
};
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
