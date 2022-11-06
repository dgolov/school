<template>
  <div v-if="profile" class="col-xl-10 col-lg-9">
    <div class="cabinet-content">
      <div class="user-info">
        <profile-header :profile="profile"></profile-header>
        <div v-if="isFriend(profile.id) || profile.id === $store.state.authUser.id">
          <profile-main-block :profile="profile"></profile-main-block>
          <profile-contacts-block :profile="profile"></profile-contacts-block>
          <profile-about-block :profile="profile"></profile-about-block>
        </div>
        <div v-else id="hide_profile_info">
          <hide-profile-block></hide-profile-block>
        </div>
      </div>
      <div class="users" v-if="isFriend(profile.id) || profile.id === $store.state.authUser.id">
        <div class="flex">
          <div class="top-text">
            Друзья <span>{{ profile.friends.length }}</span>
          </div>
          <a href="#" @click="goTo('Friends', {id: profile.id})" class="top-link">Все друзья</a>
        </div>
        <div class="flex">
          <div class="item" v-for="friend in profile.friends.slice(0, 9)">
            <img v-if="friend.avatar" class="profile-avatar left"
                 :src="`${friend.avatar.image}`"
                 @click="goTo('Profile', {id: friend.profile_id})">
            <img v-else src="../../assets/images/avatars/mike2.jpeg"
                 class="profile-avatar left" @click="goTo('Profile', {id: friend.profile_id})">
            <p @click="goTo('Profile', {id: friend.profile_id})">
              {{ friend.first_name }} {{ friend.last_name }}
            </p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>


<script>
import {friendMixin} from "../mixins/friendMixin";
import ProfileContactsBlock from "./ProfileContactsBlock";
import ProfileMainBlock from "./ProfileMainBlock";
import ProfileStatisticBlock from "./ProfileStatisticBlock";
import HideProfileBlock from "./HideProfileBlock";
import ProfileHeader from "./ProfileHeader";
import ProfileAvatar from "./ProfileAvatar";
import ProfileAboutBlock from "./ProfileAboutBlock";

export default {
  name: "ProfileInfo",

  components: {
    ProfileAboutBlock,
    ProfileAvatar,
    ProfileHeader,
    HideProfileBlock,
    ProfileStatisticBlock,
    ProfileMainBlock,
    ProfileContactsBlock,
  },

  props: ['profile'],

  mixins: [friendMixin],
}
</script>


<style scoped>
.profile-avatar {
  display: block;
  width: 50%;
  border: 0;
  border-radius: 50%;
  margin: 0 auto;
  text-align: center;
}
</style>