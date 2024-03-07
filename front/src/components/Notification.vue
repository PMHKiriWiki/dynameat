<template>
    <div v-if="message" :class="{'alert-success': isSuccess, 'alert-danger': isError}" class="alert mt-3" role="alert">
      {{ message }}
    </div>
  </template>
  
  <script>
  export default {
    props: {
      message: String,
      isSuccess: Boolean,
      isError: Boolean
    },
    watch: {
      message(newMessage) {
        if (newMessage) {
          setTimeout(() => {
            this.$emit('clear-message')
          }, 3000)
        }
      }
    }
  }
  </script>
  
  <style scoped>
  /* Add any custom styles for your component here */
  .alert {
    width: 100%
  }
  </style>
  