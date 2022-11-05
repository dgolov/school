<template>
  <div class="cabinet-page">
    <div class="container">
      <button @click="openProfileMenu" class="cabinet-menu-button">МЕНЮ ЛИЧНОГО КАБИНЕТА</button>
      <div class="row">
        <profile-menu :header="header"></profile-menu>
        <friends-list :header="header" :profiles="responseData.friends"
                      @reLoad="createGetRequest(`/profile/${id}/friends/`)"></friends-list>
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
import SearchFriends from "../../components/Profile/SearchFriends";
import FriendsMenu from "../../components/Profile/FriendsMenu";
import FriendsList from "../../components/Profile/FriendsList";
import {requestsMixin} from "../../components/mixins/requestsMixin";
import {redirect} from "../../components/mixins/redirect";
import {openMenu} from "../../components/mixins/openMenu";

export default {
  title: 'Академия будущего | Личный кабинет',
  name: "Friends",

  components: {
    Navbar, ProfileMenu, SearchFriends, FriendsMenu, FriendsList
  },

  data() {
    return {
      header: 'Friends'
    }
  },

  props: {
    id: Number
  },

  created() {
    this.createGetRequest(`/profile/${String(this.id)}/friends/`)
  },

  mixins: [
      requestsMixin, redirect, openMenu
  ],
}
</script>

<style scoped>

</style>