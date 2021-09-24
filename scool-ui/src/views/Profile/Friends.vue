<template>
  <div id="friends">
    <navbar></navbar>
    <div class="step landing__section" style="background-color: #f7f7f7">
      <div class="page">
        <div class="container mt-5">
          <div class="page__inner">
            <profile-menu :header="header"></profile-menu>
            <div class="page__main">
              <search-friends></search-friends>
              <friends-menu v-if="id === $store.state.authUser.id"></friends-menu>
              <hr/>
              <friends-list :header="header" :profiles="responseData.friends"
                            @reLoad="createGetRequest(`/profile/${id}/friends/`)"></friends-list>
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
import SearchFriends from "../../components/Profile/SearchFriends";
import FriendsMenu from "../../components/Profile/FriendsMenu";
import FriendsList from "../../components/Profile/FriendsList";
import {requestsMixin} from "../../components/mixins/requestsMixin";
import {redirect} from "../../components/mixins/redirect";

export default {
  name: "Friends",

  components: {
    Navbar, ProfileMenu, SearchFriends, FriendsMenu, FriendsList
  },

  data() {
    return {
      header: 'Друзья'
    }
  },

  props: {
    id: Number
  },

  created() {
    this.createGetRequest(`/profile/${String(this.id)}/friends/`)
  },

  mixins: [requestsMixin, redirect],
}
</script>

<style scoped>

</style>