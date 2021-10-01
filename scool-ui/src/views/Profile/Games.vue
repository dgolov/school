<template>
  <div id="games">
    <navbar></navbar>
    <div class="step landing__section main-section">
      <div class="page">
        <div class="container mt-5">
          <div class="page__inner">
            <profile-menu :header="header"></profile-menu>
            <div class="page__main">
              <p>Игры в разработке</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>


<script>
import Navbar from "../../components/Navbar";
import ProfileMenu from "../../components/Profile/ProfileMenu";

export default {
  name: "Games",

  components: {
    ProfileMenu, Navbar
  },

  data() {
    return {
      header: 'Игры',
    }
  },

}
</script>


<style scoped>

</style>