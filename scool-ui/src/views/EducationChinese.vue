<template>
  <div>
  <div class="inner-first-block">
		<img src="../assets/082022/img/rounds.svg" class="rounds">
		<div class="container">
			<div class="text">
				<div class="name">
					Курс
					<span>Китайский язык</span>
				</div>
				<p>Программа разработана на базе учебников одного из ведущих вузов Китая – 
				Пекинского университета языка и культуры (北京语言大学), включает в себя работу над произношением, распознаванием тонов, каллиграфию, изучение базовой грамматики. Прохождение программы позволит уверенно общаться на бытовые темы, а также узнать культуру и традиции Китая.</p>
				<div class="children">
					<img src="../assets/082022/img/children.png"> Для детей от 8 лет
				</div>
				<div class="image">
					<img src="../assets/082022/img/chinese-header.png">
				</div>
				<div class="blocks flex">
					<div class="item">
						<div class="icon">
							<img src="../assets/082022/img/inner-first1.svg">
						</div>
						Срок обучения:
						<p>9 месяцев</p>
					</div>
					<div class="item">
						<div class="icon">
							<img src="../assets/082022/img/inner-first2.svg">
						</div>
						Режим занятий:
						<p>2 раза в неделю по 1 ак. часу</p>
					</div>
				</div>
				<div class="prices flex">
					<div class="item">
						<img src="../assets/082022/img/price1.svg">
						<span class="s1">цена от</span>
						<p>2 600 ₽</p>
						<span class="s2">в месяц</span>
					</div>
					<div class="item">
						<img src="../assets/082022/img/price2.svg">
						<span class="s3">цена одно урока от</span>
						<p class="small">от 145 ₽</p>
					</div>
					<div class="item">
						<button
						  type="button"
						  class="tinkoff-button"
						  onclick="tinkoff.create(
						    {
						      sum: 31500,
						      items: [{name: 'Китайский язык для детей', price: 31500, quantity: 1}, ],
						      promoCode: 'default',
						      shopId: '64e20d36-fcd4-47ec-b625-29fda7e58280',
						      showcaseId: '3777cafe-c874-45f0-9571-01b7c9ad9f4c',
						    },
						    {view: 'modal'}
						  )"
						>Доступно в рассрочку</button>
					</div>
				</div>
				<div class="button">
					<p>Первое занятие бесплатно</p>
					<button class="GetCourceModal">Записаться на пробное занятие</button>
				</div>
			</div>
			<div class="bottom-link">
				<img src="../assets/082022/img/round.svg" class="bg">
				<a href="#owlblock"><img src="../assets/082022/img/arrow.svg"></a>
			</div>
		</div>
	</div>
	
	<div class="english-owl-block chinese-owl-block">
		<div id="owlblock" class="anchor"></div>
		<div class="container">
			<div class="owl-owl"></div>
			<div class="owl-content">
			Изучение иностранного языка способствует развитию памяти, коммуникативных навыков, 
			кругозора ребенка. Важная часть обучения для успешного будущего в любой сфере. Основа 
			владения языком и любовь к его освоению закладывается в детстве, а постепенное и 
			корректное погружение в иноязычную среду сделает этот процесс увлекательным и эффективным. 
			</div> 
		</div>
	</div>
	
	<div class="you-learn-block">
		<div class="container">
			<div class="list">
				<div class="round">
					<img src="../assets/082022/img/round.png" style="visibility: hidden;">
					<img src="../assets/082022/img/lines1.png" style="visibility: hidden;" class="lines">
					<img src="../assets/082022/img/lines2.png" class="lines an1">
					<img src="../assets/082022/img/lines3.png" class="lines an2">
					<p>Вы научитесь</p>
				</div>
				
				<div class="mob-caption">Вы научитесь</div>
				
				<div class="item i10">
					<span class="wow fadeInLeft" data-wow-duration="2s" data-wow-delay="3.8s">Общаться на китайском языке</span>
					<img class="wow fadeInLeft" data-wow-duration="2s" data-wow-delay="3.6s" src="../assets/082022/img/line10.svg">
				</div>
				<!--  
				<div class="item i9">
					<span class="wow fadeInLeft" data-wow-duration="2s" data-wow-delay="3.4s">Получать удовольствие от изучения иностранного языка</span>
					<img class="wow fadeInLeft" data-wow-duration="2s" data-wow-delay="3.2s" src="../assets/082022/img/line9.svg">
				</div>
				-->
				<div class="item i8">
					<span class="wow fadeInLeft" data-wow-duration="2s" data-wow-delay="3s">Распознавать и воспроизводить тоны китайского языка</span>
					<img class="wow fadeInLeft" data-wow-duration="2s" data-wow-delay="2.8s" src="../assets/082022/img/line8.svg">
				</div>
				<!-- 
				<div class="item i7">
					<span class="wow fadeInLeft" data-wow-duration="2s" data-wow-delay="2.6s">Читать и понимать тексты разной сложности</span>
					<img class="wow fadeInLeft" data-wow-duration="2s" data-wow-delay="2.4s" src="../assets/082022/img/line7.svg">
				</div>
				  --> 
				<div class="item i6">
					<span class="wow fadeInLeft" data-wow-duration="2s" data-wow-delay="2.2s">Правильно произносить 414<br> звуковых сочетаний</span>
					<img class="wow fadeInLeft" data-wow-duration="2s" data-wow-delay="2s" src="../assets/082022/img/line6.svg">
				</div>
				
				<div class="item i5">
					<span class="wow fadeInLeft" data-wow-duration="2s" data-wow-delay="1.8s">
					Использовать правильный<br> 
					порядок черт, а также<br> 
					распознавать ключи в иероглифах</span>
					<img class="wow fadeInLeft" data-wow-duration="2s" data-wow-delay="1.6s" src="../assets/082022/img/line5.svg">
				</div>
				
				<!-- 
				<div class="item i4">
					<span class="wow fadeInLeft" data-wow-duration="2s" data-wow-delay="1.4s">
					Использовать правильный<br> 
					порядок черт, а также<br> 
					распознавать ключи в иероглифах</span>
					<img class="wow fadeInLeft" data-wow-duration="2s" data-wow-delay="1.2s" src="../assets/082022/img/line4.svg">
				</div>
				-->
				 
				<div class="item i3">
					<span class="wow fadeInLeft" data-wow-duration="2s" data-wow-delay="1s">Правильно писать иероглифы, начиная с основных черт</span>
					<img class="wow fadeInLeft" data-wow-duration="2s" data-wow-delay="0.8s" src="../assets/082022/img/line3.svg">
				</div>
				
				<!-- 
				<div class="item i2">
					<span class="wow fadeInLeft" data-wow-duration="2s" data-wow-delay="0.6s">Правильно писать иероглифы, начиная с основных черт</span>
					<img class="wow fadeInLeft" data-wow-duration="2s" data-wow-delay="0.4s" src="../assets/082022/img/line2.svg">
				</div>
				 -->
				
				<div class="item i1">
					<span class="wow fadeInLeft" data-wow-duration="2s" data-wow-delay="0.2s">
					Строить правильные<br> 
					грамматические предложения<br> 
					с использованием китайских<br> 
					структур и частей речи</span>
					<img class="wow fadeInLeft" data-wow-duration="2s" src="../assets/082022/img/line1.svg">
				</div>
				
				
			</div>
		</div>
	</div>
	
	
	<div class="program-block">
		<div class="container">
			<p>Эта программа подойдет тем, кто</p>
			<div class="item i1">
				<div class="text">
					<span>Хочет научиться говорить на китайском</span>
				</div>
			</div>
			<div class="item i2">
				<div class="text">
					<span>Хочет больше узнать о культуре и традициях Китая</span>
				</div>
			</div>
			<div class="item i3">
				<div class="text">
					<span>Хочет развивать внимание, память и мышление</span>
				</div>
			</div>
		</div>
	</div>
	
	<div class="course-block">
		<div class="container">
			<div class="block-name">
				Содержание курса
			</div>
			<!--  
			<div class="course-block-text">Программа обучения включает в себя изучение лексики и грамматики английского языка через все виды речевой деятельности: говорение, письмо, аудирование и чтение. Тематическое содержание соответствует уровню овладения иностранным языком и возрасту обучающихся</div>
			-->
			<div class="flex">
				<div class="item wow fadeInUp" data-wow-duration="2s">
					<p><span>Звуковые сочетания</span></p>
				</div>
				<div class="item wow fadeInUp" data-wow-duration="2s">
					<p><span>Тоны</span></p>
				</div>
				<div class="item wow fadeInUp" data-wow-duration="2s" data-wow-delay="0.4s">
					<p><span>Иероглифы</span></p>
				</div>

				<div class="item wow fadeInUp" data-wow-duration="2s">
					<p><span>Лексика и грамматика</span></p>
				</div>
				<div class="item wow fadeInUp" data-wow-duration="2s">
					<p><span>Речевые обороты</span></p>
				</div>
				<div class="item wow fadeInUp" data-wow-duration="2s" data-wow-delay="0.4s">
					<p><span>История и традиции Китая</span></p>
				</div>
			</div>
			<div class="price-block">
				<div class="price">
					<span>цена одно урока от</span>
					<img src="../assets/082022/img/price2.svg">
					<div>от 145 ₽ </div>
				</div>
				<p>Первое занятие бесплатно</p>
				<button class="GetCourceModal">Записаться на пробное занятие</button>
			</div>
		</div>
	</div>
	
	<div class="principles-block">
		<div class="block-name">
			Принципы обучения
		</div>
		
		<div class="row principles-list">
			<div class="col-md-6 item-position">
				<div class="item">
					Интерактивное обучение
				</div>
			</div>
			<div class="col-md-6 item-position">
				<div class="item">
					Опытные преподаватели
				</div>
			</div>
			<div class="col-md-6 item-position">
				<div class="item">
					Языковая практика
				</div>
			</div>
			<div class="col-md-6 item-position">
				<div class="item">
					Встречи с носителями языка
				</div>
			</div>
			<div class="col-md-6 item-position">
				<div class="item">
					Обучение через говорение
				</div>
			</div>
			<div class="col-md-6 item-position">
				<div class="item">
					Социокультурное развитие
				</div>
			</div>
		</div>
		
	</div>
		
	<div class="container">
		<div class="training-block">
			<div class="block-name">
				Как проходит обучение
			</div>
			<div class="list">
				<div class="lines wow fadeIn" data-wow-duration="2s"></div>
				<div class="item wow fadeIn" data-wow-duration="2s" data-wow-delay="0.2s">
					<span>01</span>
					Обучение в микро-группах позволяет учитывать индивидуальные особенности ребенка, а распределение на уровни перед началом обучения с помощью тестирования поможет детям чувствовать себя комфортно и прогрессировать от занятия к занятию.
				</div>
				<div class="item wow fadeIn" data-wow-duration="2s" data-wow-delay="0.4s">
					<span>02</span>
					Погружение в иноязычную среду – самый эффективный способ изучения китайского языка. Общение на уроках и переменах, разговорные клубы и мероприятия помогут ребенку почувствовать, что китайский – неотъемлемая часть жизни и еще с большим интересом изучать его.
				</div>
				<div class="item wow fadeIn" data-wow-duration="2s" data-wow-delay="0.6s">
					<span>03</span>
					Изучение китайского языка с детства значительно повышает возможность высокого уровня владения им во взрослой жизни, а чтение книг, прослушивание песен и знакомство с культурой восточных стран делают наши уроки китайского языка интересными и эффективными.
				</div>
				<div class="item wow fadeIn" data-wow-duration="2s" data-wow-delay="0.8s">
					<span>04</span>
					Программа обучения авторская с использованием лучших практик и методик восточного и российского образования, современных средств обучения позволяет добиться высоких результатов.
				</div>
			</div>
		</div>
	</div>	

	<div class="teachers-block">
		<div class="container">
			<div class="block-name">
				Наши преподаватели
			</div>
			<div class="list">
			
				<div class="item">
					<div class="img" :style="{'background': 'url(' + require('../assets/082022/img/teachers/teacher-18.png') + ')'}">
						<img src="../assets/082022/img/teacher-bg.png">
					</div>
					<div class="name">
						Деднев Евгений
					</div>
					<div class="prof">
						<span>Преподаватель программирования на Python, C++</span>
					</div>
					Специализация:  Информационные системы и технологии
					Получает повышение квалификации по направлению DevOps-разработчик.
					Владеет мультимедийными технологиями.
				</div>
				
				<div class="item">
					<div class="img" :style="{'background': 'url(' + require('../assets/082022/img/teachers/teacher-3.png') + ')'}">
						<img src="../assets/082022/img/teacher-bg.png">
					</div>
					<div class="name">
						Дементьева Юлия
					</div>
					<div class="prof">
						<span>Педагог курсов Soft Skills и Блогинг.</span>
					</div>
					Победитель всероссийских, областных и районных конкурсах 
					педагогического и творческого мастерства, организатор масштабных 
					мероприятий и событий различного уровня. Опыт работы с детьми более 9 лет. 
				</div>
				
				<div class="item">
					<div class="img" :style="{'background': 'url(' + require('../assets/082022/img/teachers/teacher-7.png') + ')'}">
						<img src="../assets/082022/img/teacher-bg.png">
					</div>
					<div class="name">
						Плющ Анна
					</div>
					<div class="prof">
						<span>Преподаватель китайского и английского языков </span>
					</div>
					Участница научно-практических конференций МГИМО и МГУ
					Международный экзамен HSK 4 и HSKK 中级
					В 2022 году более 15 учеников сдали ЕГЭ на 85 баллов и выше.
					Подготовила ученицу к сдаче экзамена HSK 3 (китайский язык) и к поступлению в китайский вуз
				</div>
				
				<div class="item">
					<div class="img" :style="{'background': 'url(' + require('../assets/082022/img/teachers/teacher-12.png') + ')'}">
						<img src="../assets/082022/img/teacher-bg.png">
					</div>
					<div class="name">
						Стибельский Александр
					</div>
					<div class="prof">
						<span>Педагог курсов Soft Skills и Блогинг.</span>
					</div>
					Специальность: социально-культурный сервис.
					Ведущий мероприятий, артист.
					Педагогический стаж – 7 лет
				</div>
				
				<div class="item">
					<div class="img" :style="{'background': 'url(' + require('../assets/082022/img/teachers/teacher-6.png') + ')'}">
						<img src="../assets/082022/img/teacher-bg.png">
					</div>
					<div class="name">
						Отделкина Алла
					</div>
					<div class="prof">
						<span>Педагог куров «Профильная математика», «Олимпиадная математика»</span>
					</div>
					Опыт преподавания 20 лет. 
					Более 15 лет работает со школьниками по подготовке к вступительным экзаменам, ЕГЭ по профильной и базовой математике. 
					С 2019 года являюсь экспертом ЕГЭ по профильной математике.
				</div>
				
				<div class="item">
					<div class="img" :style="{'background': 'url(' + require('../assets/082022/img/teachers/teacher-14.png') + ')'}">
						<img src="../assets/082022/img/teacher-bg.png">
					</div>
					<div class="name">
						Жигалко Андрей
					</div>
					<div class="prof">
						<span>Тренер по шахматам</span>
					</div>
					Международный гроссмейстер
					Чемпион Республики Беларусь 2011 г.
					Участник всемирных шахматных олимпиад и командного чемпионата Европы по шахматам
				</div>
				
				<div class="item">
					<div class="img" :style="{'background': 'url(' + require('../assets/082022/img/teachers/teacher-9.png') + ')'}">
						<img src="../assets/082022/img/teacher-bg.png">
					</div>
					<div class="name">
						Егорушкина Анна
					</div>
					<div class="prof">
						<span>Педагог курса «Базовый IT», 3D-моделирования, графического дизайна и др.</span>
					</div>
					По первому образованию – педагог начальных классов.
					Профессионально занимается фотографией и преподает этот курс детям. Может найти подход к каждому ребенку.
					Педагогическое кредо: «Самое главное - прививать вкус и любовь к учению».
				</div>
				
				<div class="item">
					<div class="img" :style="{'background': 'url(' + require('../assets/082022/img/teachers/teacher-16.png') + ')'}">
						<img src="../assets/082022/img/teacher-bg.png">
					</div>
					<div class="name">
						Павлов Данила
					</div>
					<div class="prof">
						<span>Тренер по шахматам</span>
					</div>
					Мастер Фиде по шахматам
					Международный гроссмейстер по решению шахматных композиций
					Чемпион мира по решению шахматных композиций
					Двукратный чемпион Европы по решению шахматных композиций
				</div>
				
				<div class="item">
					<div class="img" :style="{'background': 'url(' + require('../assets/082022/img/teachers/teacher-17.png') + ')'}">
						<img src="../assets/082022/img/teacher-bg.png">
					</div>
					<div class="name">
						Никишин Сергей
					</div>
					<div class="prof">
						<span>Тренер по киберспорту</span>
					</div>
					Профессиональный игрок по CSGO, Valorant, Apex Legends
					Двукратный чемпион Китая
					Двукратный чемпион России и СНГ
					Многократный участник чемпионата мира по CSGO 
					Опыт тренерской работы – 7 лет.
				</div>
				
				<div class="item">
					<div class="img" :style="{'background': 'url(' + require('../assets/082022/img/teachers/teacher-10.png') + ')'}">
						<img src="../assets/082022/img/teacher-bg.png">
					</div>
					<div class="name">
						Макарова Влада
					</div>
					<div class="prof">
						<span>Педагог английского языка</span>
					</div>
					Считает, что самое важное – привить детям любовь к изучению английского, тогда и результаты будут высокие.
					Применяет коммуникативную методику и интерактивные методы обучения языку.
				</div>
				
				<div class="item">
					<div class="img" :style="{'background': 'url(' + require('../assets/082022/img/teachers/teacher-11.png') + ')'}">
						<img src="../assets/082022/img/teacher-bg.png">
					</div>
					<div class="name">
						Рахматуллаев Евгений
					</div>
					<div class="prof">
						<span>Преподаватель программирования, робототехники, web-разработки и др.</span>
					</div>
					Специализация: Компьютерные сети.
					Педагогический стаж более 5 лет.
					Педагогическое кредо: Научить детей учиться.
				</div>
				
				<div class="item">
					<div class="img" :style="{'background': 'url(' + require('../assets/082022/img/teachers/teacher-1.png') + ')'}">
						<img src="../assets/082022/img/teacher-bg.png">
					</div>
					<div class="name">
						Нажмутдинов Рустам
					</div>
					<div class="prof">
						<span>Преподаватель робототехники и программирования на Scratch и Python.</span>
					</div>
					Сфера интересов: космические технологии в быту
					Кредо: Только знания и умения , могут насытить человеческое любопытство
				</div>
				
				<div class="item">
					<div class="img" :style="{'background': 'url(' + require('../assets/082022/img/teachers/teacher-4.png') + ')'}">
						<img src="../assets/082022/img/teacher-bg.png">
					</div>
					<div class="name">
						Кокорина Полина
					</div>
					<div class="prof">
						<span>Педагог курса «Базовый IT», программирования, 3D-моделирования и финансовой грамотности</span>
					</div>
					Имеет большой опыт работы с детьми, считает, что не бывает плохих детей, просто к каждому нужно найти свой подход.
				</div>
				
				<div class="item">
					<div class="img" :style="{'background': 'url(' + require('../assets/082022/img/teachers/teacher-2.png') + ')'}">
						<img src="../assets/082022/img/teacher-bg.png">
					</div>
					<div class="name">
						Пузанов Сергей
					</div>
					<div class="prof">
						<span>Преподаватель по web-разработке (Html5, css3, js, php и фреймворки), 3D-моделированию в Blender и UI/UX-дизайну на Figma</span>
					</div>
					Работает на должности тимлида в IT-компании по разработке сайтов.
					Увлекается изучением языков программирования и фреймворков.
				</div>
				
				<div class="item">
					<div class="img" :style="{'background': 'url(' + require('../assets/082022/img/teachers/teacher-5.png') + ')'}">
						<img src="../assets/082022/img/teacher-bg.png">
					</div>
					<div class="name">
						Вавилова Дарья
					</div>
					<div class="prof">
						<span>Преподаватель программирования, робототехники и графического дизайна.</span>
					</div>
					Специальность: программная инженерия. 
					Ее цель -  помочь детям ориентироваться в информационном пространстве, чтобы в будущем они смогли связать свою жизнь с IT
				</div>
				
				<div class="item">
					<div class="img" :style="{'background': 'url(' + require('../assets/082022/img/teachers/teacher-8.png') + ')'}">
						<img src="../assets/082022/img/teacher-bg.png">
					</div>
					<div class="name">
						Шадрин Антон
					</div>
					<div class="prof">
						<span>Педагог курсов «Программирование на Python» и «Web-разработка».</span>
					</div>
					Специальность: Программная инженерия.
					Занимается подготовкой к ЕГЭ по информатике.
					Педагогическое кредо: Если преподаватель не учится чему-то новому вместе с учениками - то это плохой преподаватель.
				</div>
				
				<div class="item">
					<div class="img" :style="{'background': 'url(' + require('../assets/082022/img/teachers/teacher-13.png') + ')'}">
						<img src="../assets/082022/img/teacher-bg.png">
					</div>
					<div class="name">
						Супруненко Константин
					</div>
					<div class="prof">
						<span>Тренер по шахматам</span>
					</div>
					Первый взрослый разряд
					Чемпион областных соревнований
					Призер всероссийских соревнований
					Опыт работы более 10 лет
				</div>
				
				<div class="item">
					<div class="img" :style="{'background': 'url(' + require('../assets/082022/img/teachers/teacher-15.png') + ')'}">
						<img src="../assets/082022/img/teacher-bg.png">
					</div>
					<div class="name">
						Куфтырев Илья
					</div>
					<div class="prof">
						<span>Тренер по шахматам</span>
					</div>
					Кандидат в мастера спорта
					Призер всероссийских соревнований
					Опыт работы более 1 года
				</div>
				
				<div class="item">
					<div class="img" :style="{'background': 'url(' + require('../assets/082022/img/teachers/teacher-19.png') + ')'}">
						<img src="../assets/082022/img/teacher-bg.png">
					</div>
					<div class="name">
						Якшенев Максим
					</div>
					<div class="prof">
						<span>Тренер по киберспорту</span>
					</div>
					Опытный тимлид в популярных Action/Shooter играх. 
					Специализируется на упражнениях по развитию меткости и микроконтроля. Поможет отточить тактики и стратегии, подскажет как адаптироваться к любой ситуации.
				</div>
				
			</div>
			<div class="bottom-button">
				<button class="GetCourceModal">Записаться на пробное занятие</button>
			</div>
		</div>
	</div>	

	<div class="portfolio-block container">
		<div class="image i2">
			<img src="../assets/082022/img/portfolio2.png">
		</div>
		<div class="name">
			Ваше будущее портфолио
		</div>
		<div class="image i1">
			<img src="../assets/082022/img/portfolio1.png">
		</div>
		<p>Каждый ученик получает сертификат Академии будущего «ХОД», который подтверждает прохождение курса. По результатам обучения каждый студент сформирует портфолио из работ, выполненных в процессе обучения</p>
	</div>
	
	<div class="lessons-block">
		<div class="container">
			<div class="block-name">
				Занятия проходят
			</div>
			<div class="top-text">
				в современных аудиториях с удобством, комфортом и заботой о студентах
			</div>
		</div>
	
		
		<div class="list">
			<img src="../assets/082022/img/gallery/lesson1.png">
			<img src="../assets/082022/img/gallery/lesson2.png">
			<img src="../assets/082022/img/gallery/lesson3.png">
			<img src="../assets/082022/img/gallery/lesson4.png">
			<img src="../assets/082022/img/gallery/lesson5.png">
			<img src="../assets/082022/img/gallery/lesson6.png">
			<img src="../assets/082022/img/gallery/lesson7.png">
			<img src="../assets/082022/img/gallery/lesson8.png">
			<img src="../assets/082022/img/gallery/lesson9.png">
			<img src="../assets/082022/img/gallery/lesson10.png">
			<img src="../assets/082022/img/gallery/lesson11.png">
			<img src="../assets/082022/img/gallery/lesson12.png">
			<img src="../assets/082022/img/gallery/lesson13.png">
			<img src="../assets/082022/img/gallery/lesson14.png">
			<img src="../assets/082022/img/gallery/lesson15.png">
		</div>                              
	</div>  	

	<div class="reviews-block">             
		<div class="container">             
			<div class="block-name">        
				Отзывы наших студентов      
			</div>                          
		</div>
		<div class="list">
			<div class="item">
				<a href="https://youtube.com/shorts/ekZlwOD7zps" data-vid="ekZlwOD7zps"><img src="../assets/082022/img/responses/1.jpg"></a>
			</div>
			<div class="item">
				<a href="https://youtube.com/shorts/xpycp2qji0g" data-vid="xpycp2qji0g"><img src="../assets/082022/img/responses/2.jpg"></a>
			</div>
			<div class="item">
				<a href="https://youtube.com/shorts/kqy8O_VvS2Y" data-vid="kqy8O_VvS2Y"><img src="../assets/082022/img/responses/3.jpg"></a>
			</div>
			<div class="item">
				<a href="https://youtube.com/shorts/Q_oKxK9_cpw" data-vid="Q_oKxK9_cpw"><img src="../assets/082022/img/responses/4.jpg"></a>
			</div>
			<div class="item">
				<a href="https://youtu.be/tcDG4-Rnjjc" data-vid="tcDG4-Rnjjc"><img src="../assets/082022/img/responses/5.jpg"></a>
			</div>
			<div class="item">
				<a href="https://youtube.com/shorts/SEQWsUdQXMU" data-vid="SEQWsUdQXMU"><img src="../assets/082022/img/responses/6.jpg"></a>
			</div>
			<div class="item">
				<a href="https://youtube.com/shorts/FgVnbckORxo" data-vid="FgVnbckORxo"><img src="../assets/082022/img/responses/7.jpg"></a>
			</div>
			<div class="item">
				<a href="https://youtu.be/u2XpPvqWnSk" data-vid="u2XpPvqWnSk"><img src="../assets/082022/img/responses/8.jpg"></a>
			</div>
			<div class="item">
				<a href="https://youtube.com/shorts/xcLzjkP9E3w" data-vid="xcLzjkP9E3w"><img src="../assets/082022/img/responses/9.jpg"></a>
			</div>
			<div class="item">
				<a href="https://youtube.com/shorts/80Fvuab-K30" data-vid="80Fvuab-K30"><img src="../assets/082022/img/responses/10.jpg"></a>
			</div>
			<div class="item">
				<a href="https://youtu.be/p2DtuGJ-TPE" data-vid="p2DtuGJ-TPE"><img src="../assets/082022/img/responses/11.jpg"></a>
			</div>
			<div class="item">
				<a href="https://youtube.com/shorts/d8jycUYQ1sQ" data-vid="d8jycUYQ1sQ"><img src="../assets/082022/img/responses/12.jpg"></a>
			</div>
			<div class="item">
				<a href="https://youtube.com/shorts/wVQGdpYeCmQ" data-vid="wVQGdpYeCmQ"><img src="../assets/082022/img/responses/13.jpg"></a>
			</div>
			<div class="item">
				<a href="https://youtube.com/shorts/rdv5UMTM7P8" data-vid="rdv5UMTM7P8"><img src="../assets/082022/img/responses/14.jpg"></a>
			</div>
			<div class="item">
				<a href="https://youtube.com/shorts/T9AqZ6Navg8" data-vid="T9AqZ6Navg8"><img src="../assets/082022/img/responses/15.jpg"></a>
			</div>
			<div class="item">
				<a href="https://youtube.com/shorts/TH96V3ifBL8" data-vid="TH96V3ifBL8"><img src="../assets/082022/img/responses/16.jpg"></a>
			</div>
			<div class="item">
				<a href="https://youtube.com/shorts/75b0NSjFaZg" data-vid="75b0NSjFaZg"><img src="../assets/082022/img/responses/17.jpg"></a>
			</div>
			<div class="item">
				<a href="https://youtu.be/cknrM276KUU" data-vid="cknrM276KUU"><img src="../assets/082022/img/responses/18.jpg"></a>
			</div>
			<div class="item">
				<a href="https://youtube.com/shorts/BUdKaNmWuMY" data-vid="BUdKaNmWuMY"><img src="../assets/082022/img/responses/19.jpg"></a>
			</div>
			<div class="item">
				<a href="https://youtube.com/shorts/3KrOP2iWB-U" data-vid="3KrOP2iWB-U"><img src="../assets/082022/img/responses/20.jpg"></a>
			</div>
			<div class="item">
				<a href="https://youtu.be/mHT3aRzjNpA" data-vid="mHT3aRzjNpA"><img src="../assets/082022/img/responses/21.jpg"></a>
			</div>
			<div class="item">
				<a href="https://www.youtube.com/shorts/dZfdgEIsFP8" data-vid="dZfdgEIsFP8"><img src="../assets/082022/img/responses/22.jpg"></a>
			</div>
			<div class="item">
				<a href="https://youtube.com/shorts/FUv1lEjFYJI" data-vid="FUv1lEjFYJI"><img src="../assets/082022/img/responses/23.jpg"></a>
			</div>
			<div class="item">
				<a href="https://youtube.com/shorts/-xlREQP2yns" data-vid="-xlREQP2yns"><img src="../assets/082022/img/responses/24.jpg"></a>
			</div>
			<div class="item">
				<a href="https://youtube.com/shorts/Y1GjgtNMD6I" data-vid="Y1GjgtNMD6I"><img src="../assets/082022/img/responses/25.jpg"></a>
			</div>
			<div class="item">
				<a href="https://youtu.be/2s7Qf4GVVCQ" data-vid="2s7Qf4GVVCQ"><img src="../assets/082022/img/responses/26.jpg"></a>
			</div>
			<div class="item">
				<a href="https://youtube.com/shorts/KXlog-POWHc" data-vid="KXlog-POWHc"><img src="../assets/082022/img/responses/27.jpg"></a>
			</div>
			<div class="item">
				<a href="https://youtube.com/shorts/GRZneePA4o0" data-vid="GRZneePA4o0"><img src="../assets/082022/img/responses/28.jpg"></a>
			</div>
			<div class="item">
				<a href="https://youtube.com/shorts/HvGlzZR64N4" data-vid="HvGlzZR64N4"><img src="../assets/082022/img/responses/29.jpg"></a>
			</div>
			<div class="item">
				<a href="https://youtube.com/shorts/lmf6NsHmd_w" data-vid="lmf6NsHmd_w"><img src="../assets/082022/img/responses/30.jpg"></a>
			</div>
			<div class="item">
				<a href="https://youtube.com/shorts/f27FNDELy0k" data-vid="f27FNDELy0k"><img src="../assets/082022/img/responses/31.jpg"></a>
			</div>
			
		</div>
	</div>
	<div class="faq-block">
		<div class="container">
			<div class="block-name">
				Спрашивали? Отвечаем:)
			</div>
			<div class="item">
				<div class="name">
					Что нужно ребенку для занятий?
				</div>
				<div class="text">
					Для занятий понадобится тетрадь и ручка.
				</div>
			</div>
			<div class="item">
				<div class="name">
					Где можно узнать расписание занятий?
				</div>
				<div class="text">
					Расписание вы можете узнать в личном кабинете студента или позвонить менеджеру Академии.
				</div>
			</div>
			<div class="item">
				<div class="name">
					Что делать, если ребенок пропустит занятие?
				</div>
				<div class="text">
					Занятия, пропущенные по уважительной причине, компенсируются посещением занятий с другой группой и специально организованного урока.
				</div>
			</div>
		</div>
	</div>
	
	<div style="display: none;" class="video-modal video-modal-about">
		<div class="modal-mask">
			<div class="video-modal-place">
				<div class="video-modal-content">
					<div class="video-modal-header">				
						<a class="video-modal-close"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" tabindex="-1"><path d="M20 20L4 4m16 0L4 20"></path></svg></a>
					</div>
					<iframe class="video-frame video-about-frame" src="" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
				</div>
			</div>
		</div>
   </div>
	
	<div style="display: none;" class="video-modal video-modal-rk">
		<div class="modal-mask">
			<div class="video-modal-place">
				<div class="video-modal-content">
					<div class="video-modal-header">				
						<a class="video-modal-close"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" tabindex="-1"><path d="M20 20L4 4m16 0L4 20"></path></svg></a>
					</div>
					<iframe class="video-frame video-rk-frame" src="" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
				</div>
			</div>
		</div>
   </div>
	
	<div style="display: none;" class="video-modal video-modal-response">
		<div class="modal-mask">
			<div class="video-modal-place">
				<div class="video-modal-content">
					<div class="video-modal-header">				
						<a class="video-modal-close"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" tabindex="-1"><path d="M20 20L4 4m16 0L4 20"></path></svg></a>
					</div>
					<iframe class="video-frame video-response-frame" src="" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
				</div>
			</div>
		</div>
   </div>
  </div>
