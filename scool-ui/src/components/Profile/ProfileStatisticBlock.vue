<template>
  <div class="counts">
    <div class="count">
      <a href="#" @click="goTo('Friends', {id: profile.id})" class="statistic-link">
        <span>{{ profile.friends.length }}</span>
      </a>
      Друзья
    </div>
    <div class="count">
      <a href="#" @click="goTo('Followers', {id: profile.id})" class="statistic-link">
        <span>{{ profile.followers.length }}</span>
      </a>
      Подписчики
    </div>
    <div class="count">
      <span>{{ profile.friend_request_out.length }}</span>
      Подписки
    </div>
    <div class="count">
      <a href="#" @click="goTo('Photo', {id: profile.id})" class="statistic-link">
        <span>{{ profile.photos.length }}</span>
      </a>
      Фотографии
    </div>
  </div>
</template>


<script>
import {redirect} from "../mixins/redirect";

export default {
  name: "StudentAbout",

  props: ['profile'],

  mixins: [redirect]
}
</script>


<style scoped>
.statistic-link {
  text-decoration: none;
}
</style>