<template>
  <div id="chess">

    <navbar-main></navbar-main>

    <div class="header-page-wrapper d-none d-lg-block">
      <div class="chess-course">
        <div class="chess-course-img-wrapp">
          <img src="../assets/images/chess-course.png" alt="" class="chess-course__img">
        </div>
        <div class="header-page-inner">
          <h1 class="chess-course-title e-course-title">{{ course.name }}</h1>
          <p class="chess-course-text e-course">{{ course.description }}</p>
        </div>
        <div class="chess-course-wrapp e-course-wrapp">
          <div class="header-desc">
            <p class="chess-course-info chess-course-info_small">Срок обучения: <span></span> {{ course.duration }}
              месяцев</p>
          </div>
          <div class="header-desc hd-m">
            <p class="chess-course-info chess-course-info_big">Режим занятий: <span></span> {{ course.activity_mode }}
            </p>
          </div>
        </div>
        <div class="chess-course-wrapp chess-course-wrapp_bottom e-course-wrapper">
          <div class="header-desc">
            <p class="chess-course-info chess-course-info_price">от {{ course.price }} ₽ в месяц</p>
          </div>
        </div>
        <p class="header-button-title hb-chess e-c-free">1 занятие бесплатное</p>
        <button class="button button-header button-chess" type="submit"
                @click="goTo('Requests', {purpose: 'event', course: course.id})" style="z-index: 999">
          Записаться на пробное занятие
        </button>
      </div>
    </div>

    <div class="header-mobi d-none">
      <div class="chess-course-img-wrapp">
        <img src="../assets/images/chess-course.png" alt="" class="chess-course__img" style="align-items:center;">
      </div>
      <div class="container">
        <div class="row">
          <div class="col-12">
            <div class="header-page-inner">
              <h1 class="chess-course-title">{{ course.name }}</h1>
              <p class="chess-course-text e-course">{{ course.description }}</p>
            </div>
            <div class="chess-course-wrapp">
              <div class="header-desc header-desc_tiny">
                <p class="chess-course-info chess-course-info_small">Срок обучения: <span></span> {{ course.duration }}
                  месяцев</p>
              </div>
              <div class="header-desc hd-m header-desc_small">
                <p class="chess-course-info chess-course-info_big">Режим занятий: <span></span> {{
                    course.activity_mode
                  }}</p>
              </div>
            </div>
            <div class="chess-course-wrapp chess-course-wrapp_bottom">
              <div class="header-desc  header-desc_big">
                <p class="chess-course-info chess-course-info_price">от {{ course.price }} ₽ в месяц</p>
              </div>
            </div>
            <p class="header-button-title hb-chess">1 занятие бесплатное</p>
            <button class="button button-header button-chess" type="button"
                    @click="goTo('Requests', {purpose: 'event', course: course.id})">
              Записаться на пробное занятие
            </button>
          </div>
        </div>
      </div>
    </div>

    <div class="steps white-section mt-3 pt-0">
      <div class="container">
        <div class="row mb-3">
          <div class="col-md-6" style="padding: 10px;">
            <h2 class="pool-blitz">Экспресс обучение для самых нетерпеливых</h2>
            <p style="text-align: left;">Повышение рейтинга до 200 единиц за минимальное количество занятий.</p>
            <button class="button button__accent" type="button"
                    @click="goTo('Requests', {purpose: 'chess_express', course: course.id})">
              Подать заявку
            </button>
          </div>
          <div class="col-md-6" style="padding: 10px;">
            <h2 class="pool-blitz">Курсы по блицу и пуле</h2>
            <p style="text-align: left;">Обучение игре с контролем по 1 минуте, по 3 минуты и 5 минут.</p>
            <button class="button button__accent" type="button"
                    @click="goTo('Requests', {purpose: 'chess_pool', course: course.id})">
              Подать заявку
            </button>
          </div>
        </div>
        <div class="row">
          <div class="col-lg-4 mb-3 mt-3 mb-5">
            <div class="owl owl-events">
              <img src="../assets/img/owl/owl-main.png" class="owl__main owl__main-events ">
              <span class="owl__frame-events"></span>
              <div class="owl-text owl-text-chess">
                <p class="owl-desc owl-desc-chess">Вы полюбите шахматы, <span></span>и вам этого будет не хватать
                  всегда!</p>
              </div>
            </div>
          </div>
          <div class="col-12 col-lg-8 mt-3 mb-5">
            <div class="events-title-wrapp chess-wrapp">
              <div class="events-title__inner c-c-title-inner">
                <img src="../assets/img/chess/chess-figure-one.svg" alt="">
                <h3 class="events-title__subject">Цель 1</h3>
                <p class="events-title__text">Привить любовь и интерес к шахматам</p>
              </div>
              <div class="events-title__inner c-c-title-inner">
                <img src="../assets/img/chess/chess-figure-two.svg" alt="">
                <h3 class="events-title__subject">Цель 2</h3>
                <p class="events-title__text">Получить удовольствие от процесса игры, от факта победы в партии, от
                  спасения</p>
              </div>
              <div class="events-title__inner t-i-chess c-c-title-inner">
                <img src="../assets/img/chess/chess-figure-three.svg" alt="">
                <h3 class="events-title__subject">Цель 3</h3>
                <p class="events-title__text">Научить анализировать свои и чужие ошибки, учиться на них с помощью GM
                  мирового уровня</p>
              </div>
              <div class="events-title__inner c-c-title-inner">
                <img src="../assets/img/chess/chess-figure-four.svg" alt="">
                <h3 class="events-title__subject">Цель 4</h3>
                <p class="events-title__text">Получить удовольствие от процесса игры, от факта победы в партии, от
                  спасения</p>
              </div>
            </div>
          </div>
          <div class="col-md-6">
            <h2 class="mb-3" style="text-align: left;">Шахматная лабаратория</h2>
            <ul style="text-align: left;">
              <li class="skills__item skills__item_marker">Разборка дебютов</li>
              <li class="skills__item skills__item_marker">Корректировка наигранных дебютов</li>
              <li class="skills__item skills__item_marker">Мониторинг и внедрение актуальных идей</li>
              <li class="skills__item skills__item_marker">Разбор игры (выявление и анализ системных ошибок;
                неточностей)
              </li>
              <li class="skills__item skills__item_marker">Формирование индивидуального уникального стиля игры
                шахматиста
              </li>
              <li class="skills__item skills__item_marker">Составление плана и контроль выполнения задач самостоятельной
                подготовки
              </li>
            </ul>
          </div>
          <div class="col-md-6">
            <h2 class="mb-3" style="text-align: left;">Тренажерный зал</h2>
            <ul style="text-align: left;">
              <li class="skills__item skills__item_marker">Занятие по тактике</li>
              <li class="skills__item skills__item_marker">Подбор и обучение шахматных тренеров</li>
              <li class="skills__item skills__item_marker">Разбор партии мировой шахматной элиты</li>
            </ul>
          </div>
          <div class="col-md-6">
            <h2 class="mb-3" style="text-align: left;">Командный пункт</h2>
            <ul style="text-align: left;">
              <li class="skills__item skills__item_marker">Формирование спортивного характера (работа с психологом)</li>
              <li class="skills__item skills__item_marker">Как не расстраиваться, использовать поражения с максимальной
                пользой
              </li>
              <li class="skills__item skills__item_marker">Как правильно использовать радость побед</li>
            </ul>
          </div>
          <div class="col-md-6">
            <div class="col-md-6">
              <h2 class="mb-3" style="text-align: left;">Центр полетов</h2>
              <ul style="text-align: left;">
                <li class="skills__item skills__item_marker">Сопровождение и помощь на соревнованиях</li>
                <li class="skills__item skills__item_marker">Разбор игры (выявление и анализ системных ошибок;
                  неточностей)
                </li>
                <li class="skills__item skills__item_marker">Занятия в рамках авторской программы от GM
                  (Гроссмейстера)
                </li>
                <li class="skills__item skills__item_marker">Аналитика и разбор партий с лучшими специалистами</li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </div>

    <section class="video v-a-a c-c">
      <div class="container">
        <div class="row justify-content-center" style="position:relative;z-index: 1;">
          <div class="col-md-12 col-lg-8">
            <div class="video-wrapper">
              <div class="video__link" v-if="videoLink">
                            <span class="video__circle" @click="videoStart()">
                                <img src="../assets/img/video/play.svg" alt="" class="video__play">
                            </span>
              </div>
              <span class="video-content__triangle video-content-position"></span>
              <span class="video-content__line-left video-content-position"></span>
              <span class="video-content__line-right video-content-position"></span>
              <span class="video-content__cross video-content-position"></span>
            </div>
            <div class="wrapper-modal" v-if="wrapperModal">
              <div class="overlay" id="overlay" @click="videoClose()"></div>
              <!--noindex-->
              <iframe class="iframe eff-h" width="560" height="315" src="https://www.youtube.com/embed/ipfc4Xq9KUo"
                      rel="nofollow noopener noreferrer" target="_blank" title="YouTube video player" frameborder="0"
                      allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                      allowfullscreen></iframe>
              <!--/noindex-->
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class="chess-school">
      <div class="container">
        <div class="row">
          <div class="col-12">
            <h2 class="program-events-title c-h-title">Школа шахмат</h2>
            <p class="chess-school-decs">Шахматы - это отличная идея для времяпрепровождения с родителями, детьми и
              друзьями. Игра дает полезные в жизни навыки: учит побеждать и проигрывать, развивает творческие
              способности, вырабатывает стрессо-устойчивость, терпение, помогает сосредоточиться, а так же помогает
              осознать последствия своих действий.</p>
          </div>
          <div class="col-12">
            <div class="chess-school-wrapp">
              <div class="chess-school__inner">
                <img src="../assets/img/chess/icon-one.svg" alt="icon" class="chess-school__img">
                <p class="chess-school__text">Интересные уроки <span class="c-s-carryover"></span> по шахматам</p>
              </div>
              <div class="chess-school__inner">
                <img src="../assets/img/chess/icon-two.svg" alt="icon" class="chess-school__img">
                <p class="chess-school__text">Шахматы для взрослых <span class="c-s-carryover"></span> и детей</p>
              </div>
              <div class="chess-school__inner">
                <img src="../assets/img/chess/icon-three.svg" alt="icon" class="chess-school__img">
                <p class="chess-school__text">Обучение <span class="c-s-carryover"></span> шахмат онлайн</p>
              </div>
              <div class="chess-school__inner">
                <img src="../assets/img/chess/icon-four.svg" alt="icon" class="chess-school__img">
                <p class="chess-school__text">Профессиональное обучение шахматам</p>
              </div>
              <div class="chess-school__inner">
                <img src="../assets/img/chess/icon-five.svg" alt="icon" class="chess-school__img">
                <p class="chess-school__text">Шахматные <span class="c-s-carryover"></span> турниры</p>
              </div>
              <div class="chess-school__inner">
                <img src="../assets/img/chess/icon-six.svg" alt="icon" class="chess-school__img">
                <p class="chess-school__text">Сеанс одновременной игры с GM</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class="record-course">
      <div class="container">
        <div class="row">
          <div class="record-course-inner">
            <div class="col-lg-5">
              <p class="record-course-text">Шахматы могут помочь вам планировать наперед, не торопиться с решениями и
                взвешивать их плюсы и минусы.</p>
            </div>
            <div class="col-lg-5">
              <p class="record-course-text">Шахматами можно наслаждаться в любом возрасте — в результате, тренировка
                мозга может укреплять ваше здоровье.
              </p>
            </div>
          </div>
          <div class="col-12">
            <button class="button button-header r-c-button" type="button" @click="pay()">Записаться на курс</button>
          </div>
        </div>
      </div>
    </section>

    <section class="chess-academy">
      <div class="container">
        <div class="row">
          <div class="col-12">
            <h2 class="program-events-title">Chess academy для школьников</h2>
            <p class="chess-academy-text">Обеспечиваем индивидуальный подходк учащимся. В основе процесса обучения —
              тесное <span class="c-s-carryover"></span> и открытое взаимодействие педагода и ученика. Обучение проходит
              по программе, созданной GM.</p>
          </div>
        </div>
      </div>
      <!-- Фотографии с прошлых мероприятий стр мероприятия -->
      <div class="carousel-past-events">
        <div class="gallery">
          <!-- Контент 1 слайда -->
          <img src="../assets/img/chess/slide-one.jpg" alt="слайд 1" class="past-events-img">
        </div>
        <div class="gallery">
          <!-- Контент 2 слайда -->
          <img src="../assets/img/chess/slide-two.jpg" alt="слайд 2" class="past-events-img">
        </div>
        <div class="gallery">
          <!-- Контент 3 слайда -->
          <img src="../assets/img/chess/slide-three.jpg" alt="слайд 3" class="past-events-img">
        </div>
        <div class="gallery">
          <!-- Контент 4 слайда -->
          <img src="../assets/img/chess/slide-four.jpg" alt="слайд 4" class="past-events-img">
        </div>
        <div class="gallery">
          <!-- Контент 5 слайда -->
          <img src="../assets/img/chess/slide-five.jpg" alt="слайд 5" class="past-events-img">
        </div>
        <div class="gallery">
          <!-- Контент 6 слайда -->
          <img src="../assets/img/chess/slide-six.jpg" alt="слайд 5" class="past-events-img">
        </div>
      </div>
    </section>

    <div class="container mt-5">
      <div class="row">
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

    <section class="teachers" v-if="course.teachers">
      <div class="row">
        <div class="col-12">
          <h2 class="reviews-title">Наши преподаватели</h2>
        </div>
      </div>
      <div class="row">
        <div class="col-12">
          <div class="teachers-wrapp">
            <div class="carousel" v-for="teacher of course.teachers">
              <!-- Контент 1 слайда -->
              <div class="col-3">
                <div class="teacher">
                  <div class="teacher__avatar">
                    <img v-if="teacher.avatar" :src="`${teacher.avatar.image}`" alt=" Фото преподавателя"
                         class="profile-avatar">
                    <img v-else src="../assets/images/avatars/mike2.jpeg" class="center profile-avatar">
                  </div>
                  <h4 class="teacher__name">{{ teacher.last_name }} {{ teacher.first_name }}</h4>
                  <p class="teacher__info">{{ teacher.about }}</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <Faq></Faq>

  </div>
</template>

<script>

import {requestsMixin} from "../components/mixins/requestsMixin";
import NavbarMain from "../components/NavbarMain";
import Lessons from "../components/Course/Lessons";
import HowGoing from "../components/Course/HowGoing";
import axios from "axios";
import CourseInfo from "../components/Course/CourseInfo";
import {playerMixin} from "../components/mixins/playerMixin";
import Faq from "../components/Faq";

export default {
  title: 'Академия будущего | Шахматная школа',
  name: "EducationSingle",

  mixins: [requestsMixin, playerMixin],

  components: {Lessons, HowGoing, NavbarMain, CourseInfo, Faq},

  data() {
    return {
      course: {},
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

h2 {
  font-weight: bold;
}

.pool-blitz {
  text-align: left;
  border-bottom: 2px solid;
  border-image-slice: 1;
  border-image-source: linear-gradient(98deg, rgba(247, 148, 29, 1), rgba(39, 170, 225, 1));
  padding-bottom: 10px;
  margin-bottom: 15px;
}
</style>