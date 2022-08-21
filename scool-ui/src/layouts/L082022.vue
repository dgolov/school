<template>
	<div>
		<Header/>
		<router-view/>
	    <Footer/>
    </div>
</template>

<style>
</style>

<script>
	import Header from "../components/082022/Header";
	import Footer from "../components/082022/Footer";
	
	window.$ = require('jquery');
	window.JQuery = window.$;
	let $ = window.$;
	let JQuery = window.JQuery; 

	//import $ from "jquery";
	import '../assets/082022/js/bootstrap.bundle.min.js';
	import '../assets/082022/js/slick.min.js';
	import '../assets/082022/js/jquery-ui.js';
	import '../assets/082022/js/jquery.sticky.js';
	import '../assets/082022/js/wow.min.js';
	
    export default {
        name: "L082022",
        
        components: {
            Header,
            Footer
        },

        created() {
      	  import('@/assets/082022/css/bootstrap.min.css');
    	  import('@/assets/082022/css/slick.css');
    	  import('@/assets/082022/css/style.css');
    	  import('@/assets/082022/css/new.0822.css');
      	  import('@/assets/082022/css/animate.0822.css');
      	  import('@/assets/082022/css/video-modal.css');
    	  
        },

        mounted: function() {
    		$(document).ready(function(){
    			$('.tabs').tabs();
    			$("#header").sticky({topSpacing:0});
    			
    			var script=document.createElement('script');
    			script.type='text/javascript';
    			script.async='async'
    			script.src='https://api-maps.yandex.ru/services/constructor/1.0/js/?um=constructor%3A87cc24d5013f025063c014b1c23ad401d1cfd347455ef2d999759fdadd29621c&amp;width=100%25&amp;height=414&amp;lang=ru_RU&amp;scroll=false';
    			$("#mapNN").append(script);
    			
    			var script=document.createElement('script');
    			script.type='text/javascript';
    			script.async='async'
    			script.src='https://api-maps.yandex.ru/services/constructor/1.0/js/?um=constructor%3Ad18c832af74e9b9b0a9ef496a75ce63297a9ecf8dc34897fc8620255cda476b8&amp;width=100%25&amp;height=414&amp;lang=ru_RU&amp;scroll=false';
    			$("#mapDZ").append(script);

      			$('.buttonGetCource, .buttonFindeCource').click(function() {
      				window.location.href = "/send-request";
      				return false;
      			});
    			
    			
    		});
        	
       		$('.footer nav p').click(function() {
       			$(this).toggleClass('active');
       			$(this).next('ul').toggleClass('opened');
       		});
       		$('.header .menu-button').click(function() {
       			$(this).toggleClass('active');
       			$('.mobile-menu').toggleClass('opened');
       		});
       		$(window).bind('mousewheel', function(event) {
       			if (event.originalEvent.wheelDelta >= 0) {
       				$('.top-page-line').addClass('opened');
       				$('.ways-block nav ul').addClass('other');
       			}
       			else {
       				$('.top-page-line').removeClass('opened');
       				$('.ways-block nav ul').removeClass('other');
       			}
       		});
       		$('.top-page-line .city .select label.l1, .mobile-menu .city .select label.l1').click(function() {
       			$('.contacts-block .map').removeClass('active');
       			$('.contacts-block .map.m2').addClass('active');
       			$('.contacts-block form.big').hide();
       			$('.contacts-block .r').show();
       		});
       		$('.top-page-line .city .select label.l2, .mobile-menu .city .select label.l2').click(function() {
       			$('.contacts-block .map').removeClass('active');
       			$('.contacts-block .map.m1').addClass('active');
       			$('.contacts-block form.big').hide();
       			$('.contacts-block .r').show();
       		});
       		$('.top-page-line .city .select label.l3, .mobile-menu .city .select label.l3').click(function() {
       			$('.contacts-block .map').removeClass('active');
       			$('.contacts-block form.big').show();
       			$('.contacts-block .r').hide();
       		});
       		$(document).mousemove(function(e) {
       			var x = (e.pageY * 1 / 35), y = (e.pageX * 1 / 35);
       			$('.rounds').css('margin', x + 'px ' + y + 'px');
       		});
       		$('.first-block .bottom-link a').bind("click", function(e){
       		  var anchor = $(this);
       		  $('html, body').stop().animate({
       			 scrollTop: $(anchor.attr('href')).offset().top
       		  }, 1000);
       		  e.preventDefault();
       		});
       		$('.index-page-slider').slick({
       		});
       		
       		$('.faq-block .item .name').click(function() {
       			$(this).toggleClass('active');
       			$(this).next('.text').slideToggle();
       		});
        },
    }
</script>