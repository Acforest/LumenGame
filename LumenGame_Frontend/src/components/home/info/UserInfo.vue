<template>
  <div class="edit-info">
    <el-form :model="userInfoForm" :rules="userInfoRules" ref="userInfoForm"
      label-width="100px" size="small" :hide-required-asterisk="true">
      <el-form-item prop="id">
        <span slot="label" class="info-label">ID</span>
        <el-input v-model="userInfoForm.id" disabled></el-input>
      </el-form-item>
      <el-form-item prop="username">
        <span slot="label" class="info-label">用户名</span>
        <el-input v-model="userInfoForm.username"></el-input>
      </el-form-item>
      <el-form-item prop="phone">
        <span slot="label" class="info-label">手机号码</span>
        <el-input v-model="userInfoForm.phone"></el-input>
      </el-form-item>
      <el-form-item prop="qq">
        <span slot="label" class="info-label">QQ</span>
        <el-input v-model="userInfoForm.qq"></el-input>
      </el-form-item>
      <el-form-item prop="email">
        <span slot="label" class="info-label">邮箱</span>
        <el-input v-model="userInfoForm.email"></el-input>
      </el-form-item>
      <el-form-item prop="avatarImgUrl">
        <span slot="label" class="info-label">头像</span>
        <el-upload class="avatar-uploader" :action="bindURL('uploadfile')"
          :show-file-list="false" :on-success="handleEditAvatarSuccess" name="files">
          <img v-if="userInfoForm.avatarImgUrl" :src="userInfoForm.avatarImgUrl"
            class="avatar" ref="preview" />
          <i v-else class="el-icon-plus avatar-uploader-icon"></i>
        </el-upload>
      </el-form-item>
      <el-form-item prop="description">
        <span slot="label" class="info-label">自我描述</span>
        <el-input v-model="userInfoForm.description" type="textarea"
          :autosize="{ minRows: 3, maxRows: 6 }" resize="none"></el-input>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="submitUser()">修改</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
import { bindURL, validateEmail, validatePhone, convertDeepCopy } from '@utils'
import { _getUserInfo } from '@api'
export default {
  props: {
    data: {
      type: Object
    }
  },
  data() {
    return {
      userInfoRules: {
        username: [
          { required: true, message: '输入用户名', trigger: 'blur' },
          { min: 2, max: 15, message: '长度在 2 到 15 个字符', trigger: 'blur' }
        ],
        phone: [
          { required: true, message: '输入电话号码', trigger: 'blur' },
          { validator: validatePhone, trigger: 'blur' }
        ],
        qq: [{ required: true, message: '输入QQ号码', trigger: 'blur' }],
        email: [
          { required: true, message: '输入电子邮箱', trigger: 'blur' },
          { validator: validateEmail, trigger: 'blur' }
        ],
        imgUrl: [{ required: true, message: '选择头像', trigger: 'blur' }]
      },
      userInfoForm: {}
    }
  },
  methods: {
    bindURL,
    handleEditAvatarSuccess(res) {
      this.$set(this.userInfoForm, 'avatarImgUrl', res)
    },
    submitUser() {
      this.$refs.userInfoForm.validate((valid) => {
        if (!valid) return
        this.$emit('submit-user', this.userInfoForm)
      })
    }
  },
  created() {
    this.userInfoForm = convertDeepCopy(this.data)
  }
}
</script>

<style lang="less" scoped>
@import '~@css/variables.less';
@import '~@css/mixins.less';

.edit-info {
  text-align: left;
  /deep/.el-upload {
    position: relative;
    border: 2px solid #3fc9d8;
    line-height: 0;
    border-radius: 2px;
    width: 120px;
    height: 120px;
    img {
      width: 100%;
      height: 100%;
    }
    &:hover {
      border: 2px solid @main-green;
    }
    i {
      .center-x-y();
      font-size: 20px;
    }
  }
  .el-input {
    // opacity: 0.7;
    // border: 1px solid #3fc9d8;
    background-color: #002D40;
  }
  .info-label {
    color: #3fc9d8;
  }
}
</style>