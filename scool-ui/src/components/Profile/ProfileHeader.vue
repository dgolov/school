<template>
  <div class="col-md-6">
    <h3 class="page__main__title left-align mb-2 center">
      {{ profile.last_name }} {{ profile.first_name }} {{ profile.middle_name }}</h3>
    <h6 v-if="profile.user_group === 'student'" class="center">Студент</h6>
    <h6 v-else-if="profile.user_group === 'teacher'" class="center">Преподаватель</h6>
    <h6 v-else-if="profile.user_group === 'manager'" class="center">Менеджер учебного процесса</h6>
    <hr/>
    <button v-if="profile.id === $store.state.authUser.id" class="gray-button">
      Редактировать профиль</button>
    <button v-if="isFriend(profile.user)" class="w-100" @click="removeFriend(profile, 'profile')">
      Удалить из друзей</button>
    <button v-else-if="isSubscription(profile.user)" class="w-100" @click="unsubscribe(profile, 'profile')">
      Отписаться</button>
    <button v-else-if="isFollower(profile.user)" class="w-100" @click="addFriendRequest(profile, 'profile')">
      Принять дружбу</button>
    <button v-else-if="profile.id !== $store.state.authUser.id" class="w-100" @click="addFriend(profile, 'profile')">
      Добавить в друзья</button>
    <button v-if="isFriend(profile.user)" class="w-100" @click="showMessageModal()">
      Написать сообщение</button>
    <message-modal v-if="isFriend(profile.user)" :id="profile.id" ref="messageModal"></message-modal>
  </div>
</template>


<script>
import {friendMixin} from "../mixins/friendMixin";
import MessageModal from "../Modal/MessageModal";

export default {
  name: "ProfileHeader",

  components: {
    MessageModal
  },

  props: ['profile'],

  mixins: [friendMixin],

  methods: {
    showMessageModal() {
      // Показать окно отправки сообщения
      this.$refs.messageModal.show = true
    },
  },
}
</script>


<style scoped>

</style>