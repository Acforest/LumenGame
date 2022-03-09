<template>
  <div class="index">
    <!-- 轮播图 -->
    <!-- <el-carousel :interval="3000" type="card" height="300px" @change="handleChange($event)">
      <el-carousel-item v-for="(item,index) in noticeList" :key="item.id">
        <div class="container" @click="showNotice(item,index)">
          <img :src="item.fields.url" alt="">
          <transition name="fade">
            <div class="banner" v-show="currentIndex === index">
              <div class="title">
                {{item.fields.title}}</div>
              <div class="desc">
                {{item.fields.comment}}</div>
            </div>
          </transition>
        </div>
      </el-carousel-item>
    </el-carousel> -->

    <div class="thumb-example">
      <!-- swiper1 -->
      <swiper class="swiper gallery-top" :options="swiperOptionTop" ref="swiperTop">
        <swiper-slide class="slide-1"></swiper-slide>
        <swiper-slide class="slide-2"></swiper-slide>
        <swiper-slide class="slide-3"></swiper-slide>
        <swiper-slide class="slide-4"></swiper-slide>
        <swiper-slide class="slide-5"></swiper-slide>
        <div class="swiper-button-next swiper-button-white" slot="button-next"></div>
        <div class="swiper-button-prev swiper-button-white" slot="button-prev"></div>
      </swiper>
      <!-- swiper2 Thumbs -->
      <swiper class="swiper gallery-thumbs" :options="swiperOptionThumbs" ref="swiperThumbs">
        <swiper-slide class="slide-1"></swiper-slide>
        <swiper-slide class="slide-2"></swiper-slide>
        <swiper-slide class="slide-3"></swiper-slide>
        <swiper-slide class="slide-4"></swiper-slide>
        <swiper-slide class="slide-5"></swiper-slide>
      </swiper>
    </div>

    <!-- 功能模块 -->
    <!-- <ul class="f-main">
      <li class="f-item" v-for="(item, index) in content" :key="index">
        <a :href="'#' + item.url">
          <div class="f-img">
            <img :src="item.src" alt="">
          </div>
          <div class="f-tips">
            <h3 class="f-title">{{item.title}}</h3>
            <p class="f-desc">{{item.desc}}</p>
          </div>
        </a>
      </li>
    </ul> -->

    <!-- 公告展示 -->
    <!-- <el-dialog :visible.sync="noticeDialogVisible" width="30%">
      <div class="d-head">
        <span class="d-title">{{currentNotice.title}}</span>
        <span class="d-date">{{currentNotice.createTime | formatDate}}</span>
      </div>
      <div class="d-main">
        <div v-html="currentNotice.comment"></div>
      </div>
    </el-dialog> -->

    <div class="hot_index">
          <h2 class="home_page_content_title">
            热门推荐
            <span class="hot_more">
              <router-link :to="{path:'/rank'}">浏览更多</router-link>
            </span>
          </h2>
          <swiper :options="swiperOption" ref="mySwiper">
              <swiper-slide class="slide-1">1</swiper-slide>
              <swiper-slide class="slide-2">Slide 2</swiper-slide>
              <swiper-slide class="slide-3">Slide 3</swiper-slide>
              <swiper-slide class="slide-4">Slide 4</swiper-slide>
              <!-- <swiper-slide v-for="(item, index) in hotList" :key="item.id"></swiper-slide> -->
              <div class="swiper-pagination" slot="pagination"></div>
              <div class="swiper-button-prev" slot="button-prev"></div>
              <div class="swiper-button-next" slot="button-next"></div>
          </swiper>
    </div>

    <div class="hot_index">
          <h2 class="home_page_content_title">
            最新发布
            <span class="hot_more">
              <router-link :to="{path:'/rank'}">浏览更多</router-link>
            </span>
          </h2>
          <swiper :options="swiperOption" ref="mySwiper">
              <swiper-slide>Slide 1</swiper-slide>
              <swiper-slide>Slide 2</swiper-slide>
              <swiper-slide>Slide 3</swiper-slide>
              <swiper-slide>Slide 4</swiper-slide>
              <!-- <swiper-slide v-for="(item, index) in hotList" :key="item.id"></swiper-slide> -->
              <div class="swiper-pagination" slot="pagination"></div>
              <div class="swiper-button-prev" slot="button-prev"></div>
              <div class="swiper-button-next" slot="button-next"></div>
          </swiper>
    </div>

    <!-- <pRecommend></pRecommend> -->
    <!-- <div>
      <pFree></pFree>
    </div> -->
    <!-- <pCheap></pCheap> -->
    <!-- <pTop></pTop> -->
  </div>
</template>

