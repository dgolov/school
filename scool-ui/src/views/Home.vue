<template>
  <div class="home">

    <navbar></navbar>

    <div class="header-wrapper d-none d-lg-block">
      <div class="header">
        <h1 class="header-title">Образовательная  IT - платформа Academy of the Future</h1>
        <p class="header-title__desc">Авторские программы обучения для детей и взрослых</p>
      </div>
    </div>

    <div class="header-mobi d-none">
      <img src="../assets/img/header/header-mobi.jpg" alt="" class="header-mobi__img">
      <div class="container">
        <div class="row">
          <div class="col-12">
            <div class="header-mobi-title">
              <h1 class="header-title">Образовательная  IT - платформа Academy of the Future</h1>
              <p class="header-title__desc">Авторские программы обучения для детей и взрослых</p>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="steps white-section mt-3 pt-0">
      <div class="container">
        <div class="row">
          <div class="col-md-3 mb-3">
            <div class="owl">
              <img src="../assets/img/owl/owl-main.png" class="owl__main">
              <span class="owl__frame"></span>
              <div class="owl-text">
                <h5 class="owl-title">Кем вы хотите стать?</h5>
                <p class="owl-desc"> Пора найти себя
                  и выбрать подходящий курс :) <span class="owl-desc-span">Удачи!</span></p>
              </div>
            </div>
          </div>

          <div class="col-md-9">
            <div class="row groups mb-4">
              <div class="col-md-4 group-active" id="children">
                <img src="../assets/images/children.svg" class="group-image">
                <div class="group-text">
                  <button @click="setAgeGroup('children')">Дети</button>
                  <span class="group-text__age">8 — 14 лет</span>
                </div>
              </div>
              <div class="col-md-4 center" id="teens">
                <img src="../assets/images/teens.svg" class="group-image">
                <div class="group-text">
                  <button @click="setAgeGroup('teens')">Подростки</button>
                  <span class="group-text__age">14 — 18 лет</span>
                </div>
              </div>
              <div class="col-md-4 center" id="adults">
                <img src="../assets/images/adults.svg" class="group-image">
                <div class="group-text">
                  <button @click="setAgeGroup('adults')">Взрослые</button>
                  <span class="group-text__age">18 — ∞</span>
                </div>
              </div>
            </div>

            <div class="mb-5">
              <div v-for="category in categoryList" v-if="category.age_group === age_group" class="category-area">
                <button class="category-button" @click="goToCategory(category.name)">
                  {{ category.name }}
                </button>
              </div>
            </div>
            <div class="row">
              <div class="col-md-12">
                <a href="/summer-camp">
                  <div class="news-block news-block-world py-5 mb-4 white-text eff-h-two"
                       style="background-color: #B8EFCF;">
                    <h2 class="bold my-0">IT летние каникулы в Академии Будущего</h2>
                  </div>
                </a>
              </div>
              <div class="col-md-4">
                <a href="#">
                  <div class="news-block news-block-world py-4 mb-4 white-text eff-h-two"
                       style="background-color: #FFEEF6;"
                       @click="$router.push({name: 'Education', params: {'category': 'Программирование', 'ageGroup': 'adults'}})">
                    <img src="../assets/img/cart/e_learning_monitor_icon_187419.svg" style="width: 70px; height: 70px;">
                    <h2 class="bold">IT обучение</h2>
                  </div>
                </a>
              </div>
              <div class="col-md-4">
                <a href="#">
                  <div class="news-block news-block-world py-4 mb-4 white-text eff-h-two"
                       style="background-color: #C7EEFF;"
                       @click="$router.push({name: 'Education', params: {'category': 'Киберспорт', 'ageGroup': 'teens'}})">
                    <img src="../assets/img/cart/game-console-svgrepo-com(1).svg" style="width: 70px; height: 70px;">
                    <h2 class="bold">Киберспорт</h2>
                  </div>
                </a>
              </div>
              <div class="col-md-4">
                <a href="#">
                  <div class="news-block news-block-world py-4 mb-4 white-text eff-h-two"
                       style="background-color: #FFCE94;"
                       @click="$router.push({name: 'Education', params: {'category': 'Шахматы', 'ageGroup': 'children'}})">
                    <img src="../assets/img/cart/3413424.svg" style="width: 70px; height: 70px;">
                    <h2 class="bold">Шахматы</h2>
                  </div>
                </a>
              </div>
              <div class="col-md-4">
                <a href="#">
                  <div class="news-block news-block-world py-4 mb-4 white-text eff-h-two"
                       style="background-color: #DDDDFF;"
                       @click="$router.push({name: 'Education', params: {'category': 'Криптовалюта', 'ageGroup': 'adults'}})">
                    <img src="../assets/img/cart/social_bitcoin_casino_cryptocurrency_icon_133203.svg"
                         style="width: 70px; height: 70px;">
                    <h2 class="bold">Криптовалюта</h2>
                  </div>
                </a>
              </div>
              <div class="col-md-4">
                <a href="#">
                  <div class="news-block news-block-world py-4 mb-4 white-text eff-h-two"
                       style="background-color: #B8EFCF;"
                       @click="$router.push({name: 'Education', params: {'category': 'Иностранные языки', 'ageGroup': 'teens'}})">
                    <img src="../assets/img/cart/1153499251637753558.svg" style="width: 70px; height: 70px;">
                    <h2 class="bold">Иностранные языки</h2>
                  </div>
                </a>
              </div>
              <div class="col-md-4">
                <a href="#">
                  <div class="news-block news-block-world py-4 mb-4 white-text eff-h-two"
                       style="background-color: #FFE38E;"
                       @click="$router.push({name: 'Education', params: {'category': 'Маркетинг', 'ageGroup': 'adults'}})">
                    <img src="../assets/img/cart/seo_training_marketing_presentation_icon_192451.svg"
                         style="width: 70px; height: 70px;">
                    <h2 class="bold">Маркетплейс</h2>
                  </div>
                </a>
              </div>
              <div class="col-md-12">
                <a href="#">
                  <div class="news-block news-block-world py-5 mb-4 white-text eff-h-two"
                       style="background-color: #FFEEF6;">
                    <h2 class="bold my-0">Образовательные программы на базе Высшей Школы Экономики</h2>
                  </div>
                </a>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <section class="video">
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
              <iframe class="iframe eff-h" width="560" height="315" src="https://www.youtube.com/embed/wfMvlFZ99RM"
                      rel="nofollow noopener noreferrer" target="_blank" title="YouTube video player" frameborder="0"
                      allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                      allowfullscreen></iframe>
              <!--/noindex-->
            </div>
          </div>
        </div>
      </div>
    </section>

    <div class="white-section">
      <div class="container">
        <div class="row">
          <div class="col-md-8">
            <h3 class="bold">Актуальные знания от признанных экспертов рынка для новичков и практикующих специалистов.</h3>
          </div>
        </div>
      </div>
    </div>

    <div class="white-section">
      <div class="container">
        <div class="row">
          <div class="text-gradient-wrapper">
            <div class="col-md-4">
              <h3 class="text-gradient mt-4 mb-0">33</h3>
              <p class="expanded__text bold px-1">Курса</p>
            </div>
            <div class="col-md-4">
              <h3 class="text-gradient mt-4 mb-0">22</h3>
              <p class="expanded__text bold px-1">Ведущих преподавателя</p>
            </div>
            <div class="col-md-4">
              <h3 class="text-gradient mt-4 mb-0">1000</h3>
              <p class="expanded__text bold px-1">Довольных студентов</p>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="white-section mt-3 mb-5">
      <div class="container">
        <div class="row ">
          <div class="col-md-12">
            <div class="container news-block py-4 mb-4" style="background-color: #F7BC75;">
              <div class="row">
                <div class="open-day open-day_home d-flex">
                  <div class="open-day__inner d-flex">
                    <div class="date" v-if="dateOpenDoors">
                      <span class="date__numder">{{ dateOpenDoors.getDate() }}</span>
                      <span class="date__month">{{ formatDate(dateOpenDoors, true) }}</span>
                    </div>
                    <div class="excursion">
                      <h2 class="excursion__open-day excursion__open-day_home">День открытых дверей</h2>
                      <p class="excursion__desc excursion__desc_home">Приглашаем всех желающих на бесплатную экскурсию
                        в мир востребованных профессий и полезных навыков</p>
                    </div>
                  </div>
                  <button type="button" class="button-open-day"
                          @click="goTo('Requests', {purpose: 'event', course: 'null', event: '1'})">
                    Записаться
                  </button>
                </div>
              </div>
            </div>
          </div>
        </div>

        <div class="row">
          <div class="col-md-5">
            <div class="news-block news-block-programs py-4 mb-4 eff-h-one" style="background-color: #C5DDFF; ">
              <img src="../assets/img/cart/education.svg">
              <h2 class="bold mb-4">Программы обучения</h2>
              <p class="news-block-text px-3" style="text-align: center">В списке наших курсов вы сможете найти профессию и занятие по
                душе, изучить новое и получить практические знания, которые помогут получить работу мечты.</p>
              <a href="/education" class="button-open-day button-open-day_home"
                 @click="goToCategory('Education')">
                Подробнее
              </a>
            </div>
          </div>
          <div class="col-md-7">
            <div class="row">
              <div class="col-md-6">
                <a href="/news">
                  <div class="news-block py-4 mb-4 eff-h-two" style="background-color: #B8EFCF;">
                    <img src="../assets/img/cart/news-main.svg">
                    <h2 class="bold">Новости академии</h2>
                  </div>
                </a>
              </div>
              <div class="col-md-6">
                <a href="">
                  <div class="news-block news-block-world py-4 mb-4 white-text eff-h-two" style="background-color: #FFEEF6;">
                    <img src="../assets/img/cart/it-world.svg">
                    <h2 class="bold">Мир IT</h2>
                  </div>
                </a>
              </div>
            </div>
            <div class="col-md-12">
              <div class="news-block py-4 mb-4 tests eff-h-two" style="background-color: #FFE38E;">
                <div class="row">
                  <a href="">
                    <div class="news-block-wrapp">
                      <div class="col-md-4 news-block-img">
                        <img src="../assets/img/cart/tests.svg" class="test-img-md">
                      </div>
                      <div class="col-md-8">
                        <h2 class="left-align  bold px-3 title-test-md">Попробуй!</h2>
                        <p class="news-block-text px-3 text-test-md">Пройдите тест и узнайте свои способности в сфере
                          информационных технологий</p>
                      </div>
                    </div>
                  </a>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <Reviews></Reviews>

    <div class="white-section mt-3 mb-5 white-section-welcome">
      <div class="container">
        <div class="row mb-5">
          <div class="col-md-12">
            <h2 class="center bold">Добро пожаловать в Академию будущего ХОД</h2>
          </div>
        </div>
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
    </div>
  </div>
