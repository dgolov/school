<template>
  <div id="profile">
    <div class="cabinet-page">
      <div class="container">
        <button @click="openProfileMenu" class="cabinet-menu-button">МЕНЮ ЛИЧНОГО КАБИНЕТА</button>
        <div class="row">
          <profile-menu :header="header"></profile-menu>
          <div class="col-xl-10 col-lg-9">
            <div class="cabinet-content">
              <h3 class="system-color mb-4">Создание новой беседы.</h3>
              <hr/>
              <div>
                <p>Выберите участников</p>
                <div class="row">
                  <div class="col-md-9 mb-3">
                  </div>
                </div>
                <div class="form-check friends-block">
                  <div v-for="friend in responseData.friends" class="my-3 py-2 row_list">
                    <input class="form-check-input " type="checkbox" :id="friend.profile_id" :value="friend.profile_id" v-model="participants">
                    <label :for="friend.profile_id">
                      {{ friend.first_name }} {{ friend.last_name }}
                    </label>
                    <img :src="getAvatarPath(friend)" class="avatar">
                  </div>
                </div>
                <hr />
                <div class="row">
                  <div class="col-md-9">
                    <form>
                      <input class="w-100" type='text' placeholder="Введите название беседы" v-model="name">
                    </form>
                  </div>
                  <div class="col-md-3">
                    <button class="btn gray-button filter-button" @click="createGroupChat">Создать</button>
                  </div>
                </div>
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
  </div>
</template>


<script>
import Navbar from "../../components/Navbar";
import ProfileMenu from "../../components/Profile/ProfileMenu";
import {requestsMixin} from "../../components/mixins/requestsMixin";
import {redirect} from "../../components/mixins/redirect";
import axios from "axios";
import {groupChatMixin} from "../../components/mixins/groupChatMixin";
import {openMenu} from "../../components/mixins/openMenu";

export default {
  title: 'Академия будущего | Личный кабинет',
  name: "CreateGroupChat",

  data() {
    return {
      name: '',
      participants: [this.$store.state.profileInfo.id],
      header: 'Chats',
    }
  },

  components: {
    Navbar, ProfileMenu
  },

  created() {
    this.createGetRequest(
        `/profile/${String(this.$store.getters.getProfileInfo.id)}/friends/`
    )
  },

  mixins: [
      requestsMixin, redirect, groupChatMixin, openMenu
  ],

  methods: {
    async createGroupChat() {
      let data = {
        "name": this.name,
        "participants": this.participants
      }
      const axiosInstance = axios.create(this.base);
      await axiosInstance({
        url: `/create-group-dialog/`,
        method: "post",
        data: data
      })
          .then(() => {
            this.goTo('Chats')
          })
          .catch((error) => {
            if (error.request.status === 401) {
              // Если 401 ошибка - токен просрочен, обновляем его и заново запрашиваем данные
              this.refreshToken();
              this.addFriend('/profile/friend-request/');
            } else {
              console.log(error.request);
            }
          })
    },
  },
}
</script>


<style scoped>
.avatar {
  width: 30px;
  height: 30px;
  border-radius: 50%;
  float: right;
  margin-top: 5px;
  margin-right: 20px;
}

.friends-block {
  text-align: left;
  height: 40vh;
  overflow: scroll;
}
</style>