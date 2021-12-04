<template>
  <div id="single">
    <navbar-main></navbar-main>
    <div class="chess-banner">
      <div class="container">
        <div class="row">
          <div class="col-md-2">
            <img src="../assets/images/x_figure.svg" class="figure">
            <img src="../assets/images/lines/chess-line1.svg" class="line">
          </div>
          <div class="col-md-5 chess-content">
            <div class="container">
              <h2 class="title mt-5">{{ course.name }}</h2>
              <p>{{ course.description }}</p>
              <div class="row mt-3">
                <div class="info-section" style="width: 30%">
                  <p class="mb-0 mt-0">Срок обучения: </p>
                  <p class="mb-0 mt-0">{{ course.duration }} месяцев</p>
                </div>
                <div class="info-section" style="width: 60%">
                  <p class="mb-0 mt-0">Режим занятий: </p>
                  <p class="mb-0 mt-0">{{ course.activity_mode }}</p>
                </div>
                <div class="info-section mt-4" style="width: 60%">
                  <h3 class="mt-0">от {{ course.price }} в месяц</h3>
                </div>
              </div>
              <div class="row">
                <h3 class="mb-0">1 занятие бесплатное</h3>
                <p class="mt-2">Прежде чем начать обучение советуем записаться на пробное заниятие</p>
                <button type="button" class="button button__accent mt-2" style="width: auto" @click="">
                  Записаться на пробное занятие
                </button>
              </div>
            </div>
          </div>
          <!--          <div class="col-md-5">-->
          <!--            <img src="../assets/images/course_image.svg" style="height: 100%;">-->
          <!--          </div>-->
        </div>
      </div>
    </div>
    <div class="container mt-5">
      <div class="row">
        <div class="col-md-3" style="padding-right: 20px;">
          <img src="../assets/images/owl-course.svg">
        </div>
        <div class="col-md-9">
          <div class="row">
            <div class="col-md-4">
              <div class="step__media">
                <img src="../assets/images/course/step1.svg" class="step__image">
              </div>
              <h3 class="bold mt-4">Актуальные программы</h3>
            </div>
            <div class="col-md-4">
              <div class="step__media">
                <img src="../assets/images/course/step2.svg" class="step__image">
              </div>
              <h3 class="bold mt-4">Удобный для вас формат обучения</h3>
            </div>
            <div class="col-md-4">
              <div class="step__media">
                <img src="../assets/images/course/step3.svg" class="step__image">
              </div>
              <h3 class="bold mt-4">Помощь в трудоустройстве</h3>
            </div>
          </div>
        </div>
      </div>
      <div class="row mt-5" style="padding-right: 30%">
        <h1 class="bold">Кто такой {{ course.profession }}</h1>
        <p>{{ course.who_is }}</p>
      </div>
    </div>
    <div class="lead_step mt-5">
      <div class="container">
        <div class="row">
          <h2 class="center" style="color: #ffffff; font-size: 36px;">Эта программа подойдет тем, кто</h2>
          <div class="col-md-4 px-5">
            <h3 style="color: #ffffff;">Никогда не работал</h3>
            <p>и хочет получить востребованную профессию, трудоустроиться или создать собственный бизнес с нуля</p>
          </div>
          <div class="col-md-4 px-5">
            <h3 style="color: #ffffff;">Хочет научиться новому</h3>
            <p>и попробовать себя в интересной и востребованной професии</p>
          </div>
          <div class="col-md-4 px-5">
            <h3 style="color: #ffffff;">Хочет сменить работу</h3>
            <p> и получить актуальную высокооплачиваемую специальность в IT</p>
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
        <h2 class="center" style="font-size: 36px;">Принципы обучения</h2>
        <div class="row center">
          <div class="col-md-3 welcome-block">
            <img src="../assets/images/main-icon1.svg">
            <p>Передовой подход к образовательному процессу</p>
          </div>
          <div class="col-md-3 welcome-block">
            <img src="../assets/images/main-icon2.svg">
            <p>Непрерывное усовершенствование и пополнение базы курсов</p>
          </div>
          <div class="col-md-3 welcome-block">
            <img src="../assets/images/main-icon3.svg">
            <p>Только практикующие преподаватели</p>
          </div>
          <div class="col-md-3 welcome-block">
            <img src="../assets/images/main-icon4.svg">
            <p>Сопровождение на всех этапах. От начала обучения до трудоустройства</p>
          </div>
        </div>
      </div>
      <div class="row">
        <div class="col-md-8">
          <h2 class="mt-5">Содержание курса</h2>
          <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque quis tellus feugiat, posuere magna
            et,
            scelerisque leo. In scelerisque pulvinar sem, et gravida mi tincidunt nec. Suspendisse a ullamcorper nisi.
            Duis et mauris et ex posuere dignissim vitae a diam. Praesent vulputate nulla sapien, nec auctor nibh congue
            eu. Nulla lectus felis, luctus et sodales ac, convallis quis urna. Etiam id ultricies dolor, non efficitur
            tellus. Interdum et malesuada fames ac ante ipsum primis in faucibus. Pellentesque in augue porttitor,
            ornare nulla id, hendrerit nunc.</p>
        </div>
        <div class="col-md-4">
          <img src="../assets/images/course/figures.svg">
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
          <p class="question">У меня нет опыта в программировании. Подойдёт ли мне этот курс?</p>
          <button v-if="!question1" class="faq-open-button" @click="openFaqBlock('question1', question1)">
            <img src="../assets/images/faq-open.svg">
          </button>
          <button v-else class="faq-open-button" @click="openFaqBlock('question1', question1)">
            <img src="../assets/images/faq-close.svg">
          </button>
          <p v-if="question1">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam dignissim, neque sit amet
            aliquam cursus, ante urna porta mauris, eget venenatis risus turpis ac nisl. Aenean blandit, nulla tincidunt
            efficitur placerat, ante nisl auctor ipsum, in auctor mauris lacus sed nibh. Quisque id imperdiet metus, non
            semper dui. Phasellus pellentesque vitae leo in dapibus. Class aptent taciti sociosqu ad litora torquent per
            conubia nostra, per inceptos himenaeos. Suspendisse id aliquam nunc. Sed dignissim, nibh quis dapibus
            dapibus, ex sapien ultricies leo, sit amet placerat arcu sem id sem..</p>
        </div>
        <div class="faq" id="question2">
          <p class="question">Нужно ли знать математику?</p>
          <button v-if="!question2" class="faq-open-button" @click="openFaqBlock('question2', question2)">
            <img src="../assets/images/faq-open.svg">
          </button>
          <button v-else class="faq-open-button" @click="openFaqBlock('question2', question2)">
            <img src="../assets/images/faq-close.svg">
          </button>
          <p v-if="question2">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam dignissim, neque sit amet
            aliquam cursus, ante urna porta mauris, eget venenatis risus turpis ac nisl. Aenean blandit, nulla tincidunt
            efficitur placerat, ante nisl auctor ipsum, in auctor mauris lacus sed nibh. Quisque id imperdiet metus, non
            semper dui. Phasellus pellentesque vitae leo in dapibus. Class aptent taciti sociosqu ad litora torquent per
            conubia nostra, per inceptos himenaeos. Suspendisse id aliquam nunc. Sed dignissim, nibh quis dapibus
            dapibus, ex sapien ultricies leo, sit amet placerat arcu sem id sem..</p>
        </div>
        <div class="faq" id="question3">
          <p class="question">Сколько часов в неделю мне нужно будет уделять курсу?</p>
          <button v-if="!question3" class="faq-open-button" @click="openFaqBlock('question3', question3)">
            <img src="../assets/images/faq-open.svg">
          </button>
          <button v-else class="faq-open-button" @click="openFaqBlock('question3', question3)">
            <img src="../assets/images/faq-close.svg">
          </button>
          <p v-if="question3">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam dignissim, neque sit amet
            aliquam cursus, ante urna porta mauris, eget venenatis risus turpis ac nisl. Aenean blandit, nulla tincidunt
            efficitur placerat, ante nisl auctor ipsum, in auctor mauris lacus sed nibh. Quisque id imperdiet metus, non
            semper dui. Phasellus pellentesque vitae leo in dapibus. Class aptent taciti sociosqu ad litora torquent per
            conubia nostra, per inceptos himenaeos. Suspendisse id aliquam nunc. Sed dignissim, nibh quis dapibus
            dapibus, ex sapien ultricies leo, sit amet placerat arcu sem id sem..</p>
        </div>
        <div class="faq" id="question4">
          <p class="question">Кто будет помогать мне на курсе?</p>
          <button v-if="!question4" class="faq-open-button" @click="openFaqBlock('question4', question4)">
            <img src="../assets/images/faq-open.svg">
          </button>
          <button v-else class="faq-open-button" @click="openFaqBlock('question4', question4)">
            <img src="../assets/images/faq-close.svg">
          </button>
          <p v-if="question4">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam dignissim, neque sit amet
            aliquam cursus, ante urna porta mauris, eget venenatis risus turpis ac nisl. Aenean blandit, nulla tincidunt
            efficitur placerat, ante nisl auctor ipsum, in auctor mauris lacus sed nibh. Quisque id imperdiet metus, non
            semper dui. Phasellus pellentesque vitae leo in dapibus. Class aptent taciti sociosqu ad litora torquent per
            conubia nostra, per inceptos himenaeos. Suspendisse id aliquam nunc. Sed dignissim, nibh quis dapibus
            dapibus, ex sapien ultricies leo, sit amet placerat arcu sem id sem.</p>
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

export default {
  name: "EducationSingle",

  mixins: [requestsMixin],

  components: {Lessons, HowGoing, NavbarMain},

  data() {
    return {
      course: {}
    }
  },

  props: {
    id: Number,
    question1: false,
    question2: false,
    question3: false,
    question4: false,
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
  padding-bottom: 75px;
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
  background-color: #00093C;
  color: #ffffff;
  padding: 100px;
}

.welcome-block {
  padding: 30px;
}

.welcome-block img {
  height: 60px;
  margin-bottom: 40px;
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

</style>