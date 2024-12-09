<script setup lang="ts">

</script>

<template>
    <h1>Job Applier</h1>
    <div class="container">
        <button>Add a Job</button>
        <button>See Applied Jobs</button>
    </div>
</template>

<style scoped>
h1 {
    font-size: 48px;
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    text-align: center;
    margin: 0;
    padding: 10px;
}

button {
    display: block;
    /* Make buttons take up their own line */
    width: 200px;
    /* Set a fixed width for larger buttons */
    height: 60px;
    /* Set a fixed height for larger buttons */
    margin: 10px auto;
    /* Add vertical spacing and center align */
    font-size: 20px;
    /* Increase font size for readability */
    background-color: #007BFF;
    /* Add a background color */
    color: white;
    /* Set text color */
    border: none;
    /* Remove borders */
    border-radius: 8px;
    /* Optional: Add rounded corners */
    cursor: pointer;
    /* Change cursor to pointer on hover */
}

button:hover {
    background-color: #0056b3;
    /* Darken the background color on hover */
}

.container {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 15px;
}
</style>