</template>

<style scoped>

	
	
	.english-owl-block {
		margin-top: 80px;
	}
	
	.english-owl-block .owl-owl {
		background: url('../assets/082022/img/owl-block-owl.png') no-repeat top right; 
		float: left;
		width: 430px;
		height: 311px;
	}
	
	.chinese-owl-block .owl-owl {
		background: url('../assets/082022/img/owl-block-cowl.png') no-repeat top right; 
	}
	
	.english-owl-block .owl-content {
		background: linear-gradient(#fff 0 0) padding-box, linear-gradient(to right, #F7941D, #27AAE1) border-box;		
		border: solid 2px transparent;
		border-radius: 15px;
		min-height: 220px;
		padding: 20px 20px 20px 22px;
		margin-left: 428px;
	}
	
	@media (max-width: 769px) {
		.english-owl-block .owl-owl {
			background: url('../assets/082022/img/owl-block-owlm.png') no-repeat top center /cover; 
			float: none;
			width: 100%;
			height: 220px;
		}

		.chinese-owl-block .owl-owl {
			background: url('../assets/082022/img/owl-block-cowlm.png') no-repeat top center /cover; 
			float: none;
			width: 100%;
			height: 220px;
		}
		
		.english-owl-block .owl-content {
			border-radius: 15px;
			min-height: auto;
			padding: 20px 20px 20px 20px;
			margin-left: 0;
		}
	
	}	
	
	.course-block-text {
		text-align: center;
		max-width: 630px;
		margin: 0 auto;
	}
	
	.course-block .item .icon {
		width: 120px;
	}
	
	.course-block .item p {
		padding: 35px 25px;
		text-align: center;
	}
	
	.course-block .item {
		background:
			url('../assets/082022/img/course-block-item-bg1.png') left top no-repeat,
			url('../assets/082022/img/course-block-item-bg2.png') right top no-repeat,
			url('../assets/082022/img/course-block-item-bg3.png') right bottom no-repeat,
			url('../assets/082022/img/course-block-item-bg4.png') left bottom no-repeat;
			
		min-height: 86px;
		box-sizing: border-box;
	}
	
	.course-block .item p span {
		font-size: 20px;
		font-weight: normal;
	}
	
	.inner-first-block {
		background: url('../assets/082022/img/first-block-common-bg.png');
	}

	.you-learn-block .list .item.i1 {
		top: 0;
	}
	
	.you-learn-block .list {
		background: url('../assets/082022/img/bg2-user.png');
		background-position: center center;
    	background-size: contain;
    	background-repeat: no-repeat;
	}
	
	.you-learn-block .mob-caption {
		display: none;
		font-style: normal;
		font-weight: 700;
		font-size: 24px;
		line-height: 29px;
		text-align: center;
		width: 100%;
		text-transform: uppercase;
		padding: 147px 0 155px 0;
	}
	
	.program-block {
		background: url(../assets/082022/img/program-block-bg.png) 50%/cover;
	}
	
	.principles-block {
		min-height: 460px;
		padding: 107px 19% 107px 45%;
		box-sizing: border-box;
		
		background: url('../assets/082022/img/principles-bg.png') right center no-repeat, linear-gradient(90.28deg, #AAD3FE 40.24%, #CEE6FF 60.2%);
		
		border: 1px solid #000000;
		border-left: none;
		border-right: none;
	}
	
	.principles-block .block-name {
		font-style: normal;
		font-weight: 700;
		font-size: 48px;
		line-height: 59px;
		margin-bottom: 52px;
	}	
	
	.principles-list .item {
		padding-left: 25px;
		background: no-repeat top left url('../assets/082022/img/principles-list.png');
		margin-bottom: 36px;
	}
	
	.levels-block {
		margin-top: 110px;
	}
	
	.teachers-block {
    	background: url('../assets/082022/img/teachers-block-bg.png') 50%/cover;
    }

	.reviews-block {
    	background: url('../assets/082022/img/reviews-block-bg.png') 50%/cover;
    }
    
    .levels-block .item {
    	cursor: pointer;
    }
    
    .levels-block .flex .item-user img {
    	top: -177px;
    }
    
	@media (max-width: 575px) {
	
		.course-block .item p span {
			font-size: 17px;
		}
	
	
		.you-learn-block .list {
			background: url('../assets/082022/img/first-block-common-bgm.png') top center no-repeat;
		}

		.you-learn-block .mob-caption {
			display: block;
		}
	
		.principles-block {
			padding: 15px;
			background: url('../assets/082022/img/principles-bgm.png') center 90px no-repeat, linear-gradient(90.28deg, #AAD3FE 40.24%, #CEE6FF 60.2%);
		}
	
		.principles-block .block-name {
			font-size: 30px;
			margin-bottom: 236px
		}	
		
		.inner-first-block .text .name span {
    		font-size: 30px;
		}
		
		.principles-list .item {
			margin-bottom: 30px;
		}
	
		#app {overflow: hidden;}
	}
</style>

<script>

export default {
  title: 'Академия будущего | Китайский язык',
  name: "EducationCheater",

  mixins: [],

  data() {
    return {
    }
  },

  props: {
  },

  components: {
  },

  created() {
  },

  methods: {
  },
  
  mounted: function() {  
		let $ = window.$;
		$(document).ready(function(){
			function makeTimer() {
				var endTime = new Date("11 September 2022 9:56:00 GMT+01:00");			
					endTime = (Date.parse(endTime) / 1000);
					var now = new Date();
					now = (Date.parse(now) / 1000);
					var timeLeft = endTime - now;
					var days = Math.floor(timeLeft / 86400); 
					var hours = Math.floor((timeLeft - (days * 86400)) / 3600);
					var minutes = Math.floor((timeLeft - (days * 86400) - (hours * 3600 )) / 60);
					var seconds = Math.floor((timeLeft - (days * 86400) - (hours * 3600) - (minutes * 60)));	  
					if (hours < "10") { hours = "0" + hours; }
					if (minutes < "10") { minutes = "0" + minutes; }
					if (seconds < "10") { seconds = "0" + seconds; }
					$("#days").html("<div>" + days + "</div><span>дней</span>");
					$("#hours").html("<div>" + hours + "</div><span>часов</span>");
					$("#minutes").html("<div>" + minutes + "</div><span>минут</span>");
					$("#seconds").html("<div>" + seconds + "</div><span>секунд</span>");
			}
			setInterval(function() { makeTimer(); }, 1000);
			
			var videoHeight = $( window ).width() * (540 / 960);
			if (videoHeight + 85 > $( window ).height()) {
				var videoWidth = ($( window ).height() - 85) * (960 / 540);
				videoHeight = videoWidth * (540 / 960) - 85;
				$('.video-modal-content').width(videoWidth);
			}
			$('.video-modal-content').height(videoHeight);
			
			$('.video-about a.play').click(function() {
				
				$('.video-about-frame').each( function () {
					$(this).attr('src', 'https://www.youtube.com/embed/1Y5n0nu98Vg?controls=1&autoplay=1&loop=1&playlist=1Y5n0nu98Vg');	
				});
				
				$('.video-modal-about').show();
				return false;
			});
			
			$('.video-rk').click(function() {
				
				$('.video-rk-frame').each( function () {
					$(this).attr('src', 'https://www.youtube.com/embed/rgNRINLfNrs?controls=1&autoplay=1&loop=1&playlist=rgNRINLfNrs');	
				});
				
				$('.video-modal-rk').show();
				return false;
			});
			
			
			// Ширина 444
			// Высота 790
			
			var wh = $( window ).height();
			var vh = wh - 85;
			var vw = vh * 444 / 790;
			
			$('.video-modal-response .video-modal-content').width(vw);
			$('.video-modal-response .video-modal-content').height(vh);
			
			$('.reviews-block .item a').click(function() {
				var vid = $(this).data('vid');
				$('.video-response-frame').each( function () {
					$(this).attr('src', 'https://www.youtube.com/embed/' + vid + '?controls=1&autoplay=1&loop=1&playlist=' + vid);	
				});
				
				$('.video-modal-response').show();
				return false;
			});
			

			$('.video-modal-close').click(function() {
				$('.video-frame').attr('src', '')
				$('.video-modal').hide();
				return false;
			});
			
			$('.buttonSendRequest').click(function() {
				window.location.href = "/send-request";
				return false;
			});
			
			$('.buttonAbout').click(function() {
				window.location.href = "/about";
				return false;
			});

			$('.goToPolzovatel').click(function() {
				window.location.href = "/education/user";
				return false;
			});

			$('.goToBeginner').click(function() {
				window.location.href = "/education/beginner";
				return false;
			});

			$('.goToProfessional').click(function() {
				window.location.href = "/education/prof";
				return false;
			});

			$('.goToChiter').click(function() {
				window.location.href = "/education/cheater";
				return false;
			});
			
		});
  },

}
</script>

<style scoped>
</style>