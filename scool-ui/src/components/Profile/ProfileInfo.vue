<template>
  <div v-if="profile" class="page__main">
    <div class="row">
      <profile-header :profile="profile"></profile-header>
      <profile-avatar :profile="profile"></profile-avatar>
    </div>
    <div v-if="isFriend(profile.user) || profile.id === $store.state.authUser.id" id="profile_info">
      <profile-statistic-block :profile="profile"></profile-statistic-block>
      <hr/>
      <div class="left-align mt-5">
        <profile-main-block :profile="profile"></profile-main-block>
        <hr/>
        <h3 class="mb-4">Контактная информация:</h3>
        <profile-contacts-block :profile="profile"></profile-contacts-block>
        <hr/>
        <h3 class="mb-4">Личная информация:</h3>
        <profile-about-block :profile="profile"></profile-about-block>
      </div>
    </div>
    <div v-else id="hide_profile_info">
      <hide-profile-block></hide-profile-block>
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

</style>