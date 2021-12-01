<template>
  <div id="chess">
    <navbar-main></navbar-main>
    <div class="chess-banner">
      <div class="container">
        <div class="row">
          <div class="col-md-2">
            <img src="../assets/images/horse-figure.svg" class="figure">
            <img src="../assets/images/lines/chess-line1.svg" class="line">
          </div>
          <div class="col-md-5 chess-content">
            <div class="container">
              <h2 class="title mt-5">Шахматная школа</h2>
              <h3>Развитие мышления и логики</h3>
              <course-info :course="course"></course-info>
              <div class="row">
                <h3 class="mb-0">1 занятие бесплатное</h3>
                <p class="mt-2">Прежде чем начать обучение советуем записаться на пробное заниятие</p>
                <button type="button" class="button button__accent mt-2" style="width: auto" @click="">
                  Записаться на пробное занятие
                </button>
              </div>
            </div>
          </div>
          <div class="col-md-5">
            <img src="../assets/images/chess-course.png" style="height: 100%;">
          </div>
        </div>
      </div>
    </div>
    <div class="container mt-5">
      <div class="row">
        <div class="col-md-3" style="padding-right: 20px;">
          <img src="../assets/images/owl-chess.svg">
        </div>
        <div class="col-md-9">
          <div class="row">
            <div class="col-md-3">
              <div class="step__media">
                <img src="../assets/images/chess/step1.svg" class="step__image">
              </div>
              <h3 class="bold mt-4">Цель 1</h3>
              <p class="left-align">Привить любовь и интерес к шахматам</p>
            </div>
            <div class="col-md-3">
              <div class="step__media">
                <img src="../assets/images/chess/step2.svg" class="step__image">
              </div>
              <h3 class="bold mt-4">Цель 2</h3>
              <p class="left-align">Получить удовольствие от процесса игры, от факта победы в партии, от спасения</p>
            </div>
            <div class="col-md-3">
              <div class="step__media">
                <img src="../assets/images/chess/step3.svg" class="step__image">
              </div>
              <h3 class="bold mt-4">Цель 3</h3>
              <p class="left-align">Научить анализировать свои и чужие ошибки, учиться на них с помощью GM мирового
                уровня</p>
            </div>
            <div class="col-md-3">
              <div class="step__media">
                <img src="../assets/images/chess/step4.svg" class="step__image">
              </div>
              <h3 class="bold mt-4">Цель 4</h3>
              <p class="left-align">Получить удовольствие от процесса игры, от факта победы в партии, от спасения</p>
            </div>
          </div>
        </div>
      </div>
      <div class="row mt-5" style="padding-right: 30%">
        <h1 class="bold">Школа шахмат</h1>
        <p>Шахматы - это отличная идея для времяпрепровождения с родителями, детьми и друзьями.
          Игра дает полезные в жизни навыки: учит побеждать и проигрывать, развивает
          творческие способности, вырабатывает стрессо-устойчивость, терпение, помогает сосредоточиться,
          а так же помогает осознать последствия своих действий.</p>
      </div>
      <div class="row mt-5 mb-5">
        <div class="col-md-2">
          <div class="step__media">
            <img src="../assets/images/chess/icon1.svg" class="step__image">
          </div>
          <p class="mt-3">Интересные уроки по шахматам</p>
        </div>
        <div class="col-md-2">
          <div class="step__media">
            <img src="../assets/images/chess/icon2.svg" class="step__image">
          </div>
          <p class="mt-3">Шахматы для взрослых и детей</p>
        </div>
        <div class="col-md-2">
          <div class="step__media">
            <img src="../assets/images/chess/icon3.svg" class="step__image">
          </div>
          <p class="mt-3">Обучение шахматам онлайн</p>
        </div>
        <div class="col-md-2">
          <div class="step__media">
            <img src="../assets/images/chess/icon4.svg" class="step__image">
          </div>
          <p class="mt-3">Профессиональное обучение шахматам</p>
        </div>
        <div class="col-md-2">
          <div class="step__media">
            <img src="../assets/images/chess/icon5.svg" class="step__image">
          </div>
          <p class="mt-3">Шахматные турниры</p>
        </div>
        <div class="col-md-2">
          <div class="step__media">
            <img src="../assets/images/chess/icon6.svg" class="step__image">
          </div>
          <p class="mt-3">Сеанс одновременной игры с GM</p>
        </div>
      </div>
    </div>
    <div class="lead_step">
      <div class="container">
        <div class="row">
          <div class="col-md-6 px-5">
            <p>Шахматы могут помочь вам планировать наперед, не торопиться с решениями и взвешивать их плюсы и
              минусы.</p>
          </div>
          <div class="col-md-6 px-5">
            <p>Шахматами можно наслаждаться в любом возрасте — в результате, тренировка мозга может укреплять ваше
              здоровье.</p>
          </div>
          <div class="center mt-4">
            <button type="button" class="button button__accent mt-2" style="width: auto" @click="pay()">
              Записаться на курс
            </button>
          </div>
        </div>
      </div>
    </div>
    <div class="container mt-5">
      <div class="row">
        <div class="col-md-8">
          <h2>Chess academy для школьников</h2>
          <p>Обеспечиваем индивидуальный подход к учащимся. В основе процесса обучения — тесное и открытое
            взаимодействие
            педагода и ученика. Обучение проходит по программе, созданной GM.</p>
        </div>
        <div class="col-md-8">
          <h2 class="mt-5">Содержание курса</h2>
          <p>Программа включает в себя изучение истории возникновения игры в шахматы, современные тенденции игры в
            онлайн-шахматы, знакомство со знаменитыми шахматистами прошлого и настоящего. Дети знакомятся с фигурами и
            правилами игры, узнают основные понятия, отрабатывая все в игровой практике. Дебют, мителльшпиль, эндшпиль,
            стратегия и тактика игры, особенности позиции – все это включено в первый год обучения, а пятилетний курс
            предполагает обучение ребенка до уровня КМС.</p>
        </div>
        <div class="col-md-4">
          <img src="../assets/images/chess/figures.svg">
        </div>
        <div class="col-md-6">
          <div class="row mt-3">
            <div class="info-section" style="width: 30%">
              <p class="mb-0 mt-0">Срок обучения: </p>
              <p class="mb-0 mt-0">{{ course.duration }} месяцев</p>
            </div>
            <div class="info-section" style="width: 60%">
              <p class="mb-0 mt-0">Режим занятий: </p>
              <p class="mb-0 mt-0">2 раза в неделю по 2 академических часа</p>
            </div>
            <div class="info-section mt-4" style="width: 60%">
              <h3 class="mt-0">от {{ course.price }} в месяц</h3>
            </div>
          </div>
          <div class="mt-4">
            <button type="button" class="button button__accent mt-2" style="width: auto" @click="pay()">
              Записаться на курс
            </button>
          </div>
        </div>
        <div class="col-md-6">
          <img src="../assets/images/owl-free.svg">
        </div>
      </div>
    </div>
    <div class="teachers_step" v-if="course.teachers">
      <div class="container">
        <div class="row center">
          <h2>Наши преподаватели</h2>
          <div v-for="teacher of course.teachers" class="teacher">
            <img v-if="teacher.avatar" class="center profile-avatar"
                 :src="`${teacher.avatar.image}`">
            <img v-else src="../assets/images/avatars/mike2.jpeg" class="center profile-avatar">
            <h3 class="bold">{{ teacher.last_name }} {{ teacher.first_name }}</h3>
            <p>{{ teacher.about }}</p>
          </div>
        </div>
      </div>
    </div>
    <div class="container mt-5 mb-5">
      <div class="row">
        <div class="faq" id="question1">
          <p class="question">Кому подойдет этот курс?</p>
          <button v-if="!question1" class="faq-open-button" @click="openFaqBlock('question1', question1)">
            <img src="../assets/images/faq-open.svg">
          </button>
          <button v-else class="faq-open-button" @click="openFaqBlock('question1', question1)">
            <img src="../assets/images/faq-close.svg">
          </button>
          <p v-if="question1">Детям от 7 лет, которых хотят научиться играть в шахматы, развить свою логику, улучшить
            память, сформировать логическое мышление, повысить успеваемость в школе.</p>
        </div>
        <div class="faq" id="question2">
          <p class="question">Что нужно ребенку для занятий?</p>
          <button v-if="!question2" class="faq-open-button" @click="openFaqBlock('question2', question2)">
            <img src="../assets/images/faq-open.svg">
          </button>
          <button v-else class="faq-open-button" @click="openFaqBlock('question2', question2)">
            <img src="../assets/images/faq-close.svg">
          </button>
          <p v-if="question2">Шахматная доска и фигуры дома – так будет легче практиковаться и делать домашние задания.</p>
        </div>
        <div class="faq" id="question3">
          <p class="question">Где можно узнать расписание занятий?</p>
          <button v-if="!question3" class="faq-open-button" @click="openFaqBlock('question3', question3)">
            <img src="../assets/images/faq-open.svg">
          </button>
          <button v-else class="faq-open-button" @click="openFaqBlock('question3', question3)">
            <img src="../assets/images/faq-close.svg">
          </button>
          <p v-if="question3">Если ребенок уже зарегистрирован – в его личном кабинете, если только планируете
            записаться – звоните, мы подберем подходящую группу.</p>
        </div>
        <div class="faq" id="question4">
          <p class="question">Что делать, если ребенок пропустит занятие?</p>
          <button v-if="!question4" class="faq-open-button" @click="openFaqBlock('question4', question4)">
            <img src="../assets/images/faq-open.svg">
          </button>
          <button v-else class="faq-open-button" @click="openFaqBlock('question4', question4)">
            <img src="../assets/images/faq-close.svg">
          </button>
          <p v-if="question4">Предупредить об уважительной причине отсутствия и  посетить занятие с другой группой в
            удобное для вас время</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>

