<template>
  <div id="nav-login">
    <ul v-if="authenticated">
      <li>
        <a href="#" @click="goTo('Profile', {id: user.id})">{{ user.first_name }} {{ user.last_name }}</a>
      </li>
      <li>
        <img class="center avatar" :src="user.avatar.image">
      </li>
    </ul>
    <ul v-else>
      <li><a href="#" @click="goTo('SignUp')">Регистрация</a></li>
      <li><a href="#" @click="goTo('Auth')">Вход</a></li>
    </ul>
  </div>
</template>

<script>
import {redirect} from "./mixins/redirect";

export default {
  data() {
    return {
      user: this.$store.state.authUser,
      authenticated: this.$store.state.isAuthenticated,
    }
  },

  name: "NavLogin",

  mixins: [redirect],
}
</script>

<style scoped>
#nav-login {
  display: inline;
}

.avatar {
  display: inline-block;
  width: 30px;
  height: 30px;
  border: 0;
  border-radius: 50%;
  margin: auto;
  text-align: right;
}
</style>