<script>
// 公告对话框形式
import { _getBannerList } from '@api'
import { bindURL, convertDeepCopy } from '@utils'
// import cheap from '../comp/Cheap'
import pRecommend from './Recommend'
import pFree from './Free'
import pTop from './Top'
import pCheap from './Cheap.vue'
import { swiper, swiperSlide } from 'vue-awesome-swiper'
import 'swiper/dist/css/swiper.css'

export default {
  data() {
    return {
      query: {
        page: 1,
        size: 5
      },
      noticeList: [],
      currentIndex: 0,
      content: [
        {
          url: '/game',
          src: require('/src/assets/img/f-img.png'),
          title: '游戏中心',
          desc: '海量游戏任你游玩'
        },
        {
          url: '/rank',
          src: require('/src/assets/img/f-img.png'),
          title: '排行榜',
          desc: '最热游戏尽在眼前'
        },
        {
          url: '/share',
          src: require('/src/assets/img/f-img.png'),
          title: '游戏论坛',
          desc: '尽情交流游戏心得'
        }
      ],
      noticeDialogVisible: false,
      currentNotice: {},
      swiperOption: {
        slidesPerView: 3,
        spaceBetween: 10,
        slidesPerGroup: 3,
        loop: true,
        loopFillGroupWithBlank: true,
        pagination: {
            el: '.swiper-pagination',
            clickable: true
        },
        navigation: {
            nextEl: '.swiper-button-next',
            prevEl: '.swiper-button-prev'
        }
      },
      swiperOptionTop: {
          loop: true,
          loopedSlides: 5, // looped slides should be the same
          spaceBetween: 10,
          navigation: {
            nextEl: '.swiper-button-next',
            prevEl: '.swiper-button-prev'
          }
        },
        swiperOptionThumbs: {
          loop: true,
          loopedSlides: 5, // looped slides should be the same
          spaceBetween: 10,
          centeredSlides: true,
          slidesPerView: 'auto',
          touchRatio: 0.2,
          slideToClickedSlide: true
        }
    }
  },
  methods: {
    bindURL,
    // 获取公告
    async fetchNotice() {
      const { status, message, data } = await _getBannerList(this.query)
      this.noticeList = JSON.parse(data)
    },
    handleChange(index) {
      this.currentIndex = index
    },
    showNotice(data, index) {
      if (this.currentIndex === index) {
        this.noticeDialogVisible = true
        this.currentNotice = convertDeepCopy(data)
      }
    }
  },
  computed: {},
  created() {
    this.fetchNotice()
  },
  components: {
    pRecommend, pTop, pFree, pCheap,
    swiper,
    swiperSlide
  },
  mounted() {
    // 顶部轮播图的方法
      this.$nextTick(() => {
        const swiperTop = this.$refs.swiperTop.swiper
        const swiperThumbs = this.$refs.swiperThumbs.swiper
        swiperTop.controller.control = swiperThumbs
        swiperThumbs.controller.control = swiperTop
      })
    }
}
</script>

<style lang="less" scoped>
@import '~@css/mixins.less';
@import '~@css/variables.less';

.el-carousel {
  background-color: #fff;
  margin-bottom: 20px;
  border: 1px solid #ccc;
}
.container {
  position: relative;
  height: 100%;
  width: 100%;
  background-color: #ccc;
  img {
    height: 100%;
    position: absolute;
    left: 50%;
    transform: translate(-50%, 0);
  }
  .banner {
    position: absolute;
    left: 0;
    bottom: 0;
    width: 100%;
    background-color: rgba(0, 0, 0, 0.5);
    box-sizing: border-box;
    padding: 14px 0;
    .title,
    .desc {
      text-align: left;
      color: #fff;
      font-weight: 700;
      .text-ellipsis();
      .text-shadow-000();
    }
    .title {
      max-width: 160px;
      font-size: 16px;
      opacity: 0.8;
      text-indent: 1em;
      margin-bottom: 0.5em;
    }
    .desc {
      max-width: 300px;
      opacity: 0.95;
      font-size: 22px;
      text-indent: 0.5em;
    }
  }
}

