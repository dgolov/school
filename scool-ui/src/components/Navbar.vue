<template>
  <div class="nav_bar" id="navbar" style="background-color: #00093c;">
    <nav class="nav__mobile"></nav>
    <div class="container">
      <div class="row navbar__inner" style="color: #ffffff;">
        <div class="col-md-2" style="height: 80px; padding-top: 8px">
          <a href="/" class="navbar__logo">
            <img src="../assets/images/logo_white.svg" style="height: 80%; margin-left: 30px;">
          </a>
          <div class="navbar__menu-mob" style="position: absolute; right: 15px; top: 15px;">
            <a href="" id='toggle' style="height: 80px;">
              <svg role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512">
                <path fill="currentColor"
                      d="M16 132h416c8.837 0 16-7.163 16-16V76c0-8.837-7.163-16-16-16H16C7.163 60 0 67.163 0 76v40c0 8.837 7.163 16 16 16zm0 160h416c8.837 0 16-7.163 16-16v-40c0-8.837-7.163-16-16-16H16c-8.837 0-16 7.163-16 16v40c0 8.837 7.163 16 16 16zm0 160h416c8.837 0 16-7.163 16-16v-40c0-8.837-7.163-16-16-16H16c-8.837 0-16 7.163-16 16v40c0 8.837 7.163 16 16 16z"
                      class=""></path>
              </svg>
            </a>
          </div>
        </div>
        <div class="col-md-10" style="height: 60px; padding-top: 15px">
          <nav class="navbar__menu">
            <ul class="main-nav">
              <li><a href="/education" @click="goTo('Education')">
                <svg width="20" height="17" viewBox="0 0 20 17" fill="none" xmlns="http://www.w3.org/2000/svg" style="padding-bottom: 3px;">
                  <rect x="1" y="1.51392" width="18" height="4.99717" rx="1" stroke="#ffffff" stroke-width="2"/>
                  <rect x="1" y="10.4858" width="18" height="5" rx="1" stroke="#ffffff" stroke-width="2"/>
                </svg>
                Все курсы
              </a></li>
              <li><a href="#" @click="goTo('Education')">Мероприятия</a></li>
              <li><a href="/about" @click="goTo('About')">Об академии</a></li>
              <li>
                <svg width="14" height="17" viewBox="0 0 17 20" fill="none" xmlns="http://www.w3.org/2000/svg" style="padding-bottom: 3px;">
                  <path d="M16 8.5C16 11.3282 14.13 13.9545 12.0535 15.9699C11.036 16.9575 10.0146 17.754 9.24613 18.304C8.95504 18.5123 8.70155 18.6843 8.5 18.8171C8.29845 18.6843 8.04496 18.5123 7.75387 18.304C6.98537 17.754 5.96395 16.9575 4.94648 15.9699C2.86999 13.9545 1 11.3282 1 8.5C1 4.35786 4.35786 1 8.5 1C12.6421 1 16 4.35786 16 8.5Z" stroke="#ffffff" stroke-width="2"/>
                  <circle cx="8.5" cy="7.5" r="2.5" fill="#ffffff"/>
                </svg>
                Нижний Новгород
                <a href="#">
                  <svg width="10" height="7" viewBox="0 0 10 7" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M1 1L5 5L9 1" stroke="#ffffff" stroke-width="2" stroke-linecap="round"/>
                  </svg>
                </a>
              </li>
              <li><a href="#">8 800 950-33-98</a></li>
            </ul>
            <ul v-if="authenticated" style="float: right;">
              <li>
                <a href="/profile" @click="goTo('MyProfile')">
                  {{ user.first_name }} {{ user.last_name }}
                </a>
              </li>
              <li>
                <img v-if="authenticated" class="center avatar" :src="getAvatar()">
              </li>
            </ul>
            <ul v-else style="float: right;">
              <li><a href="/signup" @click="goTo('SignUp')" class="border-gradient">Регистрация</a></li>
              <li><a href="/auth" @click="goTo('Auth')" class="border-gradient">Вход</a></li>
            </ul>
          </nav>
        </div>
      </div>
    </div>
  </div>
</template>


<script>
import NavLogin from "./NavLogin";
import {redirect} from "./mixins/redirect";

export default {
  name: "Navbar",

  components: {
    NavLogin
  },

  data() {
    return {
      user: {},
      authenticated: false
    }
  },

  created(){
    this.user = this.$store.getters.getProfileInfo;
    this.authenticated = this.$store.state.isAuthenticated;
  },

  mixins: [redirect],

  methods: {
    getAvatar() {
      let path = ''
      try {
        path = this.user.avatar.image;
      } catch {
        path = require('../assets/images/avatars/mike2.jpeg');
      }
      return path;
    },
  }
}
</script>


<style scoped>
@media (min-width: 992px) {

}

.avatar {
  display: inline-block;
  width: 30px;
  height: 30px;
  border: 0;
  border-radius: 50%;
  margin: auto;
  text-align: right;
}

.nav_bottom {
  border: 1px solid;
}

.border-gradient {
  /*display: inline;*/
  /*padding: 4px;*/
  /*border: 1px solid;*/
  /*border-image: linear-gradient(20deg, #eb934f 38%, #63a9da 65%);*/
  /*border-image-slice: 1;*/
}

.navbar__menu a {
  color: #ffffff;
}

</style>