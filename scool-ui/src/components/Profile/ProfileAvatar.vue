<template>
  <div>
    <img v-if="profile.avatar" class="profile-avatar left"
         :src="`${profile.avatar.image}`">
    <img v-else src="../../assets/images/avatars/mike2.jpeg" class="profile-avatar left">
  </div>
</template>

<script>
export default {
  name: "ProfileAvatar",

  props: ['profile'],
}
</script>

<style scoped>
.profile-avatar {
  display: block;
  width: 160px;
  height: 160px;
  border: 0;
  border-radius: 50%;
  margin: 0 auto;
  text-align: center;
}
</style>