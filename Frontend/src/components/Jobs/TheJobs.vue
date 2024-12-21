<template>
  <base-button @click="setSelectedTab('add-a-job')" :mode="addAJobButton">Add a Job</base-button>
  <base-button @click="setSelectedTab('applied-job')" :mode="appliedJobButton">View Applied Jobs</base-button>
  <keep-alive>
    <component :is="selectedTab"></component>
  </keep-alive>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
// import AddAJob from './AddAJob.vue';
// import AppliedJob from './AppliedJob.vue';

export default defineComponent({
  name: 'TheJobs',
  // components: {
  //   AddAJob,
  //   AppliedJob
  // },
  data() {
    return {
      selectedTab: 'add-a-job'
    }
  },
  methods: {
    setSelectedTab(tab: string) {
      this.selectedTab = tab;
    }
  },
  computed: {
    addAJobButton(): string | null {
      return this.selectedTab === 'add-a-job' ? null : 'rounded';
    },
    appliedJobButton(): string | null {
      return this.selectedTab === 'applied-job' ? null : 'rounded';
    }
  },
});
</script>