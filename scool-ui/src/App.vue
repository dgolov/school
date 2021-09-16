<template>
  <div id="app">
    <router-view/>
    <Footer/>
  </div>
</template>

<style>
@import "./assets/bootstrap/css/bootstrap.css";
@import "./assets/css/style.css";
</style>
<script>
import Footer from "./components/Footer";

export default {
  components: {Footer}
}
</script>