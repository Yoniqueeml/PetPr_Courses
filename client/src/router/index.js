import Vue from 'vue';
import VueRouter from 'vue-router';
import Moocs from '../components/Moocs.vue';
import Courses from '../components/Courses.vue';
import CourseMaterials from '../components/CourseMaterials.vue';
import NotFound from '../components/NotFound.vue';

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'Moocs',
    component: Moocs,
  },
  {
    path: '/mooc/:site',
    name: 'Courses',
    component: Courses,
  },
  {
    path: '/mooc/:site/course/:acronym',
    name: 'CourseMaterials',
    component: CourseMaterials,
  },
  {
    path: '/notfound',
    name: 'NotFound',
    component: NotFound,
    alias: '*',
  },
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

export default router;
