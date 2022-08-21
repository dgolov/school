<template>
  <div id="contacts">
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
                  <p v-if="$store.state.address" class="connection-address">{{ $store.state.address }}</p>
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
                <iframe class="contacts-map-dz" src="https://yandex.ru/map-widget/v1/?um=constructor%3Ad18c832af74e9b9b0a9ef496a75ce63297a9ecf8dc34897fc8620255cda476b8&amp;source=constructor" width="100%" height="414" frameborder="0"></iframe>
                <iframe class="contacts-map-nn" src="https://yandex.ru/map-widget/v1/?um=constructor%3A87cc24d5013f025063c014b1c23ad401d1cfd347455ef2d999759fdadd29621c&amp;source=constructor" width="100%" height="414" frameborder="0"></iframe>
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
  
  created() {
	  import('@/assets/082022/css/stumb/style.css');
	  import('@/assets/082022/css/stumb/main.css');  
  },
  
  mounted() { 

	  	let $ = window.$;
		let outerApp = this;
		
		var city = this.$store.state.city;
		$(document).ready(function(){
			
			switch(city) {
			case 'Нижний Новгород':
				$('.contacts-map-nn').show();
				break;
			case 'Дзержинск':
				$('.contacts-map-dz').show();
				break;
			};
			
       		$('.top-page-line .city .select label.l1, .mobile-menu .city .select label.l1').click(function() {
       			$('#contacts .map > iframe').hide();
       			$('.contacts-map-dz').show();
       		})

       		$('.top-page-line .city .select label.l2, .mobile-menu .city .select label.l2').click(function() {
       			$('#contacts .map > iframe').hide();
       			$('.contacts-map-nn').show();
       			
       		})
			
       		$('.top-page-line .city .select label.l3, .mobile-menu .city .select label.l3').click(function() {
       			$('#contacts .map > iframe').hide();
       		})
		});
		
},
  
}
</script>

<style scoped>
	.breadcrumb, .breadcrumb a {
		line-height: 22.5px;
	}

	.contacts-map-nn, .contacts-map-dz {
		display: none;
	}

</style>