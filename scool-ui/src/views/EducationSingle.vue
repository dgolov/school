<template>
  <div id="single">
    <navbar-main></navbar-main>
    <div class="header-page-wrapper d-none d-lg-block">
      <div class="chess-course">
        <div class="chess-course-img-wrapp">
          <img v-if="course.category.age_group === 'adults'" src="../assets/img/header/employment-course.jpg"
               alt="" class="chess-course__img">
          <img v-else src="../assets/img/header/shutterstock_1337001122.jpg" alt="" class="chess-course__img">
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
        <img src="../assets/img/header/employment-course.jpg" alt="" class="chess-course__img" style="align-self:center">
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
        <div class="row">
          <div class="col-lg-4 mb-3">
            <div class="owl owl-events">
              <img src="../assets/img/owl/owl-main.png" class="owl__main owl__main-events ">
              <span class="owl__frame-events owl-frame-employment"></span>
              <div class="owl-text owl-text-events owl-text-employment">
                <p class="owl-desc owl-desc-events">Получите востребованную профессию и возможность открыть бизнес в
                  сфере информационных технологий!</p>
              </div>
            </div>
          </div>
          <div class="col-12 col-lg-8">
            <div class="events-title-wrapp">
              <div class="events-title__inner">
                <span class="events-title__cross"></span>
                <h3 class="events-title__subject">Актуальные программы</h3>
<!--                <p class="events-title__text">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce mi elit,-->
<!--                  egestas ut feugiat id, laoreet volutpat risus. Cras condimentum, ligula eget</p>-->
              </div>
              <div class="events-title__inner ">
                <span class="events-title__circle"></span>
                <h3 class="events-title__subject">Удобный для вас формат обучения</h3>
              </div>
              <div class="events-title__inner">
                <span class="events-title__triangle"></span>
                <h3 class="events-title__subject">Помощь в трудоустройстве</h3>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

