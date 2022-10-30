<template>
  <div class="col-xl-2 col-lg-3">
    <nav class="menu">
      <ul>
        <li>
          <a href="#" @click="goTo('MyProfile')" class="active">
            <span><img src="../../assets/images/cabinet/img/cabinet-menu1.svg"></span> Моя страница
          </a>
        </li>
        <li>
          <a href="#" @click="goTo('MyCourses')">
            <span><img src="../../assets/images/cabinet/img/cabinet-menu2.svg"></span> Доступные курсы
          </a>
        </li>
        <li>
          <a href="#" @click="goTo('AcademicPerformance')">
            <span><img src="../../assets/images/cabinet/img/cabinet-menu3.svg"></span> Расписание
          </a>
        </li>
        <li>

          <a href="#">
            <span><img src="../../assets/images/cabinet/img/cabinet-menu4.svg"></span> Успеваемость
          </a>
        </li>
        <li>
          <a href="#" @click="goTo('Groups')">
            <span><img src="../../assets/images/cabinet/img/cabinet-menu5.svg"></span> Группы
          </a>
        </li>
        <li>
          <a href="#" @click="goTo('Friends', {id: $store.state.authUser.id})">
            <span><img src="../../assets/images/cabinet/img/cabinet-menu6.svg"></span> Друзья
          </a>
        </li>
        <li>
          <a href="#" @click="goTo('Followers', {id: $store.state.authUser.id})">
            <span><img src="../../assets/images/cabinet/img/cabinet-menu7.svg"></span> Подписчики
          </a>
        </li>
        <li>
          <a href="#" @click="goTo('Chats')">
            <span><img src="../../assets/images/cabinet/img/cabinet-menu8.svg"></span> Сообщения
          </a>
        </li>
        <li>
          <a href="#" @click="goTo('Photo', {id: $store.state.authUser.id})">
            <span><img src="../../assets/images/cabinet/img/cabinet-menu9.svg"></span> Фотографии
          </a>
        </li>
        <li>
          <a href="#" @click="goTo('Search')">
            <span><img src="../../assets/images/cabinet/img/cabinet-menu10.svg"></span> Поиск
          </a>
        </li>
        <li>
          <a href="#" @click="goTo('Settings')">
            <span><img src="../../assets/images/cabinet/img/cabinet-menu11.svg"></span> Настройки
          </a>
        </li>
        <li>
          <a href="#" @click="goTo('Games')">
            <span><img src="../../assets/images/cabinet/img/cabinet-menu12.svg"></span> Игры
          </a>
        </li>
        <li>
          <a href="#">
            <span><img src="../../assets/images/cabinet/img/cabinet-menu13.svg"></span> Магазин
          </a>
        </li>
        <li>
          <a href="#">
            <span><img src="../../assets/images/cabinet/img/cabinet-menu14.svg"></span> Награды
          </a>
        </li>
        <li>
          <a href="#" @click="logOut()">
            <span><img src="../../assets/images/cabinet/img/cabinet-menu15.svg"></span> Выход
          </a>
        </li>
      </ul>
    </nav>
  </div>
</template>


<script>
import {redirect} from "../mixins/redirect";

export default {
  name: "ProfileMenu",

  data() {
    return {
      user: this.$store.state.authUser,
    }
  },

  props: {
    header: String
  },

  mixins: [redirect],

  methods: {
    logOut() {
      this.$store.commit("setAuthUser", {
        authUser: null,
        isAuthenticated: false,
      });
      this.$store.commit("removeToken")
      window.location.href = '/';
    },
  }
}
</script>

<style scoped>
</style>