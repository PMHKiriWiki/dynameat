<template>
    <div class="asteroids">
      <SightingsTable/>
    </div>
</template>


<script>

import SightingsTable from '@/components/SightingsTable.vue'

export default {
  name: 'SightingsView',
  components: {
    SightingsTable
  }
}
</script>