<!--    <section class="video v-a-a c-c">-->
<!--      <div class="container">-->
<!--        <div class="row justify-content-center" style="position:relative;z-index: 1;">-->
<!--          <div class="col-md-12 col-lg-8">-->
<!--            <div class="video-wrapper video-wrapper_chess-course">-->
<!--              <div class="video__link" id="video__link">-->
<!--                        <span class="video__circle">-->
<!--                            <img src="../assets/img/video/play.svg" alt="" class="video__play">-->
<!--                        </span>-->
<!--              </div>-->
<!--              <span class="video-content__triangle video-content-position"></span>-->
<!--              <span class="video-content__line-left video-content-position"></span>-->
<!--              <span class="video-content__line-right video-content-position"></span>-->
<!--              <span class="video-content__cross video-content-position"></span>-->
<!--            </div>-->
<!--            <div class="wrapper-modal" id="wrapper-modal">-->
<!--              <div class="overlay" id="overlay"></div>-->
<!--              &lt;!&ndash;noindex&ndash;&gt;-->
<!--              <iframe class="iframe" width="560" height="315" src="https://www.youtube.com/embed/64E1DnxBRyE"-->
<!--                      rel="nofollow noopener noreferrer" target="_blank" title="YouTube video player" frameborder="0"-->
<!--                      allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"-->
<!--                      allowfullscreen></iframe>-->
<!--              &lt;!&ndash;/noindex&ndash;&gt;-->
<!--            </div>-->
<!--          </div>-->
<!--        </div>-->
<!--      </div>-->
<!--    </section>-->

    <section class="profession-info">
      <div class="container">
        <div class="row">
          <div class="col-12" v-if="course.profession">
            <h2 class="program-events-title">Кто такой {{ course.profession.name }}</h2>
            <p class="chess-school-decs e-c-desc">{{ course.who_is }}</p>
          </div>
          <div class="col-12" v-if="course.skills">
            <h2 class="program-events-title">Вы научитесь:</h2>
          </div>
          <div class="col-md-12 col-lg-9" v-if="course.skills">
            <ul class="skills">
              <li class="skills__item" v-for="skill in course.skills">{{ skill.text }}</li>
            </ul>
          </div>
        </div>
      </div>
    </section>

    <section class="program">
      <div class="container">
        <div class="row">
          <div class="col-12">
            <h2 class="program-title">Эта программа <span></span> подойдет тем, кто</h2>
          </div>
          <div class="col-12">
            <div class="program-info-wrapp">
              <div class="header-desc" v-if="course.category.age_group === 'adults'">
                <h4 class="program-info-title">Никогда не работал</h4>
                <p class="program-info-text">и хочет получить востребованную профессию, трудоустроиться или создать
                  собственный бизнес с нуля</p>
              </div>
              <div class="header-desc" v-else>
                <h4 class="program-info-title">Много времени проводит за компьютером</h4>
                <p class="program-info-text">и хочет это делать не только для развлечения, но и с пользой для своего
                  развития</p>
              </div>
              <div class="header-desc" v-if="course.category.age_group === 'adults'">
                <h4 class="program-info-title">Хочет научиться новому</h4>
                <p class="program-info-text">и попробовать себя в интересной и востребованной професии</p>
              </div>
              <div class="header-desc" v-else>
                <h4 class="program-info-title">Хочет научиться новому</h4>
                <p class="program-info-text">и готов пробовать разные направления IT-сферы, чтобы выбрать лучшее</p>
              </div>
              <div class="header-desc" v-if="course.category.age_group === 'adults'">
                <h4 class="program-info-title">Хочет сменить работу</h4>
                <p class="program-info-text">и получить актуальную высокооплачиваемую специальность в IT</p>
              </div>
              <div class="header-desc" v-else>
                <h4 class="program-info-title">Мечтает стать айтишником</h4>
                <p class="program-info-text">и хочет примерить на себя профессию программиста, веб-разработчика или
                  дизайнера.</p>
              </div>
            </div>
            <button class="button button-header  e-c-button" type="button" @click="pay()">Записаться на курс</button>
          </div>
        </div>
      </div>
    </section>

    <section class="our-values e-c-course">
      <div class="container">
        <div class="row">
          <div class="col-12">
            <h2 class="program-events-title">Принципы обучения</h2>
          </div>
          <div class="col-12">
            <div class="worth-wrapper">
              <div class="worth worth-course">
                <img src="../assets/img/founder/worth-one.svg" alt="icon" class="worth__icon">
                <p class="worth__text">Передовой подход к образовательному процессу</p>
              </div>
              <div class="worth worth-course">
                <img src="../assets/img/founder/worth-four.svg" alt="icon" class="worth__icon">
                <p class="worth__text">Непрерывное усовершенствование и пополнение базы курсов</p>
              </div>
              <div class="worth worth-course">
                <img src="../assets/img/founder/worth-six.svg" alt="icon" class="worth__icon">
                <p class="worth__text">Только практикующие преподаватели</p>
              </div>
              <div class="worth worth-course">
                <img src="../assets/img/founder/worth-two.svg" alt="icon" class="worth__icon">
                <p class="worth__text">Сопровождение на всех этапах. От начала обучения до трудоустройства</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class="earnings" v-if="course.profession">
      <div class="container">
        <div class="row">
          <div class="col-12">
            <h2 class="program-events-title mt-0 mb-5">Сколько зарабатывает {{ course.profession.name }}</h2>
          </div>
          <div class="earnings-inner">
            <div class="col-md-5 col-lg-4">
              <div class="level">
                <h5 class="level__name">{{ course.profession.junior_name }}</h5>
                <p class="level__desc">Обычно на позицию Junior претендуют выпускники, которые только закончили
                  профильное образование или имеют небольшой опыт в разработке.</p>
                <span class="level__price">от  {{ course.profession.salary_junior }} ₽ в месяц</span>
              </div>
            </div>
            <div class="col-md-5 col-lg-4">
              <div class="level level_green">
                <h5 class="level__name">{{ course.profession.middle_name }}</h5>
                <p class="level__desc">Они уже имеют хороший опыт работы, достаточный уровень знания языков
                  программирования и понимания стека технологий, могут справляться с задачами самостоятельно.</p>
                <span class="level__price">от  {{ course.profession.salary_middle }} ₽ в месяц</span>
              </div>
            </div>
            <div class="col-md-5 col-lg-4">
              <div class="level level_orange">
                <h5 class="level__name">{{ course.profession.senior_name }}</h5>
                <p class="level__desc">Это исключительный специалист, который в полной мере овладел стеком технологий и
                  языками программирования, необходимыми в его работе. </p>
                <span class="level__price">от  {{ course.profession.salary_senior }} ₽ в месяц</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class="past-events education">
      <div class="container">
        <div class="row">
          <div class="col-12">
            <h2 class="program-events-title mt-0 mb-4">Как проходит обучение</h2>
          </div>
          <div v-if="course.category.age_group === 'children' || course.category.age_group === 'teens'"
               class="col-12 col-sm-5 col-lg-3">
            <div class="education-wrapp">
              <div class="header-desc">
                <p class="education-text">
                  Наша уникальная программа сможет открыть ребенку безграничные возможности в обучении. Позволит
                  развить у учеников стремление и способности к непрерывному образованию в течение всей жизни.
                  Сформирует у учащихся критическое и рефлексивное мышление, а также способностей к самоорганизации.
                </p>
              </div>
            </div>
          </div>
          <div v-if="course.category.age_group === 'children' || course.category.age_group === 'teens'"
               class="col-12 col-sm-5 offset-sm-1 col-lg-3 offset-lg-0">
            <div class="education-wrapp">
              <div class="header-desc">
                <p class="education-text">
                  В соответствии с этими представлениями наша академия видит образование как целенаправленный
                  развивающий процесс, который приводит к определенному результату — становлению человека, развитию у
                  него интегральных человеческих качеств и способностей, которые позволяют человеку развиваться гораздо
                  быстрее, открывать новые горизонты , стать объектом собственного развития и собственной жизни.
                </p>
              </div>
            </div>
          </div>
          <div v-if="course.category.age_group === 'children' || course.category.age_group === 'teens'"
               class="col-12 col-sm-5 col-lg-3">
            <div class="education-wrapp">
              <div class="header-desc">
                <p class="education-text">
                  В своем образовательном процессе мы применяем принцип обучения по пирамиде Дейла, что способствует
                  лучшему усвоению материала. В совокупности с применением STEAM технологий, целью которых является
                  развитие интеллектуальных способностей ребенка с возможностью вовлечения его в научно-техническое
                  творчество, мы комплексно работаем с ребятами в интересных для них направлениях.
                </p>
              </div>
            </div>
          </div>
          <div v-if="course.category.age_group === 'children' || course.category.age_group === 'teens'"
               class="col-12 col-sm-5 offset-sm-1 col-lg-3 offset-lg-0">
            <div class="education-wrapp">
              <div class="header-desc">
                <p class="education-text">
                  Программа обучения –авторская, разработанная с анализом современных педагогических критериев в
                  европейской системе образования. Родители всегда видят результат занятий в выполненных проектах
                  наших детей.
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="carousel-past-events">
        <div class="gallery">
          <img src="../assets/img/education/education-one.jpg" alt="слайд 1" class="past-events-img">
        </div>
        <div class="gallery">
          <img src="../assets/img/education/education-two.jpg" alt="слайд 2" class="past-events-img">
        </div>
        <div class="gallery">
          <img src="../assets/img/education/education-three.jpg" alt="слайд 3" class="past-events-img">
        </div>
        <div class="gallery">
          <img src="../assets/img/education/education-four.jpg" alt="слайд 4" class="past-events-img">
        </div>
        <div class="gallery">
          <img src="../assets/img/education/education-five.jpg" alt="слайд 5" class="past-events-img">
        </div>
        <div class="gallery">
          <img src="../assets/img/education/education-six.jpg" alt="слайд 5" class="past-events-img">
        </div>
      </div>
    </section>

    <!--Блок cодержание курса -->
    <section class="course-content">
      <div class="container">
        <div class="row">
          <div class="col-lg-10">
            <h2 class="program-events-title mt-0 mb-3">Содержание курса</h2>
            <div class="col-12">
              <ul class="skills skills_two">
                <li class="skills__item skills__item_marker" v-for="item in contentList">{{ item }}</li>
              </ul>
            </div>
          </div>

          <div class="col-lg-5">
            <div class="course-conten-wrapp">
              <div class="header-desc header-desc_tiny  c-c-course">
                <p class="chess-course-info chess-course-info_small">Срок обучения: <span></span> {{ course.duration }}
                </p>
              </div>
              <div class="header-desc header-desc_small c-c-course c-c-l">
                <p class="chess-course-info chess-course-info_big">Режим занятий: <span></span> {{
                    course.activity_mode
                  }}</p>
              </div>
            </div>
            <div class="course-conten-wrapp">
              <div class="header-desc  header-desc_big">
                <p class="chess-course-info chess-course-info_price ">от {{ course.price }} ₽ в месяц</p>
              </div>
            </div>
            <button class="button button-header c-c-button" type="button">Записаться на курс</button>
          </div>
          <div class="col-lg-4 mb-3" style="position: relative;">
            <div class="owl owl-events owl-course">
              <img src="../assets/img/owl/owl-main.png" class="owl__main owl__main-events olw__c-c">
              <span class=" owl__frame-course"></span>
              <div class="owl-text owl-text-events owl-text-c-c">
                <p class="owl-desc owl-desc-events">1 занятие бесплатное</p>
              </div>
            </div>
            <div class="course-figure">
              <span class="education-one"></span>
              <span class="education-two"></span>
              <span class="education-three"></span>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class="teachers" v-if="course.teachers.length > 0">
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
                    <img v-if="teacher.avatar" :src="`${teacher.avatar.image}`" alt=" Фото преподавателя" class="profile-avatar">
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

    <section class="employment-business" v-if="course.category.age_group === 'adults'">
      <div class="container">
        <div class="row">
          <div class="col-12">
            <h2 class="program-events-title mt-0 mb-5">Трудоустройство или создание бизнеса</h2>
          </div>
          <div class="employment-business-wrapp">
            <div class="col-12 col-lg-6">
              <div class="cart-e-b">
                <h4 class="cart-e-b__title mt-0">Трудоустройство</h4>
                <p class="cart-e-b__desc">Полученный уровень образования позволит претендовать на реальные вакансии и
                  начать карьеру в сфере IT. Мы подберем подходящие предложения, собрем портфолио и резюме, подготовим к
                  собеседованию, научимся выполнять тестовые задания и поможем с трудоустройством.</p>
                <span class="cart-e-b__text">Планируемый доход:</span>
                <span class="cart-e-b__income">80 000—200 000 ₽ в месяц</span>
              </div>
            </div>
            <div class="col-12 col-lg-6">
              <div class="cart-e-b cart-e-b_green">
                <h4 class="cart-e-b__title mt-0">Создание бизнеса</h4>
                <p class="cart-e-b__desc cart-e-b__desc_lg">Совместно с другими студентами, вы будете продвигать,
                  разрабатывать, тестировать, и реализовывать бизнес-идеи. А также получите дополнительное обучение по
                  запуску бизнеса от экспертов приглашенных компаний.</p>
                <span class="cart-e-b__text">Планируемый доход:</span>
                <span class="cart-e-b__income">120 000—400 000 ₽ в месяц</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class="summary" v-if="course.profession">
      <div class="container">
        <div class="row">
          <div class="col-12">
            <h2 class="program-events-title mt-0 mb-5">Ваше будущее резюме</h2>
          </div>
          <div class="col-12">
            <div class="summary-wrapper">
              <div class="summary-cap">
                <div class="summary-cap__inner">
                  <div class="summary-wrapp-sm">
                    <div class="teacher__avatar summary-photo">
                                    <span class="teacher__circle summary-circle">
                                        <img src="../assets/img/diploma/photo.png" alt=" Фото резюме"
                                             class="teacher__photo summary-icon">
                                    </span>
                    </div>
                    <div class="post-name-wrapp">
                      <p class="post mb-2">Должность:</p>
                      <h5 class="post-name mt-1">{{ course.profession.name }}</h5>
                    </div>
                  </div>
                  <span class="border-summary border-summary_sm"></span>
                  <div class="money-wrapp">
                    <p class="salary-from mb-2">Зарплата от:</p>
                    <span class="money mt-1">{{ course.profession.salary_resume }} ₽</span>
                  </div>
                </div>
                <span class="border-summary b-s-sm"></span>


                <div class="skilss-wrapp">
                  <p class="skilss-title">Профессиональные навыки:</p>
                  <ul class="skills skills-summary">
                    <li class="skills__item skills__item_size" v-for="skill in course.profession.skills">
                      {{ skill.text }}
                    </li>
                  </ul>
                </div>
                <span class="border-summary"></span>

                <div class="diploma-wrapp ">
                  <div class="diploma-phopto eff-h-three">
                    <img src="../assets/img/diploma/diploma.png" alt="">
                  </div>
                  <div class="diploma-text">
                    <h4 class="diploma-title mt-2">Диплом ХОД Future Academy</h4>
                    <p class="diploma-decs">Подтвердит, что вы прошли курс, и станет дополнительным аргументом при
                      устройстве на работу.</p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <Reviews v-if="course.category.age_group === 'adults'"></Reviews>

    <Faq></Faq>
  </div>
