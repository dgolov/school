<template>
  <div class="home">
    <navbar></navbar>
    <div class="header-wrapper d-none d-lg-block">
      <div class="header">
        <h1 class="header-title">Образовательная платформа ХОД Future Academy</h1>
        <p class="header-title__desc">Актуальные знания для новичков и профессионалов</p>
      </div>
    </div>
    <div class="header-mobi d-none">
      <img src="../assets/img/header/header-mobi.jpg" alt="" class="header-mobi__img">
      <div class="container">
        <div class="row">
          <div class="col-12">
            <div class="header-mobi-title">
              <h1 class="header-title">Образовательная платформа ХОД Future Academy</h1>
              <p class="header-title__desc">Актуальные знания для новичков и профессионалов</p>
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
            <h2 class="mb-4">Наиболее популярные курсы</h2>
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
            <div class="row">
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
            <h3 class="bold">Актуальные знания от признанных экспертов рынка для новичков и практикующих
              специалистов.</h3>
          </div>
        </div>
      </div>
    </div>
    <div class="white-section">
      <div class="container">
        <div class="row">
          <div class="text-gradient-wrapper">
            <div class="col-md-4">
              <h3 class="text-gradient mt-4 mb-0">600</h3>
              <p class="expanded__text bold px-1">Курсов</p>
            </div>
            <div class="col-md-4">
              <h3 class="text-gradient mt-4 mb-0">82</h3>
              <p class="expanded__text bold px-1">Ведущих преподователей</p>
            </div>
            <div class="col-md-4">
              <h3 class="text-gradient mt-4 mb-0">14795</h3>
              <p class="expanded__text bold px-1">Выпускников</p>
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
                    <div class="date">
                      <span class="date__numder">25</span>
                      <span class="date__month">ноября</span>
                    </div>
                    <div class="excursion">
                      <h2 class="excursion__open-day excursion__open-day_home">День открытых дверей</h2>
                      <p class="excursion__desc excursion__desc_home">
                        Приглашаем всех желающих на бесплатную экскурсию в мир
                        востребованных профессий и полезных навыков
                      </p>
                    </div>
                  </div>
                  <button type="button" class="button-open-day">Записаться</button>
                  <!-- Если кнопка отправляет данные тогда type="submit, если нет то type="button"-->
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
              <p class="news-block-text px-3" style="text-align: center">В списке наших курсов вы сможете найти
                профессию и занятие по душе, изучить
                новое и получить практические знания, которые помогут получить работу мечты.</p>
              <a href="/education" class="button-open-day button-open-day_home" @click="goTo('Education')">Подробнее</a>
              <!-- <button class="button news-block-button w-50 mt-4 mb-4">Подробнее</button> -->
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
                        <p class="news-block-text px-3 text-test-md">Пройдите тест и узнайте свои способности в сфере информационных
                          технологий</p>
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

export default {
  title: 'Академия будущего',
  name: 'Home',
  components: {
    Navbar, Reviews
  },

  mixins: [playerMixin],

  data() {
    return {
      age_group: 'children',
      listCourses: [],
      typesRus: {
        'profession': 'Профессия',
        'course': 'Курс'
      }
    }
  },

  created() {
    this.loadCategoryList()
  },

  methods: {
    async loadCategoryList() {
      await axios
          .get(`${this.$store.getters.getServerUrl}/courses/`)
          .then(response => (this.listCourses = response.data));
    },

    goTo(name) {
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