.f-main {
  display: flex;
  justify-content: space-around;
  background-color: #fff;
  padding: 40px 20px;
  border: 1px solid #ccc;
  .f-item {
    position: relative;
    width: 340px;
    border: 1px solid rgba(204, 204, 204, 0.6);
    border-radius: 2px;
    transition: all 0.2s linear;
    &:hover {
      .box-shadow-000();
    }
    a {
      width: 100%;
      height: 100%;
    }
  }
  .f-img {
    img {
      width: 100%;
      vertical-align: top;
    }
  }

  .f-tips {
    position: absolute;
    top: 50%;
    left: 3%;
    transform: translate(0, -50%);
    .f-title,
    .f-desc {
      color: #fff;
    }
    .f-title {
      position: relative;
      text-align: left;
      font-size: 18px;
      line-height: 18px;
      font-weight: 400;
      padding-left: 20px;
      &::after {
        position: absolute;
        content: '';
        width: 4px;
        height: 18px;
        left: 0;
        top: 0;
        background-color: @main-orange;
      }
    }

    .f-desc {
      margin: 0 6px 0;
      font-size: 14px;
      opacity: 0.8;
    }
  }
}

/deep/.el-dialog__body {
  padding: 10px 20px 30px 20px;
}
.d-head {
  div {
    border-bottom: 1px solid #ccc;
  }
  .d-title {
    display: block;
    font-size: 28px;
    font-size: #000;
  }
  .d-date {
    display: block;
    text-align: right;
    font-size: 14px;
    color: #777;
    margin: 0 10px 20px 10px;
  }
}
.d-main {
  // text-indent: 2em;
  text-align: left;
  padding: 10px 20px;
  border: 1px solid #ccc;
  line-height: 20px;
  color: #666;
  font-size: 15px;
}
.fade-enter-active,
.fade-leave-active {
  transition: opacity 2s;
}
.fade-enter, .fade-leave-to /* .fade-leave-active below version 2.1.8 */ {
  opacity: 0;
}

// 下面推荐轮播的样式
.hot_index {
  width: 90%;
  margin: 0 auto;
  margin-bottom: 40px;

  .home_page_content_title {
    font-family: "Motiva Sans", Sans-serif;
    font-weight: 300;
    font-size: 18px;
    text-transform: uppercase;
    color: #fff;
    margin: 0 0 10px;
    letter-spacing: 0.03em;
    font-weight: normal;
    padding-top: 2px;
    justify-content: space-between;
    text-align: left;

    .hot_more {
      float: right;
      text-transform: none;
      letter-spacing: normal;
      display: inline-block;
      position: relative;
      top: -3px;
      font-size: 14px;
    }
  }
  .router-link-active {
    text-decoration: none;
    color: rgb(104, 105, 156);
  }
  a {
    text-decoration: none;
    color: rgba(255, 255, 255, 0.822);
  }
  .swiper-slide {
    width: 30%;
    line-height: 220px;
    // background: rgb(245, 255, 225);
    color: rgba(0, 0, 0, 0);
    font-size: 16px;
    text-align: center;
    margin-top: 20px;
    border: 2px solid #1AA6B7;
    border-radius: 10px ;

    background-position: center;
    background-size: cover;

    &.slide-1 {
      background-image:url('https://cdn.akamai.steamstatic.com/steam/apps/735290/header_alt_assets_2.jpg?t=1646322786')
    }
    &.slide-2 {
      background-image:url('https://cdn.akamai.steamstatic.com/steam/apps/1097150/header.jpg?t=1645126741')
    }
    &.slide-3 {
      background-image:url('https://cdn.akamai.steamstatic.com/steam/apps/1222140/header_schinese.jpg?t=1625648054')
    }
    &.slide-4 {
      background-image:url('/src/assets/temp.jpg')
    }
    &.slide-5 {
      background-image:url('/src/assets/temp.jpg')
    }
  }
}

// 顶部轮播图的样式
.thumb-example {
    height: 480px;
    background-color: rgba(0, 0, 0, 0.37);
    margin-bottom: 100px;

    .swiper {
    .swiper-slide {
      background-size: contain;
      background-position: center;
      background-repeat:no-repeat;

      &.slide-1 {
        background-image:url('https://cdn.akamai.steamstatic.com/steam/apps/1418630/header.jpg?t=1646709871');
      }
      &.slide-2 {
        background-image:url('https://cdn.akamai.steamstatic.com/steam/apps/1245620/ss_ae44317e3bd07b7690b4d62cc5d0d1df30367a91.600x338.jpg?t=1646770182');
      }
      &.slide-3 {
        background-image:url('/images/example/4.jpg');
      }
      &.slide-4 {
        background-image:url('/images/example/5.jpg');
      }
      &.slide-5 {
        background-image:url('/images/example/6.jpg');
      }
    }

    &.gallery-top {
      height: 80%;
      width: 100%;
    }
    &.gallery-thumbs {
      height: 20%;
      box-sizing: border-box;
      padding: 0;
    }
    &.gallery-thumbs .swiper-slide {
      width: 25%;
      height: 100%;
      opacity: 0.4;
    }
    &.gallery-thumbs .swiper-slide-active {
      opacity: 1;
    }
  }
}

</style>
