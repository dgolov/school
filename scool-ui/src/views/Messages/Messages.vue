<template>
  <div id="messages">
    <navbar></navbar>
    <div class="step landing__section main-section">
      <div class="page">
        <div class="container mt-5">
          <div class="page__inner">
            <profile-menu :header="header"></profile-menu>
            <div class="page__main">
              <div class="row">
                <div class="chat_header px-4" v-if="responseData.length > 0">
                  <a v-if="responseData && !responseData[0].dialog.is_group" href="#" class="pt-3"
                     @click="goTo('Profile', {id: getUserId(responseData[0].dialog)})">
                    {{ getChatName(responseData[0].dialog) }}
                  </a>
                  <a v-else-if="responseData && responseData[0].dialog.is_group" href="#" class="pt-3">
                    {{ getChatName(responseData[0].dialog) }}
                  </a>
                  <img v-if="responseData" :src="getChatImage(responseData[0].dialog)" class="chat-avatar">
                  <a href="#" v-if="responseData[0].dialog.is_group" class="group_chat_settings"
                     @click="goTo('GroupChatSettings', { dialog: responseData[0].dialog})">
                    Настройка беседы
                  </a>
                </div>
              </div>
              <hr/>
              <div id="messenger">
                <div v-for="(message, index) in responseData" :class="setClassToMessageArea(message)" :key="index">
                  <p v-if="!message.system_message" :class="setClassToMessageDate(message)">
                    {{ message.from_user.first_name }} {{ message.from_user.last_name }}
                    {{ reformatDateTime(message.date_and_time) }}
                  </p>
<!--                  <p v-else :class="setClassToMessageDate(message)">-->
<!--                    {{ reformatDateTime(message.date_and_time) }}-->
<!--                  </p>-->
                  <a href="#">
                    <img v-if="getMessageAvatar(message)" :src="getAvatarPath(message)" class="message_avatar">
                  </a>
                  <p v-if="message" :class="setClassToMessageText(message)">{{ message.text }}</p>
                </div>
              </div>
              <hr/>
              <div class="row">
                <div class="col-md-9">
                  <form>
                    <input v-model="input_text" id='input_text' type='text'
                           placeholder="Введите сообщение..." class="w-100">
                  </form>
                </div>
                <div class="col-md-3">
                  <button class="gray-button" style="height: 68%;" @click="sendMessage()">
                    Отправить
                  </button>
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
import {getDateTime} from "../../components/mixins/getDateTime";
import {dialogMixin} from "../../components/mixins/dialogMixin";
import axios from "axios";

