<template>
  <div v-if="show" class="modal-shadow" @click.self="closeModal">
    <div class="modal">
      <div class="modal-close" @click="closeModal">&#10006;</div>
      <slot name="title">
        <h3 class="system-color">Загрузить новую фотографию</h3>
      </slot>
      <slot name="body">
        <div class="modal-content">
          <p>Выберите файл изображения для загрузки в галерею</p>
          <input type="file" id="file-input" class="file-input" ref="fileInput" v-on:change="handleFileUpload()">
        </div>
      </slot>
      <slot name="footer">
        <div class="modal-footer">
          <button class="grey-button upload-photo-button" @click="submitFile()">Загрузить фото</button>
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

  mixins: [requestsMixin],

  methods: {
    closeModal() {
      this.show = false
    },
    handleFileUpload() {
      this.file = this.$refs.fileInput.files[0];
    },
    submitFile() {
      let formData = new FormData();
      let url = `${this.$store.state.backendUrl}/profile/upload-photo/`
      formData.append('image', this.file);
      axios.post(url,
          formData,
          {
            headers: {
              Authorization: `Bearer ${this.$store.state.jwt}`,
              'Content-Type': 'multipart/form-data'
            }
          }
      ).then(() => {
        console.log('SUCCESS!!');
      })
          .catch((error) => {
            console.log('FAILURE!!');
            if (error.request.status === 403 && error.request.responseText === this.errorAccessToken) {
              // Если 403 ошибка - токен просрочен, обновляем его и заново запрашиваем данные
              this.refreshToken();
              this.submitFile();
            } else {
              console.log(error);
            }
          });
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
    height: 43%;
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