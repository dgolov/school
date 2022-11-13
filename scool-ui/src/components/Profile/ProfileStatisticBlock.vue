<template>
  <div class="counts">
    <div class="count">
      <span>{{ profile.friends.length }}</span>
      Друзья
    </div>
    <div class="count">
      <span>{{ profile.followers.length }}</span>
      Подписчики
    </div>
    <div class="count">
      <span>{{ profile.friend_request_out.length }}</span>
      Подписки
    </div>
    <div class="count">
      <span>{{ profile.photos.length }}</span>
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
</style>