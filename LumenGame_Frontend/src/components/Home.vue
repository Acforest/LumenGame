<template>
  <!-- <parallax
    class="page-header-image"
    style="background-image:url('../assets/temp.jpg')"
  >
  </parallax> -->
  <div>
    <el-container class="main">
      <!-- <el-container> -->
      <el-header style="text-align: right">
        <div>
          <img src="../assets/logo.png" alt="" height="50px"/>
          <span>LumenGame</span>
        </div>
        <el-menu background-color="#00202e" mode="horizontal"
              text-color="#fff"
              default-active="currentIndex" router>
          <el-menu-item index="index"><i class="el-icon-s-home"></i>首页</el-menu-item>
          <el-menu-item index="game"><i class="el-icon-star-on"></i>个人推荐</el-menu-item>
          <el-menu-item index="info"><i class="el-icon-s-goods"></i>个人中心</el-menu-item>
          <el-menu-item index="rank"><i class="el-icon-sell"></i>热门推荐</el-menu-item>
          <el-menu-item index="share"><i class="el-icon-folder-opened"></i>游戏库</el-menu-item>
        </el-menu>
        <el-button type="success" @click="logout" id='b_log' v-if="log_status === false">登录</el-button>
        <el-button type="error" @click="logout" id='b_log' v-else>退出</el-button>
      </el-header>
      <!-- </el-container> -->

      <el-container>
        <el-main>
          <div>
            <router-view></router-view>
          </div>
        </el-main>
      </el-container>

      <el-footer style="text-align: right">© 2022, Designed by Madison. Coded by Aduiduidui.</el-footer>
    </el-container>

  </div>
</template>

<script>
import { mapMutations, mapState } from 'vuex'
import { bindURL } from '@utils'

export default {
  data() {
    return {
      log_status: false
    }
  },
  methods: {
    ...mapMutations(['setHCurrentIndex']),
    bindURL,
    logout() {
      if (document.getElementById('b_log').innerHTML === '退出') {
        document.getElementById('b_log').innerHTML = '登录'
        // sessionStorage.clear()
        this.$router.push('/home')
      } else {
        document.getElementById('b_log').innerHTML = '退出'
        this.$router.replace('/login')
      }
    }
  },
  computed: {
    ...mapState({ currentIndex: 'hCurrentIndex', currentUser: 'currentUser' })
  },
  updated() {
    this.setHCurrentIndex()
  },
  created() {
    if (this.currentUser != null) {
      this.log_status = true
    } else {
      this.log_status = false
    }
    this.setHCurrentIndex()
  }
}
</script>

<style lang="less" scoped>
@import '~@/assets/css/variables.less';
.w {
  width: 200px;
  margin: 0 auto;
}

.el-menu.el-menu--horizontal {
  border-bottom: none;
}

.el-menu--horizontal > .el-menu-item.is-active {
  border-color: #409EFF;
  color: rgb(180, 180, 180)
}

/deep/.el-submenu__icon-arrow.el-icon-arrow-down {
  display: none;
}

.main {
  display: flex;
  // flex-direction: column;
  height: 100vh;
  // header >>>
  // .logo {
  //   img {
  //     width: 50px;
  //   }
  // }
  // .user-info {
  //   float: right;
  // }
  // /deep/.el-menu--horizontal > .el-submenu.is-active .el-submenu__title {
  //   border-bottom: none;
  // }
  .el-header {
    background-color: #00202e;
    color: #333;
    line-height: 60px;
    width: 100%;

    font-size: 12px;
    font-family:'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;
    display: flex;
    justify-content: space-between;
    padding-left: 10px;
    align-items: center;
    > div {
      display: flex;
      align-items: center;
      span {
        margin-left: 15px;
        font-size: 30px;
        color: #1AA6B7;
      }
    }

  }
  // header <<<
  // main >>>
  .el-main {
    // flex: 1;
    // background-color: rgb(6, 44, 64);
    // background-image: linear-gradient(to top, rgba(255,255,255,1), rgba(255,255,255,0), url('../assets/login_background.jpg'))
    background-image: url('../assets/login_background.jpg')
    // 'linear-gradient(to top, rgba(255,255,255,1), rgba(255,255,255,0)),url(' + bgimg + ')'}"
  }
  // main <<<
  // footer >>>
  .el-footer {
    height: 150px;
    background-color: #00202e;
    color: antiquewhite;
    line-height: 60px;
    // display: flex;
  }
  // footer <<<

  .el-aside{
    background-color: #00202e;
    opacity: 0.5;    // 好丑 记得改
  }
}
</style>
