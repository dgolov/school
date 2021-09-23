<template>
  <div class="nav_bar" id="navbar">
    <nav class="nav__mobile"></nav>
    <div class="container">
      <div class="row navbar__inner">
        <div class="col-md-2" style="height: 60px; padding-top: 8px">
          <a href="#" class="navbar__logo">
            <img src="../assets/images/Logo-SCHOOL-0922-07.png"
                 style="height: 80%;">
          </a>
          <div class="navbar__menu-mob" style="position: absolute; right: 15px; top: 15px;">
            <a href="" id='toggle'>
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
              <li><a href="/">Главная</a></li>
              <li><a href="#" @click="goTo('Education')">Обучение</a></li>
              <li><a href="#" @click="goTo('News')">Новости</a></li>
              <li><a href="#" @click="goTo('About')">Об академии</a></li>
              <li><a href="#" @click="goTo('Contacts')">Контакты</a></li>
            </ul>
            <ul v-if="authenticated" style="float: right;">
              <li>
                <a href="#" @click="goTo('MyProfile')">
                  {{ user.first_name }} {{ user.last_name }}
                </a>
              </li>
              <li>
                <img v-if="authenticated" class="center avatar" :src="`http://127.0.0.1:8000${user.avatar.image}`">
              </li>
            </ul>
            <ul v-else style="float: right;">
              <li><a href="#" @click="goTo('SignUp')">Регистрация</a></li>
              <li><a href="#" @click="goTo('Auth')">Вход</a></li>
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