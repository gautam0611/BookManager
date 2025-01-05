<template>
  <the-header title="Job Tracker"></the-header>
  <the-jobs></the-jobs>
  <!-- <the-navigation></the-navigation> -->
  <!-- <main>
    <router-view></router-view>
  </main> -->
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import TheHeader from './components/Layout/TheHeader.vue';
import TheJobs from './components/Jobs/TheJobs.vue';
// import TheNavigation from './components/Nav/TheNavigation.vue';

export default defineComponent({
  name: 'App',
  components: {
    TheHeader,
    TheJobs,
    // TheNavigation
  }
});

</script>


<style scoped></style>
