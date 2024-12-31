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
          <th><b>Job URL</b></th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="job in jobs" :key=job.id>
          <td>{{ job.company_name }}</td>
          <td>{{ job.title }}</td>
          <td>{{ job.location }}</td>
          <td>{{ job.salary }}</td>
          <td>{{ job.yoe }}</td>
          <td>{{ job.workLoc }}</td>
          <td>{{ job.dateApplied }}</td>
          <td>{{ job.jobURL }}</td>
          <td>
            <div class="delete-container">
              <button>Delete Job</button>
            </div>
          </td>
        </tr>
      </tbody>
    </table>
    <!-- <div>
      <button @click="getAllJobs">get all jobs</button>
    </div> -->
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import Job from '../../../interfaces.ts';

export default defineComponent({
  props: ['company-name', 'title', 'location', 'salary', 'yoe', 'hybrid/remote', 'date-applied'],
  data() {
    return {
      jobs: [] as Job[]
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
          const jobs: Job[] = Object.keys(data).map((id) => ({
            id, // Use the key as the ID
            company_name: data[id].company_name,
            title: data[id].title,
            location: data[id].location,
            salary: Number(data[id].salary), // Ensure salary is a number
            yoe: data[id].yoe,
            workLoc: data[id].workLoc,
            dateApplied: data[id].dateApplied,
            jobURL: data[id].jobURL,
          }));
          this.jobs = jobs;
        })
        .catch((error) => {
          console.error("Error:", error);
        });
    }
  },
  mounted() {
    this.getAllJobs();
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

table {
  width: 80%;
  /* Make the table take full width of the container */
  border-collapse: collapse;
  /* Collapse borders for a clean look */
  table-layout: fixed;
  /* Ensure cells maintain equal width */
}
</style>