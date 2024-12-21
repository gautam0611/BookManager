<template>
    <header>
        <h2>{{ title }}</h2>
    </header>
</template>

<script lang="ts">
import { defineComponent } from 'vue';

export default defineComponent({
    props: ['title']
})
</script>

<style scoped></style>