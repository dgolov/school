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
            <p>Заполните краткую анкету чтобы зарегистрироваться на сайте</p>
            <form method='post' action="/example" autocompelete="new-password" role="presentation" class="form">
              <input name="email" class="fakefield">
              <label>Логин</label>
              <input type="text" name="email" id='email' placeholder="Введите имя пользователя">
              <label>Пароль</label>
              <input type="password" name="password" id='password' placeholder="Введите пароль" autocomplete="off">
              <label>Повтор пароля</label>
              <input type="password" name="password" id='password2' placeholder="Повторите пароль" autocomplete="off">
              <label>Фамилия</label>
              <input type="text" name="last_name" id='last_name' placeholder="Введите фамилию">
              <label>Имя</label>
              <input type="text" name="first_name" id='first_name' placeholder="Введите имя">
              <label>Отчество</label>
              <input type="text" name="middle_name" id='middle_name' placeholder="Введите отчество">
              <label>Телефон</label>
              <input type="text" name="phone" id='phone' placeholder="Введите номер телефона">
              <button type='submit' class="button button__accent">Зарегистрироваться</button>
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

export default {
  name: "SignUp",
  components: {Navbar},
  methods: {
    goTo(view_component) {
      this.$router.push({name: view_component, params: {}})
    }
  }

}
</script>

<style scoped>

</style>