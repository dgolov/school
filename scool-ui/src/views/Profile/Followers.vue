<template>
  <div class="cabinet-page">
    <div class="container">
      <button class="cabinet-menu-button">МЕНЮ ЛИЧНОГО КАБИНЕТА</button>
      <div class="row">
        <profile-menu :header="header"></profile-menu>
        <friends-list :header="header" :profiles="responseData.followers"
                      @reLoad="createGetRequest(`/profile/${id}/followers/`)"></friends-list>
        <div class="col-xl-2 col-lg-3"></div>
        <div class="col-xl-10 col-lg-9">
          <div class="cabinet-copy">
            © Академия будущего «ХОД», 2022
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Navbar from "../../components/Navbar";
import ProfileMenu from "../../components/Profile/ProfileMenu";
import {requestsMixin} from "../../components/mixins/requestsMixin";
import {redirect} from "../../components/mixins/redirect";
import FriendsList from "../../components/Profile/FriendsList";

export default {
  title: 'Академия будущего | Личный кабинет',
  name: "Followers",

  components: {
    Navbar, ProfileMenu, FriendsList
  },

  mixins: [requestsMixin, redirect],

  data() {
    return {
      header: 'Followers'
    }
  },

  props: {
    id: String
  },

  created() {
    this.createGetRequest(`/profile/${this.id}/followers/`)
  },
}
</script>

<style scoped>

</style>