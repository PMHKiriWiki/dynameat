<template>
    <div>
        <h2>Asteroides</h2>
        <table class="table">
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Nombre</th>
                    <th class="text-center">Imagen</th>
                    <th class="text-center">Acciones</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="item in data" :key="item.id">
                    <td class="align-middle">{{ item.id }}</td>
                    <td class="align-middle">{{ item.name }}</td>
                    <td>
                        <div style="display: flex; justify-content: center; align-items: center;">
                            <MatrixGrid :binaryString="item.matrix_shape" :matrixHeight="item.r_height"
                                :matrixWidth="item.r_width" alt="Observation Matrix" />
                        </div>
                    </td>
                    <td class="text-center align-middle">
                        <button @click="openModal(item)" class="btn btn-info btn-sm">Detalle</button>
                        <button @click="deleteItem(item.id)" class="btn btn-danger btn-sm">Borrar</button>
                    </td>
                </tr>
            </tbody>
        </table>
        <AsteroidModal v-if="isModalOpen" :selectedItem="selectedItem" :fetchData="fetchData" @close="closeModal" />
    </div>
</template>

<script>
import MatrixGrid from './MatrixGrid.vue'
import AsteroidModal from './AsteroidModal.vue'
import { fetchAsteroids, deleteAsteroid } from '@/api/apiService'
export default {
    components: {
        MatrixGrid,
        AsteroidModal
    },
    data() {
        return {
            data: [],
            isModalOpen: false,
            selectedItem: null,
        }
    },
    mounted() {
        this.fetchData()
    },
    methods: {
        async fetchData() {
            try {
                this.data = await fetchAsteroids()
            } catch (error) {
                console.error('Error fetching data:', error)
            }
        },
        openModal(item) {
            this.selectedItem = item
            this.isModalOpen = true
        },
        closeModal() {
            this.isModalOpen = false
            this.selectedItem = null
        },
        async deleteItem(itemId) {
            try {
                await deleteAsteroid(itemId);
                this.fetchData()
            } catch (error) {
                console.error('Error deleting item:', error)
            }
        }
    }
}
</script>

<style>
.btn {
    margin-right: 8px;
}
</style>