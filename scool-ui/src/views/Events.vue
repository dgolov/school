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

    <section class="all-events">
      <div class="container">
        <div class="row justify-content-center">
          <div class="col-lg-12">
            <div class="open-day d-flex">
              <div class="open-day__inner d-flex">
                <div class="date">
                  <span class="date__numder">25</span>
                  <span class="date__month">ноября</span>
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
          <div class="col-12 col-md-6 col-lg-4">
            <!--Мероприятие 1 -->
            <a href="#" class="events events_blue eff-h">
              <span class="events-meeting">Встреча</span>
              <div class="events__inner d-flex align-items-center">
                <img src="../assets/img/events/events.svg" alt="icon" class="events-icon">
                <h4 class="events-title">Заголовок мероприятия</h4>
              </div>
              <p class="events-text">
                Краткий анонс мероприятия в нескольких предложениях. Текст, который будет заинтересовывать пользователя
              </p>
              <span class="events-date">16 ноября 2021</span>
            </a>
          </div>

          <div class="col-12 col-md-6 col-lg-4">
            <!--Мероприятие 2 -->
            <a href="#" class="events events_yellow eff-h">
              <span class="events-meeting">Встреча</span>
              <div class="events__inner d-flex align-items-center">
                <img src="../assets/img/events/events.svg" alt="icon" class="events-icon">
                <h4 class="events-title">Заголовок мероприятия</h4>
              </div>
              <p class="events-text">
                Краткий анонс мероприятия в нескольких предложениях. Текст, который будет заинтересовывать пользователя
              </p>
              <span class="events-date">16 ноября 2021</span>
            </a>
          </div>

          <div class="col-12 col-md-6 col-lg-4">
            <!--Мероприятие 3 -->
            <a href="#" class="events events_violet eff-h">
              <span class="events-meeting">Встреча</span>
              <div class="events__inner d-flex align-items-center">
                <img src="../assets/img/events/events.svg" alt="icon" class="events-icon">
                <h4 class="events-title">Заголовок мероприятия</h4>
              </div>
              <p class="events-text">
                Краткий анонс мероприятия в нескольких предложениях. Текст, который будет заинтересовывать пользователя
              </p>
              <span class="events-date">16 ноября 2021</span>
            </a>
          </div>

          <div class="col-12 col-lg-8">
            <!-- Вебинар -->
            <a href="#" class="webinar d-flex eff-h">
              <div class="webinar__inner">
                <img src="../assets/img/events/webinar__image.jpg" alt="image" class="webinar__image">
              </div>
              <div class="webinar-wrapper">
                <span class="events-meeting">Вебинар</span>
                <h4 class="events-title">Заголовок мероприятия</h4>
                <p class="events-text events-text_webinar">
                  Краткий анонс мероприятия в нескольких предложениях. Текст, который будет заинтересовывать пользователя
                </p>
                <span class="events-date">16 ноября 2021</span>
              </div>
            </a>
          </div>

          <div class="col-12 col-md-6 col-lg-4">
            <!--Мероприятие 1.1 -->
            <a href="#" class="another-kind eff-h">
              <div class="events-background">
                <h3 class="another-kind__title">Заголовок мероприятия</h3>
                <p class="another-kind__text">
                  Краткий анонс мероприятия в нескольких предложениях. Текст, который будет заинтересовывать пользователя
                </p>
              </div>
            </a>
          </div>

          <div class="col-12 col-md-6 col-lg-4">
            <!--Мероприятие 1 -->
            <a href="#" class="events events_light-blue eff-h">
              <span class="events-meeting">Встреча</span>
              <div class="events__inner d-flex align-items-center">
                <img src="../assets/img/events/events.svg" alt="icon" class="events-icon">
                <h4 class="events-title">Заголовок мероприятия</h4>
              </div>
              <p class="events-text">
                Краткий анонс мероприятия в нескольких предложениях. Текст, который будет заинтересовывать пользователя
              </p>
              <span class="events-date">16 ноября 2021</span>
            </a>
          </div>

          <div class="col-12 col-md-6 col-lg-4">
            <!--Мероприятие 2 -->
            <a href="#" class="events events_pink eff-h">
              <span class="events-meeting">Встреча</span>
              <div class="events__inner d-flex align-items-center">
                <img src="../assets/img/events/events.svg" alt="icon" class="events-icon">
                <h4 class="events-title">Заголовок мероприятия</h4>
              </div>
              <p class="events-text">
                Краткий анонс мероприятия в нескольких предложениях. Текст, который будет заинтересовывать пользователя
              </p>
              <span class="events-date">16 ноября 2021</span>
            </a>
          </div>

          <div class="col-12 col-md-6 col-lg-4">
            <!--Мероприятие 3 -->
            <a href="#" class="events events_beige eff-h">
              <span class="events-meeting">Встреча</span>
              <div class="events__inner d-flex align-items-center">
                <img src="../assets/img/events/events.svg" alt="icon" class="events-icon">
                <h4 class="events-title">Заголовок мероприятия</h4>
              </div>
              <p class="events-text">
                Краткий анонс мероприятия в нескольких предложениях. Текст, который будет заинтересовывать пользователя
              </p>
              <span class="events-date">16 ноября 2021</span>
            </a>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import Navbar from "../components/Navbar";
export default {
  name: "Events",
  components: {Navbar}
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