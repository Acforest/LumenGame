<template>
  <div class="game-item">
    <template v-if="allNum">
      <!-- list -->
      <ul class="list">
        <li class="g-list" v-for="(item, index) in list" :key="index">
          <!-- <a href="javascript:;" @click="goGameDetail(item.name)"> -->
          <a>
            <div class="g-cover">
              <img :src="item.photo" alt="">
            </div>
            <div class="g-content">
              <h3 class="g-title">{{item.fields.name}}</h3>
              <!-- <img src="../../../assets/img/like.png"/> -->
              <p class="g-company">{{item.fields.publisher.split(',')[0]}}
                <span class="g-tag">
                  <el-button type="mini" v-for="(tag, idx) in item.fields.popular_tags.split(',').slice(0, 5)"
                    :key="idx" @click="handleClick(tag)">
                    {{tag}}
                  </el-button>
                </span>
              </p>
            </div>
          </a>
        </li>
        <!-- 占位 -->
        <!-- <li v-for="item in blankNum" class="g-list"></li> -->
      </ul>
      <!-- <ul v-else-if="type === 'card'"> -->
        <!-- card -->
        <!-- <li class="g-card" v-for="item in filterList" :key="item"> -->
          <!-- <a href="javascript:;" @click="goGameDetail(item)"> -->
            <!-- <div class=" g-cover"> -->
              <!-- <img :src="item.photo" alt=""> -->
            <!-- </div> -->
            <!-- <div class="g-content"> -->
              <!-- <h3 class="g-title">{{item.fields.name}}</h3> -->
              <!-- <p class="g-company">{{item.fields.publisher.split(',')[0]}}</p> -->
              <!-- <span class="g-lx" @click="handleClick(item)">{{item.fields.popular_tags}}</span> -->
            <!-- </div> -->
            <!-- <div class="g-time">
              {{item.createTime | formatDate(1)}}
            </div> -->
          <!-- </a> -->
        <!-- </li> -->
      <!-- </ul> -->
    </template>
    <template v-else>
      暂无游戏
    </template>
  </div>

</template>

<script>
import { bindURL } from '@utils'
import { mapActions, mapGetters, mapMutations } from 'vuex'

export default {
  props: {
    list: Array,
    type: String,
  },
  methods: {
    bindURL,
    ...mapActions(['fetchAllCategory']),
    ...mapMutations(['setCurrentGame']),
    handleClick(tag) {
      this.$emit('click', tag)
    },
    goGameDetail(name) {
      this.setCurrentGame(name)
      this.$router.push('/game/' + name)
    }
  },
  computed: {
    ...mapGetters(['getMiniCategoryList']),
    blankNum() {
      return this.allNum % 4 === 0 ? 0 : 4 - (this.allNum % 4)
    },
    allNum() {
      return this.list.length
    },
    filterList() {
      return this.list.map((i) => {
        const item = this.getMiniCategoryList().find(
          (j) => j.id === Number(i.lx)
        )
        i.lxName = item.name
        return i
      })
    }
  },
  created() {
    if (this.type === 'card') {
      this.fetchAllCategory()
    }
  }
}
</script>

<style lang="less" scoped>
@import '~@css/mixins.less';
@import '~@css/variables.less';
.game-item {
  padding: 20px;
  .list {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
  }
  // list
  .g-list {
    width: 300px;
    border-radius: 4px;
    // overflow: hidden;
    a {
      display: inline-block;
      width: 100%;
      height: 100%;
      margin-bottom: 60px;
      .g-cover {
        width: 300px;
        height: 140px;
        // overflow: hidden;
        img {
          width: 100%;
          height: 100%;
        }
      }
      .g-content {
        box-sizing: border-box;
        width: 100%;
        background-color: #daebeca6;
        border: 1px solid #daebeca6;
        border-top: none;
        // .box-shadow-tx(#eee, #eee);
      }
      .g-title {
        font-weight: 400;
        overflow: hidden;
        .text-ellipsis();
      }
      .g-company {
        height: 100px;
        color: #000;
        // overflow: hidden;
        // .text-ellipsis();
      }
      .g-tag {
        float: left;
      }
    }
    &:hover {
      img {
        transform: scale(1.05);
      }
      .g-content {
        background: #f4f4f4;
      }
    }
  }
  // 18 15 14
  // card
  .g-card {
    height: 160px;
    width: 100%;
    background-color: rgb(179, 33, 33);
    border: 1px solid #eee;
    .box-shadow-tx(#eee, #eee);
    margin-bottom: 10px;
    a {
      display: flex;
      position: relative;
      justify-content: start;
      transition: all 0.5s ease-in-out;
      .g-cover {
        height: 160px;
        overflow: hidden;
        img {
          // height: inherit;
          vertical-align: bottom;
        }
      }
      .g-content {
        flex: 1;
        text-align: left;
        color: #000;
        text-indent: 2em;
        .g-title {
          font-weight: 400;
        }
        .g-company {
          color: #777;
        }
        .g-lx {
          display: inline-block;
          border: 1px solid #ccc;
          padding: 0.5em 1em;
          text-indent: 0;
          font-size: 14px;
          margin: 0.5em 0 0 2em;
          &:hover {
            color: @main-orange;
            border-color: @main-orange;
          }
        }
      }
      .g-time {
        position: absolute;
        right: 20px;
        top: 20px;
        color: #909399;
        font-size: 14px;
        letter-spacing: 0.1em;
      }
      &:hover {
        img {
          transform: scale(1.1);
        }
        .g-content {
          background-color: #f4f4f4;
        }
      }
    }
  }
}
</style>