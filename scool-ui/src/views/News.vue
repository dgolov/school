<template>
  <div id="news">
    <navbar></navbar>
    <construction></construction>
  </div>
</template>

<script>
import Navbar from "../components/Navbar";
import Construction from "../components/Construction";

export default {
  name: "News",
  components: {
    Navbar, Construction
  },
}
</script>

<style scoped>

</style>