<template>
	<div>
	
	<div class="first-block">
		<img src="../assets/082022/img/rounds.svg" class="rounds">
		<div class="container">
			<div class="text">
				<div class="name">
					Все программы обучения
				</div>
				<p>
					Выберите подходящий курс в направлении, которое Вас интересует.
					Среди наших программ найдутся курсы для любого возраста, 
					навыков и интересов.
				</p>
				<div class="image">
					<img src="../assets/082022/img/edu/header.png">
				</div>
				<div class="buttons flex">
					<button class="GetCourceModal">Получить консультацию</button>
					<button class="GetCourceModal">Подобрать курс</button>
				</div>
			</div>
		</div>
	</div>
	
	<div class="ways-block">
		<div class="anchor" id="ways"></div>
		<div class="container">
			<div class="tabs flex">
				<nav>
					<ul>
						<li>
							<a href="#t1">
								<span><img src="../assets/082022/img/tab1.png"></span>
								<span>
									<i>Дети</i>
									8 — 14 лет
								</span>
							</a>
						</li>
						<li>
							<a href="#t2">
								<span><img src="../assets/082022/img/tab2.png"></span>
								<span>
									<i>Подростки</i>
									14 — 18 лет
								</span>
							</a>
						</li>
						<li>
							<a href="#t3">
								<span><img src="../assets/082022/img/tab3.png"></span>
								<span>
									<i>Взрослые</i>
									18 — ∞ 
								</span>
							</a>
						</li>
					</ul>
				</nav>
				<div id="t1" class="tab-content">
					<div class="row">
						<div class="col-md-12 categoryFilter">
							<a data-cat="all">Все</a>
							<a data-cat="Шахматы">Шахматы</a>
							<a data-cat="IT-обучение">IT-обучение</a>
							<a data-cat="Иностранные языки">Иностранные языки</a>
							<a data-cat="Общие дисциплины">Общие дисциплины</a>
						</div>
						<div class="col-md-6" @click="goToHref('https://f-academychess.ru/')" catname="Шахматы">
							<div class="item" :style="{'background': '#ECB0BC url(' + require('../assets/082022/img/edu/courses/ch1.png') + ') right bottom no-repeat'}">
								<div class="edu-course-type">Курс</div>
								<div class="edu-course-category">Шахматы</div>
								<div class="text">
									Шахматная школа
									<p class="edu-course-desc">Обучение игре в шахматы с любого уровня, развитие памяти, внимания и логического мышления ребенка.</p>
								</div>
								<div class="edu-course-lenght">9 месяцев</div>
							</div>
						</div>

						<div class="col-md-6" @click="goToHref('/education/english')" catname="Иностранные языки">
							<div class="item" :style="{'background': '#B4EEC4 url(' + require('../assets/082022/img/edu/courses/ch2.png') + ') right bottom no-repeat'}">
								<div class="edu-course-type">Курс</div>
								<div class="edu-course-category">Иностранные языки</div>
								<div class="text">
									Английский язык
									<p class="edu-course-desc">Английский язык необходим для успешной карьеры. Изучение языка с детства повышает возможность владения им во взрослой жизни.</p>
								</div>
								<div class="edu-course-lenght">9 месяцев</div>
							</div>
						</div>

						<div class="col-md-6" @click="goToHref('/education/chinese')" catname="Иностранные языки">
							<div class="item education-chinese" :style="{'background': '#B4EEC4 url(' + require('../assets/082022/img/edu/courses/ch7.png') + ') right bottom no-repeat'}">
								<div class="edu-course-type">Курс</div>
								<div class="edu-course-category">Иностранные языки</div>
								<div class="text">
									Китайский язык
									<p class="edu-course-desc">Китайский язык сегодня актуален как никогда. Изучение языка с детства повышает возможность владения им во взрослой жизни.</p>
								</div>
								<div class="edu-course-lenght">9 месяцев</div>
							</div>
						</div>
						
						<div class="col-md-6" @click="goToHref('/education/beginner')" catname="IT-обучение">
							<div class="item" :style="{'background': '#CDFDC3 url(' + require('../assets/082022/img/edu/courses/ch3.png') + ') right bottom no-repeat'}">
								<div class="edu-course-type">Курс</div>
								<div class="edu-course-category">IT-обучение</div>
								<div class="text">
									Новичок
									<p class="edu-course-desc">Обучение основам IT-технологий, английскому языку, шахматам и другим дисциплинам для комплексного развития ребёнка.</p>
								</div>
								<div class="edu-course-lenght">9 месяцев</div>
							</div>
						</div>

						<div class="col-md-6" @click="goToHref('/education/user')" catname="IT-обучение">
							<div class="item" :style="{'background': 'url(' + require('../assets/082022/img/edu/courses/ch5.png') + ') right center/cover no-repeat'}">
								<div class="edu-course-type">Курс</div>
								<div class="edu-course-category">IT-обучение</div>
								<div class="text">
									Пользователь
									<p class="edu-course-desc">Обучение по выбранному направлению: Программирование, Дизайн или Мультимедиа.</p>
								</div>
								<div class="edu-course-lenght">9 месяцев</div>
							</div>
						</div>

						<div class="col-md-6" @click="goToHref('/education/prof')" catname="IT-обучение">
							<div class="item" :style="{'background': '#D4FBFF url(' + require('../assets/082022/img/edu/courses/ch4.png') + ') right bottom no-repeat'}">
								<div class="edu-course-type">Курс</div>
								<div class="edu-course-category">IT-обучение</div>
								<div class="text">
									Профессионал
									<p class="edu-course-desc">Обучение по выбранному направлению: Программирование, Дизайн, Веб-разработка или Мультимедиа.</p>
								</div>
								<div class="edu-course-lenght">9 месяцев</div>
							</div>
						</div>

						<div class="col-md-6" @click="goToHref('/education/cheater')" catname="IT-обучение">
							<div class="item" :style="{'background': 'url(' + require('../assets/082022/img/edu/courses/ch6.png') + ') right center/cover no-repeat'}">
								<div class="edu-course-type">Курс</div>
								<div class="edu-course-category">IT-обучение</div>
								<div class="text">
									Читер
									<p class="edu-course-desc">Обучение по выбранному направлению: Программирование, Дизайн, Веб-разработка или Мультимедиа, Создание игр, Блогинг.</p>
								</div>
								<div class="edu-course-lenght">9 месяцев</div>
							</div>
						</div>

						<div class="col-md-6" @click="goToHref('/education/speedreading')" catname="Общие дисциплины">
							<div class="item" :style="{'background': 'url(' + require('../assets/082022/img/edu/courses/ch8.png') + ') right center/cover no-repeat'}">
								<div class="edu-course-type">Курс</div>
								<div class="edu-course-category">Общие</div>
								<div class="text">
									Скорочтение
									<p class="edu-course-desc">Обучение быстрому усвоению большого объёма информации при чтении, развитие памяти и внимания</p>
								</div>
								<div class="edu-course-lenght">9 месяцев</div>
							</div>
						</div>
						<div class="col-md-6" @click="goToHref('/education/arithmetic')" catname="Общие дисциплины">
							<div class="item" :style="{'background': 'url(' + require('../assets/082022/img/edu/courses/ch9.png') + ') right center/cover no-repeat'}">
								<div class="edu-course-type">Курс</div>
								<div class="edu-course-category">Общие</div>
								<div class="text">
									Ментальная арифметика
									<p class="edu-course-desc">Обучение быстрому вычислению в уме многозначных цифр, развитие интеллекта, логики и внимания ребёнка</p>
								</div>
								<div class="edu-course-lenght">9 месяцев</div>
							</div>
						</div>

					</div>
				</div>
				<div id="t2" class="tab-content">
					<div class="row">

						<div class="col-md-12 categoryFilter">
							<a data-cat="all">Все</a>
							<a data-cat="Шахматы">Шахматы</a>
							<a data-cat="Программирование">IT-обучение</a>
							<a data-cat="Иностранные языки">Иностранные языки</a>
							<a data-cat="Киберспорт">Киберспорт</a>
						</div>

						<div class="col-md-6" @click="goToHref('https://f-academychess.ru/')" catname="Шахматы">
							<div class="item" :style="{'background': 'url(' + require('../assets/082022/img/edu/courses/te1.png') + ') right center/cover no-repeat'}">
								<div class="edu-course-type">Курс</div>
								<div class="edu-course-category">Шахматы</div>
								<div class="text">
									Шахматная школа
									<p class="edu-course-desc">Обучение игре в шахматы с любого уровня, развитие памяти, внимания и логического мышления ребенка.</p>
								</div>
								<div class="edu-course-lenght">24 месяца</div>
							</div>
						</div>
						<div class="col-md-6" @click="goToHref('/education/game-development')" catname="Программирование">
							<div class="item" :style="{'background': 'url(' + require('../assets/082022/img/edu/courses/te2.png') + ') right center/cover no-repeat'}">
								<div class="edu-course-type">Курс</div>
								<div class="edu-course-category">IT-обучение</div>
								<div class="text">
									Game development
									<p class="edu-course-desc">Разработчик игр обладает навыками разработки сценария и концепции игры, геймдизайна, программирования игры. </p>
								</div>
								<div class="edu-course-lenght">24 месяца</div>
							</div>
						</div>
						
						<div class="col-md-6" @click="goToHref('/education/prikladnoe-programmirovanie')" catname="Программирование">
							<div class="item" :style="{'background': 'url(' + require('../assets/082022/img/edu/courses/te3.png') + ') right center/cover no-repeat'}">
								<div class="edu-course-type">Курс</div>
								<div class="edu-course-category">IT-обучение</div>
								<div class="text">
									Прикладное программирование
									<p class="edu-course-desc">На курсе вы познакомитесь с ключевыми инструментами разработки, ООП, будете применять полученные знания.</p>
								</div>
								<div class="edu-course-lenght">24 месяца</div>
							</div>
						</div>
						
						<div class="col-md-6" @click="goToHref('/education/kurs-po-kibersportu-dlya-podrostkov')" catname="Киберспорт">
							<div class="item" :style="{'background': 'url(' + require('../assets/082022/img/edu/courses/te4.png') + ') right center/cover no-repeat'}">
								<div class="edu-course-type">Курс</div>
								<div class="edu-course-category">Киберспорт</div>
								<div class="text">
									Киберспорт
									<p class="edu-course-desc">Современное и быстроразвивающееся направление, которое дает возможность превратить любимое хобби в сферу побед и достижений.</p>
								</div>
								<div class="edu-course-lenght">24 месяца</div>
							</div>
						</div>
						
						<div class="col-md-6" @click="goToHref('/education/web-razrabotka')" catname="Программирование">
							<div class="item" :style="{'background': 'url(' + require('../assets/082022/img/edu/courses/te5.png') + ') right center/cover no-repeat'}">
								<div class="edu-course-type">Курс</div>
								<div class="edu-course-category">IT-обучение</div>
								<div class="text">
									WEB-разработка
									<p class="edu-course-desc">Веб-разработчик разрабатывает сайт, создаёт интерфейсы, способен разбираться в устройстве сервера.</p>
								</div>
								<div class="edu-course-lenght">24 месяца</div>
							</div>
						</div>
						
						<div class="col-md-6" @click="goToHref('/education/razrabotchik-mobilnyh-prilozhenij')" catname="Программирование">
							<div class="item" :style="{'background': 'url(' + require('../assets/082022/img/edu/courses/te6.png') + ') right center/cover no-repeat'}">
								<div class="edu-course-type">Курс</div>
								<div class="edu-course-category">IT-обучение</div>
								<div class="text">
									Разработка мобильных приложений
									<p class="edu-course-desc">На курсе мы научим создавать мобильные приложения с красивым интерфейсом и широким функционалом</p>
								</div>
								<div class="edu-course-lenght">24 месяца</div>
							</div>
						</div>
						 
						<div class="col-md-6" @click="goToHref('/education/anglijskij-yazyk-dlya-podrostkov')" catname="Иностранные языки">
							<div class="item" :style="{'background': 'url(' + require('../assets/082022/img/edu/courses/te7.png') + ') right center/cover no-repeat'}">
								<div class="edu-course-type">Курс</div>
								<div class="edu-course-category">Иностранные языки</div>
								<div class="text">
									Английский язык
									<p class="edu-course-desc">Владение английским языком дает вам возможность быть более успешным в сфере IT-технологий, претендовать на высокие позиции.</p>
								</div>
								<div class="edu-course-lenght">24 месяца</div>
							</div>
						</div>
						
						<div class="col-md-6" @click="goToHref('/education/machine-learning')" catname="Программирование">
							<div class="item" :style="{'background': 'url(' + require('../assets/082022/img/edu/courses/te8.png') + ') right center/cover no-repeat'}">
								<div class="edu-course-type">Курс</div>
								<div class="edu-course-category">IT-обучение</div>
								<div class="text">
									Машинное обучение и нейросети
									<p class="edu-course-desc">Специалисты по Machine Learning обучают искусственный интеллект решению сложных задач.</p>
								</div>
								<div class="edu-course-lenght">24 месяца</div>
							</div>
						</div>
						
					</div>
				</div>
				
				<div id="t3" class="tab-content">
					<div class="row">

						<div class="col-md-12 categoryFilter">
							<a data-cat="all">Все</a>
							<a data-cat="Шахматы">Шахматы</a>
							<a data-cat="Программирование">IT-обучение</a>
							<a data-cat="Киберспорт">Киберспорт</a>
							<a data-cat="Маркетинг">Маркетинг</a>
							<a data-cat="Дизайн">Дизайн</a>
							<a data-cat="Разработка игр">Разработка игр</a>
						</div>

						<div class="col-md-6" @click="goToHref('/education/razrabotchik-igr-na-unity')" catname="Разработка игр">
							<div class="item" :style="{'background': 'url(' + require('../assets/082022/img/edu/courses/ad1.png') + ') right center/cover no-repeat'}">
								<div class="edu-course-type">Курс</div>
								<div class="edu-course-category">Разработка игр</div>
								<div class="text">
									Разработчик игр на Unity
									<p class="edu-course-desc">Программа для тех, кто хочет изучить язык программирования С# и создавать игры на одном из самых современных движков.</p>
								</div>
								<div class="edu-course-lenght">24 месяца</div>
							</div>
						</div>
						<div class="col-md-6" @click="goToHref('/education/web-razrabotka-full-stack')" catname="Программирование">
							<div class="item" :style="{'background': 'url(' + require('../assets/082022/img/edu/courses/ad2.png') + ') right center/cover no-repeat'}">
								<div class="edu-course-type">Курс</div>
								<div class="edu-course-category">IT-обучение</div>
								<div class="text">
									WEB-разработка (full-stack)
									<p class="edu-course-desc">Программа для тех, кто хочет научиться создавать сайты и стать востребованным full-stack разработчиком. </p>
								</div>
								<div class="edu-course-lenght">24 месяца</div>
							</div>
						</div>
						<div class="col-md-6" @click="goToHref('/education/kurs-po-internet-marketingu')" catname="Маркетинг">
							<div class="item" :style="{'background': 'url(' + require('../assets/082022/img/edu/courses/ad3.png') + ') right center/cover no-repeat'}">
								<div class="edu-course-type">Курс</div>
								<div class="edu-course-category">Маркетинг</div>
								<div class="text">
									Интернет-маркетинг
									<p class="edu-course-desc">Научим развиваться в сфере маркетинга, разрабатывать стратегии продвижения для крупных компаний или бизнес-проектов.</p>
								</div>
								<div class="edu-course-lenght">24 месяца</div>
							</div>
						</div>
						<div class="col-md-6" @click="goToHref('https://f-academychess.ru/')" catname="Шахматы">
							<div class="item" :style="{'background': 'url(' + require('../assets/082022/img/edu/courses/ad4.png') + ') right center/cover no-repeat'}">
								<div class="edu-course-type">Курс</div>
								<div class="edu-course-category">Шахматы</div>
								<div class="text">
									Шахматная школа
									<p class="edu-course-desc">Обучение игре в шахматы с любого уровня, развитие памяти, внимания и логического мышления ребенка.</p>
								</div>
								<div class="edu-course-lenght">24 месяца</div>
							</div>
						</div>
						<div class="col-md-6" @click="goToHref('/education/menedzher-po-rabote-s-marketplejsami')" catname="Маркетинг">
							<div class="item" :style="{'background': 'url(' + require('../assets/082022/img/edu/courses/ad5.png') + ') right center/cover no-repeat'}">
								<div class="edu-course-type">Курс</div>
								<div class="edu-course-category">Маркетинг</div>
								<div class="text">
									Менеджер по работе с маркетплейсами
									<p class="edu-course-desc">Научим зарабатывать из любой точки мира в комфортном для себя режиме.</p>
								</div>
								<div class="edu-course-lenght">24 месяца</div>
							</div>
						</div>
						<div class="col-md-6" @click="goToHref('/education/python-razrabotchik')" catname="Программирование">
							<div class="item" :style="{'background': 'url(' + require('../assets/082022/img/edu/courses/ad6.png') + ') right center/cover no-repeat'}">
								<div class="edu-course-type">Курс</div>
								<div class="edu-course-category">IT-обучение</div>
								<div class="text">
									Python-разработчик
									<p class="edu-course-desc">Программа для тех, кто хочет освоить язык программирования Python и стать востребованным разработчиком.</p>
								</div>
								<div class="edu-course-lenght">24 месяца</div>
							</div>
						</div>
						<div class="col-md-6" @click="goToHref('/education/kurs-razrabotka-po')" catname="Программирование">
							<div class="item" :style="{'background': 'url(' + require('../assets/082022/img/edu/courses/ad7.png') + ') right center/cover no-repeat'}">
								<div class="edu-course-type">Курс</div>
								<div class="edu-course-category">IT-обучение</div>
								<div class="text">
									Разработка ПО
									<p class="edu-course-desc">Программа для тех, кто хочет изучить язык программирования и средства разработки, стать востребованным специалистом в сфере IT.</p>
								</div>
								<div class="edu-course-lenght">24 месяца</div>
							</div>
						</div>
						<div class="col-md-6" @click="goToHref('/education/java-razrabotchik')" catname="Программирование">
							<div class="item" :style="{'background': 'url(' + require('../assets/082022/img/edu/courses/ad8.png') + ') right center/cover no-repeat'}">
								<div class="edu-course-type">Курс</div>
								<div class="edu-course-category">IT-обучение</div>
								<div class="text">
									Java-разработчик
									<p class="edu-course-desc">Программа для тех, кто хочет изучить самый популярный язык программирования Java и стать востребованным разработчиком.</p>
								</div>
								<div class="edu-course-lenght">24 месяца</div>
							</div>
						</div>
						<div class="col-md-6" @click="goToHref('/education/razrabotka-mobilnyh-prilozhenij')" catname="Программирование">
							<div class="item" :style="{'background': 'url(' + require('../assets/082022/img/edu/courses/ad9.png') + ') right center/cover no-repeat'}">
								<div class="edu-course-type">Курс</div>
								<div class="edu-course-category">IT-обучение</div>
								<div class="text">
									Разработчик мобильных приложений
									<p class="edu-course-desc">Научим качественно создавать и продвигать мобильные приложения любой сложности</p>
								</div>
								<div class="edu-course-lenght">24 месяца</div>
							</div>
						</div>
						<div class="col-md-6" @click="goToHref('/education/kurs-po-graficheskomu-dizajnu')" catname="Дизайн">
							<div class="item" :style="{'background': 'url(' + require('../assets/082022/img/edu/courses/ad10.png') + ') right center/cover no-repeat'}">
								<div class="edu-course-type">Курс</div>
								<div class="edu-course-category">Дизайн</div>
								<div class="text">
									Графический дизайн
									<p class="edu-course-desc">Научим совмещать творчество и цифровые технологии, разрабатывать дизайн копаний, сайтов или компьютерных игр.</p>
								</div>
								<div class="edu-course-lenght">24 месяца</div>
							</div>
						</div>
						<div class="col-md-6" @click="goToHref('/education/ios-razrabotchik')" catname="Программирование">
							<div class="item" :style="{'background': 'url(' + require('../assets/082022/img/edu/courses/ad11.png') + ') right center/cover no-repeat'}">
								<div class="edu-course-type">Курс</div>
								<div class="edu-course-category">IT-обучение</div>
								<div class="text">
									IOS-разработчик
									<p class="edu-course-desc">Научим создавать приложения на Apple, даже если вы никогда не программировали.</p>
								</div>
								<div class="edu-course-lenght">24 месяца</div>
							</div>
						</div>
						<div class="col-md-6" @click="goToHref('/education/kurs-po-kibersportu-dlya-vzroslyh')" catname="Киберспорт">
							<div class="item" :style="{'background': 'url(' + require('../assets/082022/img/edu/courses/ad12.png') + ') right center/cover no-repeat'}">
								<div class="edu-course-type">Курс</div>
								<div class="edu-course-category">Киберспорт</div>
								<div class="text">
									Киберспорт
									<p class="edu-course-desc">Современное и быстроразвивающееся направление, которое дает возможность превратить любимое хобби в сферу побед и достижений.</p>
								</div>
								<div class="edu-course-lenght">24 месяца</div>
							</div>
						</div>
						<div class="col-md-6" @click="goToHref('/education/testirovshchik-po')" catname="Программирование">
							<div class="item" :style="{'background': 'url(' + require('../assets/082022/img/edu/courses/ad13.png') + ') right center/cover no-repeat'}">
								<div class="edu-course-type">Курс</div>
								<div class="edu-course-category">IT-обучение</div>
								<div class="text">
									Тестировщик ПО (QA)
									<p class="edu-course-desc">Научим проверять качество программных продуктов, обеспечивая бесперебойную работу проекта.</p>
								</div>
								<div class="edu-course-lenght">24 месяца</div>
							</div>
						</div>
						
					</div>
				</div>
			</div>
		</div>
	</div>

	<div class="page-banner">
		<div class="container">
			<div class="banner">
				<div class="content">
					<div class="text">
						<div class="name">
							<span>Образовательные</span>
							программы на базе
						</div>
						<p>Высшей Школы Экономики</p>
						<button class="buttonHsecamp">Узнать подробнее</button>
					</div>
				</div>
			</div>
		</div>
	</div>
	
	<div class="try-block">
		<div class="container">
			<div class="block-name">
				Попробуй!
			</div>
			<p>Приглашаем всех желающих на бесплатную экскурсию в мир востребованных профессий и полезных навыков</p>
			<button class="buttonTryBlock" onclick="Marquiz.showModal('62eccda9bf65ee004700e3fe')"><span>Пройти тест</span> (5 мин)</button>
			<div class="text t1">Программирование</div>
			<div class="text t2">Маркетплейсы</div>
			<div class="text t3">WEB-дизайн</div>
			<div class="text t4">Робототехника</div>
			<div class="text t5">Анимация</div>
			<div class="text t6">Шахматы</div>
			<div class="text t7">Криптовалюта</div>
			<div class="text t8">3D-моделирование</div>
			<div class="text t9">Графический дизайн</div>
			<div class="text t10">Создание компьютерных игр</div>
		</div>
	</div>

	<div class="partners-block">
		<div class="container">
			<div class="block-name">
				Наши партнеры
			</div>
			<div class="row">
				<div class="col-md-4">
					<div class="item">
						<img src="../assets/082022/img/partner0.png">
					</div>
					<div class="item">
						<img src="../assets/082022/img/partner1.png">
					</div>
				</div>
				<div class="col-md-4">
					<div class="item big">
						<img src="../assets/082022/img/partner2.png">
					</div>
				</div>
				<div class="col-md-2 col-sm-6">
					<div class="item big">
						<img src="../assets/082022/img/partner3.png">
					</div>
				</div>
				<div class="col-md-2 col-sm-6">
					<div class="item">
						<img src="../assets/082022/img/partner4.png">
					</div>
					<div class="item">
						<img src="../assets/082022/img/partner5.png">
					</div>
				</div>
			</div>
			<div class="mob-block">
				<div class="row">
					<div class="col-4">
						<div class="item">
							<img src="../assets/082022/img/partner0.png">
						</div>
						<div class="item">
							<img src="../assets/082022/img/partner1.png">
						</div>
					</div>
					<div class="col-4">
						<div class="item big">
							<img src="../assets/082022/img/partner2.png">
						</div>
					</div>
					<div class="col-2">
						<div class="item big">
							<img src="../assets/082022/img/partner3.png">
						</div>
					</div>
					<div class="col-2">
						<div class="item">
							<img src="../assets/082022/img/partner4.png">
						</div>
						<div class="item">
							<img src="../assets/082022/img/partner5.png">
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>	
		
	</div>
