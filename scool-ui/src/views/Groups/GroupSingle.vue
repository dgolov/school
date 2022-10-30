<template>
  <div class="cabinet-page">
    <div class="container">
      <button class="cabinet-menu-button">МЕНЮ ЛИЧНОГО КАБИНЕТА</button>
      <div class="row">
        <profile-menu :header="header"></profile-menu>
        <div class="col-xl-10 col-lg-9">
          <div class="cabinet-content">
            <div class="user-info">
              <div class="top-info">
<!--                <div><img src="img/avatar4.png"></div>-->
                <div>
                  <div class="name">
                    <span>{{ responseData.name }}</span>
                  </div>
                  <div class="counts">
                    <div class="count">
                      <span>{{ responseData.students.length }}</span>
                      Студенты
                    </div>
                    <div class="count">
                      <span>{{ responseData.teachers.length }}</span>
                      Преподаватели
                    </div>
                    <div class="count">
                      <span>0</span>
                      Фотографии
                    </div>
                  </div>
                </div>
              </div>
              <div class="item">
                <p>Описание:</p>
                <div class="text">
                  Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum mattis urna risus, ac tempus massa tempus et. Nunc blandit commodo ante, vel varius lacus bibendum ut. Praesent tincidunt sodales felis, sit amet commodo justo tincidunt id. Aliquam dignissim est quis feugiat commodo. Integer feugiat faucibus mi, vitae dapibus augue euismod sit amet. Cras eget aliquet urna. Nulla et nisi eu nisl tempus convallis vel dictum nisi. Mauris condimentum velit iaculis volutpat consequat. Ut neque mi, placerat non quam eu, suscipit pretium eros. Pellentesque at laoreet augue.
                </div>
              </div>
            </div>
            <div class="users">
              <div class="flex">
                <div class="top-text">
                  Студенты <span>{{ responseData.students.length }}</span>
                </div>
                <a href="#" class="top-link" v-if="responseData.students.length > 9 ">Все студенты</a>
              </div>
              <div class="flex">
                <div class="item" v-for="student in responseData.students.slice(0, 9)">
                  <img v-if="student.avatar" class="profile-avatar left" :src="`${student.avatar.image}`">
                  <img v-else src="../../assets/images/avatars/mike2.jpeg" class="profile-avatar left">
                  <p>{{ student.first_name }} {{ student.last_name }}</p>
                </div>
              </div>
            </div>
            <div class="teachers">
              <div class="flex">
                <div class="top-text">
                  Преподаватели <span>{{ responseData.teachers.length }}</span>
                </div>
                <a href="#" class="top-link" v-if="responseData.teachers.length > 9 ">Все преподаватели</a>
              </div>
              <div class="flex">
                <div class="item" v-for="teacher in responseData.teachers.slice(0, 9)">
                  <img v-if="teacher.avatar" class="profile-avatar left" :src="`${teacher.avatar.image}`">
                  <img v-else src="../../assets/images/avatars/mike2.jpeg" class="profile-avatar left">
                  <p>{{ teacher.first_name }} {{ teacher.last_name }}</p>
                </div>
              </div>
            </div>
