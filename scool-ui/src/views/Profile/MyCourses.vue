<template>
  <div id="my-courses">
    <div class="cabinet-page">
      <div class="container">
        <button @click="openProfileMenu" class="cabinet-menu-button">МЕНЮ ЛИЧНОГО КАБИНЕТА</button>
        <div class="row">
          <profile-menu :header="header"></profile-menu>
          <div v-if="isLoaded" class="col-xl-10 col-lg-9">
            <div class="cabinet-content">
              <div class="courses">
                <div class="list-name">
                  Доступные курсы
                </div>
                <div v-if="responseData" class="list flex">
                  <div v-for="course in responseData" class="item"
                       style="background: linear-gradient(123.33deg, #B398FF 17.28%, #FFCAE0 73.82%);"
                       @click="goToCourse(course.id)">
                    <!--                    <img src="img/course1.png">-->
                    <div class="flex">
                      <div class="top-text">
                        Курс
                      </div>
                      <div class="top-text">
                        {{ course.category.name }}
                      </div>
                    </div>
                    <div class="text">
                      <span>{{ course.name }}</span>
                      <p v-if="course.description.length <= 150">{{ course.description }}</p>
                      <p v-else>{{ course.description.substr(0, 150) }}...</p>
                    </div>
                    <div class="time">
                      {{ course.duration }} месяцев
                    </div>
                  </div>
                </div>
                <div class="list-name">
                  Другие курсы
                </div>
                <div v-if="allCourses && responseData" class="list flex">
                  <div v-if="isNotAvailableCourse(course)"
                       v-for="course in allCourses"
                       class="item"
                       style="background: linear-gradient(110.82deg, #C6D5FF 3.65%, #7C9CF1 86.46%);">
<!--                    <img src="img/course3.png">-->
                    <div class="flex">
                      <div class="top-text">
                        Курс
                      </div>
                      <div class="top-text">
                        {{ course.category.name }}
                      </div>
                    </div>
                    <div class="text">
                      <span>{{ course.name }}</span>
                      <p v-if="course.description.length <= 150">{{ course.description }}</p>
                      <p v-else>{{ course.description.substr(0, 150) }}...</p>
                    </div>
                    <div class="time">
                      {{ course.duration }} месяцев
                    </div>
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
  </div>
</template>


<script>
import Navbar from "../../components/Navbar";
import ProfileMenu from "../../components/Profile/ProfileMenu";
import {requestsMixin} from "../../components/mixins/requestsMixin";
import {redirect} from "../../components/mixins/redirect";
import axios from "axios";
import {openMenu} from "../../components/mixins/openMenu";

export default {
  title: 'Академия будущего | Личный кабинет',
  name: "MyCourses",

  data() {
    return {
      header: 'MyCourses',
      base: {
        baseURL: this.$store.state.backendUrl,
        headers: {
          Authorization: `Bearer ${this.$store.state.jwt}`,
          "Content-Type": "application/json",
        },
        xhrFields: {
          withCredentials: true,
        },
      },
      allCourses: {},
    }
  },

  components: {
    Navbar, ProfileMenu
  },

  mixins: [
      requestsMixin, redirect, openMenu
  ],

  created() {
    this.createGetRequest('/courses/available/')
    this.GetAllCourses()
  },

  methods: {
    goToCourse(id) {
      this.$router.push({name: 'CourseSingle', params: {id: id}})
    },

    createBackgroundString(color) {
      return `background: linear-gradient(123.33deg, ${color} 17.28%, #FFCAE0 73.82%))`;
    },

    async GetAllCourses(url) {
      const axiosInstance = axios.create(this.base);

      await axiosInstance({
        url: "/courses/",
        method: "get",
        params: {},
      })
          .then((response) => this.allCourses = response.data)
    },

    isNotAvailableCourse(itemCourse) {
      for (let course of this.responseData) {
        if (course.id === itemCourse.id) {
          return false
        }
      }
      return true
    },
  },
}
</script>


<style scoped>
</style>