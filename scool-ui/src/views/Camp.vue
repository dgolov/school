<template>
  <div class="main-wrapper">

    <navbar></navbar>

    <section class="summery-camp">
      <div class="summery-camp_item--first">
        <div class="summery-camp_item_inner summery-camp_item__first">
          <h1 style="color: white;">IT каникулы в Академии Будущего Ход
          </h1>
          <div class="summery-camp_time">
            <p class="top-gradient">Смены полного дня</p>
            <p class="top-gradient">Смены 1/2 дня</p>
          </div>
          <div class="summery-camp__price">
            <span class="introduce_price top-gradient">от 8 900 ₽ в месяц</span>
          </div>
          <h2 style="color: white;">Открой своё IT-лето!</h2>
          <div class="btn-wrapper">
            <a class="accent-btn summery-cyamp__btn" href=""
                @click="goTo('Requests', {purpose: 'it_camp', course: null, event: 'null'})">
                Записаться
            </a>
          </div>
        </div>
      </div>
      <div class="summery-camp_item--second">
        <div class="summery-camp_item_inner summery-camp_item__second">
          <div class="summery-camp_item--item">
            <img class="summery-camp--boy" src="../assets/images/page-2/boy-girl.png" alt="boy-girl">
          </div>
        </div>
      </div>
    </section>

    <section class="slill-list">
      <div class="container slill-list_wrapper">
        <div class="slill-list_item--owl">
          <p>С нами у детей будет продуктивное IT-лето</p>
          <img src="../assets/images/svg-icons-page2/owl.png" alt="owl">
        </div>
        <div class="slill-list_item">
          <ul class="slill-list_item--list game_item_item">
            <li style="font-size: 22px;">Программирование</li>
            <li>Робототехника</li>
            <li>3D-моделирование</li>
            <li>Создание игр</li>
            <li>Анимация</li>
          </ul>
        </div>
        <div class="slill-list_item">
          <ul class="slill-list_item--list game_item_item">
            <li>Шахматы</li>
            <li>Блогинг</li>
            <li>Прогулки</li>
            <li>Игровые активности</li>
            <li>Английский язык</li>
          </ul>
        </div>
      </div>
    </section>

    <section class="certificate">
      <div class="certificate-wrapper container">
        <div class="certificate_item">
          <img src="../assets/images/page-2/certificate.png" alt="certificate">
        </div>
        <div class="certificate_item certificate_text">
          <h2>Вручение сертификата</h2>
          <p>о прохождении летней программы, море позитивных впечатлений и приобретении полезных IT-навыков</p>
        </div>
      </div>
    </section>

    <section class="schedule">
      <div class="container">
        <h2 style="color: white;">Смены полного и 1/2 дня</h2>
        <div class="schedule_wrapper">
          <div class="schedule_item">
            <p>30.05.2022<img src="../assets/images/svg-icons-page2/horiz-line.svg" alt="line">10.06.2022</p>
            <p>13.06.2022<img src="../assets/images/svg-icons-page2/horiz-line.svg" alt="line">24.06.2022</p>
            <p>27.06.2022<img src="../assets/images/svg-icons-page2/horiz-line.svg" alt="line">08.07.2022</p>
          </div>
          <div class="schedule_item">
            <p>11.07.2022<img src="../assets/images/svg-icons-page2/horiz-line.svg" alt="line">22.07.2022</p>
            <p>25.07.2022<img src="../assets/images/svg-icons-page2/horiz-line.svg" alt="line">05.08.2022</p>
            <p>08.08.2022<img src="../assets/images/svg-icons-page2/horiz-line.svg" alt="line">19.08.2022</p>
          </div>
        </div>
        <div class="schedule__btm--wrapper">
          <a class="accent-btn schedule__btn" href=""
            @click="goTo('Requests', {purpose: 'it_camp', course: null, event: 'null'})">
                Подать заявку
          </a>
        </div>
      </div>
    </section>

    <section class="plan-day">
      <div class="container plan-day_wrapper">
        <div class="plan-day_item">
          <h2>Смена полного дня</h2>
          <div class="plan-day_item__border">
            <div class="plan-day_item--item">
              <div class="plan-day_item--time">
                <p>8:30<img class="class=" src="../assets/images/svg-icons-page2/horiz-line.svg" alt="line">9:00
                </p>
              </div>
              <div class="plan-day_item--name">
                <img class="play-day_item__brace" src="../assets/images/svg-icons-page2/time/line.svg" alt="line">
                <img src="../assets/images/svg-icons-page2/time/sport.svg" alt="sport">
                <span>Сбор детей, утренняя зарядка</span>
              </div>
            </div>

            <div class="plan-day_item--item">
              <div class="plan-day_item--time">
                <p>9:00<img src="../assets/images/svg-icons-page2/horiz-line.svg" alt="line">9:40</p>
                <p>9:50<img src="../assets/images/svg-icons-page2/horiz-line.svg" alt="line">10:30</p>
              </div>
              <div class="plan-day_item--name">
                <img class="play-day_item__brace" src="../assets/images/svg-icons-page2/time/skoba.svg" alt="line">
                <img src="../assets/images/svg-icons-page2/time/learn.svg" alt="sport">
                <span>IT-урок</span>
              </div>
            </div>

            <div class="plan-day_item--item">
              <div class="plan-day_item--time">
                <p>10:30<img src="../assets/images/svg-icons-page2/horiz-line.svg" alt="line">10:40</p>
              </div>
              <div class="plan-day_item--name">
                <img class="play-day_item__brace" src="../assets/images/svg-icons-page2/time/line.svg" alt="line">
                <img src="../assets/images/svg-icons-page2/time/tea.svg" alt="sport">
                <span>Перекус (чай, снеки)</span>
              </div>
            </div>

            <div class="plan-day_item--item">
              <div class="plan-day_item--time">
                <p>10:40<img src="../assets/images/svg-icons-page2/horiz-line.svg" alt="line">11:20</p>
                <p>11:30<img src="../assets/images/svg-icons-page2/horiz-line.svg" alt="line">12:10</p>
              </div>
              <div class="plan-day_item--name">
                <img class="play-day_item__brace" src="../assets/images/svg-icons-page2/time/skoba.svg" alt="line">
                <img src="../assets/images/svg-icons-page2/time/learn.svg" alt="sport">
                <span>IT-урок</span>
              </div>
            </div>

            <div class="plan-day_item--item">
              <div class="plan-day_item--time">
                <p>12:20<img src="../assets/images/svg-icons-page2/horiz-line.svg" alt="line">13:00</p>
              </div>
              <div class="plan-day_item--name">
                <img class="play-day_item__brace" src="../assets/images/svg-icons-page2/time/line.svg" alt="line">
                <img src="../assets/images/svg-icons-page2/time/learn.svg" alt="sport">
                <span>Занятие по английскому языкуили шахматам</span>
              </div>
            </div>

            <div class="plan-day_item--item">
              <div class="plan-day_item--time">
                <p>13:00<img src="../assets/images/svg-icons-page2/horiz-line.svg" alt="line">14:00</p>
              </div>
              <div class="plan-day_item--name">
                <img class="play-day_item__brace" src="../assets/images/svg-icons-page2/time/line.svg" alt="line">
                <img src="../assets/images/svg-icons-page2/time/eat.svg" alt="sport">
                <span>Обед в кафе</span>
              </div>
            </div>

            <div class="plan-day_item--item">
              <div class="plan-day_item--time">
                <p>14:00<img src="../assets/images/svg-icons-page2/horiz-line.svg" alt="line">15:00</p>
              </div>
              <div class="plan-day_item--name">
                <img class="play-day_item__brace" src="../assets/images/svg-icons-page2/time/line.svg" alt="line">
                <img src="../assets/images/svg-icons-page2/time/smile.svg" alt="sport">
                <span>Прогулка, игры на свежем воздухе</span>
              </div>
            </div>

            <div class="plan-day_item--item">
              <div class="plan-day_item--time">
                <p>15:00<img src="../assets/images/svg-icons-page2/horiz-line.svg" alt="line">16:00</p>
              </div>
              <div class="plan-day_item--name">
                <img class="play-day_item__brace" src="../assets/images/svg-icons-page2/time/line.svg" alt="line">
                <img src="../assets/images/svg-icons-page2/time/chat.svg" alt="sport">
                <span>Тренинговое занятие по развитию различных soft skills</span>
              </div>
            </div>

            <div class="plan-day_item--item">
              <div class="plan-day_item--time">
                <p>16:00<img src="../assets/images/svg-icons-page2/horiz-line.svg" alt="line">17:00</p>
              </div>
              <div class="plan-day_item--name">
                <img class="play-day_item__brace" src="../assets/images/svg-icons-page2/time/line.svg" alt="line">
                <img src="../assets/images/svg-icons-page2/time/smile.svg" alt="sport">
                <span>Настольные игры, общение,
							проектная деятельность</span>
              </div>
            </div>

            <div class="plan-day_item--item">
              <div class="plan-day_item--time">
                <p>17:00<img src="../assets/images/svg-icons-page2/horiz-line.svg" alt="line">18:00</p>
              </div>
              <div class="plan-day_item--name">
                <img class="play-day_item__brace" src="../assets/images/svg-icons-page2/time/line.svg" alt="line">
                <img src="../assets/images/svg-icons-page2/time/sport.svg" alt="sport">
                <span>Лёгкая разминка, уход детей домой</span>
              </div>
            </div>

          </div>
        </div>

        <div class="plan-day_item">
          <h2>Смена 1/2 дня</h2>
          <div class="plan-day_item__border">
            <div class="plan-day_item--item">
              <div class="plan-day_item--time">
                <p>8:30<img src="../assets/images/svg-icons-page2/horiz-line.svg" alt="line">9:00</p>
              </div>
              <div class="plan-day_item--name">
                <img class="play-day_item__brace" src="../assets/images/svg-icons-page2/time/line.svg" alt="line">
                <img src="../assets/images/svg-icons-page2/time/sport.svg" alt="sport">
                <span>Сбор детей, утренняя зарядка</span>
              </div>
            </div>

            <div class="plan-day_item--item">
              <div class="plan-day_item--time">
                <p>9:00<img src="../assets/images/svg-icons-page2/horiz-line.svg" alt="line">9:40</p>
                <p>9:50<img src="../assets/images/svg-icons-page2/horiz-line.svg" alt="line">10:30</p>
              </div>
              <div class="plan-day_item--name">
                <img class="play-day_item__brace" src="../assets/images/svg-icons-page2/time/skoba.svg" alt="line">
                <img src="../assets/images/svg-icons-page2/time/learn.svg" alt="sport">
                <span>IT-урок</span>
              </div>
            </div>

            <div class="plan-day_item--item">
              <div class="plan-day_item--time">
                <p>10:30<img src="../assets/images/svg-icons-page2/horiz-line.svg" alt="line">10:40</p>
              </div>
              <div class="plan-day_item--name">
                <img class="play-day_item__brace" src="../assets/images/svg-icons-page2/time/line.svg" alt="line">
                <img src="../assets/images/svg-icons-page2/time/tea.svg" alt="sport">
                <span>Перекус (чай, снеки)</span>
              </div>
            </div>

            <div class="plan-day_item--item">
              <div class="plan-day_item--time">
                <p>10:40<img src="../assets/images/svg-icons-page2/horiz-line.svg" alt="line">11:20</p>
                <p>11:30<img src="../assets/images/svg-icons-page2/horiz-line.svg" alt="line">12:10</p>
              </div>
              <div class="plan-day_item--name">
                <img class="play-day_item__brace" src="../assets/images/svg-icons-page2/time/skoba.svg" alt="line">
                <img src="../assets/images/svg-icons-page2/time/learn.svg" alt="sport">
                <span>IT-урок</span>
              </div>
            </div>

            <div class="plan-day_item--item">
              <div class="plan-day_item--time">
                <p>12:20<img src="../assets/images/svg-icons-page2/horiz-line.svg" alt="line">13:00</p>
              </div>
              <div class="plan-day_item--name">
                <img class="play-day_item__brace" src="../assets/images/svg-icons-page2/time/line.svg" alt="line">
                <img src="../assets/images/svg-icons-page2/time/learn.svg" alt="sport">
                <span>Занятие по английскому языкуили шахматам</span>
              </div>
            </div>

            <div class="plan-day_item--item">
              <div class="plan-day_item--time">
                <p>13:00<img src="../assets/images/svg-icons-page2/horiz-line.svg" alt="line">14:00</p>
              </div>
              <div class="plan-day_item--name">
                <img class="play-day_item__brace" src=../assets/images/svg-icons-page2/time/line.svg" alt="line">
                <img src="../assets/images/svg-icons-page2/time/eat.svg" alt="sport">
                <span>Обед в кафе</span>
              </div>
            </div>

          </div>
        </div>
      </div>
    </section>

    <section class="child-slider">
      <div class="container child-slider_title">
        <h2>Занятия проходят</h2>
        <p>в современных аудиториях <br>
          с удобством, комфортом и заботой о студентах</p>
      </div>
      <div class="carousel-past-events">
        <div class="gallery">
          <img src="../assets/images/page-2/sliders/1.jpg" alt="слайд 1" class="past-events-img">
        </div>
        <div class="gallery">
          <img src="../assets/images/page-2/sliders/2.jpg" alt="слайд 2" class="past-events-img">
        </div>
        <div class="gallery">
          <img src="../assets/images/page-2/sliders/3.jpg" alt="слайд 3" class="past-events-img">
        </div>
        <div class="gallery">
          <img src="../assets/images/page-2/sliders/4.jpg" alt="слайд 4" class="past-events-img">
        </div>
        <div class="gallery">
          <img src="../assets/images/page-2/sliders/5.jpg" alt="слайд 5" class="past-events-img">
        </div>
        <div class="gallery">
          <img src="../assets/images/page-2/sliders/6.jpg" alt="слайд 5" class="past-events-img">
        </div>
      </div>
    </section>

    <section class="teaching-principle past-events">
      <div class="container">
        <h2>Принципы обучения</h2>
        <div class="teaching-principle_wrapper">
          <div class="teaching-principle_item">
            <img src="../assets/images/svg-icons/principle1.svg" alt="icon">
            <p>Передовой подход к образовательному процессу</p>
          </div>
          <div class="teaching-principle_item">
            <img src="../assets/images/svg-icons/principle-book.svg" alt="icon">
            <p>Непрерывное усовершенствование и пополнение базы курсов</p>
          </div>
          <div class="teaching-principle_item">
            <img src="../assets/images/svg-icons/principle-table.svg" alt="icon">
            <p>Только практикующие преподаватели</p>
          </div>
          <div class="teaching-principle_item">
            <img src="../assets/images/svg-icons/principle-man.svg" alt="icon">
            <p>Сопровождение на всех этапах. От начала обучения до трудоустройства</p>
          </div>
        </div>
      </div>
    </section>

  </div>
