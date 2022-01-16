<template>
  <div id="subscriptions">
    <navbar></navbar>
    <div class="step landing__section main-section past-events">
      <div class="page">
        <div class="container mt-1">
          <div class="page__inner">
            <profile-menu :header="header"></profile-menu>
            <div class="page__main">
              <form>
                <input type='text' placeholder="Поиск">
              </form>
              <friends-list :header="header" :profiles="responseData.friend_request_out"
                            @reLoad="createGetRequest(`/profile/${id}/subscriptions/`)"></friends-list>
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
import FriendsList from "../../components/Profile/FriendsList";
import {requestsMixin} from "../../components/mixins/requestsMixin";
import {redirect} from "../../components/mixins/redirect";

export default {
  name: "Subscriptions",

  components: {
    Navbar, ProfileMenu, FriendsList
  },

  mixins: [requestsMixin, redirect],

  data() {
    return {
      header: 'Подписки'
    }
  },

  props: {
    id: String
  },

  created() {
    this.createGetRequest(`/profile/${this.id}/subscriptions/`)
  },
}
</script>


<style scoped>

</style>