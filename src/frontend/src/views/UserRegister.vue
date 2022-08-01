<template>
  <div id="userlogin">
    <div id="registerboard" v-show="IsAppVision">
      <div id="pleaselogin">注册</div>
      <div id="input">
          <div id="address">
            <label>账号&nbsp;&nbsp;&nbsp;&nbsp;</label>
            <input id="inaddress" v-model="inputAddress">
          </div>
          <div id="secret">
            <label>密码&nbsp;&nbsp;&nbsp;&nbsp;</label>
            <input type="secret" id="secret" v-model="inputSecret">
          </div>
          <div id="secret">
            <label>确认&nbsp;&nbsp;&nbsp;&nbsp;</label>
            <input type="secret" v-model="sureSecret">
          </div>
      </div>
      <div id="btn">
          <button id="surebtn" @click="Iregister">确定</button>
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
      inputSecret: '',
      sureSecret: ''
    }
  },
  methods: {
    Iregister () {
      const params = new URLSearchParams()
      console.log(this.inputAddress)
      console.log(this.inputSecret)
      if (this.inputAddress !== '' && this.inputSecret !== '' && this.sureSecret === this.inputSecret) {
        params.append('user_address', this.inputAddress)
        params.append('user_secret', this.inputSecret)
        this.$http.post('http://localhost:8002/registerUser/', params).then((response) => {
          console.log(response.data)
          if (response.data === 'Yes') {
            this.$router.push('/login')
          } else {
            alert('账号被占用')
            params.length = 0
          }
        })
      } else {
        alert('输入不正确')
      }
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
#registerboard {
  height: 450px;
  width: 400px;
  background-color: rgba(232, 160, 210, 0.297);
}
#pleaselogin {
  margin-top: 80px;
  height: 50px;
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
}
#address{
  margin-top: 50px;
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
