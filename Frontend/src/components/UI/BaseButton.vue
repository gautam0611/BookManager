<template>
  <button :class="mode">
    <slot></slot>
  </button>
</template>

<script lang="ts">
import { defineComponent } from 'vue';

export default defineComponent({
  name: 'BaseButton',
  props: ['mode']
})
</script>

<style scoped>
button {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 20%;
  /* Full width of the parent container */
  max-width: 60rem;
  /* Constrain the maximum width */
  min-width: 20rem;
  /* Ensure a minimum size */
  border-radius: 12px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.26);
  padding: 5rem;
  margin: 3rem auto;
  font-size: 30px;
}

button:hover,
button:active {
  background-color: #de1313;
  border-color: #270041;
}

.flat {
  background-color: transparent;
  color: #3a0061;
  border: none;
}

/* .flat:hover,
.flat:active {
  background-color: #edd2ff;
} */
</style>