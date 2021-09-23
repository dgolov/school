<template>
  <div class="about">
    <navbar></navbar>
    <construction></construction>
  </div>
</template>

<script>
  import Navbar from "../components/Navbar";
  import Construction from "../components/Construction";

  export default {
    name: "About",
    components: {
      Navbar, Construction
    },
  }
</script>

<style scoped>

</style>