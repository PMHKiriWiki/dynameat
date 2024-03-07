<template>
    <div class="asteroids">
      <AsteroidsTable/>
    </div>
</template>


<script>

import AsteroidsTable from '@/components/AsteroidsTable.vue'

export default {
  name: 'AsteroidsView',
  components: {
    AsteroidsTable
  }
}
</script>
