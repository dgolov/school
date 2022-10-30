<template>
  <div class="cabinet-page">
    <div class="container">
      <button class="cabinet-menu-button">МЕНЮ ЛИЧНОГО КАБИНЕТА</button>
      <div class="row">
        <profile-menu :header="header"></profile-menu>
        <div class="col-xl-10 col-lg-9">
          <div class="cabinet-content">
            <div class="groups">
              <div class="flex">
                <div class="top-text">
                  Группы
                </div>
                <form>
                  <input type="text" placeholder="Поиск групп">
                  <button></button>
                </form>
              </div>
              <div v-for="group in responseData" class="item">
<!--                <div><img src="img/group.png"></div>-->
                <div>
                  <span>
                    <a @click="goTo('GroupSingle', {id: group.id})">{{ group.name }}</a>
                  </span>
                  {{ group.students.length }} участников
                  <a class="unsubscribe" @click="goTo('GroupSingle', {id: group.id})">
                    Подробнее
                  </a>
                </div>
              </div>
              <p v-if="responseData.length === 0" class="mt-5">Вы не состоите ни в одной группе</p>
            </div>
          </div>
        </div>
        <div class="col-xl-2 col-lg-3"></div>
        <div class="col-xl-10 col-lg-9">
          <div class="cabinet-copy">
            © Академия будущего «ХОД», 2022
          </div>
        </div>
      </div>
    </div>
  </div>
</template>


<script>
import Navbar from "../../components/Navbar";
import ProfileMenu from "../../components/Profile/ProfileMenu";
import GroupsHeader from "../../components/Groups/GroupsHeader";
import GroupSearch from "../../components/Groups/GroupSearch";
import {requestsMixin} from "../../components/mixins/requestsMixin";
import {redirect} from "../../components/mixins/redirect";

export default {
  title: 'Академия будущего | Личный кабинет',
  name: "MyGroups",

  components: {
    GroupsHeader, GroupSearch, Navbar, ProfileMenu
  },

  data() {
    return {
      header: 'Groups'
    }
  },

  mixins: [requestsMixin, redirect],

  created() {
    this.createGetRequest('/groups/')
  },
}
</script>


<style scoped>

</style>