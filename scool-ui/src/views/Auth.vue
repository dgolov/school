<template>
  <div id="auth">
    <navbar></navbar>
    <div class="auth">
      <div class="container">
        <div class="auth__inner">
          <div class="auth__media">
            <img src="../assets/images/owl-auth.svg">
          </div>
          <div class="auth__auth">
            <div class="container mb-4">
              <div class="row groups">
                <div class="col-md-6 center group-active" id="signIn">
                  <div class="group-text">
                    <button @click="setAuthMode('signIn')">Вход</button>
                  </div>
                </div>
                <div class="col-md-6 center" id="signUp">
                  <div class="group-text">
                    <button @click="setAuthMode('signUp')">Регистрация</button>
                  </div>
                </div>
              </div>
            </div>
            <div id="signInForm" v-if="signIn">
              <p v-if="error.status" class="error">{{ error.message }}</p>
              <p>Введите свой адрес электронной почты и пароль, чтобы продолжить</p>
              <form action="#" method="get" autocompelete="new-password" class="form" id="formLogin">
                <label>Логин</label>
                <input v-model="userName" type="text" name="login" placeholder="Введите имя пользователя..." required>
                <label>Пароль</label>
                <input v-model="password" type="password" name="password" placeholder="Введите пароль" autocomplete="off" required>
                <button type="button" class="button button__accent w-50" @click="login()">Войти</button>
              </form>
              <h6 class="left-align"><a href="#">Забыли пароль?</a></h6>
              <h6 class="left-align">У вас еще нет аккаунта?
                <a href="#" @click="goTo('SignUp')">Зарегистрироваться</a>
              </h6>
            </div>
            <div id="signOutForm" v-if="signOut">
              <h1 class="auth__title">Регистрация</h1>
              <ul v-if="error.status" class="error">
                <li v-for="message in error.messageList">{{ message }}</li>
              </ul>
              <p>Заполните краткую анкету чтобы зарегистрироваться на сайте</p>
              <form action="#" class="form">
                <label>Логин</label>
                <input v-model="userName" type="text" name="email" id='login' placeholder="Введите имя пользователя">
                <label>Пароль</label>
                <input v-model="password" type="password" name="password"
                       id='password' placeholder="Введите пароль" autocomplete="off">
                <label>Повтор пароля</label>
                <input v-model="password2" type="password" name="password"
                       id='password2' placeholder="Повторите пароль" autocomplete="off">
                <label>Электронная почта</label>
                <input v-model="email" type="email" name="email" id='email' placeholder="Введите email">
                <label>Фамилия</label>
                <input v-model="lastName" type="text" name="last_name" id='last_name' placeholder="Введите фамилию">
                <label>Имя</label>
                <input v-model="firstName" type="text" name="first_name" id='first_name' placeholder="Введите имя">
                <label>Отчество</label>
                <input v-model="middleName" type="text" name="middle_name" id='middle_name'
                       placeholder="Введите отчество">
                <label>Телефон</label>
                <input v-model="phone" type="text" name="phone" id='phone' placeholder="Введите номер телефона">
                <label>Пол</label>
                <div class="gender-field">
                  <input type="radio" id="one" value="m" v-model="gender">
                  <label for="one">Мужской</label>
                </div>
                <div class="gender-field">
                  <input type="radio" id="two" value="f" v-model="gender">
                  <label for="two">Женский</label>
                </div>
                <hr/>
                <button type="button" class="button button__accent mt-4" @click="singUp">Зарегистрироваться</button>
                <h6 class="left-align mb-5">
                  Уже зарегистрированы? <a href="#" @click="goTo('Auth')">Войти</a>
                </h6>
              </form>
            </div>
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
      signOut: false,
      signIn: true,
      username: '',
      userName: '',
      password: '',
      password2: '',
      email: '',
      firstName: '',
      lastName: '',
      middleName: '',
      phone: '',
      gender: '',
      error: {
        status: false,
        messageList: []
      }
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
        username: this.userName,
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

    async singUp() {
      this.error.status = false;
      this.error.messageList = [];

      if (this.password !== this.password2) {
        this.error.status = true;
        this.error.messageList.push('Пароли не совпадают');
      }
      if (!this.userName || !this.password || !this.password2 || !this.lastName || !this.firstName
          || !this.middleName || !this.email || !this.gender || !this.phone) {
        this.error.status = true;
        this.error.messageList.push('Пожалуйста заполните все поля');
      }

      if (this.error.status) {
        return false
      }

      const data = {
        "username": this.userName,
        "last_name": this.lastName,
        "first_name": this.firstName,
        "password": this.password,
        "email": this.email,
        "profile": {
          "middle_name": this.middleName,
          "gender": this.gender,
          "phone": this.phone,
        }
      }

      const base = {
        baseURL: this.$store.state.backendUrl,
        headers: {
          "Content-Type": "application/json",
        },
      }

      const axiosInstance = axios.create(base);
      await axiosInstance({
        url: "/profile/create/",
        method: "post",
        data: data
      })
          .then(() => {
            this.login();
          })
          .catch((error) => {
            if (error.request.status === 401) {
              // Если 401 ошибка - токен просрочен, обновляем его и заново запрашиваем данные
              this.refreshToken();
              this.sendToServer('/send-message/');
            } else {
              console.log(error.request);
            }
          })
    },

    setAuthMode(group) {
      if (this.signIn) {
        this.signIn = false;
        this.signOut = true;
      } else {
        this.signIn = true;
        this.signOut = false;
      }
      let groups = ['signIn', 'signUp'];
      for (let item_group of groups) {
        let item_div = document.getElementById(item_group)
        if (item_group !== group) {
          item_div.classList.remove('group-active')
        } else {
          item_div.classList.add('group-active');
        }
      }
      this.age_group = group;
    },
  }
}
</script>


<style scoped>
.gender-field {
  width: 50%;
  display: inline;
  margin: 10px 50px;
}

.error {
  color: red;
}
</style>