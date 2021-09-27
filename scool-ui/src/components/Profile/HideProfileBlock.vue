<template>
  <div class="row my-3" id="hide-block">
    <div class="center">
      <img src="../../assets/images/icons/padlock.svg" class="padlock">
      <p class="mt-3">Для просмотра подробной информации добавьте пользователя в друзья.</p>
    </div>
  </div>
</template>


<script>
export default {
  name: "HideProfileBlock"
}
</script>


<style scoped>
#hide-block {
  color: gray;
}

.padlock {
  width: 30%;
}
</style>