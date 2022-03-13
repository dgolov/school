<template>
  <div class="about">
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

    <div class="steps white-section mt-3 pt-0 st">
      <div class="container">
        <div class="row">
          <div class="owl-title-wrapp">
            <div class="col-md-3 mb-3">
              <div class="owl">
                <img src="../assets/img/owl/owl-main.png" class="owl__main owl-m-aa">
                <span class="owl__frame o-f-aa"></span>
                <div class="owl-text owl-a-a">
                  <h5 class="owl-title">Приветствуем в Академии будущего ХОД!</h5>
                  <p class="owl-desc">Вам у нас понравится:)</p>
                </div>
              </div>
            </div>

            <div class="col-12 col-md-9 col-lg-8">
              <div class="events-title-wrapp">
                <div class="events-title__inner">
                  <span class="events-title__cross"></span>
                  <h3 class="events-title__subject">Мы создали Академию </h3>
                  <p class="events-title__text">для детей, чтобы компьютер был не зависимостью и игрушкой, а другом на
                    пути обучения и развития.</p>
                </div>
                <div class="events-title__inner ">
                  <span class="events-title__circle"></span>
                  <h3 class="events-title__subject">Мы создали Академию</h3>
                  <p class="events-title__text">для подростков, чтобы «Кем я хочу стать?» больше не был самым сложным
                    вопросом.</p>
                </div>
                <div class="events-title__inner">
                  <span class="events-title__triangle"></span>
                  <h3 class="events-title__subject">Мы создали Академию</h3>
                  <p class="events-title__text">для взрослых, чтобы у них была возможность начать с читатого листа и
                    создать лучшую версию себя в любом возрасте.</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <section class="video v-a-a">
      <div class="container">
        <div class="row justify-content-center" style="position:relative;z-index: 1;">
          <div class="col-md-12 col-lg-8">
            <div class="video-wrapper video-wrapper_about-academy">
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
              <div class="overlay" @click="videoClose()"></div>
              <!--noindex-->
              <iframe class="iframe" width="560" height="315" src="https://www.youtube.com/embed/64E1DnxBRyE"
                      rel="nofollow noopener noreferrer" target="_blank" title="YouTube video player" frameborder="0"
                      allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                      allowfullscreen></iframe>
              <!--/noindex-->
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class="founder">
      <div class="container">
        <div class="row">
          <div class="founder-wrapper">
            <div class="col-lg-4">
              <div class="founder-person">
