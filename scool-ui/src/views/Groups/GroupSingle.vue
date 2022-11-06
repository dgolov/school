<template>
  <div class="cabinet-page">
    <div class="container">
      <button @click="openProfileMenu" class="cabinet-menu-button">МЕНЮ ЛИЧНОГО КАБИНЕТА</button>
      <div class="row">
        <profile-menu :header="header"></profile-menu>
        <div v-if="isLoaded" class="col-xl-10 col-lg-9">
          <div class="cabinet-content">
            <div class="user-info">
              <div class="top-info">
                <div>
                  <div class="name">
                    <span>{{ responseData.name }}</span>
                  </div>
                  <div class="counts">
                    <div class="count">
                      <span>{{ responseData.students.length }}</span>
                      Студенты
                    </div>
                    <div class="count">
                      <span>{{ responseData.teachers.length }}</span>
                      Преподаватели
                    </div>
                    <div class="count">
                      <span>0</span>
                      Фотографии
                    </div>
                  </div>
                </div>
              </div>
              <div class="item">
                <p>Описание:</p>
                <div class="text" v-if="responseData.description">
                  {{ responseData.description }}
                </div>
                <div class="text" v-else>
                  Отсутсвует
                </div>
              </div>
            </div>
            <div class="users">
              <div class="flex">
                <div class="top-text">
                  Студенты <span>{{ responseData.students.length }}</span>
                </div>
                <a href="#" class="top-link" v-if="responseData.students.length > 9 ">Все студенты</a>
              </div>
              <div class="flex">
                <div class="item" v-for="student in responseData.students.slice(0, 9)">
                  <img v-if="student.avatar" class="profile-avatar left"
                       :src="`${student.avatar.image}`"
                       @click="goTo('Profile', {id: student.id})">
                  <img v-else src="../../assets/images/avatars/mike2.jpeg"
                       class="profile-avatar left"
                       @click="goTo('Profile', {id: student.id})">
                  <p @click="goTo('Profile', {id: student.id})">
                    {{ student.first_name }} {{ student.last_name }}
                  </p>
                </div>
              </div>
            </div>
            <div class="teachers">
              <div class="flex">
                <div class="top-text">
                  Преподаватели <span>{{ responseData.teachers.length }}</span>
                </div>
                <a href="#" class="top-link" v-if="responseData.teachers.length > 9 ">Все преподаватели</a>
              </div>
              <div class="flex">
                <div class="item" v-for="teacher in responseData.teachers.slice(0, 9)">
                  <img v-if="teacher.avatar" class="profile-avatar left"
                       :src="`${teacher.avatar.image}`"
                       @click="goTo('Profile', {id: teacher.id})">
                  <img v-else src="../../assets/images/avatars/mike2.jpeg"
                       class="profile-avatar left" @click="goTo('Profile', {id: teacher.id})">
                  <p @click="goTo('Profile', {id: teacher.id})">
                    {{ teacher.first_name }} {{ teacher.last_name }}
                  </p>
                </div>
              </div>
            </div>
          </div>
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
import GroupSearch from "../../components/Groups/GroupSearch";
import SingleGroupHeader from "../../components/Groups/SingleGroupHeader";
import ProfilesList from "../../components/Profile/ProfilesList";
import {requestsMixin} from "../../components/mixins/requestsMixin";
import {redirect} from "../../components/mixins/redirect";
import {friendMixin} from "../../components/mixins/friendMixin";
import {openMenu} from "../../components/mixins/openMenu";

export default {
  title: 'Академия будущего | Личный кабинет',
  name: "GroupSingle",

  components: {
    Navbar, ProfileMenu, GroupSearch, SingleGroupHeader, ProfilesList,
  },

  data() {
    return {
      header: 'Groups'
    }
  },

  props: {
    id: String,
  },

  mixins: [
      requestsMixin, redirect, friendMixin, openMenu
  ],

  created() {
    this.createGetRequest(`/groups/${this.id}/`)
  },
}
</script>


<style scoped>
.profile-avatar {
  display: block;
  width: 50%;
  border: 0;
  border-radius: 50%;
  margin: 0 auto;
  text-align: center;
}
</style>