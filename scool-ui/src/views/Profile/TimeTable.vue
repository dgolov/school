<template>
<div id="timetable">
  <navbar></navbar>
  <div class="step landing__section main-section">
    <div class="page">
      <div class="container mt-1">
        <div class="page__inner">
          <profile-menu :header="header"></profile-menu>
          <div class="page__main">
            <button v-if="addButton" class="gray-button" @click="addToTimeTable">Добавить запись в расписание</button>
            <button v-if="cancelButton" class="red-button" @click="cancelAdd">Отмена</button>
            <label v-if="showAddGroup">Выберите группу</label>
            <select v-if="showAddGroup" v-model="groupId">
              <option disabled value="">Выберите группу</option>
              <option v-for="group in groupList" :value="group.id">{{group.name}}</option>
            </select>
            <label v-if="groupId">Выберите курс</label>
            <select v-if="groupId" v-model="selectedCourse">
              <option disabled value="">Выберите курс</option>
              <option v-for="course in courseList" :value="course">{{course.name}}</option>
            </select>
            <label v-if="selectedCourse">Выберите тему урока</label>
            <select v-model="lessonId" v-if="selectedCourse">
              <option disabled value="">Выберите урок</option>
              <option v-for="lesson in selectedCourse.lessons" :value="lesson.id">{{lesson.theme}}</option>
            </select>
            <label v-if="lessonId">Укажите дату урока</label>
            <date-picker v-if="lessonId" v-model="date" style="width: 100%;" type="datetime"></date-picker>
            <button v-if="date" class="gray-button" @click="sendData">Добавить</button>
            <div class="row">
              <div class="w-25"><h5 class="system-color">Дата и время</h5></div>
              <div class="w-50"><h5 class="system-color">Тема урока</h5></div>
              <div class="w-25"><h5 class="system-color">Название курса</h5></div>
            </div>
            <hr class="mb-4"/>
            <div v-for="timeTable in responseData" :class="setClassList(timeTable.is_finished)" :id="timeTable.id">
              <div class="w-25">
                <p>{{ reformatDateTime(timeTable.date) }}</p>
              </div>
              <div class="w-50">
                <p>{{ timeTable.lesson.theme }}</p>
              </div>
              <div class="w-25">
                <a href="#" @click="goTo('CourseSingle', {id: timeTable.lesson.course.id})">
                  {{ timeTable.lesson.course.name }}
                </a>
              </div>
            </div>
            <h6 v-if="responseData.length === 0" class="mt-5">Записи в расписании отсутствуют</h6>
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
import {getDateTime} from "../../components/mixins/getDateTime";
import DatePicker from "vue2-datepicker";
import axios from "axios";

export default {
  name: "TimeTable",

  components: {
    Navbar,
    ProfileMenu,
    DatePicker
  },

  data(){
    return {
      header: 'Расписание',
      defaultClassList: "row row_list pt-4 ",
      finished: 'finished',
      courseList: [],
      groupList: [],
      showAddGroup: false,
      showAddCourse: false,
      addButton: false,
      cancelButton: false,
      selectedCourse: false,
      groupId: 0,
      lessonId: 0,
      date: '',
    }
  },

  mixins: [requestsMixin, redirect, getDateTime],

  created() {
    this.createGetRequest('/timetable/')
    if (this.$store.state.profileInfo.user_group !== 'student') {
      this.addButton = true;
      this.courseList = this.$store.state.profileInfo.courses
      this.groupList = this.$store.state.profileInfo.group_list
    }
  },

  methods: {
    setClassList(isFinished) {
      let classList = this.defaultClassList
      if (isFinished) {
        classList += this.finished
      }
      return classList
    },

    addToTimeTable() {
      if (this.$store.state.profileInfo.user_qroup === 'student'){
        return false;
      }
      this.cancelButton = true;
      this.showAddGroup = true;
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
      this.date = ''
    },

    async sendData() {
      let data = {
        "date": this.date,
        "lesson": this.lessonId,
        "group": this.groupId
      }
      const axiosInstance = axios.create(this.base);
      await axiosInstance({
        url: `/timetable/`,
        method: "post",
        data: data
      })
          .then(() => {
            this.cancelAdd()
            this.createGetRequest('/timetable/')
          })
          .catch((error) => {
            if (error.request.status === 401) {
              // Если 401 ошибка - токен просрочен, обновляем его и заново запрашиваем данные
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
.finished {
  background-color: #e5ebf1;
}
</style>