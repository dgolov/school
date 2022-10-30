<template>
  <div class="top-info">
    <profile-avatar :profile="profile"></profile-avatar>
    <div>
      <div class="name">
        <span>{{ profile.last_name }} {{ profile.first_name }} {{ profile.middle_name }}</span>
        <small v-if="profile.user_group === 'student'" class="center">Студент</small>
        <small v-else-if="profile.user_group === 'teacher'" class="center">Преподаватель</small>
        <small v-else-if="profile.user_group === 'manager'" class="center">Менеджер учебного процесса</small>
      </div>
      <!--      <div class="col-md-6">-->
      <!--        <button v-if="profile.id === $store.state.authUser.id" class="btn" @click="goTo('Settings')">-->
      <!--          Редактировать профиль-->
      <!--        </button>-->
      <!--        <button v-if="isFriend(profile.user)" class="w-100" @click="removeFriend(profile, 'profile')">-->
      <!--          Удалить из друзей-->
      <!--        </button>-->
      <!--        <button v-else-if="isSubscription(profile.user)" class="w-100" @click="unsubscribe(profile, 'profile')">-->
      <!--          Отписаться-->
      <!--        </button>-->
      <!--        <button v-else-if="isFollower(profile.user)" class="w-100" @click="addFriendRequest(profile, 'profile')">-->
      <!--          Принять дружбу-->
      <!--        </button>-->
      <!--        <button v-else-if="profile.id !== $store.state.authUser.id" class="w-100"-->
      <!--                @click="addFriend(profile, 'profile')">-->
      <!--          Добавить в друзья-->
      <!--        </button>-->
      <!--        <button v-if="isFriend(profile.user)" class="w-100" @click="showMessageModal()">-->
      <!--          Написать сообщение-->
      <!--        </button>-->
      <!--        <message-modal v-if="isFriend(profile.user)" :id="profile.id" ref="messageModal"></message-modal>-->
      <!--      </div>-->
      <profile-statistic-block :profile="profile"></profile-statistic-block>
    </div>
  </div>
</template>


<script>
import {friendMixin} from "../mixins/friendMixin";
import MessageModal from "../Modal/MessageModal";
import ProfileAvatar from "./ProfileAvatar";
import ProfileStatisticBlock from "./ProfileStatisticBlock";

export default {
  name: "ProfileHeader",

  components: {
    MessageModal,
    ProfileAvatar,
    ProfileStatisticBlock
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