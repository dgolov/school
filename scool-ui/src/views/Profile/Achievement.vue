<template>
  <div id="profile">
    <div class="cabinet-page">
      <div class="container">
        <button @click="openProfileMenu" class="cabinet-menu-button">МЕНЮ ЛИЧНОГО КАБИНЕТА</button>
        <div class="row">
          <profile-menu :header="header"></profile-menu>
          <div class="col-xl-10 col-lg-9">
            <div class="cabinet-content bg">
              <div class="rewards flex">
                <div v-if="achievementUserList.achievement" v-for="achievement in achievementList" class="item">
                  <img v-if="containsInUserList(achievement.id)"
                       :src="achievement.image_enable" :title="achievement.description">
                  <img v-else :src="achievement.image_disable" :title="achievement.description">
                </div>
              </div>
            </div>
          </div>
          <div v-if="isLoaded" class="col-xl-2 col-lg-3"></div>
          <loader v-else object="#63a9da" color1="#ffffff" color2="#17fd3d" size="5" speed="2" bg="#343a40"
                  objectbg="#999793" opacity="80" disableScrolling="false" name="spinning"></loader>
          <div class="col-xl-10 col-lg-9">
            <div class="cabinet-copy">
              © Академия будущего «ХОД», 2022
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import ProfileMenu from "../../components/Profile/ProfileMenu";
import {redirect} from "../../components/mixins/redirect";
import {requestsMixin} from "../../components/mixins/requestsMixin";
import {openMenu} from "../../components/mixins/openMenu";


export default {
  name: "Achievement",

  components: {
    ProfileMenu,
  },

  data() {
    return {
      header: 'Achievement',
      achievementList: [],
      achievementUserList: [],
    }
  },

  props: {
    id: String
  },

  created() {
    this.getData();
  },


  mixins: [
    redirect, requestsMixin, openMenu
  ],

  methods: {
    async getData() {
      this.achievementList = await this.createGetRequest(`/profile/achievement/`);
      this.achievementUserList = await this.createGetRequest(`/profile/${String(this.id)}/achievement/`);
    },

    containsInUserList(id) {
      for (let item of this.achievementUserList.achievement) {
        if (id === item) {
          return true;
        }
      }
      return false;
    },
  },
}
</script>

<style scoped>

</style>