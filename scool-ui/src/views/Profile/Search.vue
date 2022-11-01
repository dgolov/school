<template>
  <div class="cabinet-page">
    <div class="container">
      <button class="cabinet-menu-button">МЕНЮ ЛИЧНОГО КАБИНЕТА</button>
      <div class="row">
        <profile-menu :header="header"></profile-menu>
        <div class="col-xl-10 col-lg-9">
          <div class="row mb-5 mt-3">
            <div class="col-md-6 px-5">
              <a href="#" class="user-menu" @click="getStudents()">Студенты</a>
            </div>
            <div class="col-md-6 px-5">
              <a href="#" class="user-menu" @click="getTeachers()">Преподаватели</a>
            </div>
          </div>
          <profiles-list :profiles="responseData" @reLoad="reloadList()"></profiles-list>
        </div>
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
import ProfilesList from "../../components/Profile/ProfilesList";
import {requestsMixin} from "../../components/mixins/requestsMixin";
import {redirect} from "../../components/mixins/redirect";

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

  mixins: [requestsMixin, redirect],

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