<template>
  <div class="cabinet-page">
    <div class="container">
      <button @click="openProfileMenu" class="cabinet-menu-button">МЕНЮ ЛИЧНОГО КАБИНЕТА</button>
      <div class="row">
        <profile-menu :header="header"></profile-menu>
        <div v-if="isLoaded" class="col-xl-10 col-lg-9">
          <div class="mb-3">
            <button  v-if="addButton" class="gray-button" @click="addToTimeTable">Поставить оценку</button>
            <button v-if="cancelButton" class="red-button" @click="cancelAdd">Отмена</button>
          </div>
          <div class="mb-3" v-if="showAddCourse">
            <p>Выберите группу:</p>
            <select v-model="group">
              <option disabled value="">Выберите группу</option>
              <option v-for="group in groupList" :value="group">
                {{ group.name }}
              </option>
            </select>
          </div>
          <div class="mb-3" v-if="group">
            <p>Выберите курс</p>
            <select v-model="selectedCourse">
              <option disabled value="">Выберите курс</option>
              <option v-for="course in group.courses" v-if="checkCourse(course)"
                      :value="course">{{course.name}}</option>
            </select>
          </div>
          <div class="mb-3" v-if="selectedCourse">
            <p>Выберите тему урока</p>
            <select v-model="lessonId">
              <option disabled value="">Выберите урок</option>
              <option v-for="lesson in selectedCourse.lessons" :value="lesson.id">{{lesson.theme}}</option>
            </select>
          </div>
          <div class="mb-3" v-if="lessonId">
            <table class="w-100">
              <tr>
                <th>Студент</th>
                <th>Оценка</th>
                <th>Тип оценки</th>
                <th>Опоздание/пропуск</th>
                <th>Комментарий</th>
              </tr>
              <tr v-for="student in group.students">
                <td style="width: 40%;">{{ student.first_name }} {{ student.last_name }}</td>
                <td style="width: 15%; padding-right: 15px;">
                  <select @change="setGrade($event, student)">
                    <option disabled selected value="">Выберите оценку</option>
                    <option v-for="number in 10" :value="number">{{ number }}</option>
                  </select>
                </td>
                <td style="width: 15%; padding-right: 15px;">
                  <select @change="setGradeType($event, student)">
                    <option disabled value="">Выберите тип оценки</option>
                    <option :value="'homework'">Домашняя работа</option>
                    <option selected :value="'classwork'">Классная работа</option>
                    <option :value="'test'">Контрольная работа</option>
                    <option :value="'examination'">Экзамен</option>
                  </select>
                </td>
                <td style="width: 15%; padding-right: 15px;">
                  <select @change="setLate($event, student)">
                    <option disabled value="">Выберите значение</option>
                    <option selected :value="'none'">нет</option>
                    <option :value="'late'">Опоздание</option>
                    <option :value="'absent'">Пропуск</option>
                  </select>
                </td>
                <td style="width: 15%; padding-right: 15px;">
                  <textarea @change="setComment($event, student)" class="mt-2 comment-field"></textarea>
                </td>
              </tr>
            </table>
            <button class="gray-button mt-3" @click="setGrades">Поставить оценку</button>
          </div>
          <div class="cabinet-content">
            <div class="results">
              <div class="top-text">
                Успеваемость
              </div>
              <table>
                <thead>
                <tr>
                  <td>Название курса:</td>
                  <td>Пройдено уроков:</td>
                  <td>Средний балл:</td>
                  <td></td>
                </tr>
                </thead>
                <tbody>
                <template v-for="course in courseList">
                  <tr>
                    <td>
                      <div class="name">
                        <div>{{ course.name }}</div>
                      </div>
                    </td>
                    <td>
                      <div class="slider">
                        <p>{{ getLessonCount(course) }} из {{ course.lesson_count }}</p>
                        <div><span :style="{width: getLessonPercent(course)}"></span></div>
                      </div>
                    </td>
                    <td>
                      <div class="prog color1">
                        <span>{{ getAverageGrade(course) }}</span>
                      </div>
                    </td>
                    <td>
                      <a class="link" @click="openAcademicPerformance"></a>
                    </td>
                  </tr>
                  <tr class="info">
                    <td colspan="4">
                      <table>
                        <thead>
                        <tr>
                          <td>Дата</td>
                          <td>Тема урока</td>
                          <td v-if="$store.state.profileInfo.user_group === 'teacher'">Студент</td>
                          <td>Комментарий</td>
                          <td>Оценка</td>
                        </tr>
                        </thead>
                        <tbody>
                          <template v-for="performance in responseData">
                            <tr v-if="performance.lesson.course.id === course.id">
                              <td class="w-10">{{ performance.date }}</td>
                              <td class="w-15">{{ performance.lesson.theme }}</td>
                              <td v-if="$store.state.profileInfo.user_group === 'teacher'" class="pl-3">
                                {{ performance.student.first_name }} {{ performance.student.last_name }}
                              </td>
                              <td  class="w-50">{{ performance.comment }}</td>
                              <td :class="setClassList(performance.grade)">{{ performance.grade }}</td>
                            </tr>
                          </template>
                        </tbody>
                      </table>
                    </td>
                  </tr>
                </template>
                </tbody>
              </table>
            </div>
          </div>
        </div>
        <div v-if="isLoaded" class="col-xl-2 col-lg-3"></div>
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
</template>

