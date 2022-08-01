<template>
  <div id="home">
    <div id="navigationbar">
      <button id="login" >{{User_Address}}</button>
      <button id="quit" @click="exitLogin">退出</button>
    </div>
    <div id="mid-view" v-if="!IsSendMessageVision">
      <comment-speech
      v-for="(item, index) in CommentSpeech"
      :key="index"
      :username="item.fields.User_Address"
      :comment="item.fields.User_Comment"
      :ID="index"
      >
      </comment-speech>
    </div>
    <div class="foot" v-show="!IsSendMessageVision">
      <button class="send" @click="sendMessage">发表评论吧</button>
    </div>
    <send-message v-show="IsSendMessageVision" :not-send.sync="IsSendMessageVision" @refresh-windows="Refresh"></send-message>
  </div>
</template>

<script>
import CommentSpeech from '@/components/CommentSpeech.vue'
import SendMessage from '@/components/SendMessage.vue'

export default {
  data () {
    return {
      IsSendMessageVision: false,
      UserLoginVision: true,
      User_Address: '',
      CommentSpeech: [],
      index: 0
    }
  },
  created: function () {
    this.User_Address = this.$root.mainUserAddress
    const params = new URLSearchParams()
    params.append('user_address', this.User_Address)
    this.$http.post('http://localhost:8002/getMessage/', params).then((response) => {
      this.CommentSpeech = response.data
    })
  },
  // watch: {
  //   IsSendMessageVision (newVal, oldVal) {
  //     const params = new URLSearchParams()
  //     if (newVal === true) {
  //       params.append('user_address', this.User_Address)
  //       this.$http.post('http://localhost:8002/getMessage/', params).then((response) => {
  //         this.CommentSpeech = response.data
  //       })
  //     }
  //   }
  // },
  methods: {
    exitLogin () {
      console.log(this.UserLoginUserAddress)
      this.$router.push('/login')
    },
    sendMessage () {
      this.IsSendMessageVision = true
    },
    Refresh () {
      console.log('haha')
      this.$router.go(0)
    }
  },
  components: {
    CommentSpeech,
    SendMessage
  }
}
</script>

<style scoped>
#home {
  height: 100vh;
  background-color: aliceblue;
  display: flex;
  flex-direction: column;
  align-items: center;
}
#navigationbar
{
  width: 100%;
  height: 100px;
  background-color: hotpink;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: flex-end;
}
#mid-view {
  background-color:white;
  width: 100%;
  height: 100%;
  scroll-behavior: auto;
  display: flex;
  flex-direction: column;
  align-items: center;
  overflow: auto;
}
#login,#quit{
  width: 100px;
  height: 28px;
  color: white;
  background-color: hotpink;
  border: none;
  font-size: 18px;
}
.send{
  width: 100px;
  height: 28px;
  color: white;
  background-color: hotpink;
  border: none;
  font-size: 18px;
  margin-right: 210px;
}
.foot{
  height: 70px;
  width: 100%;
  background-color: hotpink;
  display: flex;
  align-items: center;
  justify-content: flex-end;
}
</style>
