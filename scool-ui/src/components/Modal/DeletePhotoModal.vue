<template>
  <div v-if="show" class="modal-shadow" @click.self="closeModal">
    <div class="modal">
      <div class="modal-close" @click="closeModal">&#10006;</div>
      <slot name="title">
        <h3 class="system-color mb-4">Вы уверены?</h3>
      </slot>
      <slot name="footer">
        <div class="modal-footer">
          <div class="container">
            <div class="row">
              <div class="col-md-6">
                <button class="red-button upload-photo-button" @click="deletePhoto()">Удалить</button>
              </div>
              <div class="col-md-6">
                <button class="gray-button upload-photo-button" @click="closeModal()">Отменить</button>
              </div>
            </div>
          </div>
        </div>
      </slot>
    </div>
  </div>
</template>


<script>
import {requestsMixin} from "../mixins/requestsMixin";
import axios from "axios";

export default {
  name: "ModalWindow",

  data() {
    return {
      show: false,
      file: '',
    }
  },

  props: {
    id: String
  },

  mixins: [requestsMixin],

  methods: {
    closeModal() {
      this.show = false
    },

    async deletePhoto() {
      const axiosInstance = axios.create(this.base);
      await axiosInstance({
        url: `/profile/delete-photo/${this.id}/`,
        method: "delete",
      })
          .then(() => {
            this.closeModal();
            this.$emit('reLoad');
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
html, body {
  overflow-y: hidden;
}

.modal-shadow {
  position: fixed;
  top: 0;
  left: 0;
  min-height: 100%;
  width: 100%;
  background: rgba(0, 0, 0, 0.7);
  z-index: 998;
}

.modal {
  display: block;
  background: #fff;
  border-radius: 8px;
  padding: 15px;
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  z-index: 999;
}

@media (max-width: 992px) {
  .modal {
    width: 90%;
    height: 30%;
  }
}

@media (min-width: 992px) {
  .modal {
    width: 50%;
    height: 25%;
  }
}

.modal-close {
  border-radius: 50%;
  color: #fff;
  display: flex;
  align-items: center;
  justify-content: center;
  position: absolute;
  top: 7px;
  right: 7px;
  width: 30px;
  height: 30px;
  cursor: pointer;
}

.modal-content {
  margin: 20px 0 20px 0;
  padding: 10px;
}

.file-input {
  margin: 20px 0 10px 0;
  border: none;
}
</style>