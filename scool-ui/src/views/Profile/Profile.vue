<template>
  <div v-if="responseData" id="profile">
    <navbar></navbar>
    <div class="step landing__section main-section">
      <div class="page">
        <div class="container mt-5">
          <div class="page__inner">
            <profile-menu :header="header"></profile-menu>
            <profile-info :profile="responseData" @reLoad="createGetRequest(`/profile/${id}`)"></profile-info>
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
  name: "Profile",

  data() {
    return {
      header: 'Профиль',
    }
  },

  props: {
    id: String,
  },

  components: {
    ProfileMenu, Navbar, ProfileInfo
  },

  async created() {
    await this.createGetRequest(`/profile/${this.id}/`)
  },

  mixins: [redirect, requestsMixin],
}
</script>

<style scoped>

</style>