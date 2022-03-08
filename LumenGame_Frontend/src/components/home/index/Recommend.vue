<template>
  <div>
    <div class="container">
      <div class="pic">
        <img :src="recommend.cover" @click="gotodetail(recommend.id)" alt="" />
      </div>
      <div class="content">
        <h4>{{ recommend.title }}</h4>
        <p>{{ recommend.description }}</p>
        <h4>{{ "￥" + recommend.price }}</h4>
        <div class="shopping">
          <!-- <div class="buynow" @click="gotodetail(recommend.id)"> -->
          <div class="buynow" @click="gotodetail(recommend.id)">
            立即购买
            <!-- {{ recommend.price != 0 ? "立即购买" : "免费游玩" }} -->
          </div>
          <!-- <div class="cart" @click="handleAddCart(recommend.id)"> -->
          <div class="cart">
            <img
              src="https://sanegame.oss-cn-hangzhou.aliyuncs.com/%E6%B7%BB%E5%8A%A0.png"
            />添至愿望清单
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, onMounted } from "vue";
import { useRouter } from "vue-router";
import { useStore } from "vuex";
export default {
  data() {
    return {
      recommend: {
        cover: '',
        title: 'holy',
        description: 'shit',
        price: 20,
        id: 10
      }
    }
  },
  // setup() {
  //   const recommend = ref([]);
  //   const store = useStore();
  //   const cid = ref();
  //   const router = useRouter();
  //   const gotodetail = (id) => {
  //     router.push({ path: "/detail", query: { id } });
  //   };
  //   const handleAddCart = (id) => {
  //     ElMessage({
  //       showClose: true,
  //       message: "添加愿望单成功！！",
  //       type: "success",
  //     });
  //     addCart({ goods_id: id, num: 1 }).then((res) => {
  //       if (res.status == "200" || res.status == "204") {
  //         //设置store中cartCount
  //         store.dispatch("updateCart");
  //       }
  //     });
  //   };
  //   return { recommend, cid, gotodetail, handleAddCart };
  // },
  components: {},
  methods: {
    gotodetail() {

    },
    handleAddCart() {

    }
  },
};
</script>
<style lang="less" scoped>
.container {
  position: absolute;
  top: 34%;
  width: 100%;
  height: auto;
  .pic {
    width: 60%;
    height: auto;
    float: left;

    overflow: hidden;
    img {
      width: 100%;
      border-radius: 15px;
      transition: all 0.2s;
    }
    img:hover {
      filter: invert(10%);
    }
  }
  .content {
    position: absolute;
    top: 30%;
    left: 65%;
    width: 35%;
    height: 50%;
    text-align: left;
    .shopping {
      position: absolute;
      width: 80%;
      top: 170px;
      display: flex;
      .buynow {
        background: #fff;
        color: #000;
        width: 30%;
        height: 4em;
        border-radius: 5px;
        text-align: center;
        line-height: 4em;
        font-size: 12px;
      }
      .cart {
        width: 30%;
        height: 4em;
        display: flex;
        font-size: 12px;
        text-align: center;
        line-height: 4em;
        background-color: white;
        background-color: rgba(0, 0, 0, 0);
        transition: all 0.5s;
        border-radius: 3px;
        color: #fff;
        img {
          position: relative;
          top: 25%;
          width: 20px;
          height: 20px;
          margin-left: 10%;
          margin-right: 5%;
        }
      }
      .cart:hover {
        background-color: white;
        background-color: rgba(150, 150, 150, 0.5);
      }
    }

    h4 {
      color: #fff;
      font-size: 20px;
      font-weight: 400px;
    }
    p {
      color: #909399;
      margin: 8% 0 8% 0;
    }
  }
}
</style>