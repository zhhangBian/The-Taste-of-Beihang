<template>
    <div style="padding: 10px">
        <h1 class="main-title">就餐记录</h1>
        <hr class="divider">

        <el-input style="width: 300px" placeholder="请输入菜品名称..." v-model="name" clearable></el-input>
        <el-button type="primary" @click="search" style="margin-left: 5px">查询数据</el-button>

        <el-button type="primary" @click="handleAdd">新增数据</el-button>

        <div class="table-container">
            <el-table :data="pagedData" border style="width: 100%">
                <el-table-column prop="time" label="时间" width="300"/>
                <el-table-column prop="location" label="地点" width="200"/>
                <el-table-column prop="dishName" label="菜品名称" width="300"/>
                <el-table-column prop="cost" label="花费（元）" width="200"/>
                <el-table-column label="操作">
                    <template #default="scope">
                        <el-button link type="primary" size="small" @click="handleEdit(scope.row, scope.$index)">编辑
                        </el-button>
                        <el-button link type="danger" size="small" @click.prevent="remove(scope.$index)">删除</el-button>
                    </template>
                </el-table-column>
            </el-table>
        </div>

        <!-- 分页组件 -->
        <el-pagination
            background
            layout="total, prev, pager, next, jumper"
            :total="total"
            v-model:current-page="currentPage"
            :page-size="pageSize">
        </el-pagination>

        <!--弹窗-->
        <el-dialog v-model="dialogFormVisible" title="添加就餐记录" width="60%">
            <el-form :model="form" label-width="100px" style="padding-right:30px">
                <el-form-item label="时间">
                    <el-row :gutter="10">
                        <el-col :span="4">
                            <el-input v-model="form.year" placeholder="年" type="number" autocomplete="off">
                                <template #append>年</template>
                            </el-input>
                        </el-col>
                        <el-col :span="4">
                            <el-input v-model="form.month" placeholder="月" type="number" autocomplete="off">
                                <template #append>月</template>
                            </el-input>
                        </el-col>
                        <el-col :span="4">
                            <el-input v-model="form.day" placeholder="日" type="number" autocomplete="off">
                                <template #append>日</template>
                            </el-input>
                        </el-col>
                        <el-col :span="4">
                            <el-input v-model="form.hour" placeholder="时" type="number" autocomplete="off">
                                <template #append>时</template>
                            </el-input>
                        </el-col>
                        <el-col :span="4">
                            <el-input v-model="form.minute" placeholder="分" type="number" autocomplete="off">
                                <template #append>分</template>
                            </el-input>
                        </el-col>
                    </el-row>
                </el-form-item>
                <el-form-item label="地点">
                    <el-input v-model="form.location" autocomplete="off"/>
                </el-form-item>
                <el-form-item label="菜品名称">
                    <el-input v-model="form.dishName" autocomplete="off"/>
                </el-form-item>
                <el-form-item label="花费">
                    <el-input v-model="form.cost" type="number" autocomplete="off"/>
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
import { reactive, ref, computed } from "vue";

let tableData = ref([
    { time: '2023-07-29 12:30', location: '学二食堂', dishName: '麻婆豆腐', cost: 25 },
    { time: '2023-07-28 18:00', location: '学四食堂', dishName: '宫保鸡丁', cost: 30 },
    // 更多数据...
]);

let dialogFormVisible = ref(false);
let form = reactive({ year: '', month: '', day: '', hour: '', minute: '' });
const globalIndex = ref(-1);
const name = ref('');

// 分页相关的状态
const currentPage = ref(1);
const pageSize = ref(10); // 每页显示的数据条数

// 计算当前页显示的数据
const pagedData = computed(() => {
    const start = (currentPage.value - 1) * pageSize.value;
    const end = start + pageSize.value;
    return tableData.value.slice(start, end);
});

// 计算总页数
const total = computed(() => tableData.value.length);

const handleAdd = () => {
    // 获取当前时间并设置为默认值
    const now = new Date();
    form.year = now.getFullYear().toString();
    form.month = (now.getMonth() + 1).toString().padStart(2, '0'); // 月份从0开始，因此+1
    form.day = now.getDate().toString().padStart(2, '0');
    form.hour = now.getHours().toString().padStart(2, '0');
    form.minute = now.getMinutes().toString().padStart(2, '0');
    
    form.location = '';
    form.dishName = '';
    form.cost = '';
    globalIndex.value = -1;
    dialogFormVisible.value = true;
};

const save = () => {
    // 将分散的时间字段组合成一个完整的时间字符串
    form.time = `${form.year}-${form.month}-${form.day} ${form.hour}:${form.minute}`;

    if (globalIndex.value >= 0) {
        tableData.value[globalIndex.value] = { ...form };
        globalIndex.value = -1;
    } else {
        tableData.value.push({ ...form });
    }
    dialogFormVisible.value = false;
};

const handleEdit = (row, index) => {
    const [date, time] = row.time.split(' ');
    const [year, month, day] = date.split('-');
    const [hour, minute] = time.split(':');

    form.year = year;
    form.month = month;
    form.day = day;
    form.hour = hour;
    form.minute = minute;

    form.location = row.location;
    form.dishName = row.dishName;
    form.cost = row.cost;

    globalIndex.value = index;
    dialogFormVisible.value = true;
};

const remove = (index) => {
    // 计算在 tableData 中的实际索引
    const actualIndex = (currentPage.value - 1) * pageSize.value + index;
    tableData.value.splice(actualIndex, 1);
};

const search = () => {
    tableData.value = tableData.value.filter(v => v.dishName.includes(name.value));
};
</script>

<style scoped>
.main-title {
    font-size: 3.5rem;
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
</style>
