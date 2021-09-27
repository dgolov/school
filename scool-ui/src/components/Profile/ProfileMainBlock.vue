<template>
  <div id="profile-main">
    <div class="row my-3">
      <div class="col-md-3">
        <h6>День рождения:</h6>
      </div>
      <div class="col-md-9 left-align">
        <a href="#">{{ profile.date_of_birthday }}</a>
      </div>
    </div>
    <div class="row my-3">
      <div class="col-md-3">
        <h6>Пол:</h6>
      </div>
      <div class="col-md-9 left-align">
        <a v-if="profile.gender === 'm'" href="#">Мужской</a>
        <a v-else href="#">Женский</a>
      </div>
    </div>
  </div>
</template>


<script>
export default {
  name: "StudentAbout",

  props: ['profile'],
}
</script>


<style scoped>

</style>