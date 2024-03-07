<template>
    <div>
      <Notification :message="notificationMessage" :isSuccess="uploadSuccess" :isError="uploadError" @clear-message="clearMessage" />
      <div class="card">
        <div class="card-body">
          <h2 class="card-title">Subir fichero de avistamientos</h2>
          <div class="mb-3">
            <label for="fileInput" class="form-label">Elegir archivo</label>
            <input type="file" class="form-control" id="fileInput" ref="fileInput" @change="handleFileChange" />
          </div>
          <button class="btn btn-primary" @click="uploadFile" :disabled="!file">Subir</button>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import Notification from './Notification.vue'
  import { uploadFile } from '@/api/apiService'
  
  export default {
    components: {
      Notification
    },
    data() {
      return {
        file: null,
        uploadedFileName: null,
        uploadSuccess: false,
        uploadError: false
      }
    },
    computed: {
      notificationMessage() {
        if (this.uploadSuccess) {
          return 'El fichero se ha subido con éxito'
        } else if (this.uploadError) {
          return 'Error subiendo el archivo. Comprueba que el formato es correcto y vuelve a intentarlo'
        } else {
          return null
        }
      }
    },
    methods: {
      handleFileChange(event) {
        this.file = event.target.files[0]
      },
      async uploadFile() {
      try {
        if (this.file) {
          await uploadFile(this.file)
          this.uploadSuccess = true
          this.uploadError = false
        } else {
          console.error('No file selected')
          this.uploadError = true
          this.uploadSuccess = false
        }
      } catch (error) {
        console.error('Error uploading file:', error)
        this.uploadError = true
        this.uploadSuccess = false
      }
    },
      clearMessage() {
        this.uploadSuccess = false
        this.uploadError = false
      }
    }
  }
  </script>
  
  <style scoped>
  .card {
    width: 500px;
    margin: auto;
    margin-top: 50px; 
  }
  </style>
  