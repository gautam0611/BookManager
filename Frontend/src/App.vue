<template>
  <the-header title="Job Tracker"></the-header>
  <the-jobs></the-jobs>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import TheHeader from './components/Layout/TheHeader.vue';
import TheJobs from './components/Jobs/TheJobs.vue';

export default defineComponent({
  name: 'App',
  components: {
    TheHeader,
    TheJobs
  }
});

</script>


<style scoped></style>
