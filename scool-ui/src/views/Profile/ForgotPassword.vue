<template>
  <div id="auth">
    <div class="auth past-events">
      <div class="container">
        <div class="auth__inner">
          <div class="auth__media">
            <img src="../../assets/images/owl-auth.svg">
          </div>
          <div class="auth__auth white-block">
            <div id="signInForm" v-if="!showSuccessMessage && !showErrorMessage">
              <h3 class="mb-4">Забыли пароль</h3>
              <form action="#" method="get" class="form" id="formLogin">
                <div class="mb-3">
                  <label class="form-label" for="UserNameField">Для восстановления пароля введите электронную почту</label>
                  <input v-model="email" class="form-control" type="email" name="login" id="UserNameField"
                         placeholder="Введите адрес электронной почты..." required>
                </div>
                <button type="button" class="my-4 button button__accent w-50" @click="resetPassword()">Отправить</button>
              </form>
            </div>
            <div v-else>
              <h3 class="mb-4">Забыли пароль</h3>
              <p v-if="showSuccessMessage">Ссылка для сброса пароля отправлена на почту {{ email }}</p>
              <p v-else-if="showErrorMessage">
                Произошла ошибка! Ссылка для сброса пароля не была отправлена на почту {{ email }}
              </p>
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


export default {
  title: 'Академия будущего | Регистрация - Вход',
  description: 'Регистрация - Вход',
  name: "ForgotPassword",

  mixins: [redirect],

  components: {
    Navbar
  },

  data() {
    return {
      email: '',
      showSuccessMessage: false,
      showErrorMessage: false,
    }
  },

  created() {
    if (this.$store.state.isAuthenticated) {
      // Если пользователь вс системе - выгоняем его отсюда
      this.goTo('MyProfile')
    }
  },

  methods: {
    async resetPassword() {
      const body = {
        email: this.email,
      }
      axios
          .post(`${this.$store.getters.getServerUrl}/profile/reset-password/`, body)
          .then((response) => {
            if (response.status === 200) {
              this.showSuccessMessage = true;
            }
          })
          .catch((error) => {
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
</style>