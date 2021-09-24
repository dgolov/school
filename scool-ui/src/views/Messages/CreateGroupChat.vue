<template>
  <div id="create-group-chat">
    <navbar></navbar>
    <div class="step landing__section main-section">
      <div class="page">
        <div class="container mt-5">
          <div class="page__inner">
            <profile-menu :header="header"></profile-menu>
            <div class="page__main">
              <h3 class="system-color mb-4">Создание новой беседы.</h3>
              <hr/>
              <div>
                <p>Выберите участников</p>
                <div class="row">
                  <div class="col-md-9">
                    <form>
                      <input type='text' placeholder="Поиск" class="w-100">
                    </form>
                  </div>
                  <div class="col-md-3">
                    <button class="gray-button filter-button">Фильтр</button>
                  </div>
                </div>
                <div style="text-align: left; height: 40vh;">
                  <div v-for="friend in responseData.friends" class="my-3 py-2"
                       style="border-bottom: 2px solid #f7f7f7;">
                    <input type="checkbox" :id="friend.profile_id" :value="friend.profile_id" v-model="participants">
                    <label :for="friend.profile_id">
                      {{ friend.first_name }} {{ friend.last_name }}
                    </label>
                    <img :src="friend.avatar" style="float: right">
                  </div>
                </div>
                <hr />
                <div class="row">
                  <div class="col-md-9">
                    <form>
                      <input type='text' placeholder="Введите название беседы" class="w-100" v-model="name">
                    </form>
                  </div>
                  <div class="col-md-3">
                    <button class="gray-button filter-button" @click="createGroupChat">Создать</button>
                  </div>
                </div>
              </div>
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

export default {
  name: "CreateGroupChat",

  data() {
    return {
      name: '',
      participants: [this.$store.state.profileInfo.id]
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

  mixins: [requestsMixin, redirect],

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
            if (error.request.status === 403 && error.request.responseText === this.errorAccessToken) {
              // Если 403 ошибка - токен просрочен, обновляем его и заново запрашиваем данные
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

</style>