import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from "axios";
import VueAxios from "vue-axios";

Vue.config.productionTip = true

// Make BootstrapVue available throughout your project
// import  'bootstrap/dist/css/bootstrap.css'
// import  'bootstrap-vue/dist/bootstrap-vue.css'
// Optionally install the BootstrapVue icon components plugin

// Vue.use(BootstrapVue)
// Vue.use(IconsPlugin)
Vue.use(VueAxios, axios)

new Vue({
  router,
  store,
  axios,
  render: h => h(App)
}).$mount('#app')
