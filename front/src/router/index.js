// router.js

import Vue from 'vue';
import VueRouter from 'vue-router';

Vue.use(VueRouter);

const routes = [
  { path: '/dashboard', component: Dashboard },
  // Add more routes as needed
];

const router = new VueRouter({
  routes,
});

export default router;
