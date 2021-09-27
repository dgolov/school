<template>
  <div id="profile-contacts">
    <div class="row my-3">
      <div class="col-md-3">
        <h6>Телефон:</h6>
      </div>
      <div class="col-md-9 left-align">
        <a href="tel:+79082373971">{{ profile.phone }}</a>
      </div>
    </div>
    <div class="row my-3">
      <div class="col-md-3">
        <h6>Город:</h6>
      </div>
      <div class="col-md-9 left-align">
        <a v-if="profile.city" href="#">{{ profile.city }}</a>
        <p v-else class="my-0">-</p>
      </div>
    </div>
    <div class="row my-3">
      <div class="col-md-3">
        <h6>E-mail:</h6>
      </div>
      <div class="col-md-9 left-align">
        <a href="mailto:vanya_grishin@mail.ru">{{ profile.email }}</a>
      </div>
    </div>
    <div class="row my-3">
      <div class="col-md-3">
        <h6>Профиль vk.com:</h6>
      </div>
      <div class="col-md-9 left-align">
        <a v-if="profile.vk_slug" href="https://vk.com/piupiu7">{{ profile.vk_slug }}</a>
        <p v-else class="my-0">-</p>
      </div>
    </div>
    <div class="row mt-3 mb-4">
      <div class="col-md-3">
        <h6>Профиль Instagram:</h6>
      </div>
      <div class="col-md-9 left-align">
        <a v-if="profile.instagram_slug" href="#">{{ profile.instagram_slug }}</a>
        <p v-else class="my-0">-</p>
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