<template>
  <div id="lesson-single">
    <navbar></navbar>
    <div class="lesson past-events">
      <course-info v-if="responseData" :course="responseData.course"></course-info>
      <div class="course__section">
        <div class="container pb-1">
          <div class="course-info">
            <h2 class="my-4 system-color">{{responseData.theme}}</h2>
            <p class="course-text">{{responseData.description}}</p>
          </div>
          <div class="center mt-5">
            <div v-if="responseData.video_slug" class="mb-5 mt-1">
              <img src="../../assets/images/icons/youtube-video-social-media-play_icon-icons.com_59108.png"
                   class="video-image">
              <h3 class="video-header">Онлайн трансляция урока:</h3>
            </div>
            <div v-if="responseData.video_slug" class="mb-4">
              <iframe width="560" height="315" :src="responseData.video_slug"
                      title="YouTube video player" frameborder="0"
                      allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                      allowfullscreen></iframe>
            </div>
            <hr v-if="responseData.materials && responseData.video_slug" />
            <div v-if="responseData.materials" class="mt-5 system-color">
              <img src="../../assets/images/icons/download.png" class="download-button">
              <a href="#" @click="responseData.materials" download class="course-text">Скачать материал к уроку</a>
              {{responseData.materials}}
            </div>
          </div>
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
  name: "Lesson",

  components: {
    Navbar, CourseInfo
  },

  props: {
    courseId: String,
    lessonId: String
  },

  mixins: [requestsMixin, redirect],

  created() {
    this.createGetRequest(`/courses/${this.courseId}/lessons/${this.lessonId}/`)
  }
}
</script>

<style scoped>
  .lesson {
    padding-top: 24pt;
  }

  .course-poster {
    width: 300px;
    border-radius: 5%;
  }

  .course-info {
    border-bottom: 1px solid gray;
  }

  .course-text {
    font-size: 18px;
  }

  .video-image {
    margin-right: 5px;
  }

  .video-header {
    display: inline-block;
    margin-top: 30px;
  }

  .download-button {
    margin-right: 5px;
    width: 26px;
  }
</style>