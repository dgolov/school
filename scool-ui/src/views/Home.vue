<template>
  <div class="home">
    <navbar></navbar>
    <div class="hero">
      <div class="hero__inner">
        <div class="hero__content">
          <div class="hero__content__inner" id=''>
            <div style="position: absolute; width: 55%; padding: 4.5% 11%; text-align: left; color: #ffffff">
              <h4 style="color: #ffffff; margin: 0; width: 60%">Образовательная платформа ХОД Future Academy</h4>
              <h2 class="hero__title my-4">Смените профессию Научитесь новому Найдите себя</h2>
            </div>
            <img src="../assets/images/bg_test.png">
          </div>
        </div>
        <div class="hero__content__mobile">
          <div class="hero__content__inner">
            <img src="../assets/images/bg_test_mobile.png">
            <div class="cta cta--reverse left-align" style="padding-left: 20px;">
              <h4 style="color: #ffffff; margin: 0; width: 80%;">Образовательная платформа ХОД Future Academy</h4>
              <h2 class="hero__title my-2 bold" style="font-size: 26px; width: 95%">
                Смените профессию <br/>Научитесь новому<br/> Найдите себя
              </h2>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="steps white-section mt-0 pt-0">
      <div class="container">
        <div class="row">
          <div class="col-md-3">
            <img src="../assets/images/owl-main.svg">
          </div>
          <div class="col-md-9">
            <div class="row groups mb-4">
              <div class="col-md-4 group-active" id="children">
                <img src="../assets/images/children.svg" class="group-image">
                <div class="group-text">
                  <button @click="setAgeGroup('children')">Дети</button>
                </div>
              </div>
              <div class="col-md-4 center" id="teens">
                <img src="../assets/images/teens.svg" class="group-image">
                <div class="group-text">
                  <button @click="setAgeGroup('teens')">Подростки</button>
                </div>
              </div>
              <div class="col-md-4 center" id="adults">
                <img src="../assets/images/adults.svg" class="group-image">
                <div class="group-text">
                  <button @click="setAgeGroup('adults')">Взрослые</button>
                </div>
              </div>
            </div>
            <div class="mb-5">
              <div v-for="category in categoryList" v-if="category.age_group === age_group" class="category-area">
                <button class="category-button" @click="goTo(category.name)">
                  {{ category.name }}
                </button>
              </div>
            </div>
          </div>
        </div>
        <div class="row">
          <h3 class="mt-3 bold mb-3">Популярные направления</h3>
          <div class="col-md-4">
            <div class="step__media">
              <img src="../assets/images/chess.jpg" class="step__image">
            </div>
            <h4 class="bold">Шахматы</h4>
            <p class="step__text">Занятия шахматами значительно расширяют горизонты мышления и сознания у ребенка,
              развивают фантазию, аналитическое и логическое мышление, обучают принимать решения и просчитывать
              возмжный
              ход соперника.</p>
          </div>
          <div class="col-md-4">
            <div class="step__media">
              <img src="../assets/images/design.jpg" class="step__image">
            </div>
            <h4 class="bold">Дизайн</h4>
            <p class="step__text">Дизайн и рисование сопособствуют развитию зрительной координации, помогают
              развивать интеллектуальные, и физические способности. Хорошо развитая мелкая моторика будет полезна
              во многих сферах деятельности.</p>
          </div>
          <div class="col-md-4">
            <div class="step__media">
              <img src="../assets/images/coding.jpg" class="step__image ">
            </div>
            <h4 class="bold">Программирование</h4>
            <p class="step__text">Изучая программирование у ребенка развивается вычислительное мышление.
              Вычислительное
              мышление помогает развиватию навыков решения сложных задач, креативного мышления, умения учиться и
              навыков
              работы в команде.</p>
          </div>
        </div>
      </div>
    </div>
    <div class="white-section">
      <div class="container">
        <div class="row">
          <div class="col-md-8">
            <h3 class="bold">Актуальные знания от признанных экспертов рынка для новичков и практикующих
              специалистов.</h3>
          </div>
        </div>
      </div>
    </div>
    <div class="white-section">
      <div class="container">
        <div class="row">
          <div class="col-md-4">
            <h3 class="text-gradient mt-4 mb-0">600</h3>
            <p class="expanded__text bold px-1">Курсов</p>
          </div>
          <div class="col-md-4">
            <h3 class="text-gradient mt-4 mb-0">82</h3>
            <p class="expanded__text bold px-1">Ведущих преподователей</p>
          </div>
          <div class="col-md-4">
            <h3 class="text-gradient mt-4 mb-0">14795</h3>
            <p class="expanded__text bold px-1">Выпускников</p>
          </div>
        </div>
      </div>
    </div>
    <div class="white-section mt-3 mb-5">
      <div class="container">
        <div class="row">
          <div class="col-md-12">
            <div class="container news-block py-4 mb-4" style="background-color: #F7BC75;">
              <div class="row">
                <div class="col-md-2">
                  <h2 class="bold" style="font-size: 72px; margin: 0; font-weight: bold;">25</h2>
                  <p style="font-size: 22px; font-weight: bold;">ноября</p>
                </div>
                <div class="col-md-7 px-5">
                  <h3 class="left-align bold" style="font-size: 34px; margin: 20px 0 20px 0">День открытых
                    дверей </h3>
                  <p class="news-block-text">Приглашаем всех желающих на бесплатную экскурсию
                    в мир востребованных профессий и полезных навыков</p>
                </div>
                <div class="col-md-3">
                  <button class="button news-block-button w-75" style="margin-top: 20%">Записаться</button>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="row">
          <div class="col-md-5">
            <div class="news-block py-4 mb-4" style="background-color: #C5DDFF; height: 412px;">
              <img src="../assets/images/education.svg">
              <h2 class="bold mb-4">Программы обучения</h2>
              <p class="news-block-text px-3" style="text-align: center">В списке наших курсов вы сможете найти
                профессию и занятие по душе, изучить
                новое и получить практические знания, которые помогут получить работу мечты.</p>
              <button class="button news-block-button w-50 mt-4 mb-4">Подробнее</button>
            </div>
          </div>
          <div class="col-md-7">
            <div class="row">
              <div class="col-md-6">
                <div class="news-block py-4 mb-4" style="background-color: #B8EFCF;">
                  <img src="../assets/images/news-main.svg">
                  <h2 class="bold">Новости академии</h2>
                </div>
              </div>
              <div class="col-md-6">
                <div class="news-block py-4 mb-4 white-text" style="background-color: #FFEEF6;">
                  <img src="../assets/images/it-world.svg">
                  <h2 class="bold">Мир IT</h2>
                </div>
              </div>
            </div>
            <div class="col-md-12">
              <div class="news-block py-4 mb-4 tests" style="background-color: #FFE38E;">
                <div class="row">
                  <div class="col-md-4 news-image-block">
                    <img src="../assets/images/tests.svg">
                  </div>
                  <div class="col-md-8">
                    <h2 class="left-align bold px-3">Попробуй</h2>
                    <p class="news-block-text px-3">Пройдите тест и узнайте свои способности в сфере информационных
                      технологий</p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="cta cta--reverse">
      <div class="container">
        <div class="row">
          <div class="col-md-6">
            <h2 class="white-text bold">Оставьте заявку на обучение</h2>
            <p class="white-text pt-1">Мы свяжемся с вами в течении дня и отправим презентацию
              интересующего вас курса. Если у вас возникли вопросы о формате обучения, или вы не знаете что
              выбрать, мы позвоним, чтобы ответить на все ваши вопросы, произведем расчет финальной стоимости
              учитывая все возможные льготы, скидки и выбранного вами пакета.
            </p>
          </div>
          <div class="col-md-6 pt-4">
            <form>
              <input type='text' placeholder="ФИО...">
              <div class="double">
                <div class="half">
                  <input type="text" id="first" placeholder="Телефон...">
                </div>
                <div class="half">
                  <input type="text" id="second" placeholder="Электронная почта...">
                </div>
              </div>
              <button class="button button__accent w-100"> Отправить</button>
            </form>
          </div>
        </div>
      </div>
    </div>
    <div class="white-section mt-3 mb-5">
      <div class="container">
        <div class="row mb-5">
          <div class="col-md-12">
            <h2 class="center bold">Добро пожаловать в Академию будущего ХОД</h2>
          </div>
        </div>
        <div class="row center">
          <div class="col-md-3 welcome-block">
            <img src="../assets/images/main-icon1.svg">
            <p>Передовой подход к образовательному процессу</p>
          </div>
          <div class="col-md-3 welcome-block">
            <img src="../assets/images/main-icon2.svg">
            <p>Непрерывное усовершенствование и пополнение базы курсов</p>
          </div>
          <div class="col-md-3 welcome-block">
            <img src="../assets/images/main-icon3.svg">
            <p>Только практикующие преподаватели</p>
          </div>
          <div class="col-md-3 welcome-block">
            <img src="../assets/images/main-icon4.svg">
            <p>Сопровождение на всех этапах. От начала обучения до трудоустройства</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>


