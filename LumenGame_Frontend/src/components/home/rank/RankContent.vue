<template>
  <div class="rank-content">
    <ul>
      <li class="rank-item" v-for="(item, index) in filtedGames" :key="index">
        <!-- <a href="javascript:;" @click="goTo(item.fields.url)"> -->
        <a :href="item.fields.url">
          <div class="r-cover">
            <img :src="item.fields.img_url" alt="">
          </div>
          <div class="r-content">
            <p class="r-name"> {{item.fields.name}}</p>
            <span class="r-lx">{{item.fields.price}}</span>
          </div>
        </a>
        <pTips :type="item.fields.rank_type"/>
      </li>
    </ul>
  </div>
</template>

<script>
import { bindURL } from '@utils'
import { mapActions, mapGetters, mapMutations, mapState } from 'vuex'
import pTips from '@/components/common/Tips'
export default {
  props: {
    games: Array,
    tag: String,
    currentPage: Number,
    pagesize: Number
  },
  data() {
    return {
      filtedGames: [],
    }
  },
  methods: {
    ...mapMutations(['setCurrentGame', 'setHCurrentIndex']),
    ...mapActions([]),
    bindURL,
    goTo(id) {
      this.setCurrentGame(this.currentGame(id))
      this.$router.push('/game/' + id)
      this.setHCurrentIndex()
    },
  },
  computed: {
    ...mapState(['allStar', 'allGame']),
    ...mapGetters(['getStarByGameId']),
  },
  components: {
    pTips
  },

  watch: {
    tag: function(newVal, oldVal) {
      console.log(newVal)
      this.filtedGames = this.games.filter((item) => {
        return item.fields.rank_type === newVal
      })
      this.filtedGames = this.filtedGames.slice((this.currentPage - 1) * this.pagesize, this.currentPage * this.pagesize)
    },
    currentPage: function(newVal, oldVal) {
      this.filtedGames = this.games.filter((item) => {
        return item.fields.rank_type === this.tag
      })
      this.filtedGames = this.filtedGames.slice((newVal - 1) * this.pagesize, newVal * this.pagesize)
    },
    pagesize: function(newVal, oldVal) {
      this.filtedGames = this.games.filter((item) => {
        return item.fields.rank_type === this.tag
      })
      this.filtedGames = this.filtedGames.slice((this.currentPage - 1) * newVal, this.currentPage * newVal)
    }
  },

  created() {
    this.filtedGames = this.games.filter((item) => {
        return item.fields.rank_type === this.tag
    })
    this.filtedGames = this.filtedGames.slice((this.currentPage - 1) * this.pagesize, this.currentPage * this.pagesize)
  }
}
</script>

<style lang="less" scoped>
.rank-content {
  ul {
    width: 100%;
    display: flex;
    flex-wrap: wrap;
    justify-content: start;
  }
  // padding: 10px 20px;
  background-color: #fff;

  border: 1px solid #ccc;
  .rank-item {
    position: relative;
    box-sizing: border-box;
    padding: 10px;
    height: 140px;
    width: 100%;
    border-bottom: 1px solid #ccc;
    overflow: hidden;
    transition: all 0.2s cubic-bezier(0.55, 0.055, 0.675, 0.19);
    a {
      display: flex;
      height: 100%;
      width: 100%;
    }
    .r-cover {
      width: 200px;
      overflow: hidden;
      img {
        width: 100%;
        transition: all 0.3s linear;
      }
    }
    &:hover {
      background-color: #f4f4f4;
      .r-cover img {
        transform: scale(1.05);
      }
    }
    .r-content {
      text-align: left;
      color: #666;
      margin-left: 2em;
      .r-name {
        font-size: 24px;
      }
      .r-lx {
        display: inline-block;
        border: 1px solid #ccc;
        padding: 0.5em 1em;
        font-size: 14px;
      }
    }
    .p-tips {
      position: absolute;
      right: 20px;
      top: 20px;
      font-size: 20px;
    }
  }
}
</style>
