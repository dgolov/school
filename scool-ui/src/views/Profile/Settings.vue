<template>
  <div id="settings">
    <navbar></navbar>
    <div class="step landing__section main-section">
      <div class="page">
        <div class="container mt-5">
          <div class="page__inner">
            <profile-menu :header="header"></profile-menu>
            <div class="container page__main">
              <h3 class="system-color">Основные настройки</h3>
              <hr/>
              <div class="row row_list">
                <div class="col-name left-align">Фамилия:</div>
                <div class="col-value left-align">{{ lastName }}</div>
                <div class="col-change">
                  <button class="system-color button-charge" @click="showForm('LastNameForm')">
                    Изменить
                  </button>
                </div>
                <settings-charge-form v-if="showLastNameForm" @setValue="setLastName"></settings-charge-form>
              </div>
              <div class="row row_list">
                <div class="col-name left-align">Имя:</div>
                <div class="col-value left-align">{{ firstName }}</div>
                <div class="col-change">
                  <button class="system-color button-charge" @click="showForm('FirstNameForm')">
                    Изменить
                  </button>
                </div>
                <settings-charge-form v-if="showFirstNameForm" @setValue="setFirstName"></settings-charge-form>
              </div>
              <div class="row row_list">
                <div class="col-name left-align">Отчество:</div>
                <div class="col-value left-align">{{ middleName }}</div>
                <div class="col-change">
                  <button class="system-color button-charge" @click="showForm('MiddleNameForm')">
                    Изменить
                  </button>
                </div>
                <settings-charge-form v-if="showMiddleNameForm" @setValue="setMiddleName"></settings-charge-form>
              </div>
              <div class="row">
                <div class="col-name left-align">Дата рождения:</div>
                <div class="col-value left-align">{{ dateOfBirthDay }}</div>
                <div class="col-change">
                  <button class="system-color button-charge" @click="showForm('DateOfBirthDay')">
                    Изменить
                  </button>
                </div>
                <date-picker v-if="showDateOfBirthDay" v-model="dateOfBirthDay"
                             valueType="format" class="date-of-birthday-field"></date-picker>
              </div>
              <hr/>
              <h3 class="system-color">Контактные данные</h3>
              <hr/>
              <div class="row row_list">
                <div class="col-name left-align">Номер телефона:</div>
                <div class="col-value left-align">{{ phone }}</div>
                <div class="col-change">
                  <button class="system-color button-charge" @click="showForm('PhoneForm')">
                    Изменить
                  </button>
                </div>
                <settings-charge-form v-if="showPhoneForm" @setValue="setPhone"></settings-charge-form>
              </div>
              <div class="row row_list">
                <div class="col-name left-align">Электронная почта:</div>
                <div class="col-value left-align">{{ email }}</div>
                <div class="col-change">
                  <button class="system-color button-charge" @click="showForm('EmailForm')">
                    Изменить
                  </button>
                </div>
                <settings-charge-form v-if="showEmailForm" @setValue="setEmail"></settings-charge-form>
              </div>
              <div class="row row_list">
                <div class="col-name left-align">Город:</div>
                <div class="col-value left-align">{{ city }}</div>
                <div class="col-change">
                  <button class="system-color button-charge" @click="showForm('CityForm')">
                    Изменить
                  </button>
                </div>
                <settings-charge-form v-if="showCityForm" @setValue="setCity"></settings-charge-form>
              </div>
              <div class="row row_list">
                <div class="col-name left-align">Профиль vk.com:</div>
                <div class="col-value left-align">{{ vkSlug }}</div>
                <div class="col-change">
                  <button class="system-color button-charge" @click="showForm('VkForm')">
                    Изменить
                  </button>
                </div>
                <settings-charge-form v-if="showVkForm" @setValue="setVkSlug"></settings-charge-form>
              </div>
              <div class="row">
                <div class="col-name left-align">Профиль instagram:</div>
                <div class="col-value left-align">{{ instagramSlug }}</div>
                <div class="col-change">
                  <button class="system-color button-charge" @click="showForm('InstagramForm')">
                    Изменить
                  </button>
                </div>
                <settings-charge-form v-if="showInstagramForm" @setValue="setInstagramSlug"></settings-charge-form>
              </div>
              <hr/>
              <h3 class="system-color">Личная информация</h3>
              <hr/>
              <div class="row row_list">
                <div class="col-name left-align">Увлечения:</div>
                <div class="col-value left-align">{{ hobbies }}</div>
                <div class="col-change">
                  <button class="system-color button-charge" @click="showForm('HobbiesForm')">
                    Изменить
                  </button>
                </div>
                <settings-charge-form v-if="showHobbiesForm" @setValue="setHobbies"></settings-charge-form>
              </div>
              <div class="row row_list">
                <div class="col-name left-align">Мечта:</div>
                <div class="col-value left-align">{{ dream }}</div>
                <div class="col-change">
                  <button class="system-color button-charge" @click="showForm('DreamForm')">
                    Изменить
                  </button>
                </div>
                <settings-charge-form v-if="showDreamForm" @setValue="setDream"></settings-charge-form>
              </div>
              <div class="row">
                <div class="col-name left-align">О себе:</div>
                <div class="col-value left-align">{{ about }}</div>
                <div class="col-change">
                  <button class="system-color button-charge" @click="showForm('AboutForm')">
                    Изменить
                  </button>
                </div>
                <settings-charge-form v-if="showAboutForm" @setValue="setAboutInfo"></settings-charge-form>
              </div>
              <hr />
              <button class="gray-button w-100">Применить изменения</button>
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
import SettingsChargeForm from "../../components/Profile/SettingsChargeForm";
import DatePicker from "vue2-datepicker";
import 'vue2-datepicker/index.css';