</template>

<script>

import {requestsMixin} from "../components/mixins/requestsMixin";
import NavbarMain from "../components/NavbarMain";
import Lessons from "../components/Course/Lessons";
import HowGoing from "../components/Course/HowGoing";
import axios from "axios";
import Reviews from "../components/Reviews";
import Faq from "../components/Faq";
import {redirect} from "../components/mixins/redirect";

export default {
  title: 'Академия будущего | Обучение',
  name: "EducationSingle",

  mixins: [requestsMixin, redirect],

  components: {Lessons, HowGoing, NavbarMain, Reviews, Faq},

  data() {
    return {
      course: {},
      contentList: [],
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
    this.loadCourse();
  },

  methods: {
    async loadCourse() {
      await axios
          .get(`${this.$store.getters.getServerUrl}/courses/${this.id}`)
          .then(response => (this.course = response.data))
      this.contentList = this.course.content.split('.');
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
  box-shadow: 42px -37px 20px -31px rgb(39 170 237 / 35%),
  55px 56px 20px -47px rgb(39 170 225 / 35%),
  -41px 40px 20px -34px rgb(247 148 29 / 40%),
  -57px -54px 20px -50px rgb(247 148 29 / 40%);
  transition: box-shadow 0.8s ease;
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
  border: none;
  box-shadow: 18px 14px 20px -13px rgb(39 170 237 / 35%),
  26px -18px 20px -21px rgb(39 170 225 / 35%),
  -18px 7px 20px -12px rgb(247 148 29 / 40%),
  -28px -22px 20px -22px rgb(247 148 29 / 40%);
  transition: box-shadow 0.8s ease;
}

</style>