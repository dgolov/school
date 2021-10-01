<template>
  <div v-if="responseData" id="photo">
    <navbar></navbar>
    <div class="step landing__section main-section">
      <div class="page">
        <div class="container mt-5">
          <div class="page__inner">
            <profile-menu :header="header"></profile-menu>
            <div class="page__main">
              <div class="col-md-12">
                <div>
                  <button v-if="Number(id) === $store.state.authUser.id"
                          class="gray-button upload-photo-button"
                          @click="showUploadModal">Загрузить фото</button>
                  <upload-photo-modal ref="uploadModal"
                                      @reLoad="createGetRequest(`/profile/${id}/gallery/`)"></upload-photo-modal>
                </div>
              </div>
              <div class="image-container" v-if="responseData.photos">
                <div v-for="photo in responseData.photos" class="mySlides">
                  <button class="photo-button" v-if="Number(id) === $store.state.authUser.id && responseData"
                          id="set-avatar" @click="setAvatar(responseData.photos[slideIndex - 1].id)">
                    Установить как фото профиля</button>
                  <div class="number_text">{{ slideIndex }} / {{ responseData.photos.length }}</div>
                  <img :src="photo.image" class="image" @dblclick="like()">
                </div>
                <a class="prev" @click="plusSlides(-1)">&#10094;</a>
                <a class="next" @click="plusSlides(1)">&#10095;</a>
                <div class="caption-container">
                  <a v-if="responseData.photos" @click="like()"><img :src="likeImage" class="like_image"></a>
                  <p v-if="responseData.photos"
                     id="like_count">
                    {{ responseData.photos[slideIndex - 1].likes.length }}</p>
                  <button class="photo-button"
                          v-if="Number(id) === $store.state.authUser.id"
                          id="delete"
                          @click="showDeleteModal()">Удалить
                  </button>
                  <delete-photo-modal v-if="responseData.photos" ref="deleteModal"
                                      :id="responseData.photos[slideIndex - 1].id"
                                      @reLoad="createGetRequest(`/profile/${id}/gallery/`)"></delete-photo-modal>
                  <button class="photo-button" v-if="Number(id) === $store.state.authUser.id" id="edit"
                          @click="showEditModal()">Редактировать</button>
                  <edit-photo-modal v-if="responseData.photos" ref="editModal"
                                    :id="responseData.photos[slideIndex - 1].id"
                                    @reLoad="createGetRequest(`/profile/${id}/gallery/`)">
                  </edit-photo-modal>
                </div>
                <div class="description-container">
                  <p id="caption" class="py-2"></p>
                </div>
                <div class="row mt-2">
                  <div v-for="(photo, index) in responseData.photos" class="column">
                    <img class="demo cursor" :src="photo.image"
                         @click="currentSlide(index + 1)" :alt="photo.description">
                  </div>
                </div>
              </div>
              <h6 v-else class="mt-5">Вы не добавили ни одной фотографии</h6>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>


<script>
import {requestsMixin} from "../../components/mixins/requestsMixin";
import {redirect} from "../../components/mixins/redirect";
import Navbar from "../../components/Navbar";
import ProfileMenu from "../../components/Profile/ProfileMenu";
import UploadPhotoModal from "../../components/Modal/UploadPhotoModal";
import EditPhotoModal from "../../components/Modal/EditPhotoModal";
import DeletePhotoModal from "../../components/Modal/DeletePhotoModal";
import axios from "axios";


