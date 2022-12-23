<template>
  <div id="auth">
    <div class="auth past-events">
      <div class="container">
        <div class="auth__inner">
          <div class="auth__media">
            <img src="../../assets/images/owl-auth.svg">
          </div>
          <div class="auth__auth white-block">
            <div id="signInForm">
              <div class="mb-4" v-if="showErrorMessage">
                <p class="errors" v-for="message in errorMessage">{{ message }}</p>
              </div>
              <h3 class="mb-4">Восстановление пароя</h3>
              <form action="#" method="get" class="form" id="formLogin" v-if="showResetForm">
                <div class="mb-3">
                  <label class="form-label" for="Password1">Введите новый пароль</label>
                  <input v-model="newPassword" class="form-control" type="password" name="login" id="Password1"
                         placeholder="Введите новый пароль..." required>
                  <label class="form-label mt-2" for="Password12">Повторите пароль</label>
                  <input v-model="newPassword2" class="form-control" type="password" name="login" id="Password12"
                         placeholder="Повторите пароль..." required>
                </div>
                <button type="button" class="my-4 button button__accent w-50" @click="resetPassword()">Отправить</button>
              </form>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Navbar from "../../components/Navbar";
import axios from "axios";
import {redirect} from "../../components/mixins/redirect";
import {requestsMixin} from "../../components/mixins/requestsMixin";


export default {
  title: 'Академия будущего | Регистрация - Вход',
  description: 'Регистрация - Вход',
  name: "ForgotPassword",

  mixins: [
      redirect, requestsMixin
  ],

  components: {
    Navbar
  },

  data() {
    return {
      newPassword: '',
      newPassword2: '',
      errorMessage: [],
      showErrorMessage: false,
      showResetForm: false
    }
  },

  props: {
    token: String
  },

  created() {
    if (this.$store.state.isAuthenticated) {
      // Если пользователь вс системе - выгоняем его отсюда
      this.goTo('MyProfile')
    }
    this.verifyToken()
  },

  methods: {
    async verifyToken() {
      const body = {
        'token': this.token
      }
      axios
          .post(`${this.$store.getters.getServerUrl}/profile/reset-password/verify-token/`, body)
          .then((response) => {
            this.showResetForm = true;
          })
          .catch((error) => {
            this.errorMessage = [
                'Сессия восстановления пароля просрочена или не существует, пожалуйста повторите попытку заново.'
            ]
            this.showErrorMessage = true;
            console.log(error);
            console.debug(error);
            console.dir(error);
          });
    },

    async resetPassword() {
      const body = {
        'token': this.token,
        'password': this.newPassword
      }
      axios
          .post(`${this.$store.getters.getServerUrl}/profile/reset-password/confirm/`, body)
          .then((response) => {
            if (response.status === 200) {
              this.goTo('Auth')
            }
          })
          .catch((error) => {
            this.errorMessage = error.response.data.password
            this.showErrorMessage = true;
            console.log(error);
            console.debug(error);
            console.dir(error);
          });
    },
  }
}
</script>

<style scoped>
.white-block {
  background-color: #fff;
  padding: 40px 80px;
  border-radius: 15px;
}

.errors {
  color: red;
}
</style>