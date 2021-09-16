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
            <p>Введите свой адрес электронной почты и пароль, чтобы продолжить</p>
            <form method='post' action="#" autocompelete="new-password" role="presentation" class="form">
              <input name="email" class="fakefield">
              <label>Логин</label>
              <input type="text" name="email" id='email' placeholder="Имя пользователя...">
              <label>Пароль</label>
              <input type="password" name="password" id='password'
                     placeholder="&#9679;&#9679;&#9679;&#9679;&#9679;&#9679;&#9679;&#9679;&#9679;"
                     autocomplete="off">
              <button type='submit' class="button button__accent">Войти</button>
              <h6 class="left-align"><a href="#">Забыли пароль?</a></h6>
              <h6 class="left-align">У вас еще нет аккаунта? <a href="#">Зарегистрироваться</a></h6>
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
  name: "Auth",
  components: {Navbar}
}
</script>

<style scoped>

</style>