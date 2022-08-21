<template>
  <div class="event">

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
                  <span class="date__numder">{{ new Date(dateOpenDoors).getDate() }}</span>
                  <span class="date__month">{{ formatDate(dateOpenDoors, true) }}</span>
                </div>
                <div class="excursion">
                  <h2 class="excursion__open-day">День открытых дверей</h2>
                  <p class="excursion__desc">
                    Приглашаем всех желающих на бесплатную экскурсию в мир
                    востребованных профессий и полезных навыков
                  </p>
                </div>
              </div>
              <button type="button" class="button-open-day"
                      @click="goTo(
                          'Requests',
                          {purpose: 'event', course: 'null', event: String(dateOpenDoorsID)}
                          )">
                Записаться
              </button>
            </div>
          </div>
        </div>

        <div class="row" style="display: none;">
          <div class="col-12 col-md-6 col-lg-4" v-for="event in eventsList">
            <div class="events eff-h"
                 v-bind:style="{'background-color': '#' + event.color_hex, 'height': '300px'}"
               @click="goTo('EventSingle', {id: event.id, slug: event.slug})">
              <span class="events-meeting">Встреча</span>
              <div class="events__inner d-flex align-items-center">
                <img src="../assets/img/events/events.svg" alt="icon" class="events-icon">
                <h4 class="events-title">{{ event.name }}</h4>
              </div>
              <p class="events-text">{{ event.description.slice(0, 100) + '...' }}</p>
              <span class="events-date">{{ formatDate(event.date, false) }}</span>
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
  description: 'Мероприятия',
  name: "Events",

  components: {Navbar},

  mixins: [redirect],

  data() {
    return {
      eventsList: [],
      dateOpenDoors: null,
      dateOpenDoorsID: 1,
    }
  },

  created() {
	  import('@/assets/082022/css/stumb/style.css');
	  import('@/assets/082022/css/stumb/main.css');
	  
      this.loadEventList();
  },

  methods: {
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
	
	.breadcrumb, .breadcrumb a {
		line-height: 22.5px;
	}
	
	.breadcrumb li:first-child:before {
		display: none;
	}

	.contacts-map-nn, .contacts-map-dz {
		display: none;
	}


</style>