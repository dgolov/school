import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from "axios";
import VueAxios from "vue-axios";
import loader from "vue-ui-preloader";
import titleMixin from "./components/mixins/titleMixin";

import DefaultLayout from "./layouts/Default"
import Layout082022 from "./layouts/L082022.vue"

Vue.component("default-layout", DefaultLayout);
Vue.component("082022-layout", Layout082022);

Vue.config.productionTip = true

// Make BootstrapVue available throughout your project
// import  'bootstrap/dist/css/bootstrap.css'
// import  'bootstrap-vue/dist/bootstrap-vue.css'
// Optionally install the BootstrapVue icon components plugin

// Vue.use(BootstrapVue)
// Vue.use(IconsPlugin)
Vue.use(VueAxios, axios)
Vue.use(loader);
Vue.mixin(titleMixin)

new Vue({
  loader,
  router,
  store,
  axios,
  render: h => h(App)
}).$mount('#app')
