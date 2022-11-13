<template>
  <div class="item" id="hide-block">
      <img src="../../assets/images/icons/padlock.svg" class="padlock">
      <p class="mt-3">Для просмотра подробной информации добавьте пользователя в друзья.</p>
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
  text-align: center;
  padding: 80px 0;
}

.padlock {
  width: 30%;
}
</style>