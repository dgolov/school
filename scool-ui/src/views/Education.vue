<template>
  <div id="education">
    <navbar></navbar>
    <div class="step landing__section landing__section_white">
      <div class="page">
        <div class="container mt-1">
          <h1 class="center mb-4">Программы обучения</h1>
          <div class="page__inner">
            <div class="page__menu">
              <h3>Направления</h3>
              <hr>
              <education-menu></education-menu>
            </div>
            <div class="page__main">
              <form>
                <input type='text' placeholder="Поиск">
              </form>
              <div v-for="course in listCourses" :key="course.id" class="row item_course">
                <div class="col-md-8">
                  <h4 class="left-align"><a href="#" @click="goTo(course.id)">{{ course.name }}</a></h4>
                  <h6 class="left-align">{{ course.category.name }}</h6>
                </div>
                <div class="col-md-4 left-align pt-4 system-color">
                  <div><a href="#" @click="goTo(course.id)">Подробнее о курсе</a></div>
                  <div><a href="#">Записаться на курс</a></div>
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
import Navbar from "../components/Navbar";
import EducationMenu from "../components/Course/EducationMenu";
import EducationSingle from "./EducationSingle";
import axios from "axios";

export default {
  name: "Education",

  data() {
    return {
      listCourses: []
    }
  },

  components: {EducationMenu, Navbar},

  created() {
    this.loadListCourses()
  },

  methods: {
    async loadListCourses() {
      await axios
          .get(`${this.$store.getters.getServerUrl}/courses/`)
          .then(response => (this.listCourses = response.data));
    },

    goTo(id) {
      this.$router.push({name: 'EducationSingle', params: {'id': id}})
    },
  },
}
</script>

<style scoped>
.landing__section_white {
  background-color: #f7f7f7;
}

.item_course {
  border-bottom: 2px solid #f7f7f7;
  padding-bottom: 10px;
}
</style>