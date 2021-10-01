<template>
  <div class="sign-up">
    <navbar></navbar>
    <div class="auth">
      <div class="container">
        <div class="auth__inner">
          <div class="auth__media">
            <img src="../assets/images/undraw_selfie.svg">
          </div>
          <div class="auth__auth my-5">
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
                <label>Дата рождения</label>
              </div>
              <date-picker v-model="dateOfBirthDay" valueType="format" class="date-of-birthday-field"></date-picker>
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
</template>


<script>
import Navbar from "../components/Navbar";
import DatePicker from "vue2-datepicker";
import 'vue2-datepicker/index.css';
import {redirect} from "../components/mixins/redirect";
import axios from "axios";
import {requestsMixin} from "../components/mixins/requestsMixin";

export default {
  name: "SignUp",

  components: {
    Navbar, DatePicker,
  },

  data() {
    return {
      userName: '',
      password: '',
      password2: '',
      email: '',
      firstName: '',
      lastName: '',
      middleName: '',
      phone: '',
      gender: '',
      dateOfBirthDay: '',
      error: {
        status: false,
        messageList: []
      },
    }
  },

  mixins: [redirect, requestsMixin],

  methods: {
    async singUp() {
      this.error.status = false;
      this.error.messageList = [];

      if (this.password !== this.password2) {
        this.error.status = true;
        this.error.messageList.push('Пароли не совпадают');
      }
      if (!this.userName || !this.password || !this.password2 || !this.lastName || !this.firstName
          || !this.middleName || !this.email || !this.gender || !this.dateOfBirthDay || !this.phone) {
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
          "date_of_birthday": this.dateOfBirthDay
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
            this.goTo('Auth');
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
  },
}
</script>


<style scoped>
.date-of-birthday-field {
  width: 100%;
  height: 40px;
  margin-top: 20px;
}

.gender-field {
  width: 50%;
  display: inline;
  margin: 10px 50px;
}

.error {
  color: red;
}
</style>
