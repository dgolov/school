<template>
  <div class="course__section">
    <div class="container pb-5">
      <h2 class="system-color">Как проходит обучение</h2>
      <div class="row">
        <div class="col-md-6 px-2">
          <h3><span class="course_number">1</span>Изучаете темы уроков с преподавателем</h3>
          <small>Учитесь с преподавателем в режиме онлайн, так же вам будут доступны записи уроков</small>
        </div>
        <div class="col-md-6 px-2">
          <h3><span class="course_number">2</span>Выполняете домашние задания</h3>
          <small>Преподаватель проверяет выполненное вами домашнее задание и ставит оценку</small>
        </div>
        <div class="col-md-6 px-2">
          <h3><span class="course_number">3</span>Решаете контрольные работы</h3>
          <small>Вы так же будете выполнять контрольные работы по пройденному материалу и получать за них
            оценки</small>
        </div>
        <div class="col-md-6 px-2">
          <h3><span class="course_number">4</span>Сдаете экзамен</h3>
          <small>По окончанию курса вы сдаете экзамен и получаете сертификат о прохождении курса</small>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "HowGoing"
}
</script>

<style scoped>
  .course_number {
    background-color: #d94625;
    border-radius: 50%;
    color: #ffffff;
    display: inline-block;
    margin-right: 10px;
    text-align: center;
    width: 30px;
  }
</style>