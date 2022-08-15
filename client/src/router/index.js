import Vue from 'vue';
import Router from 'vue-router';
import Cours from '../components/Cours.vue';

Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'Cours',
      component: Cours,
    },
  ],
});
