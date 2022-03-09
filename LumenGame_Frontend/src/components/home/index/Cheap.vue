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
import cheapgoods from './CheapGoods.vue'
import { ref, onMounted } from 'vue'
// import { getCategory, getCategoryGoods } from "../../../network/category"
export default {

name: '',
setup() {
// const cheapgoods = ref([]);
//     onMounted(()=>{
//       getCategoryGoods("sales", 26).then((res) => {
//         cheapgoods.value = res.goods.data;
//       });
//     })

//     return {cheapgoods};
},
components: {
    cheapgoods
}

}

</script>

<style scoped  lang="less">
.container{
    position: absolute;
    top: 120%;
    width: 97%;
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
