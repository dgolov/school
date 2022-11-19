<template>
  <div class="cabinet-page">
    <div class="container">
      <button @click="openProfileMenu" class="cabinet-menu-button">МЕНЮ ЛИЧНОГО КАБИНЕТА</button>
      <div class="row">
        <profile-menu :header="header"></profile-menu>
        <div v-if="isLoaded" class="col-xl-10 col-lg-9">
          <profiles-list :profiles="responseData" @reLoad="reloadList()"></profiles-list>
        </div>
        <div v-if="isLoaded" class="col-xl-2 col-lg-3"></div>
        <loader v-else object="#63a9da" color1="#ffffff" color2="#17fd3d" size="5" speed="2" bg="#343a40"
                objectbg="#999793" opacity="80" disableScrolling="false" name="spinning"></loader>
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
import ProfilesList from "../../components/Profile/ProfilesList";
import {requestsMixin} from "../../components/mixins/requestsMixin";
import {redirect} from "../../components/mixins/redirect";
import {openMenu} from "../../components/mixins/openMenu";

export default {
  title: 'Академия будущего | Личный кабинет',
  name: "Search",

  components: {
    ProfilesList,
    Navbar, ProfileMenu
  },

  data() {
    return {
      header: 'Search',
      searchUserGroup: ''
    }
  },

  created() {
    this.createGetRequest('/students/');
    this.searchUserGroup = 'students';
  },

  mixins: [
      requestsMixin, redirect, openMenu
  ],

  methods: {
    getTeachers() {
      this.createGetRequest('/teachers/');
      this.searchUserGroup = 'teachers';
    },
    getStudents() {
      this.createGetRequest('/students/');
      this.searchUserGroup = 'students';
    },
    reloadList() {
      if(this.searchUserGroup === 'students'){
        this.createGetRequest('/students/');
      } else {
        this.createGetRequest('/teachers/');
      }
    },
  },
}
</script>


<style scoped>
.user-menu {
  text-decoration: none;
}
</style>