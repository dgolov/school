<template>
  <div id="profile">
    <div class="cabinet-page">
      <div class="container">
        <button class="cabinet-menu-button">МЕНЮ ЛИЧНОГО КАБИНЕТА</button>
        <div class="row">
          <profile-menu :header="header"></profile-menu>
          <profile-info v-if="responseData" :profile="responseData"
                        @reLoad="createGetRequest(`/profile/${id}`)"></profile-info>
          <div v-if="responseData" class="col-xl-2 col-lg-3"></div>
          <loader v-else object="#ff9633" color1="#ffffff" color2="#17fd3d" size="5" speed="2" bg="#343a40"
                  objectbg="#999793" opacity="80" disableScrolling="false" name="spinning"></loader>
          <div class="col-xl-10 col-lg-9">
            <div class="cabinet-copy">
              © Академия будущего «ХОД», 2022
            </div>
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
  name: "Profile",

  data() {
    return {
      header: 'Профиль',
      responseData: null
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