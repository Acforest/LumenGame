<template>
  <div>
    <div class="top">
      <div class="top-item">
        <el-menu
          style="border: none; width: 80%; height: auto"
          class="el-menu-demo"
          mode="horizontal"
          background-color="rgb(18,18,18)"
          text-color="#fff"
          active-text-color="#D351E1"
        >
          <el-menu-item index="1">探索</el-menu-item>
          <el-menu-item index="2">浏览</el-menu-item>
        </el-menu>
        <el-badge
          class="item"
          style="width: 7%; background: rgb(18, 18, 18)"
        >
          <router-link to="/shopcart"
            ><a href="#"><span>愿望清单</span></a></router-link
          >
        </el-badge>
        <div class="search">
          <el-input
            placeholder="搜索"
            v-model="input"
            clearable
            prefix-icon="el-icon-search"
          >
          </el-input>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { defineComponent, onMounted, ref, reactive, toRefs } from "vue";
import { useRouter } from "vue-router";
// import { searchGoods } from "../../../network/category";
import { useStore } from "vuex";
export default {
  data() {

  },
  // setup() {
  //   const activeIndex = ref("1");
  //   const activeIndex2 = ref("1");
  //   const router = useRouter();
  //   const store = useStore();
  //   onMounted(() => {
  //     store.dispatch("updateCart");
  //   });
  //   const search = ref([]);
  //   const change = (input) => {
  //     searchGoods(input).then((res) => {
  //       search.value = res.goods.data;
  //     });
  //   };
  //   const tosearch = (id) => {
  //     router.push({ path: "/category", query: { id: JSON.stringify(id) } });
  //     setTimeout(() => {
  //       router.go(0);
  //     }, 200);
  //   };
  //   const tohome = () => {
  //     router.push({ path: "/home" });
  //   };
  //   const toabout = () => {
  //     router.push({ path: "/about" });
  //   };
  //   const handleSelect = (key, keyPath) => {
  //     console.log(key, keyPath);
  //   };
  //   return {
  //     activeIndex,
  //     activeIndex2,
  //     handleSelect,
  //     input: ref(""),
  //     tohome,
  //     toabout,
  //     change,
  //     tosearch,
  //     search,
  //   };
  // },
  components: {},
  methods: {},
};
</script>
<style lang='less' scoped>
.top {
  position: fixed;
  top: 6.3%;
  width: 100%;
  height: 11%;
  background: rgb(18, 18, 18);
  /* background:rgb(18,18,18); */
  opacity: 0.95;
  z-index: 10;
}
.top-item {
  position: relative;
  width: 74%;
  height: 45%;
  margin-top: 1.5%;
  margin-left: 13%;
  background: rgb(18, 18, 18);
  display: flex;
}
.item {
  margin-top: 1%;
  margin-right: 3%;
  span {
    color: #606266;
    transition: all 0.3s;
  }
  span:hover {
    color: #fff;
  }
}

.search {
  width: 17%;
}
.explore {
  float: left;
  height: 100%;
  background: rgb(18, 18, 18);
}
.browser {
  float: left;
  height: 100%;
}

.el-input {
  --el-input-background-color: #303133;
  --el-input-border: #303133;
  --el-input-focus-border: #fff;
  --el-input-icon-color: #fff;
  --el-input-placeholder-color: #fff;
  --el-input-font-color: #fff;
}
.search {
  height: 90%;
}
.search img {
  float: left;
}
</style>