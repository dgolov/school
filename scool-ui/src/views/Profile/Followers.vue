<template>
  <div id="friends">
    <navbar></navbar>
    <div class="step landing__section main-section">
      <div class="page">
        <div class="container mt-5">
          <div class="page__inner">
            <profile-menu :header="header"></profile-menu>
            <div class="page__main">
              <form>
                <input type='text' placeholder="Поиск">
              </form>
              <friends-list :header="header" :profiles="responseData.followers" @reLoad="`/profile/${id}/followers/`"></friends-list>
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
import {requestsMixin} from "../../components/mixins/requestsMixin";
import {redirect} from "../../components/mixins/redirect";
import FriendsList from "../../components/Profile/FriendsList";

export default {
  name: "Followers",

  components: {
    Navbar, ProfileMenu, FriendsList
  },

  mixins: [requestsMixin, redirect],

  data() {
    return {
      header: 'Подписчики'
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