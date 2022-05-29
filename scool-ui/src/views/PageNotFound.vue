<template>
  <div class="main-wrapper">
    <navbar></navbar>
    <section class="page-not-found click-on">
      <div class="page-not-found_owl container">
        <img class="page-not-found_figure-1" src="../assets/images/404/1.svg" alt="">
        <img class="page-not-found_figure-2" src="../assets/images/404/2.svg" alt="">
        <img class="page-not-found_figure-3" src="../assets/images/404/3.svg" alt="">
        <img class="page-not-found_figure-4" src="../assets/images/404/4.svg" alt="">
        <h1>Страница не найдена</h1>
        <img class="page-not-found--owl" src="../assets/images/404/404-owl.png" alt="">
        <p><a href="/">Вернуться на главную</a></p>
      </div>
    </section>
  </div>
</template>

<script>
import Navbar from "../components/NavbarMain";
import Search from "./Profile/Search";

export default {
  name: "PageNotFound",
  components: {
    Search,
    Navbar
  },
}
</script>

<style scoped>

</style>