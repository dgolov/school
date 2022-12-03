<template>
  <div class="cabinet-page">
    <div class="container">
      <button @click="openProfileMenu" class="cabinet-menu-button">МЕНЮ ЛИЧНОГО КАБИНЕТА</button>
      <div class="row">
        <profile-menu :header="header"></profile-menu>
        <div class="col-xl-10 col-lg-9">
          <div class="cabinet-content">
            <div class="course">
              <div class="top-text">
                <a href="#">Назад</a>
                {{ responseData[0].course.name }}
              </div>
              <div class="tbl">
                <table>
                  <tr>
                    <td>Дата начала:</td>
                    <td v-if="responseData[0].course.start_date">{{ responseData[0].course.start_date }}</td>
                    <td v-else>Не указано</td>
                  </tr>
                  <tr>
                    <td>Дата завершения:</td>
                    <td v-if="responseData[0].course.end_date">{{ responseData[0].course.end_date }}</td>
                    <td v-else>Не указано</td>
                  </tr>
                </table>
              </div>
              <div class="info">
                <div class="name">
                  Содержание курса:
                </div>
                <p>{{ responseData[0].course.description }}</p>
                <ul>
                  <li v-for="lesson in responseData">
                    <a href="#" @click="goToLesson(responseData[0].course.id, lesson.id)" class="lesson-link">
                      {{ lesson.theme }}
                    </a>
                  </li>
                </ul>
              </div>
            </div>
          </div>
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
import CourseInfo from "../../components/Course/CourseInfo";
import {requestsMixin} from "../../components/mixins/requestsMixin";
import {redirect} from "../../components/mixins/redirect";
import {openMenu} from "../../components/mixins/openMenu";
import ProfileMenu from "../../components/Profile/ProfileMenu";

export default {
  title: 'Академия будущего | Обучение',
  name: "CourseSingle",

  components: {
    Navbar, CourseInfo, ProfileMenu
  },

  props: {
    id: String,
    header: 'MyCourses',
  },

  mixins: [
      requestsMixin, redirect, openMenu
  ],

  data() {
    return {
      course: {}
    }
  },

  created() {
    this.createGetRequest(`/courses/${this.id}/lessons/`)
  },

  methods: {
    goToLesson(courseId, lessonId) {
      this.$router.push({name: 'Lesson', params: {courseId: courseId, lessonId: lessonId}})
    }
  },
}
</script>

<style scoped>
.course {
  padding-top: 24pt;
}

.course-poster {
  width: 300px;
  border-radius: 5%;
}

.lesson-link {
  text-decoration: none;
}
</style>