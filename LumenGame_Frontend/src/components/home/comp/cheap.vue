<template>
<div>
  <div class="container"><span>特惠游戏</span>
  <div class="goods">
<cheapgoods :cheapgoods='cheapgoods'></cheapgoods>
  </div>
  </div>
  </div>
</template>

<script>
import cheapgoods from './cheapgoods.vue'
export default {
  components: {
    cheapgoods
  },
}
</script>

<style scoped lang="scss">
.container{
    position: absolute;
    top: 20%;
    width: 100%;
    height: 10%;
    
    span{
        float: left;
        color: #fff;
    }
    .goods{
        position: relative;
        top: 10%;
        width: 100%;
        height: auto;
        
    }
}
</style>