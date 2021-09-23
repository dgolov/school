<template>
  <div id="search">
    <navbar></navbar>
    <div class="step landing__section main-section">
      <div class="page">
        <div class="container mt-5">
          <div class="page__inner">
            <profile-menu :header="header"></profile-menu>
            <div class="page__main">
              <div class="row">
                <div class="col-md-9">
                  <form>
                    <input type='text' placeholder="Поиск" class="w-100">
                  </form>
                </div>
                <div class="col-md-3">
                  <button class="grey-button filter-button">Фильтр</button>
                </div>
              </div>
              <div class="row my-3">
                <div class="col-md-6">
                  <a href="#" @click="getStudents()">Студенты</a>
                </div>
                <div class="col-md-6">
                  <a href="#" @click="getTeachers()">Преподаватели</a>
                </div>
              </div>
              <hr/>
              <profiles-list :profiles="responseData"></profiles-list>
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
import ProfilesList from "../../components/Profile/ProfilesList";
import {requestsMixin} from "../../components/mixins/requestsMixin";
import {redirect} from "../../components/mixins/redirect";

export default {
  name: "Search",

  components: {
    ProfilesList,
    Navbar, ProfileMenu
  },

  data() {
    return {
      header: 'Поиск',
    }
  },

  created() {
    this.createGetRequest('/students/')
  },

  mixins: [requestsMixin, redirect],

  methods: {
    getTeachers() {
      this.createGetRequest('/teachers/')
    },
    getStudents() {
      this.createGetRequest('/students/')
    }
  },
}
</script>


<style scoped>
.filter-button {
  height: 68%;
}
</style>