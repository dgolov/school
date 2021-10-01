<template>
  <div class="col-md-6">
    <img v-if="profile.avatar" class="center profile-avatar"
         :src="`${profile.avatar.image}`">
    <img v-else src="../../assets/images/avatars/mike2.jpeg" class="center profile-avatar">
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
  margin: 30px auto;
  text-align: center;
}
</style>