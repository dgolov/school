<template>
  <div class="row my-3" id="statistic-block">
    <div class="col-md-3">
      <a v-if="profile" href="#" class="profile-counters"
         @click="goTo('Friends', {id: profile.id})">
        {{ profile.friends.length }}
      </a>
      <h6>Друзья</h6>
    </div>
    <div class="col-md-3">
      <a v-if="profile" href="#" class="profile-counters"
         @click="goTo('Followers', {id: profile.id})">
        {{ profile.followers.length }}
      </a>
      <h6>Подписчики</h6>
    </div>
    <div class="col-md-3">
      <a v-if="profile" href="#" class="profile-counters"
         @click="goTo('Subscriptions', {id: profile.id})">
        {{ profile.friend_request_out.length }}
      </a>
      <h6>Подписки</h6>
    </div>
    <div class="col-md-3">
      <a href="#" @click="goTo('Photo', {id: profile.id})"
         class="profile-counters">{{ profile.photos.length }}</a>
      <h6>Фотографии</h6>
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
.profile-counters {
  font-size: 20px;
  color: #4c28de;
}
</style>