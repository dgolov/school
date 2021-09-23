<template>
  <div id="login">
    <navbar></navbar>
    <div class="auth">
      <div class="container">
        <div class="auth__inner">
          <div class="auth__media">
            <img src="../assets/images/undraw_selfie.svg">
          </div>
          <div class="auth__auth">
            <h1 class="auth__title">Вход в аккаунт</h1>
            <p v-if="error.status" class="error">{{ error.message }}</p>
            <p>Введите свой адрес электронной почты и пароль, чтобы продолжить</p>
            <form action="#" method="get" autocompelete="new-password" class="form" id="formLogin">
              <label>Логин</label>
              <input v-model="username" type="text" name="login" placeholder="Введите имя пользователя..." required>
              <label>Пароль</label>
              <input v-model="password" type="password" name="password" placeholder="Введите пароль" autocomplete="off" required>
              <button type="button" class="button button__accent" @click="login()">Войти</button>
            </form>
              <h6 class="left-align"><a href="#">Забыли пароль?</a></h6>
              <h6 class="left-align">У вас еще нет аккаунта?
                <a href="#" @click="goTo('SignUp')">Зарегистрироваться</a>
              </h6>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Navbar from "../components/Navbar";
import axios from "axios";
import {redirect} from "../components/mixins/redirect";


export default {
  name: "Auth",

  mixins: [redirect],

  components: {
    Navbar
  },

  data() {
    return {
      username: '',
      password: '',
      error: {
        status: false,
        message: ""
      },
    }
  },

  created() {
    if (this.$store.state.isAuthenticated) {
      // Если пользователь вс системе - выгоняем его отсюда
      this.goTo('Home')
    }
  },

  methods: {
    async login() {
      const body = {
        username: this.username,
        password: this.password
      }
      axios
          .post(`${this.$store.getters.getServerUrl}/token/`, body)
          .then((response) => {
            this.$store.commit("updateToken", response.data.access);
            this.$store.commit("updateRefreshToken", response.data.refresh);
            const base = {
              baseURL: this.$store.state.backendUrl,
              headers: {
                Authorization: `Bearer ${this.$store.state.jwt}`,
                "Content-Type": "application/json",
              },
              xhrFields: {
                withCredentials: true,
              },
            };
            const axiosInstance = axios.create(base);
            axiosInstance({
              url: "/user/",
              method: "get",
              params: {},
            }).then((response) => {
              this.$store.commit("setAuthUser", {
                authUser: response.data,
                isAuthenticated: true,
              });
              this.goTo('Profile', {id: this.$store.state.authUser.id})
            });
          })
          .catch((error) => {
            if (error.request.status === 401) {
              this.error.status = true;
              this.error.message = "Указано неверное имя пользователя или пароль";
            }
            console.log(error);
            console.debug(error);
            console.dir(error);
          });
    },
  }
}
</script>


<style scoped>
.error {
  color: red;
}
</style>