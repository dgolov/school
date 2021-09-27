<template>
  <div id="student-about">
    <div v-if="profile.user_group === 'student'" class="row my-3">
      <div class="col-md-3"><h6>Увлечения:</h6></div>
      <div class="col-md-9 left-align">
        <a v-if="profile.hobbies" href="#">{{ profile.hobbies }}</a>
        <p v-else class="my-0">-</p>
      </div>
    </div>
    <div v-if="profile.user_group === 'teacher'" class="row my-3">
      <div class="col-md-3"><h6>Образование:</h6></div>
      <div class="col-md-9 left-align">
        <a v-if="profile.education" href="#">{{ profile.education }}</a>
        <p v-else class="my-0">-</p>
      </div>
    </div>
    <div v-if="profile.user_group === 'student'" class="row mt-3">
      <div class="col-md-3"><h6>Мечта:</h6></div>
      <div class="col-md-9 left-align">
        <a v-if="profile.dream" href="#">{{ profile.dream }}</a>
        <p v-else class="my-0">-</p>
      </div>
    </div>
    <div v-if="profile.user_group === 'teacher'" class="row my-3">
      <div class="col-md-3"><h6>Профессиональная деятельность:</h6></div>
      <div class="col-md-9 left-align">
        <a v-if="profile.professional_activity" href="#">{{ profile.professional_activity }}</a>
        <p v-else class="my-0">-</p>
      </div>
    </div>
    <div class="row my-3 mb-4">
      <div class="col-md-3"><h6>О себе:</h6></div>
      <div class="col-md-9 left-align ">
        <p v-if="profile.about" class="my-0">{{ profile.about }}</p>
        <p v-else class="my-0">-</p>
      </div>
    </div>
  </div>
</template>


<script>
export default {
  name: "ProfileAboutBlock",

  props: ['profile'],
}
</script>


<style scoped>

</style>