<script>
import Navbar from "../../components/Navbar";
import ProfileMenu from "../../components/Profile/ProfileMenu";
import {requestsMixin} from "../../components/mixins/requestsMixin";
import {redirect} from "../../components/mixins/redirect";
import axios from "axios";
import {openMenu} from "../../components/mixins/openMenu";

export default {
  title: 'Академия будущего | Личный кабинет',
  name: "AcademicPerformance",

  data() {
    return {
      header: 'AcademicPerformance',
      classSuccess: 'w-20 color1',
      classNormal: 'w-20 color3',
      classBad: 'w-20 color2',
      defaultClassList: 'row row_list pt-4 ',
      nullText: '',
      courseList: [],
      groupList: [],
      studentsGrades: [],
      showAddCourse: false,
      addButton: false,
      cancelButton: false,
      selectedCourse: false,
      lessonId: 0,
      group: 0,
    }
  },

  components: {
    Navbar, ProfileMenu
  },

  mixins: [
    requestsMixin, redirect, openMenu
  ],

  created() {
    this.createGetRequest('/performance/')
    this.GetCourses()
    this.GetGroups()
    if (this.$store.state.profileInfo.user_group === 'student') {
      this.nullText = "Вы пока еще не получили ни одной оценки";
    } else if (this.$store.state.profileInfo.user_group === 'teacher') {
      this.nullText = "Вы пока еще не поставили ни одной оценки";
      this.addButton = true;
    } else {
      this.nullText = "Оценки отсутствуют";
    }
  },

  methods: {
    setGrade(event, student) {
      for (let item of this.studentsGrades) {
        if (item.student === student.id) {
          item.grade = event.target.value;
          return
        }
      }
      this.studentsGrades.push(
          {
            student: student.id,
            grade: event.target.value,
            gradeType: 'classwork',
            late: false,
            absent: false, comment: ''
          }
      );
    },

    setGradeType(event, student) {
      for (let item of this.studentsGrades) {
        if (item.student === student.id) {
          item.gradeType = event.target.value;
          return
        }
      }
      this.studentsGrades.push(
          {student: student.id, grade: 0, gradeType: event.target.value, late: false, absent: false, comment: ''}
      );
    },

    setLate(event, student) {
      for (let item of this.studentsGrades) {
        if (item.student === student.id) {
          if (event.target.value === 'late') {
            item.late = true;
          } else if (event.target.value === 'absent') {
            item.absent = true;
          }
          return
        }
      }
      if (event.target.value === 'late') {
        this.studentsGrades.push(
            {student: student.id, grade: 0, gradeType: 'classwork', late: true, absent: false, comment: ''}
        );
      } else if (event.target.value === 'absent') {
        this.studentsGrades.push(
            {student: student.id, grade: 0, gradeType: 'classwork', late: false, absent: true, comment: ''}
        );
      }
    },

    setComment(event, student) {
      for (let item of this.studentsGrades) {
        if (item.student === student.id) {
          item.comment = event.target.value;
          return
        }
      }
      this.studentsGrades.push(
          {
            student: student.id,
            grade: 0,
            gradeType: 'classwork',
            late: false, absent: false,
            comment: event.target.value
          }
      );
    },

    checkCourse(course) {
      /// Проверка доступности курса в группе преподователю, если курс доступен, то он появляется в списке курсов
      // в выпадающем списке (Нужно для установки оценок)
      for (let item of this.$store.state.profileInfo.courses) {
        if (course.id === item.id) {
          return true
        }
      }
      return false
    },

    getAverageGrade(course) {
      let sumGrade = 0;
      let count = 0;
      for (let item of this.responseData) {
        if (item.lesson.course.id === course.id) {
          sumGrade += item.grade
          count += 1
        }
      }
      let result = sumGrade / count
      if (!result) {
        return '-'
      }
      return result.toFixed(1)
    },

    getLessonCount(course) {
      let count = 0;
      for (let item of this.responseData) {
        if (item.lesson.course.id === course.id) {
          count += 1
        }
      }
      return count
    },

    getLessonPercent(course) {
      let count = 0;
      for (let item of this.responseData) {
        if (item.lesson.course.id === course.id) {
          count += 1
        }
      }
      return count / course.lesson_count * 100 + '%'
    },

    setClassList(grade) {
      let classList = this.defaultClassList
      if (grade < 4) {
        classList += this.classBad;
      } else if (grade > 3 && grade < 7) {
        classList += this.classNormal;
      } else if (grade > 6) {
        classList += this.classSuccess;
      }
      return classList
    },

    getImage(url) {
      // Некоторые данные приходят с сервера с абсолютным адресом, некоторые с относительным, вероятно из-за ViewSets
      // Данный метод временно решает эту проблему
      if (url.indexOf('${this.$store.state.backendUrl}') === -1) {
        return `${this.$store.getters.getServerUrl}${url}`
      } else {
        return url
      }
    },

    addToTimeTable() {
      this.showAddCourse = true;
      this.cancelButton = true;
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
      this.group = 0;
    },

    openAcademicPerformance() {
      $('.cabinet-page .cabinet-content .results table tbody tr td .link').click(function() {
        $(this).toggleClass('active');
        $(this).parent().parent().toggleClass('active');
        $(this).parent().parent().next('.info').toggle();
      });
    },

    async GetCourses() {
      const axiosInstance = axios.create(this.base);

      await axiosInstance({
        url: "/courses/available/",
        method: "get",
        params: {},
      })
          .then((response) => this.courseList = response.data)
    },

    async GetGroups() {
      const axiosInstance = axios.create(this.base);

      await axiosInstance({
        url: "/groups/",
        method: "get",
        params: {},
      })
          .then((response) => this.groupList = response.data)
    },

    setGrades() {
      for (let item of this.studentsGrades) {
        this.sendItemGrade(item.student, item.grade, item.gradeType, item.late, item.absent, item.comment)
      }
    },

    async sendItemGrade(student, grade, gradeType, late, absent, comment) {

      const data = {
        "student": student,
        "lesson": this.lessonId,
        "grade": grade,
        "type_grade": gradeType,
        "late": late,
        "absent": absent,
        "comment": comment
      }
      const axiosInstance = axios.create(this.base);
      await axiosInstance({
        url: `/performance/`,
        method: "post",
        data: data
      })
          .then(() => {
            this.cancelAdd()
            this.createGetRequest('/performance/')
          })
          .catch((error) => {
            if (error.request.status === 401) {
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
.comment-field {
  resize: none;
}
</style>