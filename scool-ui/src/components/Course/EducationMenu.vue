<template>
  <div id="education-menu">
    <ul class="vMenu">
      <li class="left-align px-2"><a href="#"> Все направления </a></li>
      <li v-for="category in categoryList" :key="category.id" class="left-align px-2">
        <a href="#"> {{ category.name }} </a>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  data() {
    return {
      categoryList: []
    }
  },
  name: "EducationMenu",
  created() {
    this.loadCategoryList()
  },
  methods: {
    async loadCategoryList() {
      this.categoryList = await fetch(
          `${this.$store.getters.getServerUrl}/categories/`
      ).then(response => response.json())
    }
  }
}
</script>

<style scoped>

</style>