<template>
  <div class="row">
    <div class="col-md-9">
      <form>
        <input type='text' placeholder="Поиск" class="w-100">
      </form>
    </div>
    <div class="col-md-3">
      <button class="gray-button search_button">Найти друзей</button>
    </div>
  </div>
</template>

<script>
export default {
  name: "SearchFriends"
}
</script>

<style scoped>
.search_button {
  height: 68%;
}
</style>