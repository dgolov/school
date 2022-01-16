<template>
  <div id="groupChatSettings">
    <navbar></navbar>
    <div class="step landing__section main-section past-events">
      <div class="page">
        <div class="container mt-1">
          <div class="page__inner">
            <profile-menu :header="header"></profile-menu>
            <div class="container page__main">
              <div class="container">
                <div class="row">
                  <div class="col-md-10">
                    <div class="row"></div>
                    <div class="w-100">
                      <h1 style="text-align: left; margin: 0 25px;">{{ chatName }}</h1>
                    </div>
                    <div class="w-100">
                      <button class="system-color button-charge" @click="showForm('chatNameForm')">
                        Изменить название беседы
                      </button>
                    </div>
                  </div>
                  <div class="col-md-2">
                    <a href="#" @click="showUploadModal()">
                      <img v-if="dialog" :src="getChatImage(dialog)" class="chat-avatar">
                      <set-group-chat-image-modal ref="uploadModal" :id="id"
                                                  @reLoad="goTo('Messages', {id: id})">
                      </set-group-chat-image-modal>
                    </a>
                  </div>
                  <settings-charge-form v-if="showChatNameForm" @setValue="setChatName"></settings-charge-form>
                </div>
              </div>
              <hr/>
              <div v-if="showParticipants">
                <div class="pb-5 row_list">
                  <h3 style="display: inline; margin-top: 20px;">Участники беседы</h3>
                  <a href="#" class="system-color" style="float: right; font-size: 12px;" @click="showInviteArea()">
                    Пригласить новых участников
                  </a>
                </div>
                <div v-for="profile in participants" class="row row_list">
                  <div class="col-md-3 mt-3">
                    <img v-if="profile.avatar" class="center small_avatar"
                         :src="`${$store.getters.getServerUrl}${profile.avatar.image}`">
                    <img v-else class="center small_avatar" src="../../assets/images/avatars/mike2.jpeg">
                  </div>
                  <div class="col-md-5">
                    <h4 class="left-align">
                      <a href="#" @click="goTo('Profile', {id: profile.id})">
                        {{ profile.first_name }} {{ profile.last_name }}
                      </a>
                    </h4>
                    <p v-if="isGroupFounder(profile.id)" class="left-align group_founder_text">Основатель</p>
                    <h6 class="left-align"></h6>
                  </div>
                  <div class="col-md-4 left-align pt-4">
                    <div v-if="isFriend(profile.user)">
                      <button style="margin: 0; border: none; padding: 0; color: #000000;">
                        <img src="../../assets/images/icons/send-message.svg" class="friends_button">
                        Написать сообщение
                      </button>
                    </div>
                    <div v-if="isFriend(profile.user)">
                      <a href="#" @click="removeFriend(profile, 'user')">
                        <img src="../../assets/images/icons/delete.svg" class="friends_button">
                        Удалить из друзей
                      </a>
                    </div>
                    <div v-else-if="isFollower(profile.user)">
                      <a href="#" @click="addFriendRequest(profile, 'user')">
                        <img src="../../assets/images/icons/user_add.png" class="friends_button">
                        Принять дружбу
                      </a>
                    </div>
                    <div v-else-if="isSubscription(profile.user)">
                      <a href="#" @click="unsubscribe(profile, 'user')">
                        <img src="../../assets/images/icons/delete.svg" class="friends_button">
                        Отписаться
                      </a>
                    </div>
                    <div v-else-if="profile.user !== $store.state.authUser.user">
                      <a href="#" @click="addFriend(profile, 'user')">
                        <img src="../../assets/images/icons/user_add.png" class="friends_button">
                        Добавить в друзья
                      </a>
                    </div>
                  </div>
                </div>
              </div>
              <div v-if="showInvite">
                <div class="pb-5 row_list">
                  <h3 style="display: inline; margin-top: 20px;">Пригласить новых участников</h3>
                  <a href="#" class="system-color" style="float: right; font-size: 12px;"
                     @click="showParticipantsArea()">
                    Отмена
                  </a>
                </div>
                <div class="friends-block">
                  <div v-for="friend in responseData.friends" v-if="!isParticipant(friend)" class="my-3 py-2 row_list">
                    <input type="checkbox" :id="friend.profile_id" :value="friend.profile_id" v-model="inviteParticipants">
                    <label :for="friend.profile_id">
                      {{ friend.first_name }} {{ friend.last_name }}
                    </label>
                    <img :src="getAvatarPath(friend)" class="avatar">
                  </div>
                </div>
                <button class="gray-button filter-button" @click="sendInvites">Пригласить</button>
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
import SettingsChargeForm from "../../components/Settings/SettingsChargeForm";
import SetGroupChatImageModal from "../../components/Modal/SetGroupChatImageModal";
import {redirect} from "../../components/mixins/redirect";
import {friendMixin} from "../../components/mixins/friendMixin";
import {groupChatMixin} from "../../components/mixins/groupChatMixin";
import axios from "axios";

