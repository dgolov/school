<template>
  <div id="info">
    <div class="row mt-3">
      <div class="info-section" style="width: 30%">
        <p class="mb-0 mt-0">Срок обучения: </p>
        <p class="mb-0 mt-0">{{ course.duration }} месяцев</p>
      </div>
      <div class="info-section" style="width: 60%">
        <p class="mb-0 mt-0">Режим занятий: </p>
        <p class="mb-0 mt-0">2 раза в неделю по 2 академических часа</p>
      </div>
      <div class="info-section mt-4" style="width: 60%">
        <h3 class="mt-0">от {{ course.price }} в месяц</h3>
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

.info-section {
  display: inline-block;
  margin-right: 5%;
  border-top: 1px solid;
  border-image: linear-gradient(to right, #eb934f, #63a9da) 47% 0;
  padding-top: 10px;
}

.info-section p {
  font-size: 14px;
}

.info-section h3 {
  color: #ffffff;
}
</style>