export default {
  name: "Messages",

  components: {
    Navbar, ProfileMenu
  },

  data() {
    return {
      header: 'Сообщения',
      in_message_date: 'in_message_date',
      in_message: 'in_message',
      in_message_text: 'in_message_text',
      out_message_date: 'out_message_date',
      out_message: 'out_message',
      out_message_text: 'out_message_text',
      out_message_didnt_read: 'out_message_didnt_read',
      systemMessage: 'system_message',
      systemMessageText: 'system_message_text',
      containerScrollHeight: 0,
      input_text: ""
    }
  },

  props: {
    id: String
  },

  mixins: [requestsMixin, redirect, getDateTime, dialogMixin],

  created() {
    this.createGetRequest(`/dialogs/${String(this.id)}/`)
  },

  updated() {
    this.scrollMessageList()
  },

  methods: {
    getAvatarPath(message){
      let path = ''
      try {
        path = `http://127.0.0.1:8000${message.from_user.avatar.image}`;
      } catch {
        path = require('../../assets/images/avatars/mike2.jpeg');
      }
      return path;

    },

    sendMessage() {
      if (!this.input_text) {
        return 0
      }
      //TODO send message to server and parse now date and time
      let now = new Date()
      let data = {
        "from_user": {
          "id": this.$store.state.authUser.id,
          "first_name": this.$store.state.authUser.first_name,
          "last_name": this.$store.state.authUser.last_name,
        },
        "attachment": null,
        "text": this.input_text,
        "date_and_time": '2021-09-11T15:58:22.341424Z',
        "is_read": false
      }
      this.responseData.push(data)
      this.sendToServer()
    },

    async sendToServer(){
      let data = {
        "dialog": Number(this.id),
        "text": this.input_text
      }
      const axiosInstance = axios.create(this.base);
      await axiosInstance({
        url: `/send-message/`,
        method: "post",
        data: data
      })
          .then(() => {
            this.input_text = '';
            this.scrollMessageList()
          })
          .catch((error) => {
            if (error.request.status === 403 && error.request.responseText === this.errorAccessToken) {
              // Если 403 ошибка - токен просрочен, обновляем его и заново запрашиваем данные
              this.refreshToken();
              this.sendToServer('/send-message/');
            } else {
              console.log(error.request);
            }
          })
    },

    setClassToMessageArea(message) {
      if (message.system_message) {
        return this.systemMessage
      }
      if (message.from_user.id === this.$store.state.authUser.id) {
        if (message.is_read) {
          return this.out_message;
        } else {
          return this.out_message_didnt_read;
        }
      } else {
        return this.in_message;
      }
    },

    setClassToMessageDate(message) {
      if (message.from_user.id === this.$store.state.authUser.id) {
        return this.out_message_date;
      } else {
        return this.in_message_date;
      }
    },

    setClassToMessageText(message) {
      if (message.system_message) {
        return this.systemMessageText;
      }
      if (message.from_user.id === this.$store.state.authUser.id) {
        return this.out_message_text;
      } else {
        return this.in_message_text;
      }
    },

    getMessageAvatar(message) {
      if (message.system_message) {
        return false;
      }
      return message.from_user.id !== this.$store.state.authUser.id;
    },

    scrollMessageList() {
      // Прокрутка окна диалога вниз при загрузке страницы или при отправке сообщения
      if (this.responseData.length > 0) {
        setTimeout(() => {
          let div = document.getElementById('messenger')
          div.scrollTop = div.scrollHeight;
        });
      }
    }
  }
}
</script>


<style scoped>
#messenger {
  text-align: left;
  height: 70vh;
  overflow: scroll;
  padding-bottom: 30px;
  margin: 0;
}

.out_message {
  width: 100%;
  display: block;
  float: right;
}

.in_message {
  width: 100%;
  display: block;
  float: left;
}

.out_message_date {
  width: 100%;
  font-size: 12px;
  margin: 0;
  color: gray;
  text-align: right;
  padding-right: 10px;
}

.in_message_date {
  float: left;
  width: 100%;
  font-size: 12px;
  margin: 0;
  color: gray;
  padding-left: 5px;
}

.out_message_didnt_read {
  min-height: 50px;
  width: 100%;
  display: block;
  float: right;
  background-color: #e5ebf1;
}

.in_message_didnt_read {
  min-height: 50px;
  width: 100%;
  display: block;
  float: left;
  background-color: #e5ebf1;
}

.system_message {
  text-align: center;
  padding: 10px;
  width: auto;
}

.out_message_text {
  background-color: #bfe2e9;
  padding: 10px;
  border-radius: 10px;
  width: auto;
  float: right;
  margin: 0 10px 8px 50px;
}

.in_message_text {
  background-color: #fccdac;
  padding: 10px;
  border-radius: 10px;
  width: auto;
  float: left;
  margin: 0 60px 8px 5px;
}

.system_message_text {
  color: gray;
  font-size: 14px;
  width: auto;
}

.chat_header {
  width: 100%;
  text-align: left;
  font-size: 18px;
}

.chat-avatar {
  width: 50px;
  height: 50px;
  border-radius: 50%;
  float: right;
}

.message_avatar {
  width: 30px;
  height: 30px;
  border-radius: 50%;
  float: left;
  margin-top: 5px;
}

.group_chat_settings {
  display: block;
  left: 0;
  bottom: 0;
  color: gray;
  font-size: 12px;
}
</style>