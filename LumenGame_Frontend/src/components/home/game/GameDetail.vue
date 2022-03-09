<template>
  <el-container class="g-detail">
    <el-aside width="300px">
      <div class="g-cover">
        <img :src="game_detail[0].fields.img_url || 
        'https://cdn1.epicgames.com/spt-assets/a7ecccc8ca084febb744ca0d141b8061/download-amelie-offer-1tdkw.jpg?h=854&resize=1&w=640'" alt="">
        <!-- <img src="https://cdn1.epicgames.com/spt-assets/a7ecccc8ca084febb744ca0d141b8061/download-amelie-offer-1tdkw.jpg?h=854&resize=1&w=640" alt=""> -->
      </div>
    </el-aside>
    <el-main>
      <div class="g-hd">
        <div class="g-title">{{game_detail[0].fields.name}}</div>
      </div>
      <div class="g-bd">
        <div class="g-desc">{{game_detail[0].fields.desc_snippet}}</div>
      </div>
      <div class="g-tips">
        <span class="g-lx">{{game_detail[0].fields.name}}</span>
        <span class="g-company icon-home iconfont">{{game_detail[0].fields.developer}}</span>
      </div>
      <div class="g-btn">
        <button class="g-download" @click="download(game_detail[0].fields.url)"><i
            class="iconfont icon-thunderbolt"></i>下载</button>
        <button class="g-star" @click="starGame()" :class="{'g-star-active': like}"><i
            class="iconfont icon-icon-test2"></i>122</button>
      </div>
      <pTime :date="game_detail[0].fields.release_date"></pTime>
      <pBack />
    </el-main>
  </el-container>
</template>

<script>
import {  mapState } from 'vuex'
import { _getGameDetail } from '@api'
import pTime from '@/components/common/Time'
import pBack from '@/components/common/Back'
export default {
  // props: {
  //   game_detail
  // },
  data() {
    return {
      like: false,
      game_detail: null,
    }
  },
  computed: {
    ...mapState(['currentUser']),
  },
  methods: {
    // 返回
    backToLast() {
      this.$router.push('/game')
    },
    // 下载
    download(url) {
      location.href = url
    },
    async getGameDetail() {
      const { status, message, like, detail } = await _getGameDetail({'user_id': this.currentUser.id, 'game_name': this.$route.query.game_name})
      this.like = like
      this.game_detail = JSON.parse(detail)
      console.log(this.game_detail)
    },
    // 收藏游戏
    async starGame() {
      if (this.hasStar === true) {
        // 取消收藏
        if (this.currentStar && this.currentStar.id) {
          console.log(123)
          const { success } = await _deleteStar(this.currentStar.id)
          if (success) {
            this.$message.success('取消收藏')
            this.fetchAllStar()
          } else {
            this.$message.error('取消失败')
          }
        } else {
          console.log('cancel star error')
        }
      } else if (this.hasStar === false) {
        // 收藏
        const { success } = await _addStar(this.handleStar())
        if (success) {
          this.$message.success('收藏成功')
          this.fetchAllStar()
        } else {
          this.$message.error('收藏失败')
        }
      } else {
        console.log('star error')
      }
    },
  },
  components: {
    pTime,
    pBack
  },
  created() {
    this.getGameDetail()
  }
}
</script>
<style lang="less" scoped>
@import '~@css/variables.less';
.el-container {
  display: flex;
  background-color: #fff;
  padding: 20px;
}
.el-aside {
  .g-cover {
    width: 250px;
    height: 358px;
    img {
      width: inherit;
      height: inherit;
    }
  }
}
.el-main {
  flex: 1;
  position: relative;
  text-align: left;
  padding-top: 0;
  & > div {
    margin-bottom: 20px;
  }
  .g-hd {
    .g-title {
      font-size: 30px;
    }
  }
  .g-bd {
    padding-right: 200px;
    .g-desc {
      color: #3c3c3c;
      line-height: 1.8;
    }
  }
  .g-tips {
    .g-lx {
      display: inline-block;
      padding: 4px 10px;
      border: 1px solid #ccc;
      border-radius: 4px;
      font-size: 14px;
    }
    .g-company {
      display: block;
      margin-top: 20px;
      letter-spacing: 2px;
      color: #6c757d;
    }
  }
  .g-btn {
    position: absolute;
    text-align: center;
    bottom: 0;
    left: 50%;
    transform: translateX(-50%);
    button {
      background-color: transparent;
      outline: none;
      cursor: pointer;
      border-radius: 4px;
      padding: 8px 10px;
      font-size: 15px;
      margin-right: 10px;
      transition: color 0.15s ease-in-out, background-color 0.15s ease-in-out,
        border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out;
      i {
        font-size: inherit;
      }
    }
    .g-star {
      border: 0.2px solid #eb4d4b;
      color: #eb4d4b;
      &:hover {
        box-shadow: 0 0 0 3px rgba(235, 77, 75, 0.5);
        background-color: #eb4d4b;
        color: #fff;
      }
    }
    .g-star-active {
      background-color: #eb4d4b;
      color: #fff;
    }
    .g-download {
      border: 0.2px solid #6c757d;
      color: #6c757d;
      &:hover {
        box-shadow: 0 0 0 3px rgba(108, 117, 125, 0.5);
        background-color: #6c757d;
        color: #fff;
      }
    }
  }
  .p-back {
    position: absolute;
    top: 10px;
    right: 40px;
  }
  .p-time {
    position: absolute;
    top: 80px;
    right: 20px;
  }
}
</style>
