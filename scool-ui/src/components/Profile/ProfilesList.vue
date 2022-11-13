<!--Для отображения одногруппников в группах и пользователей в поиске
(для списка друзей, подписчиков и подписок другой алгоритм запросов на бэк)-->
<template>
  <div v-if="profiles">
    <message-modal v-if="modalVisible" @close="modalVisible = false" :id="modalData"></message-modal>
    <div class="cabinet-content">
      <div class="groups">
        <div class="flex">
          <div class="top-text">{{ headerName }}</div>
          <form>
            <input type="text" placeholder="Поиск">
            <button></button>
          </form>
        </div>
        <div v-for="profile in profiles" class="item">
          <div>
            <img v-if="profile.avatar" class="center small_avatar"
                 :src="profile.avatar">
            <img v-else class="center small_avatar" src="../../assets/images/avatars/mike2.jpeg">
          </div>
          <div>
            <span>
              <a href="#" @click="goTo('Profile', {id: profile.id})">
                {{ profile.first_name }} {{ profile.last_name }}
              </a>
            </span>
            <a href="#" v-if="isFriend(profile.user)" @click="showMessageModal(profile.id)">Написать
              сообщение</a>
            <a class="unsubscribe" v-if="isFriend(profile.user)" @click="removeFriend(profile, 'profile')">
              Удалить из друзей
            </a>
            <a class="unsubscribe" v-else-if="isFollower(profile.user)" @click="addFriendRequest(profile, 'profile')">
              Принять дружбу
            </a>
            <a class="unsubscribe" v-else-if="isSubscription(profile.user)" @click="unsubscribe(profile, 'profile')">
              Отписаться
            </a>
            <a class="unsubscribe" v-else-if="profile.user !== $store.state.authUser.user"
               @click="addFriend(profile, 'profile')">
              Добавить в друзья
            </a>
          </div>
        </div>
        <small v-if="profiles.length === 0" class="mt-5">{{ headerName }} отсутствуют</small>
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
      if (url.indexOf(`${this.$store.state.backendUrl}`) === -1) {
        return `${this.$store.state.baseUrl}${url}`
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