<template>
  <div id="userlogin">
    <div id="loginboard" v-show="IsAppVision">
      <div id="pleaselogin">Welcome</div>
      <div id="input">
          <div id="address">
            <label>账号&nbsp;&nbsp;&nbsp;&nbsp;</label>
            <input v-model="inputAddress">
          </div>
          <div id="secret">
            <label>密码&nbsp;&nbsp;&nbsp;&nbsp;</label>
            <input type="password" v-model="inputSecret">
          </div>
      </div>
      <div id="btn">
          <button id="loginbtn" @click="Ilogin">登录</button>
        <button id="registerbtn" @click="Iregister">注册</button>
      </div>
    </div>
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  data () {
    return {
      IsAppVision: true,
      inputAddress: '',
      inputSecret: ''
    }
  },
  methods: {
    Ilogin () {
      const params = new URLSearchParams()
      if (this.inputAddress !== '' && this.inputSecret !== '') {
        params.append('user_address', this.inputAddress)
        params.append('user_secret', this.inputSecret)
        this.$http.post('http://localhost:8002/loginUser/', params).then((response) => {
          console.log(response.data)
          if (response.data === 'Yes') {
            this.$root.mainUserAddress = this.inputAddress
            this.$router.push('/home/')
          } else {
            alert('账号密码不匹配或者未注册')
            params.length = 0
          }
        })
      } else {
        alert('请正确输入')
      }
    },
    Iregister () {
      this.$router.push('/register')
    }
  }
}

</script>

<style scoped>
* {
  margin: 0;
  padding: 0;
}
#userlogin {
  height: 100vh;
  background-color: aliceblue;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  margin-top: -40px;
}
#loginboard {
  height: 400px;
  width: 400px;
  background-color: rgba(232, 160, 210, 0.297);
}
#pleaselogin {
  margin-top: 80px;
  height: 100px;
  width: 400px;
  text-align: center;
  font-size: 30px;
}
#input{
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}
#input input{
  height: 25px;
  width: 200px;
  border-radius: 5px;
  padding-left: 10px;
  font-size: 15px;
}
#address{
  margin-top: 30px;
}
#secret{
  margin-top: 30px;
}
#btn{
  text-align: center;
}
button{
  background-color: coral;
  height: 35px;
  width: 90px;
  border-radius: 5px;
  border: none;
  padding: 9px;
  font-size: 16px;
  color: #fff;
  margin-top: 30px;
}
#registerbtn{
  margin-left: 20px;
}
</style>
