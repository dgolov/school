<template>
  <div id="course_single">
    <navbar></navbar>
    <div class="first-section">
      <div class="step course__section center">
        <div class="container">
          <div class="row mt-5">
            <div class="col-md-6">
              <img :src="course.poster" class="my-4 poster">
            </div>
            <div class="col-md-6 mt-5">
              <p class="left-align">Курс</p>
              <h1>{{ course.name }}</h1>
              <h5>Преподаватель:
                <a href="#">
                  {{ course.teacher.last_name }} {{ course.teacher.first_name }} {{ course.teacher.middle_name }}
                </a>
              </h5>
              <h4>Стоимость обучения: <span class="system-color">{{ course.price }}</span> рублей.</h4>
              <button class="button button__accent buy_button">Записаться на курс</button>
            </div>
          </div>
        </div>
      </div>
      <div class="course__section">
        <div class="container my-5">
          <p class="left-align">{{ course.description }}</p>
        </div>
      </div>
      <how-going></how-going>
      <div class="course__section">
        <div class="container pb-5">
          <h2>Программа курса:</h2>
          <div class="accordion accordion-flush" id="accordionFlushExample">
            <lessons :course="course"></lessons>
          </div>
        </div>
      </div>
    </div>
    <course-form></course-form>
  </div>
</template>

<script>
import Navbar from "../components/Navbar";
import CourseForm from "../components/Course/CourseForm";
import HowGoing from "../components/Course/HowGoing";
import Lessons from "../components/Course/Lessons";
import axios from "axios";

export default {
  name: "EducationSingle",

  props: {
    id: Number
  },

  components: {Lessons, HowGoing, CourseForm, Navbar},

  data() {
    return {
      course: {}
    }
  },

  created() {
    this.loadCourse()
  },

  methods: {
    async loadCourse() {
      await axios
          .get(`${this.$store.getters.getServerUrl}/courses/${this.id}`)
          .then(response => (this.course = response.data))
    }
  }
}
</script>

<style scoped>
.first-section {
  padding-top: 24pt;
}

.poster {
  width: 300px;
  border-radius: 5%;
}

.buy_button {
  display: block;
  margin: 30px auto
}
</style>