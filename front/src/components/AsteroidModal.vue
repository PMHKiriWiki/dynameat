<template>
  <div class="modal" @click="closeModal">
    <div class="modal-content" :style="{ width: modalWidth + 'px', height: modalHeight + 'px'} " @click.stop>
      <div class="top-content">
        <h2>Detalle del asteroide: {{ selectedItem.name ? selectedItem.name : 'Desconocido' }} </h2>
        <form @submit.prevent="updateItem">
          <label for="itemName">Name:</label>
          <input v-model="updatedName" id="itemName" type="text" required />
        </form>
        <div class="in-modal-table">
          <SightingsTable :asteroidId="selectedItem.id" />
        </div>
      </div>
      <div class="buttons-container">
        <button class="submit-button" type="submit" @click="updateItem">Update</button>
        <button class="close-button" @click="closeModal">Close</button>
      </div>
    </div>
  </div>
</template>

<script>
import MatrixGrid from '@/components/MatrixGrid.vue'
import SightingsTable from './SightingsTable.vue'
import { updateAsteroid } from '@/api/apiService'

export default {
  components: {
    MatrixGrid,
    SightingsTable,
  },
  props: {
    selectedItem: Object,
    fetchData: Function,
  },
  data() {
    return {
      modalWidth: 800,
      modalHeight: 800,
      updatedName: '',
    }
  },
  methods: {
    closeModal() {
      this.$emit('close')
    },
    async updateItem() {
      try {
        if (this.selectedItem) {
          const data = {
            name: this.updatedName,
          }

          await updateAsteroid(this.selectedItem.id, data)
          this.fetchData()
          this.closeModal()
        } else {
          console.error('No selectedItem available')
          this.closeModal()
        }
      } catch (error) {
        console.error('Error updating item:', error)
        this.closeModal()
      }
    },
  },
  watch: {
    selectedItem: {
      immediate: true,
      handler(newVal) {
        this.updatedName = newVal ? newVal.name : ''
      },
    },
  },
}
</script>

<style scoped>
.modal {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
}

.modal-content {
  background-color: white;
  padding: 20px;
  border-radius: 8px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.top-content {
  margin-bottom: 20px;
}

form {
  display: flex;
  flex-direction: column;
}

label {
  margin-bottom: 8px;
}

input {
  margin-bottom: 16px;
  width: 80%;
}

.buttons-container {
  display: flex;
  justify-content: space-evenly;
}

button {
  padding: 8px 16px;
  cursor: pointer;
}

.submit-button {
  background-color: #007bff;
  color: white;
}

.close-button {
  background-color: #dc3545;
  color: white;
}
</style>