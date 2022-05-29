<template>
  <div>
    <div v-for="course in listCourses" :key="course.id" class="col-md-5 course-block mx-2 my-2"
         v-if="course.is_active && course.category.age_group === age_group && course.in_main_page"
         :style="{ 'background-color': '#' + course.color_hex }"
         @click="goTo(course)">
      <h6 class="left-align my-1" style="display: inline; float: left;">
        {{ typesRus[course.education_type] }}</h6>
      <h6 class="right-align" style="display: inline; float: right;">{{ course.category.name }}</h6>
      <div class="course-title mt-5">
        <h3 class="left-align bold mt-3 mb-1" @click="goTo(course)">{{ course.name }}</h3>
      </div>
      <div class="course-desc">
        <p v-if="course.description.length > 120" class="mt-4">{{
            course.description.substr(0, 120)
          }}...</p>
        <p v-else class="mt-4">{{ course.description }}</p>
      </div>
      <p class="mt-3" style="color: gray; font-size: 11px;">Длительность: {{ course.duration }}
        месяцев</p>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "course-list",

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

    goTo(course) {
      if (course.category.name !== 'Шахматы') {
        this.$router.push({name: 'EducationSingle', params: {'id': course.id}})
      } else {
        this.$router.push({name: 'ChessSingle', params: {'id': course.id}})
      }
    },
  }
}
</script>

<style scoped>
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