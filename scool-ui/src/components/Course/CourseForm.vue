<template>
  <div class="cta cta--reverse">
    <div class="container">
      <div class="row">
        <div class="col-md-5">
          <h3 class="cta__title">Записаться на курс или получить бесплатную консультацию</h3>
          <p>Наш специалист свяжестся с вами м предоставит подробную информацию с презентацией курса.</p>
        </div>
        <div class="col-md-7 px-5 mt-4">
          <form>
            <input type='text' placeholder="ФИО...">
            <div class="double">
              <div class="half">
                <input type="text" id="first" placeholder="Телефон...">
              </div>
              <div class="half">
                <input type="text" id="second" placeholder="Электронная почта...">
              </div>
            </div>
            <button class="button button__accent w-100"> Отправить</button>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "CourseForm"
}
</script>

<style scoped>

</style>