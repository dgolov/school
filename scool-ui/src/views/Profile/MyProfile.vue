<template>
  <div id="profile">
    <navbar></navbar>
    <div class="step landing__section main-section past-events">
      <div class="page">
        <div class="container mt-1">
          <div class="page__inner">
            <profile-menu :header="header"></profile-menu>
            <profile-info v-if="responseData" :profile="responseData"></profile-info>
            <loader v-else object="#ff9633" color1="#ffffff" color2="#17fd3d" size="5" speed="2" bg="#343a40"
                    objectbg="#999793" opacity="80" disableScrolling="false" name="spinning"></loader>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Navbar from "../../components/Navbar";
import ProfileMenu from "../../components/Profile/ProfileMenu";
import ProfileInfo from "../../components/Profile/ProfileInfo";
import {redirect} from "../../components/mixins/redirect";
import {requestsMixin} from "../../components/mixins/requestsMixin";

export default {
  title: 'Академия будущего | Личный кабинет',
  name: "MyProfile",

  data() {
    return {
      header: 'Личный кабинет',
      responseData: null
    }
  },

  components: {
    ProfileMenu, Navbar, ProfileInfo
  },

  created() {
    this.createGetRequest(`/profile/${this.$store.state.authUser.id}/`)
  },

  mixins: [redirect, requestsMixin],
}
</script>

<style scoped>

</style>