<template>
  <base-card>
    <form>
      <h1>Add a Job</h1>
      <div class="form-control">
        <label for="company-name"><b>Company Name:</b></label>
        <input id="company-name" type="text">
      </div>
      <div class="form-control">
        <label for="title"><b>Title:</b></label>
        <input id="title" type="text">
      </div>
      <div class="form-control">
        <label for="location"><b>Location:</b></label>
        <input id="location" type="text">
      </div>
      <div class="form-control">
        <label for="salary"><b>Salary:</b></label>
        <input id="salary" type="text">
      </div>
      <div class="form-control">
        <label for="yoe"><b>YOE Required:</b></label>
        <input id="yoe" type="text">
      </div>
      <div class="form-control">
        <label for="hybrid/remote"><b>Hybrid/Remote:</b></label>
        <div>
          <label for="hybrid">Hybrid</label>
          <input id="hybrid" type="radio">
        </div>
        <div>
          <label for="remote">Remote</label>
          <input id="remote" type="radio">
        </div>
      </div>
      <div class="form-control">
        <label for="date-applied"><b>Date Applied:</b></label>
        <input id="date-applied" type="text">
      </div>
    </form>
  </base-card>
</template>

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
</style>