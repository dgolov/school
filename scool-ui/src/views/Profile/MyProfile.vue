<template>
  <div id="profile">
    <div class="cabinet-page">
      <div class="container">
        <button class="cabinet-menu-button">МЕНЮ ЛИЧНОГО КАБИНЕТА</button>
        <div class="row">
          <div class="col-xl-2 col-lg-3">
            <nav class="menu">
              <ul>
                <li><a href="#" class="active"><span><img src="img/cabinet-menu1.svg"></span> Моя страница</a></li>
                <li><a href="#"><span><img src="img/cabinet-menu2.svg"></span> Доступные курсы</a></li>
                <li><a href="#"><span><img src="img/cabinet-menu3.svg"></span> Расписание</a></li>
                <li><a href="#"><span><img src="img/cabinet-menu4.svg"></span> Успеваемость</a></li>
                <li><a href="#"><span><img src="img/cabinet-menu5.svg"></span> Группы</a></li>
                <li><a href="#"><span><img src="img/cabinet-menu6.svg"></span> Друзья</a></li>
                <li><a href="#"><span><img src="img/cabinet-menu7.svg"></span> Подписчики</a></li>
                <li><a href="#"><span><img src="img/cabinet-menu8.svg"></span> Сообщения</a></li>
                <li><a href="#"><span><img src="img/cabinet-menu9.svg"></span> Фотографии</a></li>
                <li><a href="#"><span><img src="img/cabinet-menu10.svg"></span> Поиск</a></li>
                <li><a href="#"><span><img src="img/cabinet-menu11.svg"></span> Настройки</a></li>
                <li><a href="#"><span><img src="img/cabinet-menu12.svg"></span> Игры</a></li>
                <li><a href="#"><span><img src="img/cabinet-menu13.svg"></span> Магазин</a></li>
                <li><a href="#"><span><img src="img/cabinet-menu14.svg"></span> Награды</a></li>
                <li><a href="#"><span><img src="img/cabinet-menu15.svg"></span> Выход</a></li>
              </ul>
            </nav>
          </div>
          <div class="col-xl-10 col-lg-9">
            <div class="cabinet-content">
              <div class="user-info">
                <div class="top-info">
                  <div><img src="img/avatar3.png"></div>
                  <div>
                    <div class="name">
                      <span>Константинопольский Константин Константинович</span>
                      Студент
                    </div>
                    <div class="counts">
                      <div class="count">
                        <span>246</span>
                        Друзья
                      </div>
                      <div class="count">
                        <span>3 257</span>
                        Подписчики
                      </div>
                      <div class="count">
                        <span>17</span>
                        Подписки
                      </div>
                      <div class="count">
                        <span>57</span>
                        Фотографии
                      </div>
                    </div>
                  </div>
                </div>
                <div class="item">
                  <table>
                    <tr>
                      <td>День рождения:</td>
                      <td>23 июня 2007 года</td>
                    </tr>
                    <tr>
                      <td>Пол:</td>
                      <td>Мужской</td>
                    </tr>
                  </table>
                </div>
                <div class="item">
                  <p>Контактная информация:</p>
                  <table>
                    <tr>
                      <td>Телефон:</td>
                      <td>+7 927 374 51 23</td>
                    </tr>
                    <tr>
                      <td>Город:</td>
                      <td>Дзержинск</td>
                    </tr>
                    <tr>
                      <td>E-mail:</td>
                      <td>kostya2007@mail.ru</td>
                    </tr>
                    <tr>
                      <td>Профиль VK:</td>
                      <td>https://vk.com/kkostya</td>
                    </tr>
                  </table>
                </div>
                <div class="item">
                  <p>Личная информация:</p>
                  <table>
                    <tr>
                      <td>О себе:</td>
                      <td>Люблю учиться в Академии будущего ХОД</td>
                    </tr>
                    <tr>
                      <td>Увлечения:</td>
                      <td>Книги, спорт, верховая езда, игра на арфе, пилотирование самолёта</td>
                    </tr>
                  </table>
                </div>
              </div>
            </div>
          </div>
          <div class="col-xl-2 col-lg-3"></div>
          <div class="col-xl-10 col-lg-9">
            <div class="cabinet-copy">
              © Академия будущего «ХОД», 2022
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="step landing__section main-section past-events">
      <div class="page">
        <div class="container mt-1">
          <div class="page__inner">
            <profile-menu :header="header"></profile-menu>
            <profile-info v-if="responseData" :profile="responseData"></profile-info>
            <loader v-else object="#ff9633" color1="#ffffff" color2="#17fd3d" size="5" speed="2" bg="#343a40"
                    objectbg="#999793" opacity="80" disableScrolling="false" name="spinning"></loader>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Navbar from "../../components/Navbar";
import ProfileMenu from "../../components/Profile/ProfileMenu";
import ProfileInfo from "../../components/Profile/ProfileInfo";
import {redirect} from "../../components/mixins/redirect";
import {requestsMixin} from "../../components/mixins/requestsMixin";

export default {
  title: 'Академия будущего | Личный кабинет',
  name: "MyProfile",

  data() {
    return {
      header: 'Личный кабинет',
      responseData: null
    }
  },

  components: {
    ProfileMenu, Navbar, ProfileInfo
  },

  created() {
    this.createGetRequest(`/profile/${this.$store.state.authUser.id}/`)
  },

  mixins: [redirect, requestsMixin],
}
</script>

<style scoped>

</style>