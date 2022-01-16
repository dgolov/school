<template>
  <div id="friends">
    <navbar></navbar>
    <div class="step landing__section main-section past-events">
      <div class="page">
        <div class="container mt-1">
          <div class="page__inner">
            <profile-menu :header="header"></profile-menu>
            <div class="page__main">
              <search-friends></search-friends>
              <friends-menu></friends-menu>
              <hr/>
              <profiles-list :header="header" :profiles="responseData.friend_request_in"></profiles-list>
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
import ProfilesList from "../../components/Profile/FriendsList";
import {requestsMixin} from "../../components/mixins/requestsMixin";
import {redirect} from "../../components/mixins/redirect";
import SearchFriends from "../../components/Profile/SearchFriends";
import FriendsMenu from "../../components/Profile/FriendsMenu";

export default {
  name: "FriendRequests",

  components: {
    Navbar, ProfileMenu, SearchFriends, FriendsMenu, ProfilesList
  },

  mixins: [requestsMixin, redirect],

  data() {
    return {
      header: 'Заявки в друзья'
    }
  },

  created() {
    this.createGetRequest(`/profile/friend-requests/`)
  },
}
</script>


<style scoped>

</style>