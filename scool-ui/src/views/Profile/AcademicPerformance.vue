<template>
  <div id="academic-performance">
    <navbar></navbar>
    <div class="step landing__section" style="background-color: #f7f7f7">
      <div class="page">
        <div class="container mt-5">
          <div class="page__inner">
            <profile-menu :header="header"></profile-menu>
            <div class="page__main">
              <div class="row">
                <div class="w-25"><h5 class="system-color">Дата</h5></div>
                <div class="w-50"><h5 class="system-color">Тема урока</h5></div>
                <div class="w-25"><h5 class="system-color">Оценка</h5></div>
              </div>
              <hr class="mb-4"/>
              <div v-for="performance in responseData" :class="setClassList(performance.grade)" :id="performance.id">
                <div class="w-25">
                  <p class="date">{{ performance.date }}</p>
                </div>
                <div class="w-50">
                  <p class="small_text">Курс:
                    <a href="">{{ performance.lesson.course.name }}</a>
                  </p>
                  <p>{{ performance.lesson.theme }}</p>
                </div>
                <div class="w-25">
                  <p class="small_text">{{ performance.type }}</p>
                  <p>{{ performance.grade }}</p>
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

export default {
  name: "AcademicPerformance",

  data() {
    return {
      header: 'Успеваемость',
      classSuccess: 'success',
      classNormal: 'normal',
      classBad: 'bad',
      defaultClassList: 'row row_list pt-4 '
    }
  },

  components: {
    Navbar, ProfileMenu
  },

  mixins: [requestsMixin, redirect],

  created() {
    this.createGetRequest('/performance/')
  },

  methods: {
    setClassList(grade) {
      let classList = this.defaultClassList
      if (grade < 4) {
        classList += this.classBad;
      }
      else if (grade > 3 && grade < 7) {
        classList += this.classNormal;
      }
      else if (grade > 6) {
        classList += this.classSuccess;
      }
      return classList
    }
  }
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