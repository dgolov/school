<template>
  <div>
    <Header/>
    <router-view/>
    <div style="display: none;" class="common-modal">
      <div class="modal-mask">
        <div class="common-modal-place">
          <div class="common-modal-content">
            <div class="common-modal-header">
              <a class="common-modal-close">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" tabindex="-1">
                  <path d="M20 20L4 4m16 0L4 20"></path>
                </svg>
              </a>
            </div>
            <div class="data-place">
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="contact-form-sent" style="display: none;">
      <h2 class="contact-form-caption">Ваша заявка успешно отправлена</h2>
      <div class="contact-form-owl-block">
        <div class="owl-owl"></div>
        <div class="owl-content">
          Скоро мы свяжемся с вами и ответим на все вопросы.
          А пока вы можете посмотреть какие интересные у нас есть курсы.
        </div>
        <img src="../assets/082022/img/contact-form-owl-owlm.png" class="owl-owlm">
        <div class="owl-link">
          <a href="/education">Смотреть все курсы</a>
        </div>
        <br clear="all">
      </div>
    </div>

    <div class="contact-form-error" style="display: none;">
      <div class="error-container">
        <h2 class="contact-form-caption">Ошибка</h2>
        <div class="contact-form-owl-block">
          <div class="owl-owl"></div>
          <div class="owl-content">
          </div>
          <img src="../assets/082022/img/contact-form-owl-owlm.png" class="owl-owlm">
          <br clear="all">
        </div>
      </div>
    </div>

    <div class="contact-form-place" style="display: none;">
      <div class="form-container">
        <h2 class="contact-form-caption">Отправить заявку</h2>
        <form class="contact-form">
          <div class="row">
            <div class="col-12"><input type="text" name="name" placeholder="Ваше имя"></div>
            <div class="col-sm-6"><input type="text" name="phone" placeholder="Ваш телефон"></div>
            <div class="col-sm-6"><input type="text" name="email" placeholder="Ваш e-mail"></div>
            <div class="col-12"><textarea name="message" placeholder="Ваше сообщение"></textarea></div>
            <div class="col-sm-6"><p>Нажимая на кнопку, я соглашаюсь на обработку персональных данных и с правилами
              пользования Платформой</p></div>
            <div class="col-sm-6">
              <button type="submit">Отправить</button>
            </div>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<style>
.contact-form-owl-block {
  background: no-repeat left center url('../assets/082022/img/contact-form-owl-block-bg.png');
  background-size: 60%;
  box-sizing: border-box;
  padding: 50px 200px 50px 118px;
}

.contact-form-owl-block .owl-owlm {
  display: none;
}

.contact-form-owl-block .owl-owl {
  background: url('../assets/082022/img/contact-form-owl-owl.png') no-repeat 100% 0;
  float: left;
  width: 274px;
  height: 294px;
}

