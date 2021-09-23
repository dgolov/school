<template>
  <div class="row my-3">
    <div class="col-md-12">
      <a href="#">Одногруппники {{ groupName }}</a>
    </div>
<!--    <div class="col-md-6">-->
<!--      <a href="#">Преподаватели группы</a>-->
<!--    </div>-->
  </div>
</template>


<script>
export default {
  name: "SingleGroupHeader",

  props: {
    groupName: String,
  },
}
</script>


<style scoped>

</style>