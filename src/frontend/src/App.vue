<template>
  <div id="app">
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  data () {
    return {
      IsAppVision: true
    }
  },
  methods: {
    Iregister () {
      this.IsAppVision = false
      this.$router.push('/home/')
    }
  }
}
</script>

<style>
* {
  margin: 0;
  padding: 0;
}
#app {
}
</style>
