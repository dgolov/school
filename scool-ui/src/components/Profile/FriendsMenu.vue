<template>
  <div class="row my-3">
    <div class="col-md-6">
      <a href="#" @click="goTo('Friends', {id: $store.state.authUser.id})">Все друзья</a>
    </div>
    <div class="col-md-6">
      <a href="#" @click="goTo('FriendRequests')">Заявки в друзья</a>
      <!--                  <div class="notification_numbers">1</div>-->
    </div>
  </div>
</template>

<script>
import {redirect} from "../mixins/redirect";

export default {
  name: "FriendsMenu",

  mixins: [redirect],
}
</script>

<style scoped>

</style>