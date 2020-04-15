// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import axios from 'axios'
import MyHeader from './components/MyHeader.vue'
import MyFooter from './components/MyFooter.vue'

Vue.component("MyHeader", MyHeader)
Vue.component("MyFooter", MyFooter)


Vue.config.productionTip = false

axios.defaults.baseURL="http://localhost:5050/";
// axios.defaults.withCredentials=true;

Vue.prototype.axios=axios;

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