<!--            <div class="media">-->
<!--              <div class="flex">-->
<!--                <div class="top-text">-->
<!--                  Фотоальбомы <span>6</span>-->
<!--                </div>-->
<!--                <a href="#" class="top-link">Все фотографии</a>-->
<!--              </div>-->
<!--              <div class="list">-->
<!--                <div class="item">-->
<!--                  <img src="img/media.png">-->
<!--                  <div class="flex">-->
<!--                    <div>Название альбома</div>-->
<!--                    <div>12</div>-->
<!--                  </div>-->
<!--                </div>-->
<!--                <div class="item">-->
<!--                  <img src="img/media.png">-->
<!--                  <div class="flex">-->
<!--                    <div>Название альбома</div>-->
<!--                    <div>12</div>-->
<!--                  </div>-->
<!--                </div>-->
<!--                <div class="item">-->
<!--                  <img src="img/media.png">-->
<!--                  <div class="flex">-->
<!--                    <div>Название альбома</div>-->
<!--                    <div>12</div>-->
<!--                  </div>-->
<!--                </div>-->
<!--                <div class="item">-->
<!--                  <img src="img/media.png">-->
<!--                  <div class="flex">-->
<!--                    <div>Название альбома</div>-->
<!--                    <div>12</div>-->
<!--                  </div>-->
<!--                </div>-->
<!--                <div class="item">-->
<!--                  <img src="img/media.png">-->
<!--                  <div class="flex">-->
<!--                    <div>Название альбома</div>-->
<!--                    <div>12</div>-->
<!--                  </div>-->
<!--                </div>-->
<!--              </div>-->
<!--            </div>-->
<!--            <div class="media">-->
<!--              <div class="flex">-->
<!--                <div class="top-text">-->
<!--                  Видео <span>2</span>-->
<!--                </div>-->
<!--                <a href="#" class="top-link">Все видео</a>-->
<!--              </div>-->
<!--              <div class="list">-->
<!--                <div class="item">-->
<!--                  <img src="img/media2.png">-->
<!--                  <div class="flex">-->
<!--                    <div></div>-->
<!--                    <div>13:24</div>-->
<!--                  </div>-->
<!--                </div>-->
<!--                <div class="item">-->
<!--                  <img src="img/media2.png">-->
<!--                  <div class="flex">-->
<!--                    <div></div>-->
<!--                    <div>13:24</div>-->
<!--                  </div>-->
<!--                </div>-->
<!--              </div>-->
<!--            </div>-->
          </div>
<!--          <div class="cabinet-content other">-->
<!--            <div class="user-info">-->
<!--              <div class="top-info small">-->
<!--                <div><img src="img/avatar5.png"></div>-->
<!--                <div>-->
<!--                  <div class="name">-->
<!--                    <span>Название группы</span>-->
<!--                    дата записи-->
<!--                  </div>-->
<!--                </div>-->
<!--              </div>-->
<!--            </div>-->
<!--            <div class="media">-->
<!--              <div class="list">-->
<!--                <div class="item">-->
<!--                  <img src="img/media.png">-->
<!--                </div>-->
<!--                <div class="item">-->
<!--                  <img src="img/media.png">-->
<!--                </div>-->
<!--              </div>-->
<!--              <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum mattis urna risus, ac tempus massa tempus et. Nunc blandit commodo ante, vel varius lacus bibendum ut. Praesent tincidunt sodales felis, sit amet commodo justo tincidunt id. Aliquam dignissim est quis feugiat commodo. Integer feugiat faucibus mi, vitae dapibus augue euismod sit amet. Cras eget aliquet urna. Nulla et nisi eu nisl tempus convallis vel dictum nisi. Mauris condimentum velit iaculis volutpat consequat. Ut neque mi, placerat non quam eu, suscipit pretium eros. Pellentesque at laoreet augue.</p>-->
<!--              <a class="like">322</a>-->
<!--            </div>-->
<!--          </div>-->
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
</template>


<script>
import Navbar from "../../components/Navbar";
import ProfileMenu from "../../components/Profile/ProfileMenu";
import GroupSearch from "../../components/Groups/GroupSearch";
import SingleGroupHeader from "../../components/Groups/SingleGroupHeader";
import ProfilesList from "../../components/Profile/ProfilesList";
import {requestsMixin} from "../../components/mixins/requestsMixin";
import {redirect} from "../../components/mixins/redirect";
import {friendMixin} from "../../components/mixins/friendMixin";

export default {
  title: 'Академия будущего | Личный кабинет',
  name: "GroupSingle",

  components: {
    Navbar, ProfileMenu, GroupSearch, SingleGroupHeader, ProfilesList,
  },

  data() {
    return {
      header: 'Группы'
    }
  },

  props: {
    id: String,
  },

  mixins: [requestsMixin, redirect, friendMixin],

  created() {
    this.createGetRequest(`/groups/${this.id}/`)
  },
}
</script>


<style scoped>
.profile-avatar {
  display: block;
  width: 50%;
  border: 0;
  border-radius: 50%;
  margin: 0 auto;
  text-align: center;
}
</style>