export default {
  name: "Photo",

  components: {
    Navbar, ProfileMenu, UploadPhotoModal, EditPhotoModal, DeletePhotoModal
  },

  data() {
    return {
      slideIndex: 1,
      header: 'Галерея',
      photos: 0,
      likeImage: ''
    }
  },

  props: {
    id: Number,
  },

  created() {
    this.createGetRequest(`/profile/${this.id}/gallery/`)
  },

  updated() {
    this.showSlides(this.slideIndex);
    this.likeImage = this.getSelfLikeImage()
  },

  mixins: [requestsMixin, redirect],

  methods: {
    showUploadModal() {
      // Показать окно загрузки изображения
      this.$refs.uploadModal.show = true
    },

    showDeleteModal() {
      // Показать окно удаления изображения
      this.$refs.deleteModal.show = true
    },

    showEditModal() {
      // Показать окно редактирования описания к изображению
      this.$refs.editModal.show = true
    },

    plusSlides(n) {
      // Переключение слайдов стрелками
      this.slideIndex += n
      this.showSlides(this.slideIndex);
    },

    currentSlide(n) {
      // Выбор слайда из из общего списка внизу
      this.showSlides(this.slideIndex = n);
    },

    showSlides(n) {
      // Показ слайда
      let i;
      let slides = document.getElementsByClassName("mySlides");
      let dots = document.getElementsByClassName("demo");
      let captionText = document.getElementById("caption");
      if (n > slides.length) {
        this.slideIndex = 1
      }
      if (n < 1) {
        this.slideIndex = slides.length
      }
      for (i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
      }
      for (i = 0; i < dots.length; i++) {
        dots[i].className = dots[i].className.replace(" active", "");
      }
      slides[this.slideIndex - 1].style.display = "block";
      dots[this.slideIndex - 1].className += " active";
      captionText.innerHTML = dots[this.slideIndex - 1].alt;
    },

    async like() {
      // Поставить лайк / дизлайк
      let body = {
        'id': this.responseData.photos[this.slideIndex - 1].id
      };
      const axiosInstance = axios.create(this.base);
      await axiosInstance({
        url: '/profile/like-photo/',
        method: "post",
        data: body,
      })
          .then(() => {
            let likesList = this.responseData.photos[this.slideIndex - 1].likes
            let selfLiked = false; // Лайк текущего пользователя изначально ставим в false
            if (likesList.length === 0) {
              likesList.push(this.$store.state.authUser)
            } else {
              for (let i = 0; i < likesList.length; i++) {
                if (this.$store.state.authUser.id === likesList[i].id) {
                  likesList.splice(i, 1); // Если находим текущего пользователя в списке лайков, то удаляем его оттуда
                  selfLiked = true;       // и переводим флаг лайка текущего пользователя в true
                  break;
                }
              }
              if (!selfLiked) {   // Если текущего пользователя в списке лайков не нашлось, то добавляем его в список
                likesList.push(this.$store.state.authUser)
              }
            }
          })
          .catch((error) => {
            if (error.request.status === 401) {
              // Если 401 ошибка - токен просрочен, обновляем его и заново запрашиваем данные
              this.refreshToken()
              this.addFriend('/profile/friend-response')
            } else {
              console.log(error)
            }
          })
      this.likeImage = this.getSelfLikeImage()
    },

    getSelfLikeImage() {
      //Показывает соответствующую иконку был ли лайк от текущего пользователя
      let likesList = this.responseData.photos[this.slideIndex - 1].likes;
      if (likesList.length === 0) {
        return  require('../../assets/images/icons/like.svg');
      }
      for (let like of likesList) {
        if (this.$store.state.authUser.id === like.id) {
          return require('../../assets/images/icons/like_fill.svg');
        }
      }
      return require('../../assets/images/icons/like.svg');
    },

    async setAvatar(id) {
      let body = {
        "id": id
      }
      const axiosInstance = axios.create(this.base);
      await axiosInstance({
        url: `/profile/set-avatar/`,
        method: "put",
        data: body
      })
          .then(() => {
            this.createGetRequest(`/profile/${this.$store.state.authUser.id}`)
            setTimeout(() => {
              window.location.reload()
            }, 20)
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
* {
  box-sizing: border-box;
}

.upload-photo-button {
  height: 68%;
  width: 100%;
}

.image-container {
  position: relative;
}

.mySlides {
  display: none;
  min-height: 70vh;
  background-color: #222;
  margin: auto;
  position: relative;
  border-top-right-radius: 8px;
  border-top-left-radius: 8px;
}

@media (max-width: 992px) {
  .mySlides {
    min-height: 55vh;
  }
}

.cursor {
  width: auto;
  height: auto;
  max-height: 95px;
  cursor: pointer;
}

.prev,
.next {
  cursor: pointer;
  position: absolute;
  top: 45%;
  width: auto;
  padding: 16px;
  margin-top: -50px;
  color: white;
  font-weight: bold;
  font-size: 20px;
  border-radius: 0 3px 3px 0;
  user-select: none;
  -webkit-user-select: none;
}

.next {
  right: 0;
  border-radius: 3px 0 0 3px;
}

.prev {
  left: 0;
  border-radius: 3px 0 0 3px;
}

.prev:hover,
.next:hover {
  background-color: rgba(0, 0, 0, 0.8);
}

.number_text {
  color: #f2f2f2;
  font-size: 12px;
  padding: 8px 12px;
  position: absolute;
  top: 0;
}

.caption-container {
  height: 4vh;
  display: block;
  text-align: center;
  background-color: #222;
  padding: 2px 16px 50px 16px;
  color: white;
}

.description-container {
  height: auto;
  display: block;
  text-align: center;
  background-color: #222;
  padding: 2px 16px;
  color: white;
  border-top: 1px solid gray;
}

.row:after {
  content: "";
  display: table;
  clear: both;
}

.column {
  float: left;
  width: 33.33%;
  margin-bottom: 5px;
}

@media (min-width: 992px) {
  .column {
    float: left;
    width: 16.66%;
  }
}

.column img {
  border-radius: 10px;
}

.image {
  width: auto;
  height: auto;
  max-height: 70vh;
  margin: auto;
  padding-top: 30px;
  position: absolute;
  left: 0;
  top: 0;
  bottom: 0;
  right: 0;
}

.demo {
  opacity: 0.6;
}

.active,
.demo:hover {
  opacity: 1;
}

.like_image {
  width: 30px;
  position: absolute;
  left: 30px;
  padding-top: 5px;
}

#like_count {
  position: absolute;
  left: 60px;
  padding: 5px 0 0 8px;
  font-size: 20px;
}

#delete {
  position: absolute;
  right: 15px;
  color: gray;
  padding-top: 5px;
}

#delete:hover {
  color: #ffffff;
}

#edit {
  position: absolute;
  right: 85px;
  color: gray;
  padding-top: 5px;
}

#edit:hover {
  color: #ffffff;
}

#set-avatar {
  position: absolute;
  top: 0;
  right: 15px;
  color: gray;
  padding-top: 5px;
}

#set-avatar:hover {
  color: #ffffff;
}

.liked {
  color: #FF7979;
}

.photo-button {
  border: none;
  background: none;
}
</style>
