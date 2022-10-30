<template>
  <div>
    <nav class="mobile-menu">
      <div class="container">
        <ul>
          <li><a href="/education">Все курсы</a></li>
          <li><a href="/events">Мероприятия</a></li>
          <li><a href="/about">Об академии</a></li>
          <li><a href="/reviews">Отзывы</a></li>
          <li><a href="/contacts">Контакты</a></li>
        </ul>
        <div class="city">
          <a class="link">{{ $store.state.city }} <span></span></a>
          <div class="select">
            <input type="radio" class="radio" id="city4" name="city2" @click="setCity('Дзержинск')"><label for="city4"
                                                                                                           class="l1">Дзержинск</label>
            <input type="radio" class="radio" id="city5" name="city2" @click="setCity('Нижний Новгород')"><label
              for="city5" class="l2">Нижний Новгород</label>
            <input type="radio" class="radio" id="city6" name="city2" @click="setCity('Online')"><label for="city6"
                                                                                                        class="l3">On-line</label>
          </div>
        </div>

        <a v-if="authenticated" href="#" class="user-link" @click="goTo('Profile', {id: user.id})"><img
            src="@/assets/082022/img/avatar.png"> {{ user.first_name }} {{ user.last_name }}</a>
        <span v-else>
      			<!--  <a href="#" @click="goTo('SignUp')">Регистрация</a> / --><a href="#" @click="goTo('Auth')">Вход</a>
			</span>

        <a v-bind:href="'tel:'+ $store.state.phone" class="phone">{{ $store.state.phone }}</a>
        <div class="adress">
          {{ $store.state.address }}
        </div>
        <a href="mailto:info@info@f-academy.ru" class="mail">info@f-academy.ru</a>
        <div class="social">
          <a href="https://t.me/+qsd97a8BPXVmNjQy"><img src="@/assets/082022/img/social1.svg"></a>
          <a v-bind:href="$store.state.wa"><img src="@/assets/082022/img/social2.svg"></a>
          <a v-bind:href="$store.state.vb"><img src="@/assets/082022/img/social3.svg"></a>
        </div>
      </div>
    </nav>
    <div id="header">
      <div class="top-page-line">
        <div class="container flex">
          <div class="adress">
            {{ $store.state.address }}
          </div>
          <a href="mailto:info@f-academy.ru" class="mail">info@f-academy.ru</a>
          <div class="social">
            <a href="https://t.me/+qsd97a8BPXVmNjQy"><img src="@/assets/082022/img/social1.svg"></a>
            <a v-bind:href="$store.state.wa"><img src="@/assets/082022/img/social2.svg"></a>
            <a v-bind:href="$store.state.vb"><img src="@/assets/082022/img/social3.svg"></a>
          </div>
          <div class="city">
            <a class="link">{{ $store.state.city }} <span></span></a>
            <div class="select">
              <input type="radio" class="radio" id="city1" name="city" @click="setCity('Дзержинск')"><label for="city1"
                                                                                                            class="l1">Дзержинск</label>
              <input type="radio" class="radio" id="city2" name="city" @click="setCity('Нижний Новгород')"><label
                for="city2" class="l2">Нижний Новгород</label>
              <input type="radio" class="radio" id="city3" name="city" @click="setCity('Online')"><label for="city3"
                                                                                                         class="l3">On-line</label>
            </div>
          </div>

          <a v-if="authenticated" href="#" class="user-link" @click="goTo('Profile', {id: user.id})">
            <img src="@/assets/082022/img/avatar.png"> {{ user.first_name }} {{ user.last_name }}
          </a>
          <span v-else>
	      			<a href="#" @click="goTo('Auth')">Вход</a>
				  </span>
        </div>
      </div>

      <header class="header">
        <div class="container flex">
          <div class="logo">
            <a href="/"><img src="@/assets/082022/img/logo.svg"></a>
          </div>
          <ul>
            <li><a href="/education">Все курсы</a></li>
            <li><a href="/events">Мероприятия</a></li>
            <li><a href="/about">Об академии</a></li>
            <li><a href="/reviews">Отзывы</a></li>
            <li><a href="/contacts">Контакты</a></li>
          </ul>
          <a v-bind:href="'tel:'+ $store.state.phone" class="phone">{{ $store.state.phone }}</a>
          <a class="menu-button"></a>
        </div>
      </header>
    </div>
  </div>
</template>

<script>
import NavLogin from "../NavLogin";

import {redirect} from "../mixins/redirect";
import {cityMixin} from "../mixins/cityMixin";

export default {
  name: "Header",

  components: {
    NavLogin,
  },

  data() {
    return {
      user: {},
      authenticated: false,
    }
  },

  mixins: [cityMixin, redirect],

  mounted: function () {
    let $ = window.$;
    let store = this.$store;

    $(document).ready(function () {
      $('.city input[name="city"], .city input[name="city2"]').each(function () {
        var cityName = $(this).next('label').text();
        if (cityName == store.state.city) {
          $(this).prop('checked', true);
        }
      })
      $('.contacts-block .map').removeClass('active');
      $('.contacts-block form.big').hide();
      $('.contacts-block .r').show();
      switch (store.state.city) {
        case 'Дзержинск':
          $('.contacts-block .map.m2').addClass('active');
          break;
        case 'Нижний Новгород':
          $('.contacts-block .map.m1').addClass('active');
          break;
        default:
          $('.contacts-block form.big').show();
          $('.contacts-block .r').hide();
          break;
      }
    });
  },

  created() {
    this.user = this.$store.getters.getProfileInfo;
    this.authenticated = this.$store.state.isAuthenticated;
  },

  methods: {},
}
</script>