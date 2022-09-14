<template>
  <div>
    <navbar></navbar>
    <div class="step landing__section main-section past-events">
      <div class="page">
        <div class="container mt-1">
          <div class="page__inner">
            <profile-menu :header="'Расписание'"></profile-menu>
            <div class="page__main">
              <h2>{{ responseData.lesson.theme }}</h2>
              <hr class="mb-4"/>
              <div class="row mt-4">
                <div class="w-50">Дата</div>
                <div class="w-50">{{ reformatDateTime(responseData.date) }}</div>
              </div>
              <div class="row mt-4">
                <div class="w-50">Курс</div>
                <div class="w-50">
                  <a href="#" @click="goTo('CourseSingle', {id: responseData.lesson.course.id})">
                    {{ responseData.lesson.course.name }}
                  </a>
                </div>
              </div>
              <div class="row mt-4" v-if="responseData.material">
                <div class="w-50">Материал</div>
                <div class="w-50">
                  <a :href="responseData.material" download target="_blank">
                    Скачать
                  </a>
                </div>
              </div>
              <div class="row mt-4" v-if="responseData.material_link">
                <div class="w-50">Ссылка на материалы</div>
                <div class="w-50">
                    <a :href="responseData.material_link" target="_blank">Перейти</a>
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
import DatePicker from "vue2-datepicker";
import {requestsMixin} from "../../components/mixins/requestsMixin";
import {redirect} from "../../components/mixins/redirect";
import {getDateTime} from "../../components/mixins/getDateTime";

export default {
  name: "TimeTableDetail",

  components: {
    Navbar,
    ProfileMenu,
    DatePicker
  },

  props: {
    id: String,
  },

  mixins: [requestsMixin, redirect, getDateTime],

  created() {
    this.createGetRequest(`/timetable/${this.id}`)
    if (this.$store.state.profileInfo.user_group !== 'student') {
      this.addButton = true;
      this.courseList = this.$store.state.profileInfo.courses
      this.groupList = this.$store.state.profileInfo.group_list
    }
  },

  methods: {
    downloadItem (url) {
      window.location.href = url
    }
  }
}
</script>

<style scoped>

</style>