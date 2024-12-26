<template>
  <base-card>
    <form @submit.prevent="submitData">
      <h1>Add a Job</h1>
      <div class="form-control">
        <label for="company-name"><b>Company Name:</b></label>
        <input id="company-name" type="text" v-model="companyName">
      </div>
      <div class="form-control">
        <label for="title"><b>Title:</b></label>
        <input id="title" type="text" v-model="title">
      </div>
      <div class="form-control">
        <label for="location"><b>Location:</b></label>
        <input id="location" type="text" v-model="location">
      </div>
      <div class="form-control">
        <label for="salary"><b>Salary:</b></label>
        <input id="salary" type="text" v-model="salary">
      </div>
      <div class="form-control">
        <label for="yoe"><b>YOE Required:</b></label>
        <input id="yoe" type="text" v-model="yoe">
      </div>
      <div class="form-control">
        <label for="hybrid/remote"><b>Hybrid/Remote:</b></label>
        <div>
          <label for="hybrid">Hybrid</label>
          <input id="hybrid" type="radio" ref="hybridRadio">
        </div>
        <div>
          <label for="remote">Remote</label>
          <input id="remote" type="radio" ref="remoteRadio">
        </div>
      </div>
      <div class="form-control">
        <label for="date-applied"><b>Date Applied:</b></label>
        <input id="date-applied" type="text" v-model="dateApplied">
      </div>
      <div class="form-control">
        <label for="jobURL"><b>Job URL:</b></label>
        <input id="jobURL" type="text" v-model="jobURL">
      </div>
      <div class="button-class">
        <button>Add Job</button>
        <button @click="clearForm">Clear Form</button>
      </div>
    </form>
    <p v-if="invalidInput">One or more inputs is empty. Please check</p>
  </base-card>
</template>

<script lang="ts">
import { defineComponent } from 'vue';

export default defineComponent({
  data() {
    return {
      invalidInput: false,
      companyName: '',
      salary: null,
      workLoc: '',
      yoe: '',
      dateApplied: null,
      jobURL: '',
      title: '',
      location: ''
    }
  },
  methods: {
    submitData() {
      // getting our refs
      // const companyName = this.$refs.companyName as HTMLInputElement;
      // const title = this.$refs.title as HTMLInputElement;
      // const salary = this.$refs.salary as HTMLInputElement;
      // const location = this.$refs.location as HTMLInputElement;
      // const yoe = this.$refs.yoe as HTMLInputElement;
      const hybridOrRemote: string = this.$refs.hybridRadio !== undefined ? 'hybrid' : 'remote';
      // const dateApplied = this.$refs.dateApplied as HTMLInputElement;
      // const jobURL = this.$refs.jobURL as HTMLInputElement;

      if (this.companyName === '' || this.title === '' || this.salary === '' || this.location === '' || this.yoe === '' || hybridOrRemote === '' || this.dateApplied === '' || this.jobURL === '') {
        this.invalidInput = true;
        return;
      }
      this.invalidInput = false;

      fetch("http://127.0.0.1:8000/job", {
        method: 'POST',
        headers: {
          'Content-type': 'application/json'
        },
        body: JSON.stringify({
          company_name: this.companyName,
          title: this.title,
          salary: this.salary,
          location: this.location,
          yoe: this.yoe,
          workLoc: hybridOrRemote, // we just return a string
          dateApplied: new Date(this.dateApplied).toISOString(),
          jobURL: this.jobURL
        })
      }).then((response) => {
        if (!response.ok) {
          throw new Error(`HTTP error! Status: ${response.status}`);
        }
        return response.json();
      })
        .then((data) => {
          console.log("Response:", data);
        })
        .catch((error) => {
          console.error("Error:", error);
        });

      // clear our form after adding
      this.clearForm();
    },
    clearForm() {
      this.companyName = '';
      this.location = '';
      this.salary = null;
      this.yoe = '';
      this.dateApplied = null;
      this.jobURL = '';
      this.title = '';
    }
  },
  mounted() {
    this.submitData();
  }
});
</script>

<style scoped>
input[type='radio'] {
  display: inline-block;
  width: auto;
  margin-right: 1rem;
}

div {
  margin-top: 1rem
}

h1 {
  text-align: center;
}

input[type='text'] {
  display: block;
  width: 20rem;
  margin-top: 0.5rem;
}

.button-class {
  display: flex;
  justify-content: center;
  align-items: center;
  /* width: 20rem; */
}

button {
  width: 10rem;
  height: 3rem;
  /* border-radius: 12px; */
}

button:hover,
button:active {
  background-color: #de1313;
  border-color: #b80000;
}
</style>