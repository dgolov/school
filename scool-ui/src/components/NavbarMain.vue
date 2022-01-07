<template>
  <div class="nav_bar" id="navbar">
    <nav class="nav__mobile"></nav>
    <div class="container">
      <div class="row navbar__inner">
        <div class="col-md-2" style="height: 80px; padding-top: 8px">
          <a href="/" class="navbar__logo">
            <img src="../assets/images/logo.svg" style="height: 80%; margin-left: 30px;">
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
              <li>
                <a href="/education" @click="goTo('Education')" class="bold">
                  <svg width="20" height="17" viewBox="0 0 20 17" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <rect x="1" y="1.51392" width="18" height="4.99717" rx="1" stroke="#00093C" stroke-width="2"/>
                    <rect x="1" y="10.4858" width="18" height="5" rx="1" stroke="#00093C" stroke-width="2"/>
                  </svg>
                  Все курсы
                </a>
              </li>
              <li><a href="/events" @click="goTo('Events')" class="bold">Мероприятия</a></li>
              <li><a href="/about" @click="goTo('About')" class="bold">Об академии</a></li>
              <li>
                <svg width="14" height="17" viewBox="0 0 17 20" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <path
                      d="M16 8.5C16 11.3282 14.13 13.9545 12.0535 15.9699C11.036 16.9575 10.0146 17.754 9.24613 18.304C8.95504 18.5123 8.70155 18.6843 8.5 18.8171C8.29845 18.6843 8.04496 18.5123 7.75387 18.304C6.98537 17.754 5.96395 16.9575 4.94648 15.9699C2.86999 13.9545 1 11.3282 1 8.5C1 4.35786 4.35786 1 8.5 1C12.6421 1 16 4.35786 16 8.5Z"
                      stroke="#00093C" stroke-width="2"/>
                  <circle cx="8.5" cy="7.5" r="2.5" fill="#00093C"/>
                </svg>
                <a href="#" class="bold">
                  Нижний Новгород
                  <svg width="10" height="7" viewBox="0 0 10 7" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M1 1L5 5L9 1" stroke="#00093C" stroke-width="2" stroke-linecap="round"/>
                  </svg>
                </a>
              </li>
              <li><a href="#" class="bold">8 800 950-33-98</a></li>
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
              <li>
                <svg width="15" height="15" viewBox="0 0 18 19" fill="none" xmlns="http://www.w3.org/2000/svg"
                     style="margin-right: 10px">
                  <rect x="5.18018" y="1" width="6.63833" height="8.41108" rx="3.31917" stroke="#00093C"
                        stroke-width="2"/>
                  <path
                      d="M1 15.4102C1 13.7533 2.34315 12.4102 4 12.4102H13.2795C14.9364 12.4102 16.2795 13.7533 16.2795 15.4102V16.322C16.2795 16.8742 15.8318 17.322 15.2795 17.322H2C1.44772 17.322 1 16.8742 1 16.322V15.4102Z"
                      stroke="#00093C" stroke-width="2"/>
                </svg>
                <a href="/auth" @click="goTo('Auth')" class="bold">Вход</a>
              </li>
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

  created() {
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

</style>