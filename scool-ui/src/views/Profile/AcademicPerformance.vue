<template>
  <div id="academic-performance">
    <navbar></navbar>
    <div class="step landing__section past-events" style="background-color: #f7f7f7">
      <div class="page">
        <div class="container mt-1">
          <div class="page__inner">
            <profile-menu :header="header"></profile-menu>
            <div class="page__main">
              <button v-if="addButton" class="gray-button" @click="addToTimeTable">Поставить оценку</button>
              <button v-if="cancelButton" class="red-button" @click="cancelAdd">Отмена</button>
              <label v-if="showAddCourse">Выберите курс</label>
              <select v-if="showAddCourse" v-model="selectedCourse">
                <option disabled value="">Выберите курс</option>
                <option v-for="course in courseList" :value="course">{{course.name}}</option>
              </select>
              <label v-if="selectedCourse">Выберите тему урока</label>
              <select v-model="lessonId" v-if="selectedCourse">
                <option disabled value="">Выберите урок</option>
                <option v-for="lesson in selectedCourse.lessons" :value="lesson.id">{{lesson.theme}}</option>
              </select>
              <label v-if="lessonId">Выберите студента</label>
              <select v-if="lessonId" v-model="student">
                <option disabled value="">Выберите студента</option>
                <option v-for="student in selectedCourse.students" :value="student.id">
                  {{ student.first_name }} {{ student.last_name }}
                </option>
              </select>
              <label v-if="student">Выберите оценку</label>
              <select v-model="grade" v-if="student">
                <option disabled value="">Выберите оценку</option>
                <option v-for="number in 10" :value="number">{{ number }}</option>
              </select>
              <label v-if="student">Выберите тип оценки</label>
              <select v-model="gradeType" v-if="grade">
                <option disabled value="">Выберите тип оценки</option>
                <option :value="'homework'">Домашняя работа</option>
                <option :value="'classwork'">Классная работа</option>
                <option :value="'test'">Контрольная работа</option>
                <option :value="'examination'">Экзамен</option>
              </select>
              <button v-if="gradeType" class="gray-button" @click="sendGrade">Поставить оценку</button>
              <div class="row">
                <div class="w-25"><h5 class="system-color">Дата</h5></div>
                <div class="w-50"><h5 class="system-color">Тема урока</h5></div>
                <div class="w-25"><h5 class="system-color">Оценка</h5></div>
              </div>
              <hr class="mb-4"/>
              <div v-for="performance in responseData" :class="setClassList(performance.grade)" :id="performance.id">
                <div class="row">
                  <div class="w-25">
                    <p class="date">{{ performance.date }}</p>
                  </div>
                  <div class="w-50">
                    <p class="small_text">Курс: <a href="">{{ performance.lesson.course.name }}</a></p>
                    <p>{{ performance.lesson.theme }}</p>
                  </div>
                  <div class="w-25">
                    <p class="small_text pt-2">{{ getTypeGrade(performance.type_grade) }}</p>
                    <p><b>{{ performance.grade }}</b>
                      <a v-if="$store.state.profileInfo.user_group === 'teacher'" href=""
                         @click="goTo('Profile', {id: performance.student.id})">
                        ({{ performance.student.first_name }} {{ performance.student.last_name }})
                      </a></p>
                  </div>
                </div>
              </div>
              <h6 v-if="responseData.length === 0" class="mt-5">{{ nullText }}</h6>
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
import {friendMixin} from "../../components/mixins/friendMixin";
import axios from "axios";

export default {
  title: 'Академия будущего | Личный кабинет',
  name: "AcademicPerformance",

  data() {
    return {
      header: 'Успеваемость',
      classSuccess: 'success',
      classNormal: 'normal',
      classBad: 'bad',
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
    }
  },

  components: {
    Navbar, ProfileMenu
  },

  mixins: [requestsMixin, redirect],

  created() {
    this.createGetRequest('/performance/')
    if (this.$store.state.profileInfo.user_group === 'student') {
      this.nullText = "Вы пока еще не получили ни одной оценки";
    } else if (this.$store.state.profileInfo.user_group === 'teacher') {
      this.nullText = "Вы пока еще не поставили ни одной оценки";
      this.addButton = true;
      this.courseList = this.$store.state.profileInfo.courses
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
      if (url.indexOf('http://127.0.0.1:8000') === -1) {
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

    getTypeGrade(type_grade) {
      switch (type_grade) {
        case ('homework'): {
          return 'Домашняя работа'
        }
        case ('classwork'): {
          return 'Классная работа'
        }
        case ('test'): {
          return 'Контрольная работа'
        }
        case ('examination'): {
          return 'Экзамен'
        }
      }
    },

    async sendGrade() {
      const data = {
        "student": this.student,
        "lesson": this.lessonId,
        "grade": this.grade,
        "type_grade": this.gradeType,
        "late": false,
        "absent": false
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
              // Если 403 ошибка - токен просрочен, обновляем его и заново запрашиваем данные
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
.success {
  background-color: #bae5c6;
}

.normal {
  background-color: #f7f1d0;
}

.bad {
  background-color: #ffd6d6;
}

.small_text {
  color: gray;
  font-size: 12px;
  margin: 0;
}

.date {
  margin-top: 7px;
}

.main-section {
  background-color: #f7f7f7;
}
</style>