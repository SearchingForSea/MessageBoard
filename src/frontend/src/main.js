import Vue from 'vue'
import App from './App.vue'
import router from './router'
import axios from 'axios'

axios.defaults.withCredentials = true
axios.defaults.xsrfHeaderName = 'X-CSRFTOKEN'
axios.defaults.xsrfCookieName = 'csrftoken'

Vue.prototype.$http = axios

Vue.config.productionTip = false

new Vue({
  router,
  data: function () {
    return {
      mainUserAddress: ''
    }
  },
  render: function (h) { return h(App) }
}).$mount('#app')
