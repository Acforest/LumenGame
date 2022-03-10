<template>
  <div class="game-item">
    <template v-if="allNum">
      <ul>
        <!-- card -->
        <li class="g-card" v-for="(item, index) in list" :key="index">
          <a style="cursor: pointer" @click="goGameDetail(item.fields.name)">
            <div class="g-cover">
              <img :src="item.fields.img_url" alt="">
            </div>
            <div class="g-content">
              <h3 class="g-title">{{item.fields.name}}</h3>
              <div class="g-company">{{(item.fields.publisher || '').split(',')[0]}}
                <span class="g-lx">
                  <el-button type="mini" v-for="(tag, idx) in (item.fields.popular_tags || '').split(',').slice(0, 5)"
                    :key="idx" v-on:click.stop="handleClick(tag)">
                    {{tag}}
                  </el-button>
                </span>
              </div>
            </div>
            <div class="g-time">
              {{item.fields.release_date !== 'NaN' ? item.fields.release_date : '未知'}}
            </div>
          </a>
        </li>
      </ul>
    </template>
    <template v-else>
      暂无游戏
    </template>
  </div>

</template>

<script>
import { bindURL, convertParams } from '@utils'
import { mapActions, mapGetters, mapMutations, mapState } from 'vuex'
import { _likeGame, _cancelLikeGame } from '@api'

export default {
  props: {
    list: Array,
    type: String,
    like: Set
  },
  data() {
    return {
      likeSet: null
    }
  },
  methods: {
    // ...mapActions(['fetchAllCategory']),
    // ...mapMutations(['setCurrentGame']),
    handleClick(tag) {
      this.$emit('click', tag)
    },
    goGameDetail(name) {
      this.$router.push({path: '/game/' + name, query: {'game_name': name}})
    },
    async handleLike(game_name) {
      const { status, message, data } = await _likeGame(convertParams({'user_id': this.currentUser.id, 'game_name': game_name}))
      if (status) {
        // this.$emit('addLike', game_name)
        this.likeSet.add(game_name)
        this.$forceUpdate()
        // this.likeSet = new Set()
        this.$message({
          message: '收藏成功',
          type: 'success',
          offset: 300
        })
      } else {
        this.$message({
          message: '收藏失败',
          type: 'error',
          offset: 300
        })
      }
    },
    async handleCancelLike(game_name) {
      const { status, message, data } = await _cancelLikeGame(convertParams({'user_id': this.currentUser.id, 'game_name': game_name}))
      if (status) {
        // this.$emit('deleteLike', game_name)
        this.likeSet.delete(game_name)
        this.$forceUpdate()
        // this.likeSet = new Set()
        this.$message({
          message: '取消收藏成功',
          type: 'success',
          offset: 300
        })
      } else {
        this.$message({
          message: '取消收藏失败',
          type: 'error',
          offset: 300
        })
      }
    }
  },
  watch: {
    likeSet: {
      handler: function(newVal, oldVal) {
        console.log('change!')
      },
      deep: true
    }
  },
  computed: {
    ...mapState(['currentUser']),
    blankNum() {
      return this.allNum % 4 === 0 ? 0 : 4 - (this.allNum % 4)
    },
    allNum() {
      return this.list.length
    },
  },
  created() {
    this.likeSet = this.like
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
        background-color: #1aa7b785;    // 卡片底色
        border: 1px solid #1aa7b785;
        border-top: none;
        // .box-shadow-tx(#eee, #eee);
      }
      .g-title {
        margin-bottom: 10px;
        font-size: 500;
        color: #ebebeb;                 // 游戏名颜色
        overflow: hidden;
        .text-ellipsis();
      }
      .g-company {
        height: 100px;
        color: #1AA6B7;
        font-weight: 300;
        // overflow: hidden;
        // .text-ellipsis();
      }
      .g-tag {
        float: left;
        .el-button {
          background-color: rgba(0, 0, 0, 0.253);
          border: 0px;
          color: rgba(202, 202, 202, 0.527);
          margin-top: 5px;
        }
      }
    }
    &:hover {
      img {
        transform: scale(1.05);
      }
      .g-content {
        background: #056c7785;
      }
    }
  }
  // 18 15 14
  // card
  .g-card {
    height: 160px;
    width: 100%;
    background-color: rgba(41, 126, 145, 0.568);
    border: 1px solid rgb(175, 206, 231);
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
        color: rgb(255, 255, 255);
        text-indent: 2em;
        .g-title {
          font-weight: 520;
        }
        .g-company {
          color: rgb(255, 255, 255);
        }
        .g-lx {
          display: inline-block;
          // border: 1px solid rgb(94, 87, 87);
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
        color: #ffffff;
        font-size: 16px;
        letter-spacing: 0.1em;
      }
      &:hover {
        img {
          transform: scale(1.1);
        }
        .g-content {
          background-color: #50959e7a;
        }
      }
    }
  }
}
</style>