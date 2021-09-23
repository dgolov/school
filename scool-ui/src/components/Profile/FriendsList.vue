<!--Для отображения друзей, подписчиков, подписок (для списка в поиске и в группах другой алгоритм запросов на бэк-->
<template>
  <div v-if="profiles" id="profile-list">
    <div v-for="profile in profiles" class="row row_list">
      <div class="col-md-3 mt-3">
        <img v-if="profile.avatar" class="center small_avatar"
             :src="`http://127.0.0.1:8000${profile.avatar}`">
        <img v-else class="center small_avatar" src="../../assets/images/avatars/mike2.jpeg">
      </div>
      <div class="col-md-5">
        <h4 class="left-align">
          <a href="#" @click="goTo('Profile', {id: profile.profile_id})">
            {{ profile.first_name }} {{ profile.last_name }}
          </a>
        </h4>
        <h6 class="left-align">{{ getUserGroup(profile.user_group) }}</h6>
      </div>
      <div class="col-md-4 left-align pt-4">
        <div v-if="isFriend(profile.id)">
          <a href="#">
            <img src="../../assets/images/icons/send-message.svg" class="friends_button">
            Написать сообщение
          </a>
        </div>
        <div v-if="isFriend(profile.id)">
          <a href="#" @click="removeFriend(profile, 'user')">
            <img src="../../assets/images/icons/delete.svg" class="friends_button">
            Удалить из друзей
          </a>
        </div>
        <div v-else-if="isFollower(profile.id)">
          <a href="#" @click="addFriendRequest(profile, 'user')">
            <img src="../../assets/images/icons/user_add.png" class="friends_button">
            Принять дружбу
          </a>
        </div>
        <div v-else-if="isSubscription(profile.id)">
          <a href="#" @click="unsubscribe(profile, 'user')">
            <img src="../../assets/images/icons/delete.svg" class="friends_button">
            Отписаться
          </a>
        </div>
        <div v-else-if="profile.id !== $store.state.authUser.user">
          <a href="#" @click="addFriend(profile, 'user')">
            <img src="../../assets/images/icons/user_add.png" class="friends_button">
            Добавить в друзья
          </a>
        </div>
      </div>
    </div>
    <h6 v-if="profiles.length === 0" class="mt-5">{{ header }} отсутствуют</h6>
  </div>
</template>

<script>
import {redirect} from "../mixins/redirect";
import {friendMixin} from "../mixins/friendMixin";

export default {
  name: "FriendsList",

  props: {
    profiles: Array,
    header: String,
  },

  mixins: [redirect, friendMixin],

  methods: {
    getUserGroup(userGroup) {
      if (userGroup === 'student') {
        return 'Студент';
      } else if (userGroup === 'teacher') {
        return 'Преподаватель';
      } else if (userGroup === 'manager') {
        return 'Менеджер учебного процесса';
      } else {
        return '';
      }
    }
  },
}
</script>

<style scoped>
.friends_button {
  width: 15px;
  margin-right: 5px;
}
</style>