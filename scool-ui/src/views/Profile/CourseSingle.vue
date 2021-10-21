<template>
  <div id="single-course">
    <navbar></navbar>
    <div class="course">
      <course-info v-if="responseData" :course="responseData[0].course"></course-info>
      <div class="course__section">
        <div class="container pb-1">
          <h2 class="my-4 system-color">Программа курса:</h2>
          <p>Здесь собраны все доступные уроки с пожизненным доступом к видео и материалам с прошедших вебинаров</p>
          <hr/>
          <ol class="lesson-list">
            <li v-if="responseData" v-for="lesson in responseData" class="py-3">
              <a v-if="lesson.is_active" href="#" @click="goToLesson(lesson.course.id, lesson.id)">{{lesson.theme}}</a>
              <p v-else class="no-active" style="margin: 0;">{{lesson.theme}} (Урок недоступен)</p>
            </li>
          </ol>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Navbar from "../../components/Navbar";
import CourseInfo from "../../components/Course/CourseInfo";
import {requestsMixin} from "../../components/mixins/requestsMixin";
import {redirect} from "../../components/mixins/redirect";

export default {
  name: "CourseSingle",

  components: {
    Navbar, CourseInfo
  },

  props: {
    id: String
  },

  mixins: [requestsMixin, redirect],

  data() {
    return {
      course: {}
    }
  },

  created() {
    this.createGetRequest(`/courses/${this.id}/lessons/`)
  },

  methods: {
    goToLesson(courseId, lessonId) {
      this.$router.push({name: 'Lesson', params: {courseId: courseId, lessonId: lessonId}})
    }
  },
}
</script>

<style scoped>
.course {
  padding-top: 24pt;
}

.course-poster {
  width: 300px;
  border-radius: 5%;
}

.lesson-list {
  font-size: 20px;
}
</style>