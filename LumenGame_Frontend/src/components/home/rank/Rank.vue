<template>
  <div class="rank">
    <el-container class="r-main">
      <el-aside width="160px">
        <a href="javascript:;" class="ranks-tag" v-for="(item, index) in ranks"
          :key="index" :class="{'ranks-tag-active':item.tag === currentIndex}"
          @click="setActive(item.tag)">{{item.name}}
        </a>
      </el-aside>
      <el-main>
        <rank-content v-if="flag" :games="gameList"
                      :currentPage="currentPage" :pagesize="pagesize"
                      :tag="currentIndex" :curPage="currentPage"/>
      </el-main>
    </el-container>
    <el-pagination
        @current-change="handleCurrentChange"
        v-if="flag"
        :total="total"
        :page-size="pagesize"
        layout="prev, pager, next"
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
        { name: '最高热度', tag: 'hot' },
        // { name: '口碑佳作', tag: 'score' },
        { name: '最新上架', tag: 'new' }
      ],
      currentIndex: 'hot',
      currentPage: 1,
      pagesize: 5,
      gameList: [],
      total: 0,
      flag: false
    }
  },
  methods: {
    ...mapActions([]),
    async fetchGameRank() {
      const { status, message, data } = await _getRank()
      this.gameList = JSON.parse(data)
      this.total = this.gameList ? this.gameList[0].fields.length : 0
      this.flag = true
    },
    setActive(val) {
      this.currentIndex = val
    },
    handleCurrentChange(currentPage) {
      this.currentPage = currentPage
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
  margin: 0 120px;
  .el-aside {
    padding: 20px 0;
    background-color: #fff;
    border: 1px solid #ccc;
    .box-shadow-in(#e4e4e4);
  }
  /deep/.el-main {
    padding: 0 20px 20px;
  }
  .ranks-tag {
    display: block;
    height: 30px;
    line-height: 30px;
    padding: 8px 10px;
    color: #666;
    &:hover {
      background-color: #f4f4f4;
    }
  }
  .ranks-tag-active {
    background-color: #f4f4f4;
  }
}
</style>
