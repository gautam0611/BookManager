import { createApp } from 'vue'
import App from './App.vue'
import BaseCard from './components/UI/BaseCard.vue';
import BaseButton from './components/UI/BaseButton.vue';
import {createRouter, createWebHistory} from 'vue-router';
import AddAJob from './components/Jobs/AddAJob.vue';
import AppliedJob from './components/Jobs/AppliedJob.vue';

const app = createApp(App);

// global components
app.component('base-button', BaseButton)
app.component('base-card', BaseCard)

// creating routes for our router
const router = createRouter({
  history: createWebHistory(),
  routes: [
    {path: '/addJob', component: AddAJob},
    {path: '/appliedJobs', component: AppliedJob}
  ]
});

app.use(router);
app.mount('#app');
