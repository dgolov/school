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