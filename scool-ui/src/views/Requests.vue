<template>
<div class="requests">
  <Navbar></Navbar>
  <div class="container past-events">
    <h1 class="breadcrumb-title mb-5" v-if="purpose==='free_lesson'">Отправить заявку на бесплатный урок</h1>
    <h1 class="breadcrumb-title mb-5" v-if="purpose==='event'">Отправить заявку на мероприятие</h1>
    <h1 class="breadcrumb-title mb-5" v-else-if="purpose==='buy'">Отправить заявку на запись</h1>
    <h1 class="breadcrumb-title mb-5" v-else>Отправить заявку</h1>
    <h2 v-if="success" class="success mb-5">Ваша заявка отправлена!</h2>
    <form action="#" method="get" autocompelete="new-password" class="form" id="formLogin">
      <input class="input" v-model="request_fio" type="text" name="request_fio" placeholder="Введите ФИО..." required>
      <input class="input" v-model="request_phone" type="text" name="request_phone" placeholder="Введите номер теелефона..." required>
      <input class="input" v-model="request_email" type="text" name="request_email" placeholder="Введите email..." required>
      <textarea class="input" v-model="comment"  name="comment"
                placeholder="Комментарий..." required style="border-radius: 5px; padding: 10pt 20pt;"></textarea>
      <button type="button" class="button button__accent w-100" @click="send()">Отправить заявку</button>
    </form>
  </div>
</div>
</template>

<script>
import Navbar from "../components/Navbar";
import {requestsMixin} from "../components/mixins/requestsMixin";
import {redirect} from "../components/mixins/redirect";
import axios from "axios";

export default {
  name: "Requests",

  components: {Navbar},

  mixins: [requestsMixin, redirect],

  data() {
    return {
      student: null,
      request_fio: null,
      request_phone: null,
      request_email: null,
      purpose: localStorage.getItem('purpose'),
      comment: "",
      success: false
    }
  },

  props: {purpose: String, course: String},

  created() {
    if (this.purpose) {
      localStorage.setItem('purpose', this.purpose)
      localStorage.setItem('course', this.course)
    }
  },

  mounted() {
    this.purpose = localStorage.getItem('purpose')
  },

  methods: {
    async send() {
      let data = {
        student: this.$store.state.authUser.id,
        client: null,
        request_fio: this.request_fio,
        request_phone: this.request_phone,
        request_email: this.request_email,
        type_request: "online",
        status: "new",
        purpose: localStorage.getItem('purpose'),
        result: null,
        remind: null,
        date: "2022-01-07T16:55:43.151840+03:00",
        comment: this.comment,
        course: localStorage.getItem('course')
      }
      axios
          .post(`${this.$store.getters.getServerUrl}/requests/`, data)
          .then((response) => {
            this.success = true
            this.request_fio = null
            this.request_phone = null
            this.request_email = null
          });
    },
  }
}
</script>

<style scoped>
.success {
  background-color: #B8EFCF;
  padding: 10px;
}
</style>