<template>
  <el-container class="g-detail">
    <el-aside width="300px">
      <div class="g-cover">
        <img :src="game_detail[0].fields.img_url" alt="">
      </div>
    </el-aside>
    <el-main>
      <div class="g-hd">
        <div class="g-title">{{game_detail[0].fields.name}}</div>
      </div>
      <div class="g-bd">
        <!-- <div class="g-desc">{{game_detail[0].fields.desc_snippet}}</div> -->
        <div class="g-desc">{{game_detail[0].fields.game_description}}</div>
      </div>
      <div class="g-tips">
        <span class="g-lx" v-if="game_detail[0].fields.minimum_requirements">{{game_detail[0].fields.minimum_requirements}}</span>
        <span class="g-lx" v-if="game_detail[0].fields.recommended_requirements">{{game_detail[0].fields.recommended_requirements}}</span>
        <span class="g-company el-icon-s-platform" v-if="game_detail[0].fields.types">  {{game_detail[0].fields.types}}</span>
        <span class="g-company el-icon-chat-line-round" v-if="game_detail[0].fields.languages">  {{game_detail[0].fields.languages}}</span>
        <span class="g-company el-icon-collection-tag" v-if="game_detail[0].fields.genre">  {{game_detail[0].fields.genre}}</span>
        <span class="g-company el-icon-office-building" v-if="game_detail[0].fields.developer">  {{game_detail[0].fields.developer}}</span>
        <span class="g-company el-icon-warning-outline" v-if="game_detail[0].fields.mature_conten">  {{game_detail[0].fields.mature_content}}</span>
      </div>
      <div class="g-btn">
        <button class="g-download" @click="download(game_detail[0].fields.url)"><i class="iconfont icon-thunderbolt"></i> Download</button>
        <button class="g-star" @click="like ? handleCancelLike(game_detail[0].fields.name) : handleLike(game_detail[0].fields.name)">
          <img src="../../../assets/img/like-active.png" v-if="like" width="15px" height="15px" style="cursor: pointer"/>
          <img src="../../../assets/img/like.png" v-else width="15px" height="15px" style="cursor: pointer"/>
          {{like ? ' Cancel Like' : ' Like'}}
        </button>
      </div>
      <pTime :date="game_detail[0].fields.release_date"></pTime>
      <pBack />
    </el-main>
  </el-container>
</template>

<script>
import {  mapState } from 'vuex'
import { _getGameDetail, _likeGame, _cancelLikeGame } from '@api'
import { convertParams } from '@utils'
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
      history.go(-1)
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
    async handleLike() {
      const { status, message, data } = await _likeGame(convertParams({'user_id': this.currentUser.id, 'game_name': this.$route.query.game_name}))
      if (status) {
        this.like = true
        this.$forceUpdate()
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
      const { status, message, data } = await _cancelLikeGame(convertParams({'user_id': this.currentUser.id, 'game_name': this.$route.query.game_name}))
      if (status) {
        this.like = false
        this.$forceUpdate()
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
  background-color: rgba(225, 240, 241, 0.651);
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
      color: #130c0c;
      line-height: 1.8;
    }
  }
  .g-tips {
    .g-lx {
      display: inline-block;
      padding: 4px 10px;
      border: 1px solid rgba(204, 204, 204, 0.459);
      border-radius: 4px;
      font-size: 14px;
    }
    .g-company {
      display: block;
      margin-top: 20px;
      letter-spacing: 2px;
      color: #1d2227;
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
      border: 0.2px solid #0b0f13;
      color: #0b0f13;
      &:hover {
        box-shadow: 0 0 0 3px rgba(235, 77, 75, 0.5);
        background-color: #eb4d4b;
        color: #fff;
      }
    }
    // .g-star {
    //   border: 0.2px solid #eb4d4b;
    //   color: #eb4d4b;
    //   &:hover {
    //     box-shadow: 0 0 0 3px rgba(235, 77, 75, 0.5);
    //     background-color: #eb4d4b;
    //     color: #fff;
    //   }
    // }
    .g-star-active {
      background-color: #eb4d4b;
      color: #fff;
    }
    .g-download {
      border: 0.2px solid #0b0f13;
      color: #0b0f13;
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
