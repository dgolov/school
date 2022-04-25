<template>
  <div id="contacts">
    <navbar></navbar>
    <section class="breadcrumbs breadcrumbs_all-news">
      <div class="container">
        <div class="row">
          <div class="col-12">
            <ul class="breadcrumb">
              <li class="breadcrumb__list">
                <a href="/" class="breadcrumb__item">Главная</a>
              </li>
              <li class="breadcrumb__list">
                <span style="display: inline-block;">Контакты</span>
              </li>
            </ul>
            <h1 class="breadcrumb-title">Контакты</h1>
          </div>
        </div>
      </div>
    </section>

    <section class="connection">
      <div class="container">
        <div class="row">
          <div class="connection-wrapp">
            <div class="col-lg-3 order-1 order-xl-0 order-lg-0">
              <div class="connection-inner">
                <div class="connection-one">
                  <img src="../assets/img/connection/connection-phone.svg" alt="phone" class="connection-tel-icon">
                  <a href="tel:+88009503398 " class="connection-number">{{ $store.state.phone }}</a>
                </div>
                <div class="connection-two">
                  <img src="../assets/img/connection/connection-email.svg" alt="email" class="connection-email-icon">
                  <a href="mailto:info@hodfutureacademy.ru"
                     class="connection-email">info@hodfutureacademy.ru</a>
                </div>
                <div class="connection-three">
                  <img src="../assets/img/connection/connection-adress.svg" alt="adress"
                       class="connection-adress-icon">
                  <p class="connection-address">{{ $store.state.address }}</p>
                </div>
                <div class="connection-social d-flex">
                  <!--noindex-->
                  <a href="https://vk.com/club208872699" rel="nofollow noopener noreferrer" target="_blank" class="vk"></a>
                  <!--/noindex-->
                  <!--noindex-->
                  <a href="https://www.instagram.com/future_academyrus"
                     rel="nofollow noopener noreferrer" target="_blank" class="instagram"></a>
                  <!--/noindex-->
                  <!--noindex-->
                  <a href="https://www.facebook.com/Академия-будущего-ХОД-106638701868195"
                     rel="nofollow noopener noreferrer" target="_blank" class="facebook"></a>
                  <!--/noindex-->
                  <!--noindex-->
                  <a href="https://www.youtube.com/channel/UCZjqT7xZQRA73hPwUMWudUQ"
                     rel="nofollow noopener noreferrer" target="_blank" class="youtube"></a>
                  <!--/noindex-->
                  <!--noindex-->
                  <a href="https://t.me/+qsd97a8BPXVmNjQy" rel="nofollow noopener noreferrer" target="_blank"
                     class="telegram"></a>
                  <!--/noindex-->
                </div>
              </div>
            </div>
            <div class="col-lg-9">
              <div class="map">
                <iframe src="https://yandex.ru/map-widget/v1/?um=constructor%3Af104aa0bf14eab2d1fd50d53f8f2b0b05e21df8aec0c01e80f40ce27f75cb0ff&amp;source=constructor" width="882" height="410" frameborder="0"></iframe>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import Navbar from "../components/Navbar";
import Construction from "../components/Construction";

export default {
  title: 'Академия будущего | Контакты',
  description: 'Контакты',
  name: "Contacts",
  components: {
    Navbar
  },
}
</script>

<style scoped>

</style>