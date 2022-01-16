<template>
  <div class="mt-5">
    <div class="cta cta--reverse">
      <div class="container">
        <div class="row">
          <div class="col-12">
            <div class="application-wrapp">
              <div class="application">
                <div class="col-12 col-lg-7">
                  <div class="owl-footer">
                    <div class="owl-footer__inner">
                      <img src="../assets/img/owl/owl-footer-one.png" alt="" class="owl-footer__img">
                    </div>
                    <div class="owl-footer-text-wrapp">
                      <span class="owl-footer-frame"></span>
                      <h4 class="owl-frame-title">Помочь с выбором?</h4>
                      <p class="owl-frame-text"> Оставьте заявку и наши специалисты свяжутся с вами, ответят на все вопросы и подберут подходящий вариант обучения.</p>
                    </div>
                  </div>
                </div>
                <!-- Добавлю к input класс для стилизации class="input" -->
                <div class="col-12 col-lg-5">
                  <form class="form-footer">
                    <input type='text' placeholder="Ваше имя" class="input">
                    <div class="double">
                      <div class="half">
                        <input type="tel" class="input" id="first" placeholder="Ваш телефон">
                      </div>
                      <div class="half">
                        <input type="email" class="input" id="second" placeholder="Ваш e-mail">
                      </div>
                    </div>
                    <div class="form-info">
                      <p class="form-info__text">Нажимая на кнопку, я соглашаюсь
                        на обработку персональных данных
                        и с правилами пользования Платформой</p>
                      <button class="button button__accent"> Отправить</button>
                    </div>
                  </form>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="footer footer--dark">
      <div class="container">
        <div class="footer__inner">
          <div class="footer__data__item footer__data__item-bottom">
            <div class="footer__row mb-5">
              <a href="/" class="navbar__logo">
                <img src="../assets/img/logo-footer.svg" style="width: 83px;"></a>
            </div>
            <div class="footer__row">
              <div class="menu-contact d-flex">
                <a href="tel:+88009503398 " class="number number-footer">8 800 950-33-98</a>
                <p class="menu-contact__address address-footer">г. Москва, ул. Ленина, д. 50</p>
                <a href="mailto:info@hodfutureacademy.ru" class="menu-contact__email email-footer">info@hodfutureacademy.ru</a>
              </div>
              <div class="social social-footer d-flex">
                <!--noindex-->
                <a href="#" rel="nofollow noopener noreferrer" target="_blank" class="social__vk c-f-vk"></a>
                <!--/noindex-->
                <!--noindex-->
                <a href="#" rel="nofollow noopener noreferrer" target="_blank"
                   class="social__instagram c-f-instagram"></a>
                <!--/noindex-->
                <!--noindex-->
                <a href="#" rel="nofollow noopener noreferrer" target="_blank"
                   class="social__facebook c-f-facebook"></a>
                <!--/noindex-->
                <!--noindex-->
                <a href="https://www.youtube.com/channel/UCZjqT7xZQRA73hPwUMWudUQ"
                   rel="nofollow noopener noreferrer" target="_blank" class="social__youtube c-f-youtube"></a>
                <!--/noindex-->
                <!--noindex-->
                <a href="#" rel="nofollow noopener noreferrer" target="_blank"
                   class="social__telegram c-f-telegram "></a>
                <!--/noindex-->
              </div>
              <p style="font-size: 14px; color: gray; margin: 0;">© ХОД, Future Academy</p></div>
          </div>

          <div class="footer__data__item d-none d-lg-block">
            <div class="footer__row mb-5">
              <h3 style="font-size: 18px; color: #ffffff; font-weight: bold;">Детям</h3>
            </div>
            <div v-for="category in categoryList" :key="category.id" class="footer__row">
              <p v-if="category.age_group === 'children'">
                <a href="#" @click="goToCategory(category.id)">{{ category.name }}</a>
              </p>
            </div>
          </div>
          <div class="footer__data__item d-none d-lg-block">
            <div class="footer__row mb-5">
              <h3 style="font-size: 18px; color: #ffffff; font-weight: bold;">Подросткам</h3>
            </div>
            <div v-for="category in categoryList" :key="category.id" class="footer__row">
              <p v-if="category.age_group === 'teens'">
                <a href="#" @click="goToCategory(category.id)">{{ category.name }}</a>
              </p>
            </div>
          </div>
          <div class="footer__data__item d-none d-lg-block">
            <div class="footer__row mb-5">
              <h3 style="font-size: 18px; color: #ffffff; font-weight: bold;">Взрослым</h3>
            </div>
            <div v-for="category in categoryList" :key="category.id" class="footer__row">
              <p v-if="category.age_group === 'adults'">
                <a href="#" @click="goToCategory(category.id)">{{ category.name }}</a>
              </p>
            </div>
          </div>
          <div class="footer__data__item footer__data__item-info">
            <div class="footer__row">
              <div class="footer__row mb-5">
                <h3 style="font-size: 18px; color: rgb(255, 255, 255); font-weight: bold;">Информация</h3></div>
              <div class="footer__row"><a href="/about">Об академии</a></div>
              <div class="footer__row"><a href="/events" @click="goTo('Events')">Мероприятия</a></div>
              <div class="footer__row"><a href="/news" @click="goTo('News')">Новости</a></div>
              <div class="footer__row"><a href="/career" @click="goTo('Career')">Карьера</a></div>
              <div class="footer__row"><a href="/contacts" @click="goTo('Contacts')">Контакты</a></div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import {redirect} from "./mixins/redirect";

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

  mixins: [redirect],

  methods: {
    async loadCategoryList() {
      await axios
          .get(`${this.$store.getters.getServerUrl}/categories/`)
          .then(response => (this.categoryList = response.data));
    },

    goToCategory(id) {
      this.$router.push({name: 'Education', params: {'category': id}})
    },
  },
}
</script>

<style scoped>

</style>