export default {
  name: "ChatSettings",

  components: {
    SettingsChargeForm,
    ProfileMenu,
    Navbar,
    SetGroupChatImageModal
  },

  data() {
    return {
      showChatNameForm: false,
      chatName: '',
      participants: [],
      inviteParticipants: [],
      showParticipants: true,
      showInvite: false,
      header: 'Сообщения'
    }
  },

  props: {
    id: String,
    dialog: Object,
  },

  mixins: [redirect, friendMixin, groupChatMixin],

  created() {
    if (!this.dialog) {
      this.goTo('Messages', {id: String(this.id)})
    }
    this.chatName = this.dialog.name
    this.participants = this.dialog.participants
    this.createGetRequest(
        `/profile/${String(this.$store.getters.getProfileInfo.id)}/friends/`
    )
  },

  methods: {
    showUploadModal() {
      // Показать окно загрузки изображения
      this.$refs.uploadModal.show = true
    },

    showForm(formName) {
      // Отображает блок настроек
      if (formName !== 'chatNameForm') {
        this.showChatNameForm = false;
      }
      switch (formName) {
        case 'chatNameForm': {
          this.showChatNameForm = !this.showChatNameForm;
          break;
        }
      }
    },

    showInviteArea() {
      // Отображает блок для приглашения новых участников
      this.showParticipants = false;
      this.showInvite = true;
    },

    showParticipantsArea(){
      // Отображает блок с текущими участниками беседы
      this.showParticipants = true;
      this.showInvite = false;
    },

    async setChatName(data) {
      // Изменяет имя чата и отправляет данные на сервер
      this.chatName = data.value;

      const axiosInstance = axios.create(this.base);
      await axiosInstance({
        url: `/update-group-chat/${this.id}/`,
        method: "put",
        data: {
          "name": this.chatName
        }
      })
          .then(() => {
            this.showChatNameForm = false;
          })
          .catch((error) => {
            if (error.request.status === 401) {
              // Если 403 ошибка - токен просрочен, обновляем его и заново запрашиваем данные
              this.refreshToken();
              this.addFriend('/profile/friend-request/');
            } else {
              console.log(error.request);
            }
          })
    },

    getChatImage(chat) {
      let path = '';
      if (chat.image) {
        path = chat.image.file;
      } else {
        path = require('../../assets/images/group_chat.png');
      }

      return path;
    },

    isGroupFounder(profileId) {
      // Проверяет является ли пользователь основателем беседы
      return profileId === this.dialog.group_founder;
    },

    isParticipant(user) {
      // Проверяет состоит ли пользователь в данной беседе, если состоит то не отображаем его в списке для приглашений
      for (let participant of this.participants) {
        if (user.profile_id === participant.id) {
          return true;
        }
      }
      return false
    },

    async sendInvites() {
      let data = {
        "id": this.dialog.id,
        "users": this.inviteParticipants
      }
      const axiosInstance = axios.create(this.base);
      await axiosInstance({
        url: `/create-group-dialog/`,
        method: "put",
        data: data
      })
          .then(() => {
            this.goTo('Messages', {id: String(this.id)})
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
    }
  },
}
</script>


<style scoped>
.col-name {
  margin-top: 10px;
  color: gray;
  width: 30%;
}

.col-value {
  margin-top: 10px;
  width: 50%;
  font-weight: 600;
}

.col-change {
  width: 20%;
}

.button-charge {
  border: none;
  background: none;
  margin: 0;
  font-size: 12px;
  display: block;
  float: left;
}

.chat-avatar {
  width: 80px;
  height: 80px;
  border-radius: 50%;
}

.friends_button {
  width: 15px;
  margin-right: 5px;
}

.group_founder_text {
  font-size: 12px;
  color: gray;
}

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