</template>

<script>

import axios from "axios";

export default {
  title: 'Академия будущего | Обучение',
  description: 'Обучение',
  name: "EducationNew",

  data() {
    return {
        category_name: "all",
        age_group: "children",
    };
  },

  props: {
    category: String,
    ageGroup: String,
  },

  components: {  },

  created() {
	  if (!this.category) {
	      this.category_name = "all";
	  } else {
	      this.category_name = this.category;
	  }
	
	  if (!this.ageGroup) {
		    this.age_group = "children";
	  } else {
		    this.age_group = this.ageGroup;
	  }
  },

  mounted() {
		var age_group = this.age_group;
		var category_name = this.category_name;
		let $ = window.$;
		let outerApp = this; 
		
		$(document).ready(function() {
			
			switch (age_group) {
				case 'children':
					$( ".ways-block .tabs" ).tabs({ active: 0 });
					outerApp.setCategoryFilter('#t1', category_name);
					break; 
				case 'teens':
					$( ".ways-block .tabs" ).tabs({ active: 1 });
					outerApp.setCategoryFilter('#t2', category_name);
					break; 
				case 'adults':
					$( ".ways-block .tabs" ).tabs({ active: 2 });
					outerApp.setCategoryFilter('#t3', category_name);
					break; 
			}
			
			$('.categoryFilter a').click(function() {
				var tabSection = $(this).parents('.tab-content');
				var filterCategory = $(this).data('cat');
				
				outerApp.setCategoryFilter('#' + $(tabSection).attr('id'), filterCategory);
				
				$(tabSection).find('.categoryFilter a').removeClass('active');
				$(this).addClass('active');
				
				return false;
			});
			
		})	  
  },

  methods: {
      goToHref(href) {
		  window.location.href = href;
      },
      
      setCategoryFilter(tab, category) {
    	  let $ = window.$;
    	  
    	  $(tab + ' .categoryFilter a[data-cat="'+category+'"]').addClass('active');
    	  
    	  $(tab + ' > .row > div').each(function() {
    		  if (!$(this).hasClass('categoryFilter')) {
    			  $(this).show	();
	    		  if (category != 'all') {
	    			  if ($(this).attr('catname') != category) {
	    				  $(this).hide();
	    			  }
	    		  }
    		  }
    	  });
      }
  },
};
</script>

