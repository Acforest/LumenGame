<template>
  <div>
    <el-container class="main">
      <el-menu-item class="logo">
          <img src="../assets/logo.png" alt="">
        </el-menu-item>
      <el-aside width="200px" style="text-align: left">
        
        <el-menu :default-active="currentIndex" router>
          <el-submenu index="1">
            <template slot="title"><i class="el-icon-s-home"></i>首页</template>
            <el-menu-item-group>
              <el-menu-item index="index"><i class="el-icon-s-home"></i>首页</el-menu-item>
              <el-menu-item index="game"><i class="el-icon-star-on"></i>个人推荐</el-menu-item>
              <el-menu-item index="info"><i class="el-icon-s-goods"></i>个人中心</el-menu-item>
              <el-menu-item index="rank"><i class="el-icon-sell"></i>热门推荐</el-menu-item>
              <el-menu-item index="share"><i class="el-icon-folder-opened"></i>游戏库</el-menu-item>
            </el-menu-item-group>
          </el-submenu>
          <!-- <el-menu-item class="logo">
            <img src="../assets/logo.png" alt="">
          </el-menu-item>
          <el-menu-item index="/index">主页</el-menu-item>
          <el-menu-item index="/game">游戏中心</el-menu-item>
          <el-menu-item index="/rank">排行榜</el-menu-item>
          <el-menu-item index="/share">游戏论坛</el-menu-item>
          <el-menu-item index="/info">个人中心</el-menu-item>
          <el-submenu index="2" class="user-info">
            <template slot="title">
              <el-avatar size="large" :src="bindURL(currentUser.avatarImgUrl)">
              </el-avatar>
            </template>
            <el-menu-item index="/info"><i class="iconfont icon-user1">个人信息</i>
            </el-menu-item>
            <el-menu-item index="/admin"><i class="iconfont icon-home">前往后台</i>
            </el-menu-item>
            <el-menu-item @click="logout()"> <i class="iconfont icon-logout">退出系统</i>
            </el-menu-item>
          </el-submenu> -->
        </el-menu>
      </el-aside>

      <el-container>
        <el-header style="text-align: right; font-size: 12px">
          <el-dropdown>
            <i class="el-icon-setting" style="margin-right: 15px"></i>
            <el-dropdown-menu slot="dropdown">
              <el-dropdown-item>查看</el-dropdown-item>
              <el-dropdown-item>新增</el-dropdown-item>
              <el-dropdown-item>删除</el-dropdown-item>
            </el-dropdown-menu>
          </el-dropdown>
          <!-- <span>王小虎</span> -->
        </el-header>

        <el-main>
          <div>
            <router-view></router-view>
          </div>
        </el-main>
      </el-container>
    </el-container>

  </div>
</template>

<script>
import { mapMutations, mapState } from 'vuex'
import { bindURL } from '@utils'

export default {
  data() {
    return {}
  },
  methods: {
    ...mapMutations(['setHCurrentIndex']),
    bindURL,
    logout() {
      sessionStorage.clear()
      this.$router.push('/login')
    }
  },
  computed: {
    ...mapState({ currentIndex: 'hCurrentIndex', currentUser: 'currentUser' })
  },
  updated() {
    this.setHCurrentIndex()
  },
  created() {
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
  border-color: @main-green;
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
    background-color: #B3C0D1;
    color: #333;
    line-height: 60px;
  }
  // header <<<
  // main >>>
  .el-main {
    // flex: 1;
    background-color: rgb(6, 44, 64);
  }
  // main <<<
  // footer >>>
  .el-footer {
    height: 150px;
  }
  // footer <<<
}
</style>
