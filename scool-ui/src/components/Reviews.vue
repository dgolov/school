<template>
  <section class="reviews">
    <div class="container">
      <div class="row">
        <div class="col-12">
          <h2 class="reviews-title">Отзывы наших студентов</h2>
        </div>
      </div>
    </div>
    <div class="row">
      <div class="col-12">
        <div class="slider-wrapper d-flex justify-content-center">
          <div class="slide">
            <!-- Контент 1 слайда -->
            <div class="col-3">
              <div class="reviews-student">
                <div class="reviews-inner d-flex">
                  <div class="reviews-inner__userpic wrapper-review review">
                    <img src="../assets/img/reviews/rew4.jpeg" alt="Фото студента">
                  </div>
                  <div class="userpic-about">
                    <h5 class="userpic-about__name">Александра Ястребова</h5>
                    <p class="userpic-about__course">Студент курса
                      <span class="course-name">«Pro»</span>
                    </p>
                  </div>
                </div>
                <p class="reviews-desc">Занимаемся с конца октября. Это действительно то, что может увлечь ребенка.
                  Яркий пример, как ребенок 10 лет, приобретает новое самостоятельное современное увлечение, в
                  котором может еще и "обскакать" родителей.</p>
              </div>
            </div>
          </div>
          <div class="slide">
            <!-- Контент 2 слайда -->
            <div class="col-3">
              <div class="reviews-student">
                <div class="reviews-inner d-flex">
                  <div class="reviews-inner__userpic wrapper-review review">
                    <img src="../assets/img/reviews/rew3.jpeg" alt="Фото студента">
                  </div>
                  <div class="userpic-about">
                    <h5 class="userpic-about__name">Евгения Дзонова</h5>
                    <p class="userpic-about__course">Студент курса
                      <span class="course-name">«Web разработчик»</span>
                    </p>
                  </div>
                </div>
                <p class="reviews-desc">Поступила на направление web разработки, очень огромным плюсом по моему
                  мнению является то, что занятия онлайн, в любом месте можно подключиться! У меня есть связь с
                  преподавателем 24/7 и конечно комьюнити с одногруппниками.</p>
              </div>
            </div>
          </div>
          <div class="slide ">
            <!-- Контент 3 слайда -->
            <div class="col-3">
              <div class="reviews-student">
                <div class="reviews-inner d-flex">
                  <div class="reviews-inner__userpic wrapper-review review">
                    <img src="../assets/img/reviews/rew2.jpg" alt="Фото студента">
                  </div>
                  <div class="userpic-about">
                    <h5 class="userpic-about__name">Людмила Понизова</h5>
                    <p class="userpic-about__course">Студент курса
                      <span class="course-name">«User»</span>
                    </p>
                  </div>
                </div>
                <p class="reviews-desc">Узнала об этом заведении благодаря рекламе в Инстаграмм. Сходили с дочерью на
                  бесплатный мастер-класс и лекцию для родителей. Все очень понравилось, и сразу заключили договор на
                  программу Юзер)))</p>
              </div>
            </div>
          </div>
          <div class="slide ">
            <!-- Контент 4 слайда -->
            <div class="col-3">
              <div class="reviews-student">
                <div class="reviews-inner d-flex">
                  <div class="reviews-inner__userpic wrapper-review review">
                    <img src="../assets/img/reviews/rew1.jpeg" alt="Фото студента">
                  </div>
                  <div class="userpic-about">
                    <h5 class="userpic-about__name">Ульяна Новикова</h5>
                    <p class="userpic-about__course">Студент курса
                      <span class="course-name">«Тестировщик ПО»</span>
                    </p>
                  </div>
                </div>
                <p class="reviews-desc">Учусь в Академии Будущего  уже  два месяца на QA-инженера. Ни разу не
                  пожалела, что выбрала курсы именно тут. Администрация всегда на связи, решит любой вопрос по первой
                  просьбе. Преподаватель искренне заинтересован в предмете, что ещё больше мотивирует учиться.</p>
                <!--                  <div class="rating d-flex align-items-center">-->
                <!--                    <span class="rating__star"></span>-->
                <!--                    <span class="rating__number">4,87</span>-->
                <!--                    <p class="rating__number">/</p>-->
                <!--                    <span class="rating__number">5</span>-->
                <!--                  </div>-->
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>


<script>
export default {
  name: "Reviews"
}
</script>


<style scoped>

.wrapper-review {
  width: 50px;
  height: 50px;
}
.review {
  overflow: hidden;
  display: flex;
  justify-content: center;
  align-items: center;
}
.review img {
  height: auto;
  width: 100%;
  border-radius: 50%;
}
</style>