<template>
  <div class="talk">
    <div class="user-name">{{username}}</div>
    <div class='comment'>{{comment}}</div>
    <div class="icon">
        <button class="praise" @click="PraiseComment">赞</button>
        <button class="tread" @click="TreadComment">踩</button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'CommentSpeech',
  data () {
    return {
      do_praise: 1,
      do_tread: 1
    }
  },
  props: {
    username: {
      type: String,
      default: 'You'
    },
    comment: {
      type: String,
      default: 'GOOD!'
    },
    ID: {
      type: Number
    }
  },
  methods: {
    PraiseComment () {
      console.log(this.key)
      document.getElementsByClassName('praise')[this.ID].innerText = '已赞'
    },
    TreadComment () {
      console.log(this.key)
      document.getElementsByClassName('tread')[this.ID].innerText = '已踩'
    }
  }
}
</script>
<style scoped>
  .talk{
    background-color: rgb(246, 238, 248);
    width: 900px;
    height: 180px;
  }
  .user-name{
    height: 20px;
    width: 50px;
    margin-left: 20px;
    margin-top: 10px;
    margin-bottom: 10px;
  }
  .comment{
    background-color: white;
    border-radius: 8px;
    margin-left: 15px;
    margin-right: 15px;
    padding-top: 2px;
    padding-left: 10px;
    height: 110px;
  }
  .icon{
    margin-top: 5px ;
    margin-right: 25px;
    margin-bottom: 5px;
    display: flex;
    justify-content: flex-end;
  }
  .icon button{
    margin-right: 50px;
    background-color: rgb(246, 238, 248);
    border: none;
  }
</style>