export default {
  name: "Settings",

  components: {
    SettingsChargeForm,
    ProfileMenu,
    Navbar,
    DatePicker,
  },

  data() {
    return {
      header: 'Настройки',
      firstName: '',
      showFirstNameForm: false,
      lastName: '',
      showLastNameForm: false,
      middleName: '',
      showMiddleNameForm: false,
      dateOfBirthDay: '',
      showDateOfBirthDay: false,
      email: '',
      showEmailForm: false,
      phone: '',
      showPhoneForm: false,
      city: '',
      showCityForm: false,
      vkSlug: '',
      showVkForm: false,
      instagramSlug: '',
      showInstagramForm: false,
      hobbies: '',
      showHobbiesForm: false,
      dream: '',
      showDreamForm: false,
      about: '',
      showAboutForm: false,
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
    this.hobbies = this.$store.state.profileInfo.hobbies
    this.dream = this.$store.state.profileInfo.dream
    this.about = this.$store.state.profileInfo.about
  },

  methods: {
    showForm(formName) {
      if (formName !== 'FirstNameForm') {
        this.showFirstNameForm = false;
      }
      if (formName !== 'LastNameForm') {
        this.showLastNameForm = false;
      }
      if (formName !== 'MiddleNameForm') {
        this.showMiddleNameForm = false;
      }
      if (formName !== 'DateOfBirthDay') {
        this.showDateOfBirthDay = false;
      }
      if (formName !== 'EmailForm') {
        this.showEmailForm = false;
      }
      if (formName !== 'PhoneForm') {
        this.showPhoneForm = false;
      }
      if (formName !== 'CityForm') {
        this.showCityForm = false;
      }
      if (formName !== 'VkForm') {
        this.showVkForm = false;
      }
      if (formName !== 'InstagramForm') {
        this.showInstagramForm = false;
      }
      if (formName !== 'HobbiesForm') {
        this.showHobbiesForm = false;
      }
      if (formName !== 'DreamForm') {
        this.showDreamForm = false;
      }
      if (formName !== 'AboutForm') {
        this.showAboutForm = false;
      }

      switch (formName) {
        case 'FirstNameForm': {
          this.showFirstNameForm = !this.showFirstNameForm;
          break;
        }
        case 'LastNameForm': {
          this.showLastNameForm = !this.showLastNameForm;
          break;
        }
        case 'MiddleNameForm': {
          this.showMiddleNameForm = !this.showMiddleNameForm;
          break;
        }
        case 'DateOfBirthDay': {
          this.showDateOfBirthDay = !this.showDateOfBirthDay;
          break;
        }
        case 'EmailForm': {
          this.showEmailForm = !this.showEmailForm;
          break;
        }
        case 'PhoneForm': {
          this.showPhoneForm = !this.showPhoneForm;
          break;
        }
        case 'CityForm': {
          this.showCityForm = !this.showCityForm;
          break;
        }
        case 'VkForm': {
          this.showVkForm = !this.showVkForm;
          break;
        }
        case 'InstagramForm': {
          this.showInstagramForm = !this.showInstagramForm;
          break;
        }
        case 'HobbiesForm': {
          this.showHobbiesForm = !this.showHobbiesForm;
          break;
        }
        case 'DreamForm': {
          this.showDreamForm = !this.showDreamForm;
          break;
        }
        case 'AboutForm': {
          this.showAboutForm = !this.showAboutForm;
          break;
        }
      }
    },

    setFirstName(data) {
      this.firstName = data.value
    },

    setLastName(data) {
      this.lastName = data.value
    },

    setMiddleName(data) {
      this.middleName = data.value
    },

    setEmail(data) {
      this.email = data.value
    },

    setPhone(data) {
      this.phone = data.value
    },

    setCity(data) {
      this.city = data.value
    },

    setVkSlug(data) {
      this.vkSlug = data.value
    },

    setInstagramSlug(data) {
      this.instagramSlug = data.value
    },

    setHobbies(data) {
      this.hobbies = data.value
    },

    setDream(data) {
      this.dream = data.value
    },

    setAboutInfo(data) {
      this.about = data.value
    },
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