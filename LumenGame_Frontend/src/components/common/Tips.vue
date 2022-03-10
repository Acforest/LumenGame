<template>
  <div class="p-tips">
    <div class="warp">
      
      <div class="text">发布时间</div>
      <div class="desc">{{date || '未知'}}</div>
    </div>
    <!-- <div class="warp" v-else-if="type==='score'">
      <div class="text">{{score || 0}} 分</div>
      <div class="desc">当前评分</div>
    </div>
    <div class="warp" v-else-if="type==='star'">
      <div class="text">{{star}}</div>
      <div class="desc">收藏数量</div>
    </div> -->
  </div>
</template>

<script>
// type - new score star
export default {
  props: {
    date: {
      type: String
    },
    type: {
      type: String
    }
  },
  data() {
    return {}
  },
  created() {}
}
</script>

<style lang="less" scoped>
@import '~@css/mixins.less';
.warp {
  position: relative;
  width: 140px;
  text-align: center;
  &::before {
    position: absolute;
    left: 0;
    content: '';
    width: 2px;
    height: 100%;
    background-color: #ccc;
  }
  .text {
    color: #3c3c3c;
    text-shadow: -1px 1px 0px #ccc;
  }
  .desc {
    color: #6c757d;
    font-size: 14px;
  }
}
</style>
