<!--Для отображения друзей, подписчиков, подписок (для списка в поиске и в группах другой алгоритм запросов на бэк-->
<template>
  <div v-if="profiles" class="col-xl-10 col-lg-9">
    <message-modal v-if="modalVisible" @close="modalVisible = false" :id="modalData"></message-modal>
    <div class="cabinet-content">
      <div class="groups">
        <div class="flex">
          <div class="top-text">{{ headerName }}</div>
          <form>
            <input v-if="header === 'Friends'" type="text" placeholder="Поиск друзей">
            <input v-if="header === 'Followers'" type="text" placeholder="Поиск подписчиков">
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
              <a href="#" @click="goTo('Profile', {id: profile.profile_id})">
                {{ profile.first_name }} {{ profile.last_name }}
              </a>
            </span>
            <a href="#" v-if="isFriend(profile.id)" @click="showMessageModal(profile.profile_id)">Написать сообщение</a>
            <a class="unsubscribe" v-if="isFriend(profile.id)" @click="removeFriend(profile, 'user')">
              Удалить из друзей
            </a>
            <a class="unsubscribe" v-else-if="isFollower(profile.id)" @click="addFriendRequest(profile, 'user')">
              Принять дружбу
            </a>
            <a class="unsubscribe" v-else-if="isSubscription(profile.id)" @click="unsubscribe(profile, 'user')">
              Отписаться
            </a>
            <a class="unsubscribe" v-else-if="profile.id !== $store.state.authUser.user" @click="addFriend(profile, 'user')">
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
import {redirect} from "../mixins/redirect";
import {friendMixin} from "../mixins/friendMixin";
import MessageModal from "../Modal/MessageModalFromUsersList";

export default {
  name: "FriendsList",

  data() {
    return {
      modalVisible: false,
      modalData: null,
      headerName: ''
    }
  },

  props: {
    profiles: Array,
    header: String,
  },

  components: {
    MessageModal
  },

  mixins: [redirect, friendMixin],

  created() {
    if (this.header === 'Friends') {
      this.headerName = 'Друзья';
    } else if (this.header === 'Followers') {
      this.headerName = 'Подписчики';
    }
    else {
      this.headerName = 'Пользователи';
    }
  },

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
    }
  },
}
</script>


<style scoped>
</style>