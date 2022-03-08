<template>
  <div>
    <div class="free">
      <div class="top">
        <img
          src="https://sanegame.oss-cn-hangzhou.aliyuncs.com/%E7%A4%BC%E7%89%A9.png"
          style="height: 80%; float: left"
        />
        <p>免费游戏</p>
        <el-button style="float: right; background: #303133" type="info"
          >查看更多</el-button
        >
      </div>
      <div class="container">
        <div class="item" v-for="item in freegoods" :key="item.id">
          <img :src="item.cover" alt="" @click="gotodetail(item.id)" />

          <p @click="gotodetail(item.id)">{{ item.title }}</p>
          <div class="price">
            <div class="cheapper"><p>-100%</p></div>
            <p style="color: grey; text-decoration: line-through">
              {{ "￥" + item.price }}
            </p>
            <p>免费</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { useRouter } from "vue-router";
export default {
  props: {
    // freegoods: {
    //   type: Array,
    //   default() {
    //     return [];
    //   },
    // },
  },
  data() {
    return {
      freegoods: [
        { id: 1, title: "shit", price: 20, cover: 'https://cdn1-epicgames-1251447533.file.myqcloud.com/salesEvent/salesEvent/EGS_VoidBastards_BlueManchu_S1_2560x1440-6ffb5f547e5434d115cc6de7d13b1bc6?h=480&resize=1&w=854' },
        { id: 2, title: "haha", price: 10, cover: 'https://cdn1-epicgames-1251447533.file.myqcloud.com/salesEvent/salesEvent/EGS_YookaLaylee_Playtonic_S3_2560x1440-779ed9403879e74fe1992fefeec9b0d5?h=480&resize=1&w=854' },
        { id: 3, title: "haha", price: 10, cover: 'https://cdn1-epicgames-1251447533.file.myqcloud.com/salesEvent/salesEvent/EGS_YookaLaylee_Playtonic_S3_2560x1440-779ed9403879e74fe1992fefeec9b0d5?h=480&resize=1&w=854' },
      ],
    };
  },
  components: {},
  methods: {},
};
</script>

<style lang="less" scoped >
.free {
  position: absolute;
  left: 3%;
  width: 94%;
  height: 100%;

  .container {
    display: flex;
    .item {
      width: 32%;
      height: auto;
      margin: 0 1% 0 1%;
      border-radius: 10px;

      p {
        color: #fff;
        line-height: 200%;
        text-align: left;
        margin: 0% 0 1% 0;
      }
      img {
        width: 100%;
        border-radius: 5px;
        transition: all 0.2s;
      }
      img:hover {
        filter: invert(15%);
      }
      .price {
        display: flex;
        p {
          margin: 5% 1.5% 0 1.5%;
          font-family: sans-serif;
          font-weight: 700;
        }
        .cheapper {
          position: relative;
          top: 23px;
          width: 15%;
          height: 30%;
          background: #721e78;
          border-radius: 5px;
          margin-right: 1.5%;
          p {
            text-align: center;
            font-size: 12px;
          }
        }
      }
    }
  }
  .top {
    width: 100%;
    height: 10%;

    margin: 2.5% 0 1% 0;
    p {
      float: left;
      color: #fff;
      font-size: 18px;
      line-height: 2em;
      margin-left: 1%;
    }
  }
}
</style>