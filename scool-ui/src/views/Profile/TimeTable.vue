<template>
  <div id="profile">
    <div class="cabinet-page">
      <div class="container">
        <button @click="openProfileMenu" class="cabinet-menu-button">МЕНЮ ЛИЧНОГО КАБИНЕТА</button>
        <div class="row">
          <profile-menu :header="header"></profile-menu>
          <div v-if="isAllLoaded" class="col-xl-10 col-lg-9">
            <div class="cabinet-content">
              <FullCalendar :options="calendarOptions" />
            </div>
          </div>
          <div v-if="isAllLoaded" class="col-xl-2 col-lg-3"></div>
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
import {getDateTime} from "../../components/mixins/getDateTime";
import DatePicker from "vue2-datepicker";
import axios from "axios";
import {openMenu} from "../../components/mixins/openMenu";

import '@fullcalendar/core/vdom'
import FullCalendar from '@fullcalendar/vue'
import ruLocale from '@fullcalendar/core/locales/ru'
import dayGridPlugin from '@fullcalendar/daygrid'
import listPlugin from '@fullcalendar/list'
import interactionPlugin from '@fullcalendar/interaction'


export default {
  title: 'Академия будущего | Личный кабинет',
  name: "TimeTable",

  components: {
    Navbar,
    ProfileMenu,
    DatePicker,
    FullCalendar
  },

  data(){
    return {
      header: 'TimeTable',
      defaultClassList: "row row_list pt-4 ",
      finished: 'finished',
      courseList: [],
      groupList: [],
      showAddGroup: false,
      showAddCourse: false,
      addButton: false,
      cancelButton: false,
      selectedCourse: false,
      isAllLoaded: false,
      groupId: 0,
      lessonId: 0,
      date: '',
      calendarOptions: {
        plugins: [ dayGridPlugin, interactionPlugin, listPlugin ],
        initialView: 'listWeek',
        headerToolbar: {
          left: "prev,next today",
          center: 'title',
          right: 'dayGridMonth,listWeek',
        },
        weekends: true,
        events: [
        ],
        locale: ruLocale,
        select: (arg) => {
          console.log(arg.start)
        }
      }
    }
  },

  mixins: [
      requestsMixin, redirect, getDateTime, openMenu
  ],

  created() {
    this.loadEvents()
    if (this.$store.state.profileInfo.user_group !== 'student') {
      this.addButton = true;
      this.courseList = this.$store.state.profileInfo.courses;
      this.groupList = this.$store.state.profileInfo.group_list;
    }
  },

  methods: {
    setClassList(isFinished) {
      let classList = this.defaultClassList;
      if (isFinished) {
        classList += this.finished;
      }
      return classList
    },

    async loadEvents() {
      await this.createGetRequest('/timetable/');
      if (this.responseData) {
        for (let event of this.responseData) {
          let eventDate = Date.parse(event.date);
          this.calendarOptions.events.push({
            title: event.group.name + ' ' + event.lesson.theme,
            date: eventDate,
            url: 'my-courses/' + event.lesson.course.id + '/lesson/' + event.lesson.id
          })
        }
      }
      this.isAllLoaded = true;
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
      this.date = '';
    },
    //
    // async sendData() {
    //   let data = {
    //     "date": this.date,
    //     "lesson": this.lessonId,
    //     "group": this.groupId
    //   }
    //   const axiosInstance = axios.create(this.base);
    //   await axiosInstance({
    //     url: `/timetable/`,
    //     method: "post",
    //     data: data
    //   })
    //       .then(() => {
    //         this.cancelAdd()
    //         this.createGetRequest('/timetable/')
    //       })
    //       .catch((error) => {
    //         if (error.request.status === 401) {
    //           // Если 401 ошибка - токен просрочен, обновляем его и заново запрашиваем данные
    //           this.refreshToken();
    //         } else {
    //           console.log(error.request);
    //         }
    //       })
    // },
  },
}
</script>

<style scoped>
</style>