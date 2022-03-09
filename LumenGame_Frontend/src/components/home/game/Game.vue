<template>
  <div class="game">
    <div class="g-search">
      <p class="g-search-wrap">
        <el-input type="text" v-model="query.keyword" placeholder="请输入游戏名称" @keydown.enter.native="searchGame"></el-input>
        <span class="g-search-btn" @click="searchGame()">
          <i class="iconfont icon-search"></i>
        </span>
        <i class="iconfont icon-cuohao g-search-cls" v-show="showClear"
          @click="clearSearch()"></i>
      </p>
    </div>
    <el-container class="g-container">
      <el-aside class="g-nav" width="240px">
        <a href="javascript:;" class="nav-item" v-for="item in Array.from(category).slice(0, 36)" :key="item"
          :class="{'nav-active':currentItem === item}"
          @click="setActiveItem(item)">{{item}}</a>
      </el-aside>
      <el-container>
        <el-header class="g-header" style="height:40px">
          <game-tab :num="listNum" @click="changeTab($event)" />
        </el-header>
        <el-main class="g-main" v-if="gameList">
          <game-item :list="gameList.slice((currentPage - 1) * pagesize, currentPage * pagesize)"
            :curPage="currentPage"
            @click="setActiveItem($event)" />
        </el-main>
      </el-container>
    </el-container>
    <el-pagination
        @current-change="handleCurrentChange"
        :total="total"
        :current-page="currentPage"
        :page-size="pagesize"
        layout="prev, pager, next, total, jumper"
        background
        >
    </el-pagination>
  </div>
</template>

<script>
import { mapActions, mapState } from 'vuex'
import { _getRecGame1, _getRecGame2, _searchGame, _searchTag } from '@api'

import gameItem from './GameItem'
import gameTab from './GameTab'
const ALL = 0
export default {
  data() {
    return {
      query: {
        keyword: ''
      },
      category: new Set(),
      currentItem: 0,
      currentPage: 1,
      gameList: [],
      pagesize: 8,
      total: 0,
      // currentShow: 'list'
    }
  },
  methods: {
    ...mapActions(['fetchAllCategory', 'fetchAllGame']),
    // 获取游戏列表
    async fetchGame() {
      const { status, message, data } = await _getRecGame1({user_id: this.currentUser.id})
      this.gameList = JSON.parse(data)
      this.total = this.gameList ? this.gameList.length : 0
      this.handleCategory()
    },
    // 搜索游戏
    async searchGame() {
      const { status, message, data } = await _searchGame(this.query)
      this.gameList = JSON.parse(data)
      this.total = this.gameList ? this.gameList.length : 0
      this.handleCategory()
    },
    // 搜索标签
    async searchTag(tag) {
      const { status, message, data } = await _searchTag({'tag': tag})
      this.gameList = JSON.parse(data)
      this.total = this.gameList ? this.gameList.length : 0
      this.handleCategory()
    },
    // 清除搜索框
    clearSearch() {
      this.query.keyword = null
    },
    // 设置当前item
    setActiveItem(item) {
      this.searchTag(item)
      this.currentItem = item
    },
    // 处理分类
    handleCategory() {
      for (const item of this.gameList) {
        const tags = item.fields.popular_tags.split(',').slice(0, 5)
        for (const tag of tags) {
          this.category.add(tag)
        }
      }
    },
    // 切换列表
    // changeTab(val) {
    //   this.currentShow = val
    // },
    // 切换页面
    handleCurrentChange(currentPage) {
      this.currentPage = currentPage
    },
  },
  computed: {
    ...mapState(['allCategory', 'allGame', 'currentUser']),
    listNum() {
      return this.gameList.length
    },
    showClear() {
      return this.query.keyword !== ''
    }
  },
  components: {
    gameItem,
    gameTab
  },
  async created() {
    this.fetchGame()
    // console.log(this.allGame)
  }
}
</script>

<style lang="less" scoped>
@import '~@css/variables.less';
@import '~@css/mixins.less';
.g-search {
  .flex-x-y();
  height: 80px;
  .g-search-wrap {
    position: relative;
    margin: 0;
    // overflow: hidden;
    input {
      width: 500px;
      height: 40px;
      border: 1px solid #c4c4c4;
      box-sizing: border-box;
      padding: 0 20px;
      border-radius: 20px;
      &:focus {
        // border-color: @main-green;
        box-shadow: 0 0 0 3px rgba(66, 185, 131, 0.5);
      }
    }
    span {
      position: absolute;
      top: 0;
      right: 0;
      .flex-x-y();
      height: 40px;
      padding: 0 16px;
      border-left: 1px solid #ccc;
      cursor: pointer;
      border-radius: 0 20px 20px 0;
      transition: all 0.2s linear;
      &:hover {
        background-color: @main-green;
        color: #fff;
      }
    }
    .g-search-cls {
      position: absolute;
      top: 50%;
      right: 56px;
      transform: translate(0, -50%);
      &:hover {
        color: @main-green;
      }
    }
  }
}
.g-nav {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-evenly;
  align-content: space-around;
  height: 100%;
  border: 1px solid #1AA6B7;
  box-shadow: inset 0 0 0 1px #1AA6B7;
  padding: 20px 0;
  background-color: #fff;
  .nav-item {
    width: 100px;
    height: 30px;
    line-height: 30px;
    font-size: 14px;
    margin-top: 20px;
    background-color: #1aa7b785;      // 标签底色
    overflow: hidden;
    .box-shadow-in(#e4e4e400);
    color: #ffffff;                   // 标签文字颜色
    &:hover {
      background-color: #eee;
      border-color: transparent;
    }
  }
  .nav-item:nth-child(-n + 2) {
    margin-top: 0;
  }
  .nav-active {
    box-shadow: inset 0 0 0 1px @main-orange;
    background-color: #f69c001a;
    color: @main-orange;
  }
}
.g-main {
  background-color: #002d4091;     // 搜索出来的游戏结果显示的底色
  padding-top: 10px;
  padding: 0;
  margin: 20px;
  border: 1px solid #1AA6B7;
  color: #ffffff;
}

.g-header {
  background-color: #a4ccdcc5;   // 显示搜索到内容的底色
  padding: 0;
  margin: 0 20px;
  color: #ffffff;                 // 搜索条数字体的颜色
}

.el-input {
  width: 500px;
}

.el-aside {
  background-color: #002D40;
}

</style>
