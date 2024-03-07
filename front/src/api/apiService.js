import axios from 'axios'

const baseURL = 'http://localhost:8000/api/'

export const updateAsteroid = async (asteroidId, data) => {
    const url = `${baseURL}asteroids/${asteroidId}/`

    try {
        await axios.patch(url, data);
    } catch (error) {
        console.error('Error updating asteroid:', error)
        throw error
    }
}

export const fetchSightings = async (asteroidId = null) => {
    const url = asteroidId
        ? `${baseURL}asteroids/${asteroidId}/asteroid_sightings/`
        : `${baseURL}sightings`

    try {
        const response = await axios.get(url);
        return response.data
    } catch (error) {
        console.error('Error fetching sightings:', error)
        throw error
    }
}

export const fetchAsteroids = async () => {
    const url = `${baseURL}asteroids`

    try {
        const response = await axios.get(url)
        return response.data
    } catch (error) {
        console.error('Error fetching asteroids:', error)
        throw error
    }
}

export const deleteAsteroid = async (asteroidId) => {
    const url = `${baseURL}asteroids/${asteroidId}`

    try {
        await axios.delete(url);
    } catch (error) {
        console.error('Error deleting asteroid:', error)
        throw error
    }
}

export const uploadFile = async (file) => {
    const url = `${baseURL}sightings/upload_file/`;

    try {
        const formData = new FormData()
        formData.append('file', file)

        await axios.post(url, formData, {
            headers: {
                'Content-Type': 'multipart/form-data'
            }
        })

        return true;
    } catch (error) {
        console.error('Error uploading file:', error)
        throw error
    }
}