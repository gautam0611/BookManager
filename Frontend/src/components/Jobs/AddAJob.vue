<template>
  <form>
    <h1>Add a Job</h1>
    <div class="form-control">
      <label for="company-name">Company Name</label>
      <input id="company-name" type="text">
    </div>
    <div class="form-control">
      <label for="title">Title</label>
      <input id="title" type="text">
    </div>
    <div class="form-control">
      <label for="location">Location</label>
      <input id="location" type="text">
    </div>
    <div class="form-control">
      <label for="salary">Salary</label>
      <input id="salary" type="text">
    </div>
    <div class="form-control">
      <label for="yoe">YOE Required</label>
      <input id="yoe" type="text">
    </div>
    <div class="form-control">
      <label for="hybrid/remote">Hybrid/Remote:</label>
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
      <label for="date-applied">Date Applied</label>
      <input id="date-applied" type="text">
    </div>
  </form>
</template>

<style scoped>
input[type='radio'] {
  display: inline-block;
  width: auto;
  margin-right: 1rem;
}
</style>