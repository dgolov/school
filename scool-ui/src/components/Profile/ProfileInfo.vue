<template>
  <div v-if="profile" class="page__main">
    <div class="row">
      <div class="col-md-6">
        <h3 class="page__main__title left-align mb-2 center">
          {{ profile.last_name }} {{ profile.first_name }} {{ profile.middle_name }}
        </h3>
        <h6 v-if="profile.user_group === 'student'" class="center">Студент</h6>
        <h6 v-else-if="profile.user_group === 'teacher'" class="center">Преподаватель</h6>
        <h6 v-else-if="profile.user_group === 'manager'" class="center">Менеджер учебного процесса</h6>
        <hr/>
        <button v-if="profile.id === $store.state.authUser.id" class="gray-button">Редактировать профиль</button>
        <button v-if="isFriend(profile.user)" class="w-100"
                @click="removeFriend(profile, 'profile')">Удалить из друзей</button>
        <button v-else-if="isSubscription(profile.user)" class="w-100"
                @click="unsubscribe(profile, 'profile')">Отписаться</button>
        <button v-else-if="isFollower(profile.user)" class="w-100"
                @click="addFriendRequest(profile, 'profile')">Принять дружбу</button>
        <button v-else-if="profile.id !== $store.state.authUser.id" class="w-100"
                @click="addFriend(profile, 'profile')">Добавить в друзья
        </button>
        <a v-if="isFriend(profile.user)" href="#">
          <button class="w-100">Написать сообщение</button>
        </a>
      </div>
      <div class="col-md-6">
        <img v-if="profile.avatar" class="center profile-avatar"
             :src="`http://127.0.0.1:8000${profile.avatar.image}`">
        <img v-else src="../../assets/images/avatars/mike2.jpeg" class="center profile-avatar">
      </div>
    </div>
    <div v-if="isFriend(profile.user) || profile.id === $store.state.authUser.id" id="profile_info">
      <div class="row my-3">
        <div class="col-md-3">
          <a v-if="profile" href="#" class="profile-counters"
             @click="goTo('Friends', {id: profile.id})">
            {{ profile.friends.length }}
          </a>
          <h6>Друзья</h6>
        </div>
        <div class="col-md-3">
          <a v-if="profile" href="#" class="profile-counters"
             @click="goTo('Followers', {id: profile.id})">
            {{ profile.followers.length }}
          </a>
          <h6>Подписчики</h6>
        </div>
        <div class="col-md-3">
          <a v-if="profile" href="#" class="profile-counters"
             @click="goTo('Subscriptions', {id: profile.id})">
            {{ profile.friend_request_out.length }}
          </a>
          <h6>Подписки</h6>
        </div>
        <div class="col-md-3">
          <a href="#" @click="goTo('Photo', {id: profile.id})"
             class="profile-counters">{{ profile.photos.length }}</a>
          <h6>Фотографии</h6>
        </div>
      </div>
      <hr/>
      <div class="left-align mt-5">
        <div class="row my-3">
          <div class="col-md-3">
            <h6>День рождения:</h6>
          </div>
          <div class="col-md-9 left-align">
            <a href="#">{{ profile.date_of_birthday }}</a>
          </div>
        </div>
        <div class="row my-3">
          <div class="col-md-3">
            <h6>Пол:</h6>
          </div>
          <div class="col-md-9 left-align">
            <a v-if="profile.gender === 'm'" href="#">Мужской</a>
            <a v-else href="#">Женский</a>
          </div>
        </div>
        <hr/>
        <h3 class="mb-4">Контактная информация:</h3>
        <div class="row my-3">
          <div class="col-md-3">
            <h6>Телефон:</h6>
          </div>
          <div class="col-md-9 left-align">
            <a href="tel:+79082373971">{{ profile.phone }}</a>
          </div>
        </div>
        <div class="row my-3">
          <div class="col-md-3">
            <h6>Город:</h6>
          </div>
          <div class="col-md-9 left-align">
            <a v-if="profile.city" href="#">{{ profile.city }}</a>
            <p v-else class="my-0">-</p>
          </div>
        </div>
        <div class="row my-3">
          <div class="col-md-3">
            <h6>E-mail:</h6>
          </div>
          <div class="col-md-9 left-align">
            <a href="mailto:vanya_grishin@mail.ru">{{ profile.email }}</a>
          </div>
        </div>
        <div class="row my-3">
          <div class="col-md-3">
            <h6>Профиль vk.com:</h6>
          </div>
          <div class="col-md-9 left-align">
            <a v-if="profile.vk_slug" href="https://vk.com/piupiu7">{{ profile.vk_slug }}</a>
            <p v-else class="my-0">-</p>
          </div>
        </div>
        <div class="row mt-3 mb-4">
          <div class="col-md-3">
            <h6>Профиль Instagram:</h6>
          </div>
          <div class="col-md-9 left-align">
            <a v-if="profile.instagram_slug" href="#">{{ profile.instagram_slug }}</a>
            <p v-else class="my-0">-</p>
          </div>
        </div>
        <hr/>
        <h3 class="mb-4">Личная информация:</h3>
        <div class="row my-3">
          <div class="col-md-3">
            <h6>Увлечения:</h6>
          </div>
          <div class="col-md-9 left-align">
            <a v-if="profile.hobbies" href="#">{{ profile.hobbies }}</a>
            <p v-else class="my-0">-</p>
          </div>
        </div>
        <div class="row mt-3">
          <div class="col-md-3">
            <h6>Мечта:</h6>
          </div>
          <div class="col-md-9 left-align">
            <a v-if="profile.dream" href="#">{{ profile.dream }}</a>
            <p v-else class="my-0">-</p>
          </div>
        </div>
        <div class="row my-3 mb-4">
          <div class="col-md-3">
            <h6>О себе:</h6>
          </div>
          <div class="col-md-9 left-align ">
            <p v-if="profile.about" class="my-0">{{ profile.about }}</p>
            <p v-else class="my-0">-</p>
          </div>
        </div>
      </div>
    </div>
    <div v-else id="hide_profile_info">
      <div class="row my-3">
        <div class="center" style=" color: gray;">
          <img src="../../assets/images/icons/padlock.svg" class="padlock">
          <p class="mt-3">Для просмотра подробной информации добавьте пользователя в друзья.</p>
        </div>
      </div>
    </div>
  </div>
</template>


<script>
import {redirect} from "../mixins/redirect";
import {friendMixin} from "../mixins/friendMixin";
import {requestsMixin} from "../mixins/requestsMixin";
import axios from "axios";

export default {
  name: "ProfileInfo",

  props: ['profile'],

  mixins: [redirect, friendMixin, requestsMixin],
}
</script>


<style scoped>
.profile-avatar {
  display: block;
  width: 200px;
  height: 200px;
  border: 0;
  border-radius: 50%;
  margin: 30px auto;
  text-align: center;
}

.profile-counters {
  font-size: 20px;
  color: #4c28de;
}

.padlock {
  width: 30%;
}
</style>