import {requestsMixin} from "../components/mixins/requestsMixin";
import NavbarMain from "../components/NavbarMain";
import Lessons from "../components/Course/Lessons";
import HowGoing from "../components/Course/HowGoing";
import axios from "axios";
import CourseInfo from "../components/Course/CourseInfo";

export default {
  name: "EducationSingle",

  mixins: [requestsMixin],

  components: {Lessons, HowGoing, NavbarMain, CourseInfo},

  data() {
    return {
      course: {},
      question1: false,
      question2: false,
      question3: false,
      question4: false,
    }
  },

  props: {
    id: Number
  },

  created() {
    this.loadCourse()
  },

  methods: {
    async loadCourse() {
      await axios
          .get(`${this.$store.getters.getServerUrl}/courses/${this.id}`)
          .then(response => (this.course = response.data))
    },

    async pay() {
      let data = {
        "id": this.course.id,
      }
      const axiosInstance = axios.create(this.base);
      await axiosInstance({
        url: `/courses/buy/`,
        method: "post",
        data: data
      })
          .then((response) => {
            window.open(response.data._PaymentResponse__confirmation[0][1])
          })
          .catch((error) => {
            if (error.request.status === 401) {
              // Если 401 ошибка - токен просрочен, обновляем его и заново запрашиваем данные
              this.refreshToken();
              this.sendToServer('/send-message/');
            } else {
              console.log(error.request);
            }
          })
    },

    openFaqBlock(blockId, question) {
      switch (blockId) {
        case 'question1': {
          this.question1 = !this.question1;
          break;
        }
        case 'question2': {
          this.question2 = !this.question2;
          break;
        }
        case 'question3': {
          this.question3 = !this.question3;
          break;
        }
        case 'question4': {
          this.question4 = !this.question4;
          break;
        }
      }
      let block = document.getElementById(blockId);
      if (question) {
        block.classList.remove('faq_active');
      } else {
        block.classList.add('faq_active');
      }
    },
  }
}
</script>

