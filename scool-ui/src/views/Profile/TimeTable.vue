<template>
<div id="timetable">
  <navbar></navbar>
  <div class="step landing__section main-section">
    <div class="page">
      <div class="container mt-5">
        <div class="page__inner">
          <profile-menu :header="header"></profile-menu>
          <div class="page__main">
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

export default {
  name: "TimeTable",

  components: {
    Navbar, ProfileMenu
  },

  data(){
    return {
      header: 'Расписание',
      defaultClassList: "row row_list pt-4 ",
      finished: 'finished'
    }
  },

  mixins: [requestsMixin, redirect, getDateTime],

  created() {
    this.createGetRequest('/timetable/')
  },

  methods: {
    setClassList(isFinished) {
      let classList = this.defaultClassList
      if (isFinished) {
        classList += this.finished
      }
      return classList
    },
  },
}
</script>

<style scoped>
.finished {
  background-color: #e5ebf1;
}
</style>