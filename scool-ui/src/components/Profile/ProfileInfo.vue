<template>
  <div v-if="profile" class="col-xl-10 col-lg-9">
    <div class="cabinet-content">
      <div class="user-info">
        <profile-header :profile="profile"></profile-header>
        <div v-if="isFriend(profile.user) || profile.id === $store.state.authUser.id">
          <profile-main-block :profile="profile"></profile-main-block>
          <profile-contacts-block :profile="profile"></profile-contacts-block>
          <profile-about-block :profile="profile"></profile-about-block>
        </div>
        <div v-else id="hide_profile_info">
          <hide-profile-block></hide-profile-block>
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

</style>