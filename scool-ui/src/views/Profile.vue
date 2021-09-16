<template>
  <div id="profile">
    <navbar></navbar>
    <div class="step landing__section" style="background-color: #f7f7f7">
      <div class="page">
        <div class="container mt-5">
          <div class="page__inner">
            <div class="page__menu">
              <h3>Профиль</h3>
              <hr>
              <profile-menu></profile-menu>
            </div>
            <div class="page__main">
              <div class="row">
                <div class="col-md-6">
                  <h3 class="page__main__title left-align mb-2 center">Гришин Иван Николаевич</h3>
                  <h6 class="center">Студент</h6>
                  <hr/>
                  <button class="grey-button">Редактировать профиль</button>
                </div>
                <div class="col-md-6">
                  <img class="center" src="../assets/images/avatars/mike.jpeg"
                       style="display: block; width: 180px; height: 180px; border: 0; border-radius: 50%; margin: 30px auto; text-align: center">
                </div>
              </div>
              <div class="row my-3">
                <div class="col-md-3">
                  <a href="#" style="font-size: 20px; color: #4c28de;">2</a>
                  <h6>Друзья</h6>
                </div>
                <div class="col-md-3">
                  <a href="#" style="font-size: 20px; color: #4c28de;">1</a>
                  <h6>Подписчики</h6>
                </div>
                <div class="col-md-3">
                  <a href="#" style="font-size: 20px; color: #4c28de;">0</a>
                  <h6>Подписки</h6>
                </div>
                <div class="col-md-3">
                  <a href="#" style="font-size: 20px; color: #4c28de;">3</a>
                  <h6>Фотографии</h6>
                </div>
              </div>
              <hr/>
              <div class="left-align mt-5">
                <div class="row my-3">
                  <div class="col-md-3">
                    <h6>День рождения:</h6>
                  </div>
                  <div class="col-md-9 left-align">
                    <a href="#">24 декабря 1985</a>
                  </div>
                </div>
                <div class="row my-3">
                  <div class="col-md-3">
                    <h6>Пол:</h6>
                  </div>
                  <div class="col-md-9 left-align">
                    <a href="#">Женский</a>
                  </div>
                </div>
                <hr/>
                <h3 class="mb-4">Контактная информация:</h3>
                <div class="row my-3">
                  <div class="col-md-3">
                    <h6>Телефон:</h6>
                  </div>
                  <div class="col-md-9 left-align">
                    <a href="tel:+79082373971">+7 (908) 237-39-71</a>
                  </div>
                </div>
                <div class="row my-3">
                  <div class="col-md-3">
                    <h6>Город:</h6>
                  </div>
                  <div class="col-md-9 left-align">
                    <a href="#">Дзержинск</a>
                  </div>
                </div>
                <div class="row my-3">
                  <div class="col-md-3">
                    <h6>E-mail:</h6>
                  </div>
                  <div class="col-md-9 left-align">
                    <a href="mailto:vanya_grishin@mail.ru">vanya_grishin@mail.ru</a>
                  </div>
                </div>
                <div class="row my-3">
                  <div class="col-md-3">
                    <h6>Профиль vk.com:</h6>
                  </div>
                  <div class="col-md-9 left-align">
                    <a href="https://vk.com/piupiu7">https://vk.com/piupiu7</a>
                  </div>
                </div>
                <div class="row mt-3 mb-4">
                  <div class="col-md-3">
                    <h6>Профиль Instagram:</h6>
                  </div>
                  <div class="col-md-9 left-align">
                    <a href="#">-</a>
                  </div>
                </div>
                <hr/>
                <h3 class="mb-4">Личная информация:</h3>
                <div class="row my-3">
                  <div class="col-md-3">
                    <h6>Увлечения:</h6>
                  </div>
                  <div class="col-md-9 left-align">
                    <a href="#">Велосипед, спорт, бег</a>
                  </div>
                </div>
                <div class="row mt-3">
                  <div class="col-md-3">
                    <h6>Мечта:</h6>
                  </div>
                  <div class="col-md-9 left-align">
                    <a href="#">Слетать на луну</a>
                  </div>
                </div>
                <div class="row my-3 mb-4">
                  <div class="col-md-3">
                    <h6>О себе:</h6>
                  </div>
                  <div class="col-md-9 left-align">
                    <p>Lorem Ipsum - это текст-"рыба", часто используемый в печати и вэб-дизайне.
                      Lorem Ipsum является стандартной "рыбой" для текстов на латинице с начала XVI века.
                    </p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Navbar from "../components/Navbar";
import ProfileMenu from "../components/ProfileMenu";

export default {
  name: "Profile",
  components: {ProfileMenu, Navbar}
}
</script>

<style scoped>

</style>