.contact-form-owl-block .owl-content {
  background: linear-gradient(#fff 0 0) padding-box, linear-gradient(90deg, #f7941d, #27aae1) border-box;
  border: 2px solid transparent;
  border-radius: 15px;
  min-height: 160px;
  padding: 20px 20px 20px 32px;
  margin-left: 272px;

  font-style: normal;
  font-weight: 500;
  font-size: 20px;
  line-height: 28px;
}

.contact-form-owl-block .owl-link {
  margin-left: 274px;
  margin-top: 56px;
  text-align: center;
}

.contact-form-owl-block .owl-link a {

  color: #00093C;

  padding-right: 30px;

  background: no-repeat right center url('../assets/082022/img/contact-form-owl-link.png');

  font-style: normal;
  font-weight: 500;
  font-size: 16px;
  line-height: 20px;
  text-decoration: none;
}


h2.contact-form-caption {
  margin-top: 15px;
  font-style: normal;
  font-weight: 500;
  font-size: 40px;
  line-height: 120%;
  text-align: center;
  color: #00093C;
  padding: 0 40px;
}

form.contact-form {
  padding: 50px 15px 50px 50%;
  background: no-repeat left center url('../assets/082022/img/contact-form-bg.png');
  background-size: 50%;
  box-sizing: border-box;
}

form.contact-form input[type='text'], form.contact-form textarea {
  width: 100%;
  height: 50px;
  background: rgba(0, 9, 60, 0.1);
  -webkit-border-radius: 6px;
  -moz-border-radius: 6px;
  border-radius: 6px;
  margin-bottom: 20px;
  padding: 0 20px;
  position: relative;
  z-index: 2;
  -webkit-transition: all 200ms ease;
  -moz-transition: all 200ms ease;
  -ms-transition: all 200ms ease;
  -o-transition: all 200ms ease;
  transition: all 200ms ease;
}

form.contact-form input[type='text']:focus, form.contact-form textarea:focus {
  box-shadow: 0 0 0 1px #F7941D;
}

form.contact-form textarea {
  height: 100px;
  padding: 20px;
  box-sizing: border-box;
}

form.contact-form p {
  font-size: 10px;
  line-height: 14px;
  color: #4F4F4F;
  padding-bottom: 15px;
}

form.contact-form button {
  width: 100%;
  height: 50px;
  color: #fff;
  background: #F7941D;
  border-radius: 10px;
  font-weight: 700;
}

form.contact-form button:hover {
  background: #FFAE4D;
}

form.contact-form .text {
  width: 495px;
  height: 400px;
  background: url('../assets/082022/img/text.png');
  position: absolute;
  bottom: 20px;
  left: -83px;
  -webkit-box-sizing: border-box;
  -moz-box-sizing: border-box;
  box-sizing: border-box;
  font-weight: 500;
  font-size: 16px;
  line-height: 26px;
  padding: 20px 16px 0 130px;
}

form.contact-form .text span {
  display: block;
  font-weight: 600;
  font-size: 22px;
  line-height: 29px;
  margin-bottom: 20px;
}

@media (max-width: 885px) {
  .contact-form-owl-block {
    padding: 15px 30px 10px 30px;
  }

  .contact-form-owl-block .owl-content {
    margin-left: 271px;
  }
}

@media (max-width: 768px) {
  h2.contact-form-caption {
    font-size: 24px;
  }

  .contact-form-owl-block .owl-content {
    font-size: 16px;
    line-height: 22px;
    padding: 10px 10px 10px 22px;
  }
}

@media (max-width: 575px) {

  h2.contact-form-caption {
    font-size: 20px;
  }

  .contact-form-owl-block .owl-owl {
    display: none;
  }

  .contact-form-owl-block .owl-owlm {
    display: block;
    position: relative;
    top: -3px;
  }

  form.contact-form {
    padding: 20px;
    background: none;
  }

  .contact-form-owl-block .owl-content {
    margin-left: auto;
    min-height: auto;
  }

  .contact-form-owl-block .owl-link {
    margin-left: auto;
    margin-top: -50px;
    position: relative;
    z-index: 1000;
  }

  .contact-form-owl-block {
    background: none;
  }
}
</style>

<script>
import Header from "../components/082022/Header";
import Footer from "../components/082022/Footer";

window.$ = require('jquery');
window.JQuery = window.$;
let $ = window.$;
let JQuery = window.JQuery;

import '../assets/082022/js/bootstrap.bundle.min.js';
import '../assets/082022/js/slick.min.js';
import '../assets/082022/js/jquery-ui.js';
import '../assets/082022/js/jquery.sticky.js';
import '../assets/082022/js/wow.min.js';

import axios from "axios";

window.validatePhone = function validatePhone(phone) {
  phone = ('' + phone).replace(/\D/g, '');
  phone = '+' + phone.replace(/^8/, '7');
  var phonemask = new RegExp('^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$', 'im');
  return phonemask.test(phone);
}

window.validateEmail = function validateEmail(email) {
  return String(email)
      .toLowerCase()
      .match(
          /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
      );
}

window.setModalFormError = function setModalFormError(formPlace, message) {
  formPlace.find('.form-container').hide();
  formPlace.parent().find('.common-modal-close').hide();
  formPlace
      .append($('.contact-form-error').html())
      .find('.owl-content').text(message);

  window.ModalFormErrorTimer = setTimeout(function () {
    formPlace.find('.error-container').hide();
    formPlace.find('.form-container').show();
    formPlace.parent().find('.common-modal-close').show();
  }, 1500);
}

window.CourceModalShow = function CourceModalShow(thisapp) {
  $('.common-modal-content .data-place').html($('.contact-form-place').html());
  $('.common-modal-content form').submit(function () {

    var phone = '';
    var email = '';
    var name = '';

    const body = {
      request_fio: name = $(this).find('input[name="name"]').val(),
      request_phone: phone = $(this).find('input[name="phone"]').val(),
      request_email: email = $(this).find('input[name="email"]').val(),
      type_request: thisapp.typeRequest,
      status: thisapp.status,
      date: thisapp.dates,
      student: null,
      client: null,
      purpose: 'info',
      result: null,
      remind: null,
      comment: $(this).find('textarea[name="message"]').val(),
      manager: null,
      course: null,
      event: null
    }

    if (!name) name = '';
    if (!phone) phone = '';
    if (!email) email = '';

    if (name == '') {
      window.setModalFormError($('.common-modal-content .data-place'), 'Введите Ваше имя!');
      return false;
    }

    if (phone == '' && email == '') {
      window.setModalFormError($('.common-modal-content .data-place'), 'Введите номер телефона или адрес электронной почты!');
      return false;
    } else {
      if (phone != '') {
        if (!window.validatePhone(phone)) {
          window.setModalFormError($('.common-modal-content .data-place'), 'Проверьте, возможно вы ввели неверный номер телефона. ');
          return false;
        }
      }

      if (email != '') {
        if (!window.validateEmail(email)) {
          window.setModalFormError($('.common-modal-content .data-place'), 'Проверьте, возможно вы ввели неверный email.');
          return false;
        }
      }
    }

    axios
        .post(thisapp.$store.getters.getServerUrl + '/requests/', body)
        .then((response) => {
          thisapp.$store.commit("setAuthUser", {
            authUser: response.data,
            isAuthenticated: true,
          });
        });
    $('.common-modal-content .data-place').html($('.contact-form-sent').html());
    return false;
  })
  $('.common-modal').show();
}

export default {
  name: "L082022",

  components: {
    Header,
    Footer
  },

  data() {
    return {
      typeRequest: 'online',
      status: 'new',
      date: '',
    }
  },

  created() {
    import('@/assets/082022/css/bootstrap.min.css');
    import('@/assets/082022/css/slick.css');
    import('@/assets/082022/css/style.css');
    import('@/assets/082022/css/new.0822.css');
    import('@/assets/082022/css/animate.0822.css');
    import('@/assets/082022/css/video-modal.css');
    import('@/assets/082022/css/common-modal.css');
    import('@/assets/css/cabinet.css');

  },

  mounted: function () {

    let thisapp = this;

    let tinkoffScript = document.createElement('script')
    tinkoffScript.setAttribute('src', 'https://forma.tinkoff.ru/static/onlineScript.js')
    document.head.appendChild(tinkoffScript)

    $(document).ready(function () {
      $('.tabs').tabs();
      $("#header").sticky({topSpacing: 0});

      $('.buttonGetCource, .buttonFindeCource').click(function () {
        window.location.href = "/send-request";
        return false;
      });
    });

    $('.GetCourceModal').click(function () {
      window.CourceModalShow(thisapp);
      return false;
    });

    $('.common-modal-close').click(function () {
      $('.common-modal-content .data-place').html('')
      $('.common-modal').hide();
      return false;
    });

    $('.footer nav p').click(function () {
      $(this).toggleClass('active');
      $(this).next('ul').toggleClass('opened');
    });
    $('.header .menu-button').click(function () {
      $(this).toggleClass('active');
      $('.mobile-menu').toggleClass('opened');
    });
    $(window).bind('mousewheel', function (event) {
      if (event.originalEvent.wheelDelta >= 0) {
        $('.top-page-line').addClass('opened');
        $('.ways-block nav ul').addClass('other');
      } else {
        $('.top-page-line').removeClass('opened');
        $('.ways-block nav ul').removeClass('other');
      }
    });
    $('.top-page-line .city .select label.l1, .mobile-menu .city .select label.l1').click(function () {
      $('.contacts-block .map').removeClass('active');
      $('.contacts-block .map.m2').addClass('active');
      $('.contacts-block form.big').hide();
      $('.contacts-block .r').show();
    });
    $('.top-page-line .city .select label.l2, .mobile-menu .city .select label.l2').click(function () {
      $('.contacts-block .map').removeClass('active');
      $('.contacts-block .map.m1').addClass('active');
      $('.contacts-block form.big').hide();
      $('.contacts-block .r').show();
    });
    $('.top-page-line .city .select label.l3, .mobile-menu .city .select label.l3').click(function () {
      $('.contacts-block .map').removeClass('active');
      $('.contacts-block form.big').show();
      $('.contacts-block .r').hide();
    });
    $(document).mousemove(function (e) {
      var x = (e.pageY * 1 / 35), y = (e.pageX * 1 / 35);
      $('.rounds').css('margin', x + 'px ' + y + 'px');
    });
    $('.first-block .bottom-link a').bind("click", function (e) {
      var anchor = $(this);
      $('html, body').stop().animate({
        scrollTop: $(anchor.attr('href')).offset().top
      }, 1000);
      e.preventDefault();
    });
    $('.index-page-slider').slick({});

    $('.faq-block .item .name').click(function () {
      $(this).toggleClass('active');
      $(this).next('.text').slideToggle();
    });
  },
}
</script>