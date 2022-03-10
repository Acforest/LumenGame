<template>
  <div class="rank">
    <el-container class="r-main">
      <el-aside width="160px">
        <a href="javascript:;" class="ranks-tag" v-for="(item, index) in ranks"
          :key="index" :class="{'ranks-tag-active': item.tag === currentIndex}"
          @click="setActive(item.tag)"><i :class="item.icon" style="margin-right: 6px;"></i>{{item.name}}
        </a>
      </el-aside>
      <el-main>
        <rank-content v-if="flag" :games="filtedGames" :tag="currentIndex"/>
      </el-main>
    </el-container>
    <el-pagination style="font-color: red;"
        @current-change="handleCurrentChange"
        v-if="flag"
        :current-page="currentPage"
        :total="total"
        :page-size="pagesize"
        layout="prev, pager, next, total, jumper"
        background
        >
    </el-pagination>
  </div>
</template>

<script>
import rankContent from './RankContent'
import { mapActions, mapState } from 'vuex'
import { _getRank } from '@api'
export default {
  data() {
    return {
      ranks: [
        { name: '最高热度', tag: 'hot', icon: 'el-icon-trophy' },
        { name: '最新上架', tag: 'new', icon: 'el-icon-time' },
        { name: '特别优惠', tag: 'special', icon: 'el-icon-shopping-bag-2' },
      ],
      currentIndex: 'hot',
      currentPage: 1,
      pagesize: 5,
      gameList: [],
      filtedGames: [],
      total: 0,
      flag: false
    }
  },
  methods: {
    ...mapActions([]),
    async fetchGameRank() {
      const { status, message, data } = await _getRank()
      this.gameList = JSON.parse(data)
      this.setActive(this.currentIndex)
      this.flag = true
    },
    setActive(val) {
      this.currentIndex = val
      this.currentPage = 1
      this.filtedGames = this.gameList.filter((item) => {
        return item.fields.rank_type === this.currentIndex
      })
      this.total = this.filtedGames.length
      // this.filtedGames = this.filtedGames.slice(0, this.pagesize)
      this.filtedGames = this.filtedGames.slice((this.currentPage - 1) * this.pagesize, this.currentPage * this.pagesize)
    },
    handleCurrentChange(currentPage) {
      this.currentPage = currentPage
      this.filtedGames = this.gameList.filter((item) => {
        return item.fields.rank_type === this.currentIndex
      })
      this.filtedGames = this.filtedGames.slice((this.currentPage - 1) * this.pagesize, this.currentPage * this.pagesize)
    }
  },
  computed: {
    ...mapState([]),
  },
  components: {
    rankContent
  },
  created() {
    this.currentIndex = 'hot'
    this.fetchGameRank()
  }
}
</script>
<style lang="less" scoped>
@import '~@css/variables.less';
@import '~@css/mixins.less';
.r-main {
  margin: 20px 120px;
  .el-aside {
    padding: 20px 0;
    background-color: #002D40;
    border: 1px solid #1AA6B7;
    .box-shadow-in(#1AA6B7);
  }
  /deep/.el-main {
    padding: 20px 20px 20px 20px;
    // ;
  }
  .ranks-tag {
    display: block;
    height: 30px;
    line-height: 30px;
    padding: 8px 10px;
    color: #5290aa;
    &:hover {
      background-color: #3fc9d877;
      color: #002D40;
    }
  }
  .ranks-tag-active {
    background-color: #3fc9d8;
    color: #002D40;
  }
}
</style>
