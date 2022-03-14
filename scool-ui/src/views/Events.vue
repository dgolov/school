<template>
  <div class="event">

    <navbar></navbar>

    <section class="breadcrumbs">
      <div class="container">
        <div class="row">
          <div class="col-12">
            <ul class="breadcrumb">
              <li class="breadcrumb__list">
                <a href="/" class="breadcrumb__item">Главная</a>
              </li>
              <li class="breadcrumb__list">
                <span style="display: inline-block;">Мероприятия</span>
              </li>
            </ul>
            <h1 class="breadcrumb-title">Все мероприятия</h1>
          </div>
        </div>
      </div>
    </section>

    <section class="all-events past-events">
      <div class="container">
        <div class="row justify-content-center">
          <div class="col-lg-12">
            <div class="open-day d-flex">
              <div class="open-day__inner d-flex">
                <div class="date">
                  <span class="date__numder">19</span>
                  <span class="date__month">марта</span>
                </div>
                <div class="excursion">
                  <h2 class="excursion__open-day">День открытых дверей</h2>
                  <p class="excursion__desc">
                    Приглашаем всех желающих на бесплатную экскурсию в мир
                    востребованных профессий и полезных навыков
                  </p>
                </div>
              </div>
              <button type="button" class="button-open-day">Записаться</button>
            </div>
          </div>
        </div>

        <div class="row">
          <div class="col-12 col-md-6 col-lg-4" v-for="event in eventsList">
            <div class="events eff-h" v-bind:style="{'background-color': '#' + event.color_hex}"
               @click="goTo('EventSingle', {id: event.id})">
              <span class="events-meeting">Встреча</span>
              <div class="events__inner d-flex align-items-center">
                <img src="../assets/img/events/events.svg" alt="icon" class="events-icon">
                <h4 class="events-title">{{ event.name }}</h4>
              </div>
              <p class="events-text">{{ event.description.slice(0, 100) + '...' }}</p>
              <span class="events-date">{{ formatDate(event.date) }}</span>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import Navbar from "../components/Navbar";
import axios from "axios";
import {redirect} from "../components/mixins/redirect";
export default {
  title: 'Академия будущего | Мероприятия',
  name: "Events",

  components: {Navbar},

  mixins: [redirect],

  data() {
    return {
      eventsList: [],
    }
  },

  created() {
    this.loadEventList();
  },

  methods: {
    async loadEventList() {
      await axios
          .get(`${this.$store.getters.getServerUrl}/events/`)
          .then(response => (this.eventsList = response.data));
    },

    formatDate(date) {
      let d1 = new Date(date);
      let ms = [
          'января', 'февряля', 'марта', 'апреля', 'мая', 'июня',
        'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря'
      ];
      return d1.getDate() + ' ' + ms[d1.getMonth()] + ' ' + d1.getFullYear();
    }
  },
}
</script>

<style scoped>
a {
  color: #000;
  text-decoration: none;
  font-weight: 400;
  display: block;
}

a:hover {
  color: #000;
}
</style>