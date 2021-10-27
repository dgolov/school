<template>
  <div id="settings">
    <navbar></navbar>
    <div class="step landing__section main-section">
      <div class="page">
        <div class="container mt-1">
          <div class="page__inner">
            <profile-menu :header="header"></profile-menu>
            <div class="container page__main">
              <p class="bold" style="color: gray">
                Для сохранения изменений данных профиля нажмите кнопку "Применить изменения внизу страницы"</p>
              <p class="bold" style="color: green">{{ successMessage }}</p>
              <button class="gray-button upload-photo-button" @click="showUploadModal">Изменить фото профиля</button>
              <upload-photo-modal ref="uploadModal" :mode="'avatar'" @reLoad="setSuccessMessage"></upload-photo-modal>
              <h3 class="system-color">Основные настройки</h3>
              <hr/>
              <settings-field :value="lastName" :label="'Фамилия'" @setValue="lastName = $event.value"></settings-field>
              <settings-field :value="firstName" :label="'Имя'" @setValue="firstName = $event.value"></settings-field>
              <settings-field :value="middleName" :label="'Отчество'" @setValue="middleName = $event.value"></settings-field>
              <div class="row row_list">
                <div class="col-name left-align">Дата рождения:</div>
                <div class="col-value left-align">{{ dateOfBirthDay }}</div>
                <div class="col-change">
                  <button class="system-color button-charge" @click="showForm">Изменить</button>
                </div>
                <date-picker v-if="showDateOfBirthDay" v-model="dateOfBirthDay" valueType="format" class="date-of-birthday-field">
                </date-picker>
              </div>
              <h3 class="system-color">Контактные данные</h3>
              <hr/>
              <settings-field :value="phone" :label="'Номер телефона'" @setValue="phone = $event.value"></settings-field>
              <settings-field :value="email" :label="'Электронная почта'" @setValue="email = $event.value"></settings-field>
              <settings-field :value="city" :label="'Город'" @setValue="city = $event.value"></settings-field>
              <settings-field :value="vkSlug" :label="'Профиль vk.com'" @setValue="vkSlug = $event.value"></settings-field>
              <settings-field :value="instagramSlug" :label="'Профиль instagram'" @setValue="instagramSlug = $event.value"></settings-field>
              <h3 class="system-color">Личная информация</h3>
              <hr/>
              <settings-field v-if="userGroup === 'student'" :value="hobbies" :label="'Увлечения'"
                              @setValue="hobbies = $event.value"></settings-field>
              <settings-field v-else-if="userGroup === 'teacher'" :value="education" :label="'Образование'"
                              @setValue="education = $event.value"></settings-field>
              <settings-field v-if="userGroup === 'student'" :value="dream" :label="'Мечта'"
                              @setValue="dream = $event.value"></settings-field>
              <settings-field v-else-if="userGroup === 'teacher'" :value="professionalActivity" :label="'Профессиональная деятельность'"
                              @setValue="professionalActivity = $event.value"></settings-field>
              <settings-field :value="about" :label="'О себе'" @setValue="about = $event.value"></settings-field>
              <button class="gray-button w-100 mt-4" @click="sendSettings">Применить изменения</button>
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
import DatePicker from "vue2-datepicker";
import 'vue2-datepicker/index.css';
import SettingsField from "../../components/Settings/SettingsField";
import axios from "axios";
import {requestsMixin} from "../../components/mixins/requestsMixin";
import {redirect} from "../../components/mixins/redirect";
import UploadPhotoModal from "../../components/Modal/UploadPhotoModal";

export default {
  name: "Settings",

  components: {
    SettingsField,
    SettingsChargeForm,
    ProfileMenu,
    Navbar,
    DatePicker,
    UploadPhotoModal
  },

  data() {
    return {
      header: 'Настройки',
      userGroup: null,
      firstName: null,
      lastName: null,
      middleName: null,
      dateOfBirthDay: null,
      showDateOfBirthDay: false,
      email: null,
      phone: null,
      city: null,
      vkSlug: null,
      instagramSlug: null,
      hobbies: null,
      dream: null,
      about: null,
      education: null,
      professionalActivity: null,
      successMessage: ''
    }
  },

  created() {
    this.lastName = this.$store.state.profileInfo.last_name
    this.firstName = this.$store.state.profileInfo.first_name
    this.middleName = this.$store.state.profileInfo.middle_name
    this.dateOfBirthDay = this.$store.state.profileInfo.date_of_birthday
    this.email = this.$store.state.profileInfo.email
    this.phone = this.$store.state.profileInfo.phone
    this.city = this.$store.state.profileInfo.city
    this.vkSlug = this.$store.state.profileInfo.vk_slug
    this.instagramSlug = this.$store.state.profileInfo.instagram_slug
    this.userGroup = this.$store.state.profileInfo.user_group
    this.about = this.$store.state.profileInfo.about
    if (this.userGroup === 'student') {
      this.hobbies = this.$store.state.profileInfo.hobbies
      this.dream = this.$store.state.profileInfo.dream
    } else if (this.userGroup === 'teacher') {
      this.education = this.$store.state.profileInfo.education
      this.professionalActivity = this.$store.state.profileInfo.professional_activity
    }
  },

  mixins: [requestsMixin, redirect],

  methods: {
    showForm() {
      this.showDateOfBirthDay = !this.showDateOfBirthDay;
    },

    showUploadModal() {
      // Показать окно загрузки изображения
      this.$refs.uploadModal.show = true
    },

    getData(){
      let data = {
        "first_name": this.firstName,
        "middle_name": this.middleName,
        "last_name": this.lastName,
        "email": this.email,
        "phone": this.phone,
        "city": this.city,
        "vk_slug": this.vkSlug,
        "instagram_slug": this.instagramSlug,
        "about": this.about,
        "date_of_birthday": this.dateOfBirthDay
      }
      if (this.$store.state.profileInfo.user_group === 'student') {
        data.hobbies = this.hobbies;
        data.dream = this.dream;
      }  else if (this.$store.state.profileInfo.user_group === 'teacher') {
        data.education = this.education;
        data.professionalActivity = this.professionalActivity;
      }
      return data;
    },

    async sendSettings(){
      let data = this.getData()
      const axiosInstance = axios.create(this.base);
      await axiosInstance({
        url: `/profile/${this.$store.state.profileInfo.id}/`,
        method: "put",
        data: data
      })
          .then(() => {
            this.goTo('Profile', {id: this.$store.state.profileInfo.id})
          })
          .catch((error) => {
            if (error.request.status === 401) {
              // Если 401 ошибка - токен просрочен, обновляем его и заново запрашиваем данные
              this.refreshToken();
            } else {
              console.log(error.request);
            }
          })
    },

    setSuccessMessage() {
      this.successMessage = 'Фото профиля успешно изменено'
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
}

.col-change {
  width: 20%;
}

.button-charge {
  border: none;
  background: none;
  margin: 0;
  font-size: 14px;
  width: 100%;
}

.date-of-birthday-field {
  width: 100%;
  height: 40px;
  margin-top: 20px;
}
</style>