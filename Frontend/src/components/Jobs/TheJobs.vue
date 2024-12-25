<template>
  <div class="button-container">
    <base-button @click="setSelectedTab('add-a-job')" :mode="addAJobButton">Add a Job</base-button>
    <base-button @click="setSelectedTab('applied-job')" :mode="appliedJobButton">View Applied Jobs</base-button>
  </div>
  <keep-alive>
    <component :is="selectedTab"></component>
  </keep-alive>
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
    }
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
</style>