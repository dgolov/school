<template>
  <div>
    <navbar></navbar>

    <div class="header-page-wrapper d-none d-lg-block">
      <div class="header-page">
        <div class="header-page-img-wrapp">
          <img src="../assets/img/header/header-page.jpg" alt="" class="header-page__img">
        </div>
        <div class="header-page-inner">
          <h1 class="header-page-title" style="max-width: 40%;">{{ event.name }}</h1>
          <p class="header-page-text" style="max-width: 40%;">{{ event.signature }}</p>
        </div>
        <div class="header-page-wrapp">
          <div class="header-desc">
            <p class="header-desc-info">{{ event.text1 }}</p>
          </div>
          <div class="header-desc header-desc_margin">
            <p class="header-desc-info">{{ event.text2 }}</p>
          </div>
          <div class="header-desc">
            <p class="header-desc-info">{{ event.text3 }}</p>
          </div>
        </div>
        <button class="button button-header" type="button"
                @click="goTo('Requests', {purpose: 'event', course: null, event: event.id})"
                style="z-index: 999">
          Записаться на интенсив
        </button>
      </div>
    </div>

    <div class="header-mobi d-none">
      <div class="header-page-img-wrapp">
        <img src="../assets/img/header/header-page.jpg" alt="" class="header-page__img">
      </div>
      <div class="container">
        <div class="row">
          <div class="col-12">
            <div class="header-page-lg">
              <div class="header-page-inner">
                <h1 class="header-page-title">{{ event.name }}</h1>
                <p class="header-page-text">{{ event.signature }}</p>
              </div>
              <div class="header-page-wrapp">
                <div class="header-desc header-desc_tiny">
                  <p class="header-desc-info">{{ event.text1 }}</p>
                </div>
                <div class="header-desc header-desc_small header-desc_margin">
                  <p class="header-desc-info">{{ event.text2 }}</p>
                </div>
                <div class="header-desc header-desc_big">
                  <p class="header-desc-info">{{ event.text3 }}</p>
                </div>
              </div>
              <h2 class="header-button-title">Запишись сейчас</h2>
              <button class="button button-header" type="button"
                      @click="goTo('Requests', {purpose: 'event', course: null, event: event.id})"
                      style="z-index: 999">
                Записаться на интенсив
              </button>
            </div>
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
              <span class="owl__frame-events"></span>
              <div class="owl-text owl-text-events">
                <p class="owl-desc owl-desc-events">{{ event.text_owl }}</p>
              </div>
            </div>
          </div>
          <div class="col-12 col-lg-8">
            <div class="events-title-wrapp">
              <div class="events-title__inner">
                <span class="events-title__cross mb-4"></span>
                <p class="events-title__text">{{ event.text_x }}</p>
              </div>
              <div class="events-title__inner">
                <span class="events-title__circle mb-4"></span>
<!--                <h3 class="events-title__subject">Заголовок</h3>-->
                <p class="events-title__text">{{ event.text_o }}</p>
              </div>
              <div class="events-title__inner">
                <span class="events-title__triangle mb-4"></span>
<!--                <h3 class="events-title__subject">Заголовок</h3>-->
                <p class="events-title__text">{{ event.text_d }}</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <section class="program-events">
      <div class="program-events-wrapp">
        <div class="container">
          <div class="row" style="position: relative;">
            <div class="col-12">
              <h2 class="program-events-title">Программа мероприятия</h2>
              <div class="col-12">
                <ul class="skills skills_two">
                  <li class="skills__item skills__item_marker" v-for="item in contentList">{{ item }}</li>
                </ul>
              </div>
            </div>
            <div v-if="event.days" class="col-12" style="padding-bottom: 80px;">
              <div v-for="day in event.days" id="question1" class="faq faq_active">
                <p class="question">День {{ day.number }}</p>
                <button class="faq-open-button">
                  <img src="../assets/images/faq-close.svg">
                </button>
                <p>{{ day.description }}</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section v-if="event.speakers.length > 0" class="teachers">
      <div class="row">
        <div class="col-12">
          <h2 class="reviews-title">Мероприятие проводят</h2>
        </div>
      </div>
      <div class="row">
        <div class="col-12">
          <div class="teachers-wrapp">
            <div class="carousel" v-for="speaker of event.speakers">
              <div class="col-3">
                <div class="teacher">
                  <div class="teacher__avatar">
                    <img v-if="speaker.avatar" :src="`${speaker.avatar.image}`" alt=" Фото преподавателя" class="profile-avatar">
                    <img v-else src="../assets/images/avatars/mike2.jpeg" class="center profile-avatar">
                  </div>
                  <h4 class="teacher__name">{{ speaker.last_name }} {{ speaker.first_name }}</h4>
                  <p class="teacher__info">{{ speaker.about }}</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class="past-events">
      <div class="container">
        <div class="row">
          <div class="col-12">
            <h2 class="program-events-title mb-5">Фотографии с прошлых мероприятий</h2>
          </div>
        </div>
      </div>
      <div class="carousel-past-events">
        <div class="gallery">
          <img src="../assets/img/past-events/past-events__one.jpg" alt="слайд 1" class="past-events-img">
        </div>
        <div class="gallery">
          <img src="../assets/img/past-events/past-events__two.jpg" alt="слайд 2" class="past-events-img">
        </div>
        <div class="gallery">
          <img src="../assets/img/past-events/past-events__three.jpg" alt="слайд 3" class="past-events-img">
        </div>
        <div class="gallery">
          <img src="../assets/img/past-events/past-events__four.jpg" alt="слайд 4" class="past-events-img">
        </div>
        <div class="gallery">
          <img src="../assets/img/past-events/past-events__five.jpg" alt="слайд 5" class="past-events-img">
        </div>
        <div class="gallery">
          <img src="../assets/img/past-events/past-events__six.jpg" alt="слайд 5" class="past-events-img">
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import Navbar from "../components/NavbarMain";
import Construction from "../components/Construction";
import axios from "axios";
import {redirect} from "../components/mixins/redirect";

export default {
  title: 'Академия будущего | Мероприятия',
  name: "EventSingle",

  mixins: [redirect],

  data() {
    return {
      event: {},
      contentList: [],
    }
  },

  props: {
    id: String
  },

  components: {
    Navbar, Construction
  },

  created() {
    this.loadEvent()
  },

  methods: {
    async loadEvent() {
      await axios
          .get(`${this.$store.getters.getServerUrl}/events/${this.id}`)
          .then(response => (this.event = response.data))
      this.contentList = this.event.content.split('.');
    },
  },
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
  box-shadow:
      42px -37px 20px -31px rgb(39 170 237 / 35%),
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
  box-shadow:
      18px 14px 20px -13px rgb(39 170 237 / 35%),
      26px -18px 20px -21px rgb(39 170 225 / 35%),
      -18px 7px 20px -12px rgb(247 148 29 / 40%),
      -28px -22px 20px -22px rgb(247 148 29 / 40%);
  transition: box-shadow 0.8s ease;
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
</style>