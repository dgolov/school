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
                <img src="../assets/img/founder/founder-person__photo.jpg" alt="Основатель Академии будущего ХОД"
                     class="founder-person__photo">
                <h5 class="founder-person__name">Имя Фамилия</h5>
                <p class="founder-person__desc">Основатель Академии будущего ХОД</p>
              </div>
            </div>
            <div class="col-lg-7">
              <div class="founder-info">
                <p class="founder-info__text">«Все началось с любви к шахматам. Я хотел предвидеть ход противника, хотел
                  просчитать его действия, хотел побеждать. Я не стал гением шахмат, но стратег и психолог из меня
                  неплохой» - смеется Иван Иванович. Идея открыть Академию шахмат пришла к нему в 2020 году, когда в
                  период полного локдауна он вдруг вспомнил про хобби - игру в шахматы. Оказалось, что для игры в
                  шахматы сейчас и доска-то не обязательна, все есть в телефоне. Племянник (сын?) Ивана Ивановича
                  большую часть дня проводил в стрелялках на планшете.
                  <span></span>
                  «Я показал ему шахматы. К июню он уже был неплохим соперником» -
                  Вскоре идея небольшой академии шахмат превратилась в план создания Академии Будущего, где дети смогут
                  учиться тому, что им нравится, а взрослые попытаются изменить жизнь. Уж очень это сейчас актуально".
                </p>
                <span class="founder-info__desc">Из интервью с основателем Академии Будущего Ивановым И.И.</span>
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

    <section class="teachers">
      <div class="row">
        <div class="col-12">
          <h2 class="reviews-title">Наши люди</h2>
        </div>
      </div>
      <div class="row">
        <div class="col-12">
          <div class="teachers-wrapp">
            <div class="carousel">
              <!-- Контент 1 слайда -->
              <div class="col-3">
                <div class="teacher">
                  <div class="teacher__avatar">
                    <span class="teacher__circle">
                      <img src="../assets/img/teacher/teacher__photo-one.png" alt=" Фото преподавателя" class="teacher__photo">
                    </span>
                  </div>
                  <h4 class="teacher__name">Имя Фамилия</h4>
                  <p class="teacher__info">Выпускница Гарвардского Университета. Более 10 лет играет в шахматы и
                    участвует в турнирах.</p>
                </div>
              </div>
            </div>
            <div class="carousel">
              <!-- Контент 2 слайда -->
              <div class="col-3">
                <div class="teacher">
                  <div class="teacher__avatar">
                  <span class="teacher__circle">
                    <img src="../assets/img/teacher/teacher__photo-two.png" alt=" Фото преподавателя" class="teacher__photo">
                  </span>
                  </div>
                  <h4 class="teacher__name">Имя Фамилия</h4>
                  <p class="teacher__info">Выпускница Гарвардского Университета. Более 10 лет играет в шахматы и
                    участвует в турнирах.</p>
                </div>
              </div>
            </div>
            <div class="carousel">
              <!-- Контент 3 слайда -->
              <div class="col-3">
                <div class="teacher">
                  <div class="teacher__avatar">
                <span class="teacher__circle">
                  <img src="../assets/img/teacher/teacher__photo-three.png" alt=" Фото преподавателя" class="teacher__photo">
                </span>
                  </div>
                  <h4 class="teacher__name">Имя Фамилия</h4>
                  <p class="teacher__info">Выпускница Гарвардского Университета. Более 10 лет играет в шахматы и
                    участвует в турнирах.</p>
                </div>
              </div>
            </div>
            <div class="carousel">
              <!-- Контент 4 слайда -->
              <div class="col-3">
                <div class="teacher">
                  <div class="teacher__avatar">
              <span class="teacher__circle">
                <img src="../assets/img/teacher/teacher__photo-five.png" alt=" Фото преподавателя" class="teacher__photo">
              </span>
                  </div>
                  <h4 class="teacher__name">Имя Фамилия</h4>
                  <p class="teacher__info">Выпускница Гарвардского Университета. Более 10 лет играет в шахматы и
                    участвует в турнирах.</p>
                </div>
              </div>
            </div>
            <div class="carousel">
              <!-- Контент 5 слайда -->
              <div class="col-3">
                <div class="teacher">
                  <div class="teacher__avatar">
              <span class="teacher__circle">
                <img src="../assets/img/teacher/teacher__photo-six.jpg" alt=" Фото преподавателя" class="teacher__photo">
              </span>
                  </div>
                  <h4 class="teacher__name">Имя Фамилия</h4>
                  <p class="teacher__info">Выпускница Гарвардского Университета. Более 10 лет играет в шахматы и
                    участвует в турнирах.</p>
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
              <h3 class="text-gradient mt-4 mb-0">600</h3>
              <p class="expanded__text bold px-1 o-p">Курсов</p>
            </div>
            <div class="col-md-3 t-g">
              <h3 class="text-gradient mt-4 mb-0">82</h3>
              <p class="expanded__text bold px-1 o-p">Ведущих преподователей</p>
            </div>
            <div class="col-md-5">
              <h3 class="text-gradient mt-4 mb-0">14 795</h3>
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
              <div class="col-md-4 col-lg-3 col-xl-2">
                <div class="partners-cart eff-h-three">
                  <img src="../assets/img/our-partners/our-partners-two.png" alt="партнер" class="partner-img">
                </div>
              </div>
              <div class="col-md-4 col-lg-3 col-xl-2">
                <div class="partners-cart  p-c-r eff-h-three">
                  <img src="../assets/img/our-partners/our-partners-three.png" alt="партнер" class="partner-img">
                </div>
              </div>
              <div class="col-md-4 col-lg-3 col-xl-2">
                <div class="partners-cart p-c-l  eff-h-three">
                  <img src="../assets/img/our-partners/our-partners-four.png" alt="партнер" class="partner-img">
                </div>
              </div>
              <div class="col-md-4 col-lg-3 col-xl-2">
                <div class="partners-cart eff-h-three">
                  <img src="../assets/img/our-partners/our-partners-three.png" alt="партнер" class="partner-img">
                </div>
              </div>
              <div class="col-md-4 col-lg-3 col-xl-2">
                <div class="partners-cart  p-c-r eff-h-three">
                  <img src="../assets/img/our-partners/our-partners-one.png" alt="партнер" class="partner-img">
                </div>
              </div>
              <div class="col-md-4 col-lg-3 col-xl-2">
                <div class="partners-cart p-c-l  eff-h-three">
                  <img src="../assets/img/our-partners/our-partners-two.png" alt="партнер" class="partner-img">
                </div>
              </div>
              <div class="col-md-4 col-lg-3 col-xl-2">
                <div class="partners-cart eff-h-three">
                  <img src="../assets/img/our-partners/our-partners-four.png" alt="партнер" class="partner-img">
                </div>
              </div>
              <div class="col-md-4 col-lg-3 col-xl-2">
                <div class="partners-cart  p-c-r eff-h-three">
                  <img src="../assets/img/our-partners/our-partners-one.png" alt="партнер" class="partner-img">
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


export default {
  title: 'Академия будущего | Об Академии',
  name: "About",
  components: {
    Navbar
  },

  mixins: [playerMixin],
}
</script>

<style scoped>

</style>