<style scoped>
	.first-block {
		padding: 130px 0 285px 0;
	}
	
	.ways-block {
	    margin-top: -285px;
    	position: relative;	
	}

	.edu-course-type, .edu-course-category, .edu-course-lenght, .edu-course-desc {
		font-size: 12px;
		line-height: 18px;
		font-weight: normal;
	} 
	
	.edu-course-type {
		position: absolute;
		top: 27px;
		left: 30px;
	}
	.edu-course-category {
		position: absolute;
		top: 27px;
		right: 30px;
	}
	
	.edu-course-lenght {
		position: absolute;
		bottom: 15px;
		left: 30px;
	}
	
	.edu-course-desc {
  	  	margin-top: 30px;
  	  	letter-spacing: normal;
	}
	
	.ways-block .tab-content .item .text {
		padding: 30px;
		top: 38px;
		padding-right: 130px;
	}
	
	.categoryFilter a {
		display: inline-block;
		
		background: #FFF;
		border: solid 2px #FFF;	
		padding: 15px 20px;
		background: #FFFFFF;

		box-shadow: 0px 0px 27px rgba(0, 0, 0, 0.05);
		border-radius: 6px;
		
		margin-right: 20px;
		box-sizing: border-box;
		text-decoration: none;	
		margin-bottom: 20px;
	}
	
	.categoryFilter a:last-child {
		margin-right: 0px;
	}
	
	.categoryFilter a:hover,
	.categoryFilter a.active {
		background: linear-gradient(#fff 0 0) padding-box, linear-gradient(to right, #27AAE1, #D851FF) border-box;		
		border: solid 2px transparent;
	}
	
	.ways-block .tab-content .item.education-chinese {
		color: yellow;
	}

</style>
