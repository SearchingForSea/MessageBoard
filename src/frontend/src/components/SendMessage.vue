<template>
    <div id="sendmessage">
        <div>
            <label>友善评论哦~</label>
            <form class="input">
                <textarea class="message" v-model="talkmessage"/>
            </form>
        </div>
        <div>
            <button class="send" @click="sendMessage">发送</button>
        </div>
    </div>
</template>

<script>
export default {
  data () {
    return {
      talkmessage: ''
    }
  },
  props: {
    notSend: {
      type: Boolean,
      default: true
    }
  },
  methods: {
    sendMessage () {
      console.log(this.talkmessage)
      const params = new URLSearchParams()
      params.append('user_address', this.$root.mainUserAddress)
      params.append('talk', this.talkmessage)
      this.$http.post('http://localhost:8002/sendMessage/', params).then((response) => {
        if (response.data === 'Yes') {
          this.$emit('update:notSend', false)
          alert('发布成功')
          this.$emit('refresh-windows')
        }
      })
    }
  }
}
</script>

<style scoped>
#sendmessage{
  height: 200px;
  width: 100%;
  background-color: rgba(255, 105, 180, 0.819);
  display: flex;
  align-items: center;
  justify-content: center;
}
.message{
    height: 70px;
    width: 900px;
    border-radius: 5px;
    border: none;
    margin-left: 120px;
    padding-top: 5px;
    padding-left: 15px;
    font-size: 15px;
}
label{
    font-size: 18px;
    color: white;
    margin-top: -10px;
    margin-bottom: 10px;
}
button{
  background-color: rgb(252, 253, 253);
  height: 35px;
  width: 90px;
  border-radius: 5px;
  border: none;
  padding: 9px;
  font-size: 16px;
  margin-left: 50px;
  margin-top: 20px;
  color: rgb(18, 17, 17);
}
</style>