</template>

<script>
import Navbar from "../components/NavbarMain";
import Reviews from "../components/Reviews";
import {requestsMixin} from "../components/mixins/requestsMixin";

export default {
  name: "Camp",

  mixins: [requestsMixin],

  components: {
    Navbar, Reviews
  },
}
</script>

<style scoped>

.btn-wrapper {
    position: relative;
    z-index: 30
}

.accent-btn {
    background-color: #f7941d;
    border-radius: 6px;
    padding: 16px 22px 16px 22px;
    color: #fff;
    font-family: Montserrat-SemiBold;
    text-decoration: none;
    -webkit-transition: background .8s ease, border .8s ease;
    -o-transition: background .8s ease, border .8s ease;
    transition: background .8s ease, border .8s ease;
    z-index: 30
}

.accent-btn:hover {
    background: #ffae4d;
    color: inherit
}

.top-gradient {
    border-top: 2px solid;
    -o-border-image: -o-linear-gradient(left, #eb934f, #63a9da) 47% 0;
    border-image: -webkit-gradient(linear, left top, right top, from(#eb934f), to(#63a9da)) 47% 0;
    border-image: linear-gradient(90deg, #eb934f, #63a9da) 47% 0
}

.introduce_price {
    font-family: Montserrat-Bold;
    font-size: 28px;
    line-height: 34px;
    border-top: linear-gradient(90deg, #eb934f, #63a9da) 47% 0;
    padding-top: 5px
}

@media (max-width: 575.98px) {
    .introduce_price {
        font-size: 22px
    }
}

.will-learn_owl p {
    margin-left: 50px;
    max-width: 340px;
    font-size: 14px;
    line-height: 20px;
    padding-right: 30px;
    padding-left: 20px;
    padding-top: 23px
}

@media (max-width: 360px) {
    .will-learn_owl p {
        font-size: 12px
    }
}

@media (max-width: 575.98px) {
    .will-learn_owl p {
        margin-left: 0
    }
}

.will-learn_list p {
    font-size: 22px;
    line-height: 27px;
    margin-top: 20px
}

@media (max-width: 1199.98px) {
    .will-learn_list p {
        font-size: 17px
    }
}

@media (max-width: 991.98px) {
    .will-learn_list p {
        padding-left: 15px;
        font-size: 18px
    }
}

.will-learn_game h2 {
    font-family: Montserrat-Bold;
    font-size: 36px;
    line-height: 34px
}

@media (max-width: 767.98px) {
    .will-learn_game h2 {
        font-size: 30px
    }
}

.game_item_video p {
    margin-bottom: 0;
    font-family: Montserrat-SemiBold;
    font-size: 18px;
    line-height: 34px;
    margin-right: 17px
}

.game_item_video img {
    cursor: pointer
}

.game_item_item {
    list-style: none;
    padding-left: 0;
    padding-bottom: 0;
    max-width: 530px
}

.game_item_item li {
    font-family: Montserrat-Regular;
    font-size: 24px;
    line-height: 16px;
    margin-bottom: 16px;
    display: -webkit-box;
    display: -ms-flexbox;
    display: flex
}

.game_item_item li:before {
    content: "";
    background: url(../assets/images/svg-icons/checkpoint.svg);
    background-repeat: no-repeat;
    padding-left: 30px;
    display: block;
    width: 30px;
    height: 30px
}

.teaching-principle {
    padding-top: 50px
}

.teaching-principle h2 {
    font-family: Montserrat-Bold;
    font-size: 36px;
    line-height: 34px;
    margin-bottom: 53px
}

@media (max-width: 767.98px) {
    .teaching-principle h2 {
        font-size: 24px;
        margin-bottom: 25px;
        text-align: center
    }
}

@media (max-width: 767.98px) {
    .teaching-principle {
        padding-top: 25px
    }
}

.teaching-principle_wrapper {
    display: -webkit-box;
    display: -ms-flexbox;
    display: flex;
    -webkit-box-pack: justify;
    -ms-flex-pack: justify;
    justify-content: space-between;
    -ms-flex-wrap: wrap;
    flex-wrap: wrap
}

.teaching-principle_item {
    margin-top: 25px;
    max-width: 256px
}

.teaching-principle_item p {
    font-size: 18px;
    line-height: 26px;
    padding-top: 17px
}

@media (max-width: 767.98px) {
    .teaching-principle_item p {
        font-size: 14px;
        line-height: 1.3;
        padding-top: 17px;
        text-align: center
    }
}

.teaching-principle_item img {
    width: 60px;
    height: 60px
}

@media (max-width: 767.98px) {
    .teaching-principle_item img {
        display: block;
        margin: 0 auto
    }
}

@media (max-width: 767.98px) {
    .teaching-principle_item {
        max-width: auto;
        width: 45%
    }
}

@media (max-width: 575.98px) {
    .teaching-principle_item {
        max-width: 100%;
        width: 100%
    }
}

.teaching-principle_slider {
    margin-top: 60px;
    overflow: hidden
}

.how-happening h2 {
    line-height: 34px
}

@media (max-width: 575.98px) {
    .how-happening h2 {
        text-align: center
    }
}

.feedback-form__form input {
    max-width: 520px
}

.feedback-form__form_send p {
    margin: 0;
    font-size: 10px;
    line-height: 14px;
    font-family: Montserrat-Regular
}

@media (max-width: 575.98px) {
    .feedback-form__form_send p {
        margin-bottom: 15px
    }
}

.child-slider {
    margin-top: 60px;
    overflow: hidden;
    margin-bottom: 50px
}

@media (max-width: 767.98px) {
    .child-slider {
        margin-top: 20px
    }
}

.child-slider_title h2 {
    font-size: 36px;
    line-height: 34px;
    text-align: center;
    margin-bottom: 20px
}

@media (max-width: 575.98px) {
    .child-slider_title h2 {
        font-size: 24px;
        line-height: 34px
    }
}

.child-slider_title p {
    font-size: 18px;
    line-height: 26px;
    text-align: center;
    max-width: 450px;
    margin: 0 auto
}

@media (max-width: 575.98px) {
    .child-slider_title p {
        font-size: 14px;
        line-height: 18px
    }
}

.child-slider--slider {
    margin-top: 45px
}

@media (max-width: 767.98px) {
    .child-slider--slider {
        margin-top: 12px
    }
}

.main-wrapper {
    -webkit-box-flex: 1;
    -ms-flex: 1 0 auto;
    flex: 1 0 auto
}

.swiper {
    height: 250px
}

@media (max-width: 575.98px) {
    .swiper {
        height: 164px
    }
}

.swiper-scrollbar {
    background: #e0e0e0;
    height: 2px !important
}

.swiper-scrollbar {
    background: -webkit-gradient(linear, left top, right top, from(#eb934f), to(#63a9da)) 47% 0;
    background: -o-linear-gradient(left, #eb934f, #63a9da) 47% 0;
    background: linear-gradient(90deg, #eb934f, #63a9da) 47% 0;
    height: 5px;
    top: -3px
}

.swiper-container-horizontal > .swiper-scrollbar {
    position: relative;
    border-radius: 2px;
    height: 5px;
    max-width: 1180px;
    bottom: 0;
    left: 50%;
    -webkit-transform: translateX(-50%);
    -ms-transform: translateX(-50%);
    transform: translateX(-50%)
}

.swiper-slide {
    width: auto !important
}

.swiper-slide img {
    height: 210px;
    max-width: 100%;
    border-radius: 20px;
    -o-object-fit: cover;
    object-fit: cover
}

@media (max-width: 575.98px) {
    .swiper-slide img {
        height: 140px
    }
}
</style>