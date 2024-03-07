<template>
    <div>
      <table class="table-bordered">
        <tbody>
          <tr v-for="(row, rowIndex) in matrix" :key="rowIndex">
            <td v-for="(cell, colIndex) in row" :key="colIndex" class="cell" :class="{ 'colored-1': cell === '1', 'colored-0': cell === '0' }"></td>
          </tr>
        </tbody>
      </table>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      binaryString: {
        type: String,
        required: true
      },
      matrixHeight: {
        type: Number,
        required: true
      },
      matrixWidth: {
        type: Number,
        required: true
      }
    },
    computed: {
      matrix() {
        const matrix = []
        let index = 0
  
        for (let i = 0; i < this.matrixHeight; i++) {
          const row = []
          for (let j = 0; j < this.matrixWidth; j++) {
            row.push(this.binaryString[index])
            index++
          }
          matrix.push(row)
        }
  
        return matrix
      }
    }
  }
  </script>
  
  <style scoped>
  .table-bordered {
    border-collapse: collapse;
  }
  
  .cell {
    border: 1px solid black;
    width: 20px;
    height: 20px;
  }
  
  .colored-1 {
    background-color: rgb(15, 18, 19); /* Color for cells with '1' */
  }
  
  .colored-0 {
    background-color: lightgrey; /* Light grey color for cells with '0' */
  }
  </style>
  
  