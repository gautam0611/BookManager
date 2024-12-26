<template>
  <div class="table-container">
    <table border="1">
      <thead>
        <tr>
          <th><b>Company Name</b></th>
          <th><b>Title</b></th>
          <th><b>Location</b></th>
          <th><b>Salary</b></th>
          <th><b>Yoe</b></th>
          <th><b>Hybrid/Remote</b></th>
          <th><b>Date Applied</b></th>
        </tr>
      </thead>
      <!-- <tbody>
        <tr v-for="job in jobs" :key=job.id>
          <td>{{ job.companyName }}</td>
          <td>{{ job.title }}</td>
          <td>{{ job.location }}</td>
          <td>{{ job.salary }}</td>
          <td>{{ job.yoe }}</td>
          <td>{{ job.hybridOrRemote }}</td>
          <td>{{ job.dateApplied }}</td>
        </tr>
      </tbody> -->
    </table>
    <div>
      <button @click="getAllJobs">get all jobs</button>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';

export default defineComponent({
  props: ['company-name', 'title', 'location', 'salary', 'yoe', 'hybrid/remote', 'date-applied'],
  data() {
    return {
      jobs: []
    }
  },
  methods: {
    getAllJobs() {
      fetch("http://127.0.0.1:8000/all_jobs").then((response) => {
        if (!response.ok) {
          console.log(response);
          throw new Error(`HTTP error! Status: ${response.status}`);
        }
        return response.json();
      })
        .then((data) => {
          console.log(data);
        })
        .catch((error) => {
          console.error("Error:", error);
        });
    }
  }

})
</script>

<style scoped>
.table-container {
  display: flex;
  flex-direction: row;
  justify-content: center;
  margin-top: 10%;
}
</style>