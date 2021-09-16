<template>
  <div id="menu">
    <ul class="vMenu">
      <li class="left-align px-2">
        <img src="../assets/images/icons/profile.svg" class="menu-icon">
        <a href="#"> Личный кабинет </a>
      </li>
      <li class="left-align px-2">
        <img src="../assets/images/icons/courses.svg" class="menu-icon">
        <a href="#"> Доступные курсы </a>
      </li>
      <li class="left-align px-2">
        <img src="../assets/images/icons/calendar.svg" class="menu-icon">
        <a href="#"> Расписание </a>
      </li>
      <li class="left-align px-2">
        <img src="../assets/images/icons/positive_dynamics.svg" class="menu-icon">
        <a href="#"> Успеваемость </a>
      </li>
      <li class="left-align px-2">
        <img src="../assets/images/icons/group.svg" class="menu-icon">
        <a href="#"> Мои группы </a>
      </li>
      <li class="left-align px-2">
        <img src="../assets/images/icons/users_people.svg" class="menu-icon">
        <a href="#"> Мои друзья </a>
        <div class="notification_numbers">1</div>
      </li>
      <li class="left-align px-2">
        <img src="../assets/images/icons/followers.svg" class="menu-icon">
        <a href="#"> Мои подписчики </a>
      </li>
      <li class="left-align px-2">
        <img src="../assets/images/icons/message.svg" class="menu-icon">
        <a href="#"> Мои сообщения </a>
        <div class="notification_numbers">2</div>
      </li>
      <li class="left-align px-2">
        <img src="../assets/images/icons/photos.svg" class="menu-icon">
        <a href="#"> Мои фотографии </a>
      </li>
      <li class="left-align px-2">
        <img src="../assets/images/icons/search.svg" class="menu-icon">
        <a href="#"> Поиск </a>
      </li>
      <li class="left-align px-2">
        <img src="../assets/images/icons/settings.svg" class="menu-icon">
        <a href="#"> Настройки </a>
      </li>
      <li class="left-align px-2">
        <img src="../assets/images/icons/games.svg" class="menu-icon">
        <a href="#"> Игры </a>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: "ProfileMenu"
}
</script>

<style scoped>
  .menu-icon {
    width: 16px;
    margin-right: 5px;
  }
</style>