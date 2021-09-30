<!--Для отображения одногруппников в группах и пользователей в поиске
(для списка друзей, подписчиков и подписок другой алгоритм запросов на бэк)-->
<template>
  <div v-if="profiles" id="profile-list">
    <message-modal v-if="modalVisible" @close="modalVisible = false" :id="modalData"></message-modal>
    <div v-for="profile in profiles" class="row row_list">
      <div class="col-md-3 mt-3">
        <img v-if="profile.avatar" class="center small_avatar"
             :src="getImage(profile.avatar.image)">
        <img v-else class="center small_avatar" src="../../assets/images/avatars/mike2.jpeg">
      </div>
      <div class="col-md-5">
        <h4 class="left-align">
          <a href="#" @click="goTo('Profile', {id: profile.id})">
            {{ profile.first_name }} {{ profile.last_name }}
          </a>
        </h4>
        <h6 class="left-align">{{ getUserGroup(profile.user_group) }}</h6>
      </div>
      <div class="col-md-4 left-align pt-4">
        <div v-if="isFriend(profile.user)">
          <button @click="showMessageModal(profile.id)" style="margin: 0; border: none; padding: 0; color: #000000;">
            <img src="../../assets/images/icons/send-message.svg" class="friends_button">
            Написать сообщение
          </button>
        </div>
        <div v-if="isFriend(profile.user)">
          <a href="#" @click="removeFriend(profile, 'profile')">
            <img src="../../assets/images/icons/delete.svg" class="friends_button">
            Удалить из друзей
          </a>
        </div>
        <div v-else-if="isFollower(profile.user)">
          <a href="#" @click="addFriendRequest(profile, 'profile')">
            <img src="../../assets/images/icons/user_add.png" class="friends_button">
            Принять дружбу
          </a>
        </div>
        <div v-else-if="isSubscription(profile.user)">
          <a href="#" @click="unsubscribe(profile, 'profile')">
            <img src="../../assets/images/icons/delete.svg" class="friends_button">
            Отписаться
          </a>
        </div>
        <div v-else-if="profile.user !== $store.state.authUser.user">
          <a href="#" @click="addFriend(profile, 'profile')">
            <img src="../../assets/images/icons/user_add.png" class="friends_button">
            Добавить в друзья
          </a>
        </div>
      </div>
    </div>
  </div>
</template>


<script>
import {friendMixin} from "../mixins/friendMixin";
import {redirect} from "../mixins/redirect";
import MessageModal from "../Modal/MessageModalFromUsersList";

export default {
  name: "ProfilesList",

  data() {
    return {
      modalVisible: false,
      modalData: null,
    }
  },

  props: {
    profiles: Array
  },

  components: {
    MessageModal
  },

  mixins: [friendMixin, redirect],

  methods: {
    showMessageModal(id) {
      // Показать окно отправки сообщения
      this.modalData = id
      this.modalVisible = true
    },

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
    },

    getImage(url) {
      // Некоторые данные приходят с сервера с абсолютным адресом, некоторые с относительным, вероятно из-за ViewSets
      // Данный метод временно решает эту проблему
      if (url.indexOf(`${this.$store.state.baseUrl}`) === -1) {
        return `${this.$store.baseUrl}${url}`
      } else {
        return url
      }
    },
  },
}
</script>


<style scoped>
.friends_button {
  width: 15px;
  margin-right: 5px;
}
</style>