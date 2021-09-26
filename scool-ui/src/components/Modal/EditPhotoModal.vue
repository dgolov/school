<template>
  <div v-if="show" class="modal-shadow" @click.self="closeModal">
    <div class="modal">
      <div class="modal-close" @click="closeModal">&#10006;</div>
      <slot name="title">
        <h3 class="system-color">Редактировать описание к фотографии</h3>
      </slot>
      <slot name="body">
        <textarea v-model="caption" id="file-input" class="file-input"></textarea>
      </slot>
      <slot name="footer">
        <div class="modal-footer">
          <div class="container">
            <div class="row">
              <div class="col-md-6">
                <button class="gray-button upload-photo-button" @click="sendDescription()">Применить</button>
              </div>
              <div class="col-md-6">
                <button class="red-button upload-photo-button" @click="closeModal()">Отменить</button>
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
      caption: ''
    }
  },

  props: {
    id: Number,
  },

  mixins: [requestsMixin],

  methods: {
    closeModal() {
      this.show = false
    },

    async sendDescription() {
      if(!this.caption) {
        return false
      }
      let data = {
        "id": this.id,
        "description": this.caption
      }
      const axiosInstance = axios.create(this.base);
      await axiosInstance({
        url: `/profile/edit-photo/`,
        method: "put",
        data: data
      })
          .then(() => {
            this.closeModal();
            this.$emit('reLoad')
            this.caption = ''
          })
          .catch((error) => {
            if (error.request.status === 401) {
              // Если 403 ошибка - токен просрочен, обновляем его и заново запрашиваем данные
              this.refreshToken();
              this.sendDescription();
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
    height: 50%;
  }
}

@media (min-width: 992px) {
  .modal {
    width: 50%;
    height: 43%;
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