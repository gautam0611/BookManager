<template>
  <div class="button-container">
    <router-link to="/addJob" class="router-button">
      <base-button :mode="addAJobButton">Add a Job</base-button>
    </router-link>
    <router-link to="/appliedJobs" class="router-button">
      <base-button :mode="appliedJobButton">View Applied Jobs</base-button>
    </router-link>
  </div>
  <router-view />
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import AddAJob from './AddAJob.vue';
import AppliedJob from './AppliedJob.vue';

export default defineComponent({
  name: 'TheJobs',
  components: {
    AddAJob,
    AppliedJob
  },
  data() {
    return {
      selectedTab: 'applied-jobs',
      allJobs: []
    }
  },
  methods: {
    setSelectedTab(tab: string) {
      this.selectedTab = tab;
    },
  },
  computed: {
    addAJobButton(): string | null {
      return this.selectedTab === 'add-a-job' ? null : 'flat';
    },
    appliedJobButton(): string | null {
      return this.selectedTab === 'applied-job' ? null : 'flat';
    }
  },
});
</script>

<style scoped>
.button-container {
  display: flex;
  flex-direction: row;
  justify-content: center;
  height: 10vh;
  gap: 5px;
}

.router-button {
  text-decoration: none
}
</style>