<template>
  <div class="footer footer--dark">
    <div class="container">
      <div class="footer__inner">
        <div class="footer__data__item">
          <div class="footer__row mb-5">
            <a href="/" class="navbar__logo">
              <img src="../assets/images/logo_white.svg" style="width: 83px;">
            </a>
          </div>
          <div class="footer__row">
            <p style="font-size: 18px;">8 800 950-33-98</p>
            <p style="font-size: 14px;">г. Москва, ул. Ленина, д. 50</p>
            <p style="font-size: 14px;">info@hodfutureacademy.ru</p>
            <img src="../assets/images/vk.svg" style="margin: 35px 20px 35px 0;">
            <img src="../assets/images/instagram.svg" style="margin: 35px 20px 35px 0;">
            <img src="../assets/images/facebook.svg" style="margin: 35px 20px 35px 0;">
            <img src="../assets/images/youtube.svg" style="margin: 35px 20px 35px 0;">
            <img src="../assets/images/telegram.svg" style="margin: 35px 0;">
            <p style="font-size: 14px; color: gray;">© ХОД, Future Academy</p>
          </div>
        </div>
        <div class="footer__data__item">
          <div class="footer__row mb-5">
            <h3 style="font-size: 18px; color: #ffffff; font-weight: bold;">Детям</h3>
          </div>
          <div v-for="category in categoryList" :key="category.id" class="footer__row">
            <p v-if="category.age_group === 'children'">
              <a href="#" @click="goTo(category.id)">{{ category.name }}</a>
            </p>
          </div>
        </div>
        <div class="footer__data__item">
          <div class="footer__row mb-5">
            <h3 style="font-size: 18px; color: #ffffff; font-weight: bold;">Подросткам</h3>
          </div>
          <div v-for="category in categoryList" :key="category.id" class="footer__row">
            <p v-if="category.age_group === 'teens'">
              <a href="#" @click="goTo(category.id)">{{ category.name }}</a>
            </p>
          </div>
        </div>
        <div class="footer__data__item">
          <div class="footer__row">
            <div class="footer__row mb-5">
              <h3 style="font-size: 18px; color: #ffffff; font-weight: bold;">Взрослым</h3>
            </div>
            <div v-for="category in categoryList" :key="category.id" class="footer__row">
              <p v-if="category.age_group === 'adults'">
                <a href="#" @click="goTo(category.id)">{{ category.name }}</a>
              </p>
            </div>
          </div>
        </div>
        <div class="footer__data__item">
          <div class="footer__row">
            <div class="footer__row mb-5">
              <h3 style="font-size: 18px; color: #ffffff; font-weight: bold;">Информация</h3>
            </div>
            <div class="footer__row"><p>Об академии</p></div>
            <div class="footer__row"><p>Мероприятия</p></div>
            <div class="footer__row"><p>Новости</p></div>
            <div class="footer__row"><p>Карьера</p></div>
            <div class="footer__row"><p>Контакты</p></div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Footer",

  data() {
    return {
      categoryList: []
    }
  },

  created() {
    this.loadCategoryList()
  },

  methods: {
    async loadCategoryList() {
      await axios
          .get(`${this.$store.getters.getServerUrl}/categories/`)
          .then(response => (this.categoryList = response.data));
    },

    goTo(id) {
      this.$router.push({name: 'Education', params: {'category': id}})
    },
  },
}
</script>

<style scoped>

</style>