<!--                <img src="../assets/img/owl/owl-main.png" alt="Основатель Академии будущего ХОД"-->
<!--                     class="founder-person__photo" style="margin: auto;">-->
              </div>
            </div>
            <div class="col-md-12">
              <div class="founder-info">
                <h2 class="program-events-title">Кто мы?</h2>
                <p class="founder-info__text">Организация дополнительного образования детей от 8 до 18 и взрослых от
                  18 до 50 лет
                </p>
                <p class="founder-info__text">
                  Уникальная авторская программа обучения с учетом современных информационных,
                  технологических и педагогических подходов и методик.
                </p>
                <p class="founder-info__text">
                  Индивидуальный подход, возможность построения индивидуальной траектории обучения
                </p>
                <p class="founder-info__text">
                  Сопровождение на протяжении всего периода обучения
                </p>
                <p class="founder-info__text">
                  Авторы программ - действующие практики из крупных ИТ компаний, не просто знающие, но и диктующие актуальные тренды
                </p>
                <p class="founder-info__text">
                  Наши программы комплексные: на равне с Hard skills, мы формируем "мягкие навыки" и верим, что настоящему специалисту без умения осуществлять эффективную коммуникацию не обойтись.
                </p>
                <p class="founder-info__text">
                  Детские программы пролонгированные и направлены на всестороннее развитие ребёнка, составлены с учётом возрастных особенностей.
                </p>
                <p class="founder-info__text">
                  Шахматы - лучшее средство развития интеллекта и логики, игра вне возврата и времени. Шахматы тренируют характер, умение принимать решения и стратегически действовать. Наверное, лучший спорт для успешной жизни.
                </p>
                <p class="founder-info__text">
                  Английский язык - средство быть на ступеньку выже каждого, кто умеет то же самое, но не готов к международному уровню. Мы и наши студенты стремимся именно туда.
                </p>
                <p class="founder-info__text">
                  Профессионалы организации образовательного процесса, учитывающие возрастные особенности студентов, их предпочтения и интересы, готовые помочь грамотно выстроить карьеру с нуля.
                </p>
                <p class="founder-info__text">
                  Наша миссия – обеспечить возможность всем желающим получить современное образование в сфере IT-технологий; детям – помочь в развитии и становлении личности, подросткам – опыт предпрофессиональной и проектной деятельности, взрослым – начать ИТ-карьеру или углубить знания в одной из специализаций. Образование – это движущая сила любого процесса. Технологии опережают образование в школах и университетах, а мы готовы идти в ногу со временем и обгонять его, чтобы миром правили технологии, а технологиями правили наши выпускники.
                </p>
              </div>
            </div>
          </div>
        </div>
        <div class="row">
          <div class="col-md-12">
            <h2 class="program-events-title mb-3">Наши принципы</h2>
            <ul class="mb-5">
              <li class="mb-2">Успех любой организации в ее организации: самые актуальные и эффективные административные
                подходы и опытная управленческая команда обеспечат максимальный результат.</li>
              <li class="mb-2">Самый ценный ресурс – время. Бережливые технологии и тайм-менеджмент – наши верные друзья</li>
              <li class="mb-2">Иди туда, где страшно: мы постоянно развиваемся сами и готовы держать вас за руку на пути
                самосовершенствования.</li>
              <li class="mb-2">Доброта – залог здоровья. Мы заботимся о каждом студенте и сотруднике, делая все
                возможное для их комфорта и успеха.</li>
              <li class="mb-2">Честность – лучшая политика. Прозрачность всех процессов, ваша полная осведомленность на
                каждом этапе обучения и сотрудничества.</li>
            </ul>
            <h3 class="mb-5 program-events-title">Три верных друга (три кита):</h3>
            <div class="events-title-wrapp row">
              <div class="col-md-4">
                <span class="events-title__circle mb-4"></span>
                <h3 class="events-title__subject">Опыт</h3>
              </div>
              <div class="col-md-4">
                <span class="events-title__triangle mb-4"></span>
                <h3 class="events-title__subject">Целеустремленность</h3>
              </div>
              <div class="col-md-4">
                <span class="events-title__cross mb-4"></span>
                <h3 class="events-title__subject">Хорошие люди</h3>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class="our-values">
      <div class="container">
        <div class="row">
          <div class="col-12">
            <h2 class="program-events-title">Наши ценности</h2>
          </div>
          <div class="col-12">
            <div class="worth-wrapper">
              <div class="worth">
                <img src="../assets/img/founder/worth-one.svg" alt="icon" class="worth__icon">
                <p class="worth__text">Содержание обучения должно быть актуальным, а методика проверенная годами.</p>
              </div>
              <div class="worth">
                <img src="../assets/img/founder/worth-two.svg" alt="icon" class="worth__icon">
                <p class="worth__text">Педагог - прежде всего личность компетентная и харизматичная.</p>
              </div>
              <div class="worth">
                <img src="../assets/img/founder/worth-three.svg" alt="icon" class="worth__icon">
                <p class="worth__text">Точка развития образования - ребенок, его интересы и потребности</p>
              </div>
              <div class="worth">
                <img src="../assets/img/founder/worth-four.svg" alt="icon" class="worth__icon">
                <p class="worth__text">Прогрессом правит любовь к знаниям</p>
              </div>
              <div class="worth">
                <img src="../assets/img/founder/worth-six.svg" alt="icon" class="worth__icon">
                <p class="worth__text">Технологии правят миром, а человек эти технологии создает</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class="teachers" v-if="teachers">
    <div class="row">
      <div class="col-12">
        <h2 class="reviews-title">Наши люди</h2>
      </div>
    </div>
    <div class="row">
      <div class="col-12">
        <div class="teachers-wrapp">
          <div class="carousel" v-for="teacher of teachers">
            <div class="col-3" v-if="teacher.is_show">
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

    <section class="our-programs">
      <div class="container">
        <div class="row">
          <div class="col-12">
            <h2 class="program-events-title">Наши программы</h2>
          </div>
          <div class="col-12">
            <div class="programs-wrapper">
              <p class="programs-info">Предполагают пролонгированное обучение</p>
              <p class="programs-info">Составлены с учетом возрастных и индивидуальных особенностей детей</p>
              <p class="programs-info">Авторские и не имеют аналогов</p>
              <p class="programs-info">Составлены на основе деятельностного и компетентностного подходов</p>
              <p class="programs-info">Реализуются с помощью современных педагогических технологий</p>
              <p class="programs-info">Актуальны и фундаментальны</p>
            </div>
          </div>
          <div class="text-gradient-wrapper">
            <div class="col-md-3">
              <h3 class="text-gradient mt-4 mb-0">33</h3>
              <p class="expanded__text bold px-1 o-p">Курса</p>
            </div>
            <div class="col-md-3 t-g">
              <h3 class="text-gradient mt-4 mb-0">22</h3>
              <p class="expanded__text bold px-1 o-p">Ведущих преподователя</p>
            </div>
            <div class="col-md-5">
              <h3 class="text-gradient mt-4 mb-0">1000</h3>
              <p class="expanded__text bold px-1 o-p">Выпускников</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class="our-partners">
      <div class="container">
        <div class="row">
          <div class="col-12">
            <h2 class="program-events-title">Наши партнеры</h2>
          </div>
          <div class="partners-wrapper">
            <div class="partners-block mb-lg-4 mb-0">
              <div class="col-md-4 col-lg-3 col-xl-2">
                <div class="partners-cart p-c-l eff-h-three">
                  <img src="../assets/img/our-partners/our-partners-one.png" alt="партнер" class="partner-img">
                </div>
              </div>
              <div class="col-md-4 col-lg-3 col-xl-2">
                <div class="partners-cart eff-h-three">
                  <img src="../assets/img/our-partners/our-partners-two.png" alt="партнер" class="partner-img">
                </div>
              </div>
              <div class="col-md-4 col-lg-3 col-xl-2">
                <div class="partners-cart p-c-r eff-h-three">
                  <img src="../assets/img/our-partners/our-partners-three.png" alt="партнер" class="partner-img">
                </div>
              </div>
              <div class="col-md-4 col-lg-3 col-xl-2">
                <div class="partners-cart p-c-l  eff-h-three">
                  <img src="../assets/img/our-partners/our-partners-four.png" alt="партнер" class="partner-img">
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class="click-on">
      <div class="container">
        <div class="row">
          <div class="col-12">
            <h2 class="program-events-title">Нажми, если это о тебе</h2>
          </div>
          <div class="click-on-wrapp">
            <div class="col-lg-3">
              <a href="#" class="click-cart click-cart_blue eff-h-four">
                <img src="../assets/img/click-on/click-on-one.svg" alt="one-icon" class="click-cart__icon">
                <p class="click-cart__info">Я хочу, чтобы мой ребенок был успешным</p>
              </a>
            </div>
            <div class="col-lg-3">
              <a href="#" class="click-cart click-cart_yellow eff-h-four">
                <img src="../assets/img/click-on/click-on-two.svg" alt="two-icon" class="click-cart__icon">
                <p class="click-cart__info">Я хочу больше зарабатывать</p>
              </a>
            </div>
            <div class="col-lg-3">
              <a href="#" class="click-cart click-cart_violet eff-h-four">
                <img src="../assets/img/click-on/click-on-three.svg" alt="three-icon" class="click-cart__icon">
                <p class="click-cart__info">Мой ребенок не выпускает гаджет из рук</p>
              </a>
            </div>
            <div class="col-lg-3">
              <a href="#" class="click-cart click-cart_green eff-h-four">
                <img src="../assets/img/click-on/click-on-four.svg" alt="four-icon" class="click-cart__icon">
                <p class="click-cart__info">Я хочу стать айтишником</p>
              </a>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import Navbar from "../components/NavbarMain";
import {playerMixin} from "../components/mixins/playerMixin";
import axios from "axios";
import {requestsMixin} from "../components/mixins/requestsMixin";


export default {
  title: 'Академия будущего | Об Академии',
  name: "About",
  components: {
    Navbar
  },

  mixins: [playerMixin, requestsMixin],

  data() {
    return {
      teachers: {}
    }
  },

  created() {
    this.loadTeachers();
  },

  methods: {
    async loadTeachers() {
      await axios
          .get(`${this.$store.getters.getServerUrl}/teachers`)
          .then(response => (this.teachers = response.data))
    },
  },
}
</script>

<style scoped>

.profile-avatar {
  display: block;
  width: 130px;
  height: 130px;
  border: 0;
  border-radius: 50%;
  margin: auto;
  text-align: center;
}

</style>