<script>
import Navbar from "../components/NavbarMain";
import axios from "axios";

export default {
  name: 'Home',
  components: {
    Navbar,
  },

  data() {
    return {
      age_group: 'children',
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

    goTo(name) {
      this.$router.push({name: 'Education', params: {'category': name, 'ageGroup': this.age_group}})
    },

    setAgeGroup(group) {
      let groups = ['children', 'teens', 'adults'];
      for (let item_group of groups) {
        let item_div = document.getElementById(item_group)
        if (item_group !== group) {
          item_div.classList.remove('group-active')
        } else {
          item_div.classList.add('group-active');
        }
      }
      this.age_group = group;
    },
  },
}
</script>


<style scoped>
.hero__content__mobile {
  display: none;
}

@media (max-width: 992px) {
  .hero__content {
    display: none;
  }

  .hero__content__mobile {
    display: block;
  }
}

.header-image {
  position: absolute;
  bottom: 0;
  right: 5%;
  width: 40%
}

.white-section {
  background-color: #ffffff;
}

.header-block {
  border-radius: 10px;
  padding: 10px;
  margin: 40px;
  background-color: #ffffff;
  width: 30%;
  display: inline-block;
  float: left;
}

@media (max-width: 992px) {
  .header-block {
    margin: 20px;
    background-color: #ffffff;
    width: 90%;
    display: block;
  }
}

@media (min-width: 992px) {
  .header-image {
    position: absolute;
    bottom: 0;
    right: 5%;
    width: 20%
  }
}

.text-gradient {
  font-size: 5em;
  font-weight: 1000;
  background: linear-gradient(135deg, #eb934f 20%, #63a9da 70%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  display: inline-block;
}

.news-block {
  border: none;
  border-radius: 10px;
  text-align: center;
}

.news-block-text {
  text-align: left;
}

.news-image-block {
  position: relative;
}

.news-image-block img {
  position: absolute;
  left: 0;
  top: 0;
  bottom: 0;
  right: 0;
  margin: auto;
}

@media (max-width: 992px) {
  .news-image-block {
    position: relative;
  }

  .news-image-block img {
    position: relative;
  }
}

.news-block-button {
  border-radius: 10px;
  background-color: #ffffff;
  border-color: #ffffff;
  color: #000000;
}

.white-text {
  color: #ffffff;
}

.welcome-block {
  padding: 30px;
}

.welcome-block img {
  height: 60px;
  margin-bottom: 40px;
}
</style>