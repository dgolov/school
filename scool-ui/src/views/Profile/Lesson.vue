<template>
  <div class="cabinet-page">
    <div class="container">
      <button @click="openProfileMenu" class="cabinet-menu-button">МЕНЮ ЛИЧНОГО КАБИНЕТА</button>
      <div class="row">
        <profile-menu :header="header"></profile-menu>
        <div class="col-xl-10 col-lg-9">
          <div class="cabinet-content">
            <div class="course">
              <div class="top-text">
                <a href="#" @click="goToCourse(courseId)">Назад</a>
                {{ responseData.course.name }} - {{ responseData.theme }}
              </div>
              <div class="tbl">
                <table>
                  <tr>
                    <td>Категория:</td>
                    <td v-if="responseData.course.category.name">{{ responseData.course.category.name }}</td>
                    <td v-else>Не указано</td>
                  </tr>
                  <tr>
                    <td>Номер урока:</td>
                    <td v-if="responseData.lesson_number">{{ responseData.lesson_number }}</td>
                    <td v-else>Не указано</td>
                  </tr>
                </table>
              </div>
              <div class="info">
                <div class="name">
                  Описание урока:
                </div>
                <p>{{ responseData.description }}</p>
              </div>
              <div class="center mt-5 tbl">
                <div v-if="responseData.video_slug" class="mb-5 mt-1">
                  <h4 class="video-header">Видео урока:</h4>
                </div>
                <div v-if="responseData.video_slug" class="mb-4">
                  <iframe width="560" height="315" :src="responseData.video_slug"
                          title="YouTube video player" frameborder="0"
                          allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                          allowfullscreen>
                  </iframe>
                </div>
              </div>
              <div v-if="responseData.materials" class="mt-5">
                <button @click="clickedDownload(responseData.materials)" class="cabinet-link-button">
                  Скачать материал к уроку
                </button>
              </div>
              <div v-if="responseData.material_link">
                <a :href="responseData.material_link" class="course-text">
                  <button class="cabinet-link-button">Материалы к уроку</button>
                </a>
              </div>
            </div>
            <div v-if="$store.state.profileInfo.user_group === 'student' && !sendSuccess">
              <form class="form-control">
                <p>Отправить комментарий к уроку</p>
                <textarea class="w-100 my-4 comment-area" v-model="comment"></textarea>
                <button type="button" @click="sendComment()" class="cabinet-link-button">Отправить</button>
              </form>
            </div>
          </div>
          <div v-if="sendSuccess">
            <h4 class="mt-4" style="color: green; margin: auto">Комментарий успешно отправлен</h4>
          </div>
        </div>
      </div>
      <div class="col-xl-2 col-lg-3"></div>
      <div class="col-xl-10 col-lg-9">
        <div class="cabinet-copy">
          © Академия будущего «ХОД», 2022
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import Navbar from "../../components/Navbar";
import CourseInfo from "../../components/Course/CourseInfo";
import {requestsMixin} from "../../components/mixins/requestsMixin";
import {redirect} from "../../components/mixins/redirect";
import {openMenu} from "../../components/mixins/openMenu";
import ProfileMenu from "../../components/Profile/ProfileMenu";

export default {
  title: 'Академия будущего | Личный кабинет',
  name: "Lesson",

  data() {
    return {
      comment: "",
      sendSuccess: false
    }
  },

  components: {
    Navbar, CourseInfo, ProfileMenu
  },

  props: {
    courseId: String,
    lessonId: String
  },

  mixins: [
    requestsMixin, redirect, openMenu
  ],

  created() {
    this.createGetRequest(`/courses/${this.courseId}/lessons/${this.lessonId}/`)
  },

  methods: {
    clickedDownload(path){
      window.open(path, 'Download');
    },

    goToCourse(id) {
      this.$router.push({name: 'CourseSingle', params: {id: id}})
    },

    async sendComment() {
      if (!this.comment) {
        console.log(111)
        return
      }
      let data = {
        "user": this.$store.state.authUser.id,
        "comment": this.comment,
      }
      const axiosInstance = axios.create(this.base);
      await axiosInstance({
        url: `/courses/${this.courseId}/lessons/${this.lessonId}/`,
        method: "post",
        data: data
      })
          .then(() => {
            this.comment = ''
            this.sendSuccess = true
          })
          .catch((error) => {
            if (error.request.status === 401) {
              // Если 401 ошибка - токен просрочен, обновляем его и заново запрашиваем данные
              this.refreshToken();
            } else {
              console.log(error.request);
            }
          })
    },
  },
}
</script>

<style scoped>
.course-text {
  font-size: 18px;
}

.video-header {
  display: inline-block;
  margin-top: 30px;
}

.cabinet-link-button {
  width: 100%;
  height: 50px;
  -webkit-border-radius: 6px;
  -moz-border-radius: 6px;
  border-radius: 6px;
  color: #fff;
  font-weight: 700;
  margin-bottom: 30px;
  background: linear-gradient(271.4deg, #27aae1 0.31%, #d851ff 99.71%);
}

.comment-area {
  background-color: #f1f1f1;
  border-radius: 5px;
  height: 150px;
  resize: none;
}
</style>