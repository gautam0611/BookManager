<template>
  <base-card>
    <form @submit="submitData">
      <h1>Add a Job</h1>
      <div class="form-control">
        <label for="company-name"><b>Company Name:</b></label>
        <input id="company-name" type="text" ref="companyName">
      </div>
      <div class="form-control">
        <label for="title"><b>Title:</b></label>
        <input id="title" type="text" ref="title">
      </div>
      <div class="form-control">
        <label for="location"><b>Location:</b></label>
        <input id="location" type="text" ref="location">
      </div>
      <div class="form-control">
        <label for="salary"><b>Salary:</b></label>
        <input id="salary" type="text" ref="salary">
      </div>
      <div class="form-control">
        <label for="yoe"><b>YOE Required:</b></label>
        <input id="yoe" type="text" ref="yoe">
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
        <input id="date-applied" type="text" ref="date-applied">
      </div>
      <div class="button-class">
        <button>Add Job</button>
      </div>
    </form>
  </base-card>
</template>

<script lang="ts">
import { defineComponent } from 'vue';

export default defineComponent({
  methods: {
    submitData() {
      // getting our refs
      const companyName = this.$refs.companyName as HTMLInputElement;
      const title = this.$refs.title as HTMLInputElement;
      const salary = this.$refs.salary as HTMLInputElement;
      const location = this.$refs.location as HTMLInputElement;
      const yoe = this.$refs.yoe as HTMLInputElement;
      const hybridOrRemote = this.$refs.hybridRadio !== undefined ? this.$refs.hybridRadio as HTMLInputElement : this.$refs.remoteRadio as HTMLInputElement;
      const dateApplied = this.$refs.dateApplied as HTMLInputElement;

      fetch("http://127.0.0.1:8000/job", {
        method: 'POST',
        headers: {
          'Content-type': 'application/json'
        },
        body: JSON.stringify({
          companyName: companyName.value,
          title: title.value,
          salary: salary.value,
          location: location.value,
          yoe: yoe.value,
          hybridOrRemote: hybridOrRemote.value,
          dateApplied: dateApplied.value
        })
      }).then(response => {
        if (response.ok) {
          return response.json();
        }
      }).catch((error) => {
        console.log(`Here is the error: ${error}`);
      });
    },
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