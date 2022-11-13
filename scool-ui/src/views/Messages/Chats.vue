<template>
  <div id="profile">
    <div class="cabinet-page">
      <div class="container">
        <button @click="openProfileMenu" class="cabinet-menu-button">МЕНЮ ЛИЧНОГО КАБИНЕТА</button>
        <div class="row">
          <profile-menu :header="header"></profile-menu>
          <div class="col-xl-10 col-lg-9">
            <div class="cabinet-content">
              <div class="row mb-4">
                <div class="col-md-9">
                  <div class="list-name bold mb-4">Чаты</div>
                </div>
                <div class="col-md-3">
                  <button class="btn gray-button create-button;" @click="goTo('CreateGroupChat')"
                          @reLoad="createGetRequest('dialogs');">
                    Создать группу
                  </button>
                </div>
              </div>
              <div v-for="chat in responseData" :class="setClassFromChatArea(chat)" :id="chat.id"
                   @click="goTo('Messages', {id: chat.id})">
                <div class="row">
                  <div class="avatar-block">
                    <img :src="getChatImage(chat)" class="avatar-image">
                  </div>
                  <div class="dialog_info">
                    <div class="row">
                      <div class="dialog_name">
                        <a href="#">{{ getChatName(chat) }}</a>
                      </div>
                      <div v-if="chat.last_message" class="dialog_date">
                        {{ reformatDateTime(chat.last_message.date_and_time) }}
                      </div>
                    </div>
                    <div class="row">
                      <div :class="setClassFromLastMessageArea(chat)"
                           @click="goTo('Messages', {id: String(chat.id)})">
                        <a v-if="chat.last_message" href="#">{{ chat.last_message.text }}</a>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              <h6 v-if="responseData.length === 0" class="mt-5">Список сообщений пуст</h6>
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
import {getDateTime} from "../../components/mixins/getDateTime";
import {dialogMixin} from "../../components/mixins/dialogMixin";
import {openMenu} from "../../components/mixins/openMenu";

export default {
  title: 'Академия будущего | Личный кабинет',
  name: "Chats",

  data() {
    return {
      header: 'Chats',
      messagesAreaClass: 'messages_area',
      newMessagesAreaClass: 'new_messages_area',
      last_message_area_didnt_read: 'last_message_area_didnt_read',
      last_message_area: 'last_message_area'
    }
  },

  components: {
    Navbar, ProfileMenu
  },

  mixins: [
      requestsMixin, redirect, getDateTime, dialogMixin, openMenu
  ],

  created() {
    this.createGetRequest('/dialogs/');
  },

  methods: {
    setClassFromChatArea(chat) {
      if (!chat.last_message) {
        return this.messagesAreaClass;
      }
      if (chat.last_message.is_read) {
        return this.messagesAreaClass;
      } else {
        if (chat.last_message.from_user === this.$store.state.authUser.id) {
          return this.messagesAreaClass;
        }
        return this.newMessagesAreaClass;
      }
    },

    setClassFromLastMessageArea(chat) {
      if (!chat.last_message) {
        return this.last_message_area;
      }
      if (chat.last_message.is_read) {
        return this.last_message_area;
      } else {
        if (chat.last_message.from_user === this.$store.state.authUser.id) {
          return this.last_message_area_didnt_read;
        }
        return this.last_message_area;
      }
    },
  }
  ,
}
</script>

<style scoped>
.messages_area {
  border-bottom: 2px solid #f7f7f7;
  padding: 10px 5px;
  display: inline-block;
  height: 100px;
  width: 100%;
}

.messages_area:hover {
  border-bottom: 2px solid #f7f7f7;
  padding: 10px 5px;
  display: block;
  height: 100px;
  width: 100%;
  background-color: #e5ebf1;
  border-radius: 10px;
}

.new_messages_area {
  border-bottom: 2px solid #f7f7f7;
  padding: 10px 5px;
  display: block;
  height: 100px;
  width: 100%;
  background-color: #e5ebf1;
  border-radius: 10px;
}

.create-button {
  height: 68%;
}

.avatar-block {
  width: 20%;
}

.avatar-image {
  width: 75px;
  height: 75px;
  border-radius: 50%;
}

.dialog_info {
  width: 80%;
}

.dialog_name {
  width: 70%;
  text-align: left;
}

.dialog_date {
  width: 30%;
}

.last_message_area {
  width: 99%;
  text-align: left;
  padding: 10px;
  font-size: 14px;
  color: gray;
}

.last_message_area_didnt_read {
  width: 99%;
  text-align: left;
  padding: 10px;
  font-size: 14px;
  color: gray;
  background-color: #e5ebf1;
  border-radius: 10px;
}
</style>