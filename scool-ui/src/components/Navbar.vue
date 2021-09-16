<template>
  <div class="nav_bar">
    <nav class="nav__mobile"></nav>
    <div class="container">
      <div class="navbar__inner">
        <a href="#" class="navbar__logo">Logo</a>
        <nav class="navbar__menu">
          <ul class="main-nav">
            <li><a href="#">Главная</a></li>
            <li><a href="#">Обучение</a></li>
            <li><a href="#">Новости</a></li>
            <li><a href="#">Об академии</a></li>
            <li><a href="#">Контакты</a></li>
          </ul>
          <ul>
            <li><a href="#">Регистрация</a></li>
            <li><a href="#">Вход</a></li>
          </ul>
        </nav>
        <div class="navbar__menu-mob">
          <a href="" id='toggle'>
            <svg role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512">
              <path fill="currentColor"
                    d="M16 132h416c8.837 0 16-7.163 16-16V76c0-8.837-7.163-16-16-16H16C7.163 60 0 67.163 0 76v40c0 8.837 7.163 16 16 16zm0 160h416c8.837 0 16-7.163 16-16v-40c0-8.837-7.163-16-16-16H16c-8.837 0-16 7.163-16 16v40c0 8.837 7.163 16 16 16zm0 160h416c8.837 0 16-7.163 16-16v-40c0-8.837-7.163-16-16-16H16c-8.837 0-16 7.163-16 16v40c0 8.837 7.163 16 16 16z"
                    class=""></path>
            </svg>
          </a>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Navbar"
}
</script>

<style scoped>

</style>