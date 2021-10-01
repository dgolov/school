<template>
  <div class="step course__section center">
    <div class="container">
      <div class="row mt-5">
        <div v-if="course" class="col-md-6">
          <img :src="course.poster" class="course-poster my-4">
        </div>
        <div v-if="course" class="col-md-6 mt-5">
          <p class="left-align">Курс</p>
          <h1>{{course.name}}</h1>
          <div class="left-align">
            <h5 class="system-color">Преподаватель:</h5>
            <a href="#">{{course.teacher.last_name}} {{course.teacher.first_name}} {{course.teacher.middle_name}}</a>
          </div>
          <div class="left-align">
            <h5 class="system-color">Менеджер учебного процесса:</h5>
            <a href="#">Макаров Николай Викторович</a>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "CourseInfo",
  props: ['course']
}
</script>

<style scoped>

</style>