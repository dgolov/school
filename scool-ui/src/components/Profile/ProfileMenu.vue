<template>
  <div class="page__menu">
    <h3>{{ header }}</h3>
    <hr>
    <ul class="vMenu">
      <li class="left-align px-2">
        <img src="../../assets/images/icons/profile.svg" class="menu-icon">
        <a href="#" @click="goTo('MyProfile')"> Личный кабинет </a>
      </li>
      <li class="left-align px-2">
        <img src="../../assets/images/icons/courses.svg" class="menu-icon">
        <a href="#" @click="goTo('MyCourses')"> Доступные курсы </a>
      </li>
      <li class="left-align px-2">
        <img src="../../assets/images/icons/calendar.svg" class="menu-icon">
        <a href="#" @click="goTo('TimeTable')"> Расписание </a>
      </li>
      <li class="left-align px-2">
        <img src="../../assets/images/icons/positive_dynamics.svg" class="menu-icon">
        <a href="#" @click="goTo('AcademicPerformance')"> Успеваемость </a>
      </li>
      <li class="left-align px-2">
        <img src="../../assets/images/icons/group.svg" class="menu-icon">
        <a href="#" @click="goTo('Groups')"> Мои группы </a>
      </li>
      <li class="left-align px-2">
        <img src="../../assets/images/icons/users_people.svg" class="menu-icon">
        <a href="#" @click="goTo('Friends', {id: $store.state.authUser.id})"> Мои друзья </a>
<!--        <div class="notification_numbers">1</div>-->
      </li>
      <li class="left-align px-2">
        <img src="../../assets/images/icons/followers.svg" class="menu-icon">
        <a href="#" @click="goTo('Followers', {id: $store.state.authUser.id})"> Мои подписчики </a>
      </li>
      <li class="left-align px-2">
        <img src="../../assets/images/icons/message.svg" class="menu-icon">
        <a href="#" @click="goTo('Chats')"> Мои сообщения </a>
<!--        <div class="notification_numbers">2</div>-->
      </li>
      <li class="left-align px-2">
        <img src="../../assets/images/icons/photos.svg" class="menu-icon">
        <a href="#" @click="goTo('Photo', {id: $store.state.authUser.id})"> Мои фотографии </a>
      </li>
      <li class="left-align px-2">
        <img src="../../assets/images/icons/search.svg" class="menu-icon">
        <a href="#" @click="goTo('Search')"> Поиск </a>
      </li>
      <li class="left-align px-2">
        <img src="../../assets/images/icons/settings.svg" class="menu-icon">
        <a href="#" @click="goTo('Settings')"> Настройки </a>
      </li>
      <li class="left-align px-2">
        <img src="../../assets/images/icons/games.svg" class="menu-icon">
        <a href="#" @click="goTo('Games')"> Игры </a>
      </li>
      <li class="left-align px-2">
        <img src="../../assets/images/icons/exit.svg" class="menu-icon">
        <a href="#" @click="logOut()"> Выход </a>
      </li>
    </ul>
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
      this.goTo('Home')
    },
  }
}
</script>


<style scoped>
.menu-icon {
  width: 16px;
  margin-right: 5px;
}
</style>