</template>


<script>
import Navbar from "../components/NavbarMain";
import Reviews from "../components/Reviews";
import axios from "axios";
import {playerMixin} from "../components/mixins/playerMixin";
import {requestsMixin} from "../components/mixins/requestsMixin";

export default {
  title: 'Академия будущего',
  description: 'Академия будущего',
  name: 'Home',
  components: {
    Navbar, Reviews
  },

  mixins: [playerMixin, requestsMixin],

  data() {
    return {
      age_group: 'children',
      categoryList: [],
      typesRus: {
        'profession': 'Профессия',
        'course': 'Курс'
      },
      dateOpenDoors: null,
      dateOpenDoorsID: 1,
    }
  },

  created() {
    this.loadCategoryList();
    this.loadEventList();
  },

  methods: {
    async loadCategoryList() {
      await axios
          .get(`${this.$store.getters.getServerUrl}/categories/`)
          .then(response => (this.categoryList = response.data));
    },

     async loadEventList() {
      await axios
          .get(`${this.$store.getters.getServerUrl}/events/`)
          .then(response => (this.eventsList = response.data));
      this.getDateOpenDoors();
    },

    getDateOpenDoors() {
      for (let itemEvent of this.eventsList) {
        if (itemEvent.open_doors_day) {
          this.dateOpenDoors = new Date(itemEvent.date);
          this.dateOpenDoorsID = itemEvent.id;
        }
      }
    },

    formatDate(date, onlyMonth) {
      let d1 = new Date(date);
      let ms = [
          'января', 'февряля', 'марта', 'апреля', 'мая', 'июня',
        'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря'
      ];
      if (onlyMonth) {
        return ms[d1.getMonth()];
      }
      return d1.getDate() + ' ' + ms[d1.getMonth()] + ' ' + d1.getFullYear();
    },

    goToCategory(name) {
      this.$router.push({name: 'Education', params: {'category': name, 'ageGroup': this.age_group}})
    },

    setAgeGroup(group) {
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

.news-block {
  border: none;
  border-radius: 10px;
  text-align: center;
}

.news-block-text {
  text-align: left;
}

.welcome-block {
  padding: 30px;
}

.welcome-block img {
  height: 60px;
  margin-bottom: 40px;
}
</style>