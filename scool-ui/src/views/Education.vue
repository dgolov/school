<template>
  <div id="education">
    <navbar></navbar>
    <div class="step landing__section landing__section_white">
      <div class="page">
        <div class="container mt-1">
          <h1 class="mb-5 bold">Все программы обучения</h1>
          <div class="container mb-4">
            <div class="row groups">
              <div class="col-md-3" id="menu"></div>
              <div class="col-md-3 center" id="children">
                <img src="../assets/images/children.svg" class="group-image">
                <div class="group-text">
                  <button @click="setAgeGroup('children')">Дети</button>
                </div>
              </div>
              <div class="col-md-3 center" id="teens">
                <img src="../assets/images/teens.svg" class="group-image">
                <div class="group-text">
                  <button @click="setAgeGroup('teens')">Подростки</button>
                </div>
              </div>
              <div class="col-md-3 center" id="adults">
                <img src="../assets/images/adults.svg" class="group-image">
                <div class="group-text">
                  <button @click="setAgeGroup('adults')">Взрослые</button>
                </div>
              </div>
            </div>
            <div class="container">
              <div class="row">
                <div class="col-md-3">
                  <h4 class="bold">Уровень сложности</h4>
                  <input type="radio" id="complexityAll" value="complexityAll" v-model="complexity" checked>
                  <label for="complexityAll">Все</label><br>
                  <input type="radio" id="newbie" value="newbie" v-model="complexity">
                  <label for="newbie">Новичок</label><br>
                  <input type="radio" id="user" value="user" v-model="complexity">
                  <label for="user">Пользователь</label><br>
                  <input type="radio" id="professional" value="professional" v-model="complexity">
                  <label for="professional">Провессионал</label><br>
                  <input type="radio" id="cheater" value="cheater" v-model="complexity">
                  <label for="cheater">Читер</label><br>
                  <h4 class="bold">Тип обучения</h4>
                  <input type="radio" id="all" value="all" v-model="education_type" checked>
                  <label for="all">Любой</label><br>
                  <input type="radio" id="profession" value="profession" v-model="education_type">
                  <label for="profession">Профессия</label><br>
                  <input type="radio" id="course" value="course" v-model="education_type">
                  <label for="course">Курс</label><br>
                  <!--                  <h4 class="bold">Длительность</h4>-->
                </div>
                <div class="col-md-9 mt-4">
                  <div class="category-area">
                    <button class="category-button" @click="category_name='all'">Все категории</button>
                  </div>
                  <div v-for="category in categoryList" v-if="category.age_group === age_group" class="category-area">
                    <button class="category-button" @click="category_name=category.name">{{ category.name }}</button>
                  </div>
                  <div class="page__inner mt-4">
                    <div class="page__main">
                      <div v-if="listCourses" class="row">
                        <div v-for="course in listCourses" :key="course.id" class="col-md-5 course-block mx-2 my-2"
                             v-if="course.category.age_group === age_group &&
                             (course.complexity === complexity || complexity === 'complexityAll') &&
                             (course.education_type === education_type || education_type === 'all') &&
                             (course.category.name === category_name || category_name === 'all')"
                             :style="{ 'background-color': '#' + course.color_hex }">
                          <h6 class="left-align my-1" style="display: inline; float: left;">{{ typesRus[course.education_type] }}</h6>
                          <h6 class="right-align" style="display: inline; float: right;">{{ course.category.name }}</h6>
                          <div class="course-title mt-5">
                            <h3 class="left-align bold mt-3 mb-1">
                              <a href="#" @click="goTo(course.id)">{{ course.name }}</a>
                            </h3>
                          </div>
                          <div class="course-desc">
                            <p v-if="course.description.length > 120" class="mt-4">{{ course.description.substr(0, 120) }}...</p>
                            <p v-else class="mt-4">{{ course.description }}</p>
                          </div>
                          <p class="mt-3" style="color: gray; font-size: 11px;">Длительность: {{ course.duration }} месяцев</p>
                        </div>
                      </div>
                    </div>
                  </div>
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
import EducationSingle from "./EducationSingle";
import axios from "axios";

export default {
  name: "Education",

  data() {
    return {
      category_name: 'all',
      complexity: 'complexityAll',
      education_type: 'all',
      age_group: 'children',
      categoryList: [],
      listCourses: [],
      firstDownload: true,
      typesRus: {
        'profession': 'Профессия',
        'course': 'Курс'
      }
    }
  },

  props: {
    category: String,
    ageGroup: String
  },

  components: {Navbar},

  created() {
    console.log(this.category)
    console.log(this.ageGroup)
    if (!this.category) {
      this.category_name = 'all'
    } else {
      this.category_name = this.category
    }
    if (!this.ageGroup) {
      this.age_group = 'children'
    } else {
      this.age_group = this.ageGroup
    }
    this.loadCategoryList();
    this.loadListCourses();
  },

  mounted() {
    this.setAgeGroup(this.age_group)
  },

  methods: {
    async loadCategoryList() {
      await axios
          .get(`${this.$store.getters.getServerUrl}/categories/`)
          .then(response => (this.categoryList = response.data));
    },

    async loadListCourses() {
      await axios
          .get(`${this.$store.getters.getServerUrl}/courses/`)
          .then(response => (this.listCourses = response.data));
    },

    goTo(id) {
      this.$router.push({name: 'EducationSingle', params: {'id': id}})
    },

    setAgeGroup(group) {
      if (!this.firstDownload) {
        this.category_name = 'all'
      } else {
        this.firstDownload = false
      }
      let groups = ['children', 'teens', 'adults'];
      for (let item_group of groups) {
        let item_div = document.getElementById(item_group)
        if (item_group !== group) {
          item_div.classList.remove('group-active')
        } else {
          item_div.classList.add('group-active');
        }
      }
      this.age_group = group;
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

.course-block {
  height: 300px;
  border: none;
  border-radius: 10px;
  padding: 15px;
  box-shadow: 0 0 7px rgba(0, 0, 0, 0.3);
}

.course-block:hover {
  box-shadow: -5px 0 8px 1px rgba(235, 147, 79, 0.6),
  5px 0 8px 1px rgba(99, 169, 218, 0.6);
}

.course-title {
  height: 60px;
}

.course-desc {
  height: 100px;
}
</style>