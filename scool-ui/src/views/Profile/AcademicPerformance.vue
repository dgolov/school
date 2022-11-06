<template>
  <div class="cabinet-page">
    <div class="container">
      <button @click="openProfileMenu" class="cabinet-menu-button">МЕНЮ ЛИЧНОГО КАБИНЕТА</button>
      <div class="row">
        <profile-menu :header="header"></profile-menu>
        <div v-if="isLoaded" class="col-xl-10 col-lg-9">
          <div class="cabinet-content">
            <div class="results">
              <div class="top-text">
                Успеваемость
              </div>
              <table>
                <thead>
                <tr>
                  <td>Название курса:</td>
                  <td>Пройдено уроков:</td>
                  <td>Средний балл:</td>
                  <td></td>
                </tr>
                </thead>
                <tbody>
                <template v-for="course in courseList">
                  <tr>
                    <td>
                      <div class="name">
                        <div>{{ course.name }}</div>
                      </div>
                    </td>
                    <td>
                      <div class="slider">
                        <p>8 из 12</p>
                        <div><span style="width: 66%;"></span></div>
                      </div>
                    </td>
                    <td>
                      <div class="prog color1">
                        <span>4</span>
                      </div>
                    </td>
                    <td>
                      <a class="link" @click="openAcademicPerformance"></a>
                    </td>
                  </tr>
                  <tr class="info">
                    <td colspan="4">
                      <table>
                        <thead>
                        <tr>
                          <td>Дата</td>
                          <td>Тема урока</td>
                          <td>Оценка</td>
                        </tr>
                        </thead>
                        <tbody>
                          <template v-for="performance in responseData">
                            <tr v-if="performance.lesson.course.id === course.id">
                              <td class="w-30">{{ performance.date }}</td>
                              <td class="w-50">{{ performance.lesson.theme }}</td>
                              <td :class="setClassList(performance.grade)">{{ performance.grade }}</td>
                            </tr>
                          </template>
                        </tbody>
                      </table>
                    </td>
                  </tr>
                </template>
                </tbody>
              </table>
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
import {requestsMixin} from "../../components/mixins/requestsMixin";
import {redirect} from "../../components/mixins/redirect";
import axios from "axios";
import {openMenu} from "../../components/mixins/openMenu";

export default {
  title: 'Академия будущего | Личный кабинет',
  name: "AcademicPerformance",

  data() {
    return {
      header: 'AcademicPerformance',
      classSuccess: 'w-20 color1',
      classNormal: 'w-20 color3',
      classBad: 'w-20 color2',
      defaultClassList: 'row row_list pt-4 ',
      nullText: '',
      courseList: [],
      showAddCourse: false,
      addButton: false,
      cancelButton: false,
      selectedCourse: false,
      lessonId: 0,
      student: 0,
      grade: 0,
      gradeType: '',
      late: false,
      absent: false
    }
  },

  components: {
    Navbar, ProfileMenu
  },

  mixins: [
    requestsMixin, redirect, openMenu
  ],

  created() {
    this.createGetRequest('/performance/')
    this.GetCourses()
    if (this.$store.state.profileInfo.user_group === 'student') {
      this.nullText = "Вы пока еще не получили ни одной оценки";
    } else if (this.$store.state.profileInfo.user_group === 'teacher') {
      this.nullText = "Вы пока еще не поставили ни одной оценки";
      this.addButton = true;
    } else {
      this.nullText = "Оценки отсутствуют";
    }
  },

  methods: {
    setClassList(grade) {
      let classList = this.defaultClassList
      if (grade < 4) {
        classList += this.classBad;
      } else if (grade > 3 && grade < 7) {
        classList += this.classNormal;
      } else if (grade > 6) {
        classList += this.classSuccess;
      }
      return classList
    },

    getImage(url) {
      // Некоторые данные приходят с сервера с абсолютным адресом, некоторые с относительным, вероятно из-за ViewSets
      // Данный метод временно решает эту проблему
      if (url.indexOf('${this.$store.state.backendUrl}') === -1) {
        return `${this.$store.getters.getServerUrl}${url}`
      } else {
        return url
      }
    },

    addToTimeTable() {
      this.showAddCourse = true;
      this.cancelButton = true;
      this.addButton = false;
    },

    cancelAdd() {
      this.cancelButton = false;
      this.showAddGroup = false;
      this.showAddCourse = false;
      this.addButton = true;
      this.selectedCourse = false;
      this.groupId = 0;
      this.lessonId = 0;
      this.student = 0;
      this.grade = 0;
      this.gradeType = '';
      this.date = ''
    },

    openAcademicPerformance() {
      $('.cabinet-page .cabinet-content .results table tbody tr td .link').click(function() {
        $(this).toggleClass('active');
        $(this).parent().parent().toggleClass('active');
        $(this).parent().parent().next('.info').toggle();
      });
    },

    async GetCourses() {
      const axiosInstance = axios.create(this.base);

      await axiosInstance({
        url: "/courses/available/",
        method: "get",
        params: {},
      })
          .then((response) => this.courseList = response.data)
    },

    async sendGrade() {
      const data = {
        "student": this.student,
        "lesson": this.lessonId,
        "grade": this.grade,
        "type_grade": this.gradeType,
        "late": this.late,
        "absent": this.absent
      }
      const axiosInstance = axios.create(this.base);
      await axiosInstance({
        url: `/performance/`,
        method: "post",
        data: data
      })
          .then(() => {
            this.cancelAdd()
            this.createGetRequest('/performance/')
          })
          .catch((error) => {
            if (error.request.status === 401) {
              this.refreshToken();
            } else {
              console.log(error.request);
            }
          })
    },
  },
}
</script>

<style scoped>
</style>