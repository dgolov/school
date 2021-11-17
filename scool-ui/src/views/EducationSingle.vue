<template>
  <div id="single">
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
              <p class="left-align">Научить анализировать свои и чужие ошибки, учиться на них с помощью GM мирового уровня</p>
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
      <div class="row mt-5">
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
</style>