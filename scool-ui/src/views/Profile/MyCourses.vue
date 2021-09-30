<template>
  <div id="my-courses">
    <navbar></navbar>
    <div class="step landing__section main-section">
      <div class="page">
        <div class="container mt-5">
          <div class="page__inner">
            <profile-menu :header="header"></profile-menu>
            <div class="page__main">
              <div v-if="responseData" v-for="course in responseData" class="row course_container">
                <div class="col-md-8">
                  <h4 class="left-align" v-if="course.is_active">
                    <a v-if="course.is_active" href="#" @click="goToCourse(course.id)">{{ course.name }}</a>
                  </h4>
                  <h4 v-else class="left-align no-active">{{ course.name }}</h4>
                  <h6 class="left-align">{{ course.category.name }}</h6>
                </div>
                <div class="col-md-4 left-align pt-4 system-color">
                  <div>
                    <a v-if="course.is_active" href="#" @click="goToCourse(course.id)">Описание курса</a>
                    <p v-else class="no-active">Курс недоступен</p>
                  </div>
                </div>
              </div>
              <h6 v-if="responseData.length === 0" class="mt-5">У вас нет доступных курсов</h6>
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

export default {
  name: "MyCourses",

  data() {
    return {
      header: 'Доступные курсы',
    }
  },

  components: {
    Navbar, ProfileMenu
  },

  mixins: [requestsMixin, redirect],

  created() {
    this.courseList = this.createGetRequest('/courses/available/')
  },

  methods: {
    goToCourse(id) {
      this.$router.push({name: 'CourseSingle', params: {id: id}})
    }
  },
}
</script>


<style scoped>
.course_container {
  border-bottom: 2px solid #f7f7f7;
  padding-bottom: 10px;
}
</style>