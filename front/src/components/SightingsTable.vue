<template>
    <div>
      <h2>Avistamientos</h2>
      <div class="table-responsive">
        <table class="table">
          <thead>
            <tr>
              <th>Fecha</th>
              <th>Observatorio</th>
              <th>Dispositivo</th>
              <th>Resolución</th>
              <th class="text-center">Imagen</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="item in data" :key="item.id">
              <td class="align-middle">{{ formatDate(item.datetime) }}</td>
              <td class="align-middle">{{ item.observatory.name }}</td>
              <td class="align-middle">{{ item.device.name }}</td>
              <td class="align-middle">{{ item.device.r_width }}x{{ item.device.r_height }}</td>
              <td>
                <div style="display: flex; justify-content: center; align-items: center;">
                  <MatrixGrid :binaryString="item.device_matrix" :matrixHeight="item.device.r_height" :matrixWidth="item.device.r_width" alt="Observation Matrix" />
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </template>
  
  <script>
  import MatrixGrid from './MatrixGrid.vue'
  import moment from 'moment'
  import { fetchSightings } from '@/api/apiService'
  
  export default {
    components: {
      MatrixGrid
    },
    props: {
      asteroidId: {
        type: String,
        default: null
      }
    },
    data() {
      return {
        data: [],
      }
    },
    mounted() {
      this.fetchData()
    },
    methods: {
      async fetchData() {
      try {
        this.data = await fetchSightings(this.asteroidId)
      } catch (error) {
        console.error('Error fetching data:', error)
      }
    },
      viewDetails(itemId) {
        console.log('View details for:', itemId)
      },
      formatDate(date) {
        return moment(date).format('DD-MM-YYYY, h:mm:ss a')
      }
    }
  }
  </script>
  
  <style>
  .btn {
    margin-right: 8px;
  }
  </style>
  