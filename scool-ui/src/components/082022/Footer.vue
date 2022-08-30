<template>
  <div>
	<div class="contacts-block">
		<div class="container">
			<form class="big">
				<input type="text" v-model="fio" placeholder="Ваше имя" required>
				<div class="row">
					<div class="col-sm-6">
						<input type="text" v-model="phone" placeholder="Ваш телефон" required>
					</div>
					<div class="col-sm-6">
						<input type="text" v-model="email" placeholder="Ваш e-mail">
					</div>
					<div class="col-sm-6">
						<p>Нажимая на кнопку, я соглашаюсь на обработку персональных данных и с правилами пользования Платформой</p>
					</div>
					<div class="col-sm-6">
						<button @click="sendRequest()" type="submit">Отправить</button>
					</div>
				</div>
				<div class="text">
					<span>Помочь с выбором?</span>
					Оставьте заявку и наши специалисты свяжутся с вами, ответят на все вопросы и подберут вариант обучения.
				</div>
			</form>
			<div class="row r">
				<div class="col-lg-6">
					<form>
						<input type="text" v-model="fio" placeholder="Ваше имя">
						<div class="row">
							<div class="col-sm-6">
								<input v-model="phone" type="text" placeholder="Ваш телефон">
							</div>
							<div class="col-sm-6">
								<input type="text" v-model="email" placeholder="Ваш e-mail">
							</div>
							<div class="col-sm-6">
								<p>Нажимая на кнопку, я соглашаюсь на обработку персональных данных и с правилами пользования Платформой</p>
							</div>
							<div class="col-sm-6">
								<button @click="sendRequest()" type="submit">Отправить</button>
							</div>
						</div>
						<div class="text">
							<span>Помочь с выбором?</span>
							Оставьте заявку, наши специалисты свяжутся с вами и ответят на все вопросы!
						</div>
					</form>
				</div>
				<div class="col-lg-6">
					<div class="map m1" id="mapNN">
					</div>
					<div class="map m2" id="mapDZ">
					</div>
				</div>
			</div>
		</div>
	</div>

	<footer class="footer">
		<div class="container flex">
			<div class="left-side">
				<div class="logo">
					<a href="/"><img src="@/assets/082022/img/logo2.svg"></a>
				</div>
				<a v-bind:href="'tel:'+ $store.state.phone" class="phone">{{ $store.state.phone }}</a>
				<div class="adress">
					{{ $store.state.address }}
				</div>
				<a href="mailto:info@f-academy.ru" class="mail">info@f-academy.ru</a>
				<div class="social">
					<a href="https://vk.com/club208872699"><img src="@/assets/082022/img/soc1.svg"><img src="@/assets/082022/img/soc1h.svg"></a>
					<a href="https://www.instagram.com/future_academyrus/"><img src="@/assets/082022/img/soc2.svg"><img src="@/assets/082022/img/soc2h.svg"></a>
					<a href="https://www.facebook.com/Академия-будущего-ХОД-106638701868195"><img src="@/assets/082022/img/soc3.svg"><img src="@/assets/082022/img/soc3h.svg"></a>
					<a href="https://youtube.com/channel/UCAmIzaYYrC-X3D2F6G-0xwA"><img src="@/assets/082022/img/soc4.svg"><img src="@/assets/082022/img/soc4h.svg"></a>
					<a href="https://t.me/+qsd97a8BPXVmNjQy"><img src="@/assets/082022/img/soc5.svg"><img src="@/assets/082022/img/soc5h.svg"></a>
				</div>
				<div class="ya">
					<a href="#"><img src="@/assets/082022/img/ya.svg"><img src="@/assets/082022/img/ya2.svg"></a>
				</div>
				<div class="copy">
					© ХОД, Future Academy
				</div>
			</div>
			<nav>
				<p>Детям</p>
	            <ul>
	              <li 
	              		v-for="category in categoryList" :key="id" 
	              		v-if="category.age_group === 'children'">
	              		
	                <a href="#" @click="goToCategory(category.name, category.age_group)">{{ category.name }}</a>
	              </li>
	            </ul>
			</nav>
			<nav>
				<p>Подросткам</p>
	            <ul>
	              <li 
	              		v-for="category in categoryList" :key="id" 
	              		v-if="category.age_group === 'teens'">
	              		
	                <a href="#" @click="goToCategory(category.name, category.age_group)">{{ category.name }}</a>
	              </li>
	            </ul>
			</nav>
			<nav>
				<p>Взрослым</p>
	            <ul>
	              <li 
	              		v-for="category in categoryList" :key="id" 
	              		v-if="category.age_group === 'adults'">
	              		
	                <a href="#" @click="goToCategory(category.name, category.age_group)">{{ category.name }}</a>
	              </li>
	            </ul>
			</nav>
			<nav>
				<p>Информация</p>
				<ul>
					<li><a href="https://f-academy.ru/about">Об академии</a></li>
					<li><a href="https://f-academy.ru/events">Мероприятия</a></li>
					<li><a href="https://f-academy.ru/news">Новости</a></li>
					<li><a href="#">База знаний</a></li>
					<li><a href="https://f-academy.ru/career">Карьера</a></li>
					<li><a href="https://f-academy.ru/contacts">Контакты</a></li>
				</ul>
			</nav>
		</div>
	</footer>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Footer",

  data() {
	    return { 
	    	listCourses: [],
	    	categoryList: [],
	    }
  },
	  
  mounted: function() {  },
  
  created() {  
	  this.loadListCourses();
	  this.loadCategoryList();
  },
  methods: {
	  
      async loadCategoryList() {
          await axios
              .get(`${this.$store.getters.getServerUrl}/categories/`)
              .then(response => (this.categoryList = response.data));
      },
	    
	  async loadListCourses() {
	      await axios
	        .get(`${this.$store.getters.getServerUrl}/courses/`)
	        .then((response) => (this.listCourses = response.data));
	  },
	  
	  goTo(course) {
	      if (course.category.name !== "Шахматы") {
	        this.$router.push({
	          name: "EducationSingle",
	          params: { id: course.id, slug: course.slug },
	        });
	      } else {
	        this.$router.push({
	          name: "ChessSingle",
	          params: { id: course.id, slug: course.slug },
	        });
	      }
	      window.scrollTo(0, 0);
	  },
	  
      goToCategory(name, ageGroup) {
		  this.$router.push({name: 'Education', params: {'category': name, 'ageGroup': ageGroup}});
	      window.scrollTo(0, 0);
      },
      
      async sendRequest() {
          const body = {
            request_fio: this.fio,
            request_phone: this.phone,
            request_email: this.email,
            type_request: this.typeRequest,
            status: this.status,
            date: this.dates,
            student: null,
            client: null,
            purpose: 'info',
            result: null,
            remind: null,
            comment: "",
            manager: null,
            course: null,
            event: null
          }
          
          axios
              .post(`${this.$store.getters.getServerUrl}/requests/`, body)
              .then((response) => {
                this.$store.commit("setAuthUser", {
                  authUser: response.data,
                  isAuthenticated: true,
                });
                this.fio = null;
                this.phone = null;
                this.email = null;
              });
        },

	  
  },

}
</script>
