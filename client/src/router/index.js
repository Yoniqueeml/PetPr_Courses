import Vue from 'vue';
import VueRouter from 'vue-router';
import Moocs from '../components/Moocs.vue';
import Courses from '../components/Courses.vue';
import CourseMaterials from '../components/CourseMaterials.vue';

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
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue'),
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