<style scoped>
.chess-banner {
  background: #00093C;
}

.figure {
  position: absolute;
  left: 8%;
  top: 15%;
}

.chess-content {
  color: #FFFFFF;
}

.chess-content .title {
  margin-bottom: 0;
  font-weight: bold;
  font-size: 42px;
  line-height: 51px;
  display: flex;
  align-items: center;
  color: #FFFFFF;
}

.chess-content h3 {
  margin: 10px 0 30px 0;
  font-style: normal;
  font-weight: 500;
  font-size: 24px;
  line-height: 29px;
  display: flex;
  align-items: center;
  color: #FFFFFF;
}

.info-section {
  display: inline-block;
  margin-right: 5%;
  border-top: 1px solid;
  border-image: linear-gradient(to right, #eb934f, #63a9da) 47% 0;
  padding-top: 10px;
}

.info-section p {
  font-size: 14px;
}

.line {
  position: absolute;
  left: 2%;
  top: 45%;
}

.lead_step {
  background-image: url("../assets/images/chess/background.svg");
  background-repeat: no-repeat;
  color: #ffffff;
  padding: 100px;
}

.teachers_step {
  background-image: url("../assets/images/background.svg");
  background-repeat: no-repeat;
  padding: 100px;
  align-items: center;
}

.teachers_step h2 {
  color: #ffffff;
  font-style: normal;
  font-weight: bold;
  font-size: 36px;
  line-height: 44px;
  margin-bottom: 50px;
}

.teacher {
  width: 280px;
  height: 360px;
  background-color: #ffffff;
  border-radius: 20px;
  padding: 20px;
  margin: auto;
}

.profile-avatar {
  display: block;
  width: 130px;
  height: 130px;
  border: 0;
  border-radius: 50%;
  margin: auto;
  text-align: center;
}

.faq {
  background-color: #FFFFFF;
  border-radius: 6px;
  padding: 10px;
  margin: 10px;
  border: 0.5px solid;
  border-image: linear-gradient(to right, #eb934f, #63a9da) 47% 0;
  border-image-slice: 1;
}

.faq_active {
  box-shadow: -5px 0 8px 2px rgba(235, 147, 79, 0.6),
  5px 0 8px 2px rgba(99, 169, 218, 0.6);
}

.faq-open-button {
  height: 20px;
  border: none;
  float: right;
  align-items: center;
}

.faq .question {
  margin: 0;
  display: inline;
  font-weight: 500;
  font-size: 18px;
  align-items: center;
  line-height: 46px;
}

h2 {
  font-weight: bold;
}
</style>