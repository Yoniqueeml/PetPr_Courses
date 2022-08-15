<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <table v-if="showSites" class="table table-hover">
          <h1>Sites</h1>
          <tbody>
            <tr v-for="(sites, index) in courses" :key="index">
              <td>{{ sites.title }}</td>
              <td>
                <div class="btn-group" role="group">
                  <button
                          type="button"
                          class="btn btn-warning btn-sm"
                          @click="goCourses(sites.title)">
                      Go
                  </button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
        <table v-if="showCourses" class="table table-hover">
          <tbody>
          <h1>{{this.curr_site}}</h1>
          <tr v-for="(cs,index) in courses" :key="index">
            <td>{{ index }}</td>
            <td>
              <div class="btn-group" role="group">
                <button
                  type="button"
                  class="btn btn-warning btn-sm"
                  @click="goCourse(index, cs), curr_course = index">
                  Go
                </button>
              </div>
            </td>
          </tr>
          </tbody>
        </table>
        <table v-if="showCourse" class="table table-hover">
          <tbody>
          <h1>{{this.curr_course}}</h1>
          <td>{{this.curr_site}}</td>
            <td>
                <button type="button" class="btn btn-warning btn-sm"
                        @click="wv1=!wv1">Week 1 - Show/Hide</button>
              <div v-if="wv1">
                <tr v-for="k in week_items['1']" :key="k">
                  <td class="btn-group" role="group">
                      {{k}}
                  </td>
                </tr>
              </div>
            </td>
          <td>
            <button type="button" class="btn btn-warning btn-sm"
                    @click="wv2=!wv2">Week 2 - Show/Hide</button>
            <div v-if="wv2">
              <tr v-for="k in week_items['2']" :key="k">
                <td class="btn-group" role="group">
                    {{k}}
                </td>
              </tr>
            </div>
          </td>
          <td v-if="3<=weeks_numb">
            <button type="button" class="btn btn-warning btn-sm"
                    @click="wv3=!wv3">Week 3 - Show/Hide</button>
            <div v-if="wv3">
              <tr v-for="k in week_items['3']" :key="k">
                <td class="btn-group" role="group">
                  <button type="button"
                          class="btn tn-warning btn-sm"
                          @click="console.log('123')"
                  >{{k}}</button>
                </td>
              </tr>
            </div>
          </td>
          <td v-if="4<=weeks_numb">
            <button type="button" class="btn btn-warning btn-sm"
                    @click="wv4=!wv4">Week 4 - Show/Hide</button>
            <div v-if="wv4">
              <tr v-for="k in week_items['4']" :key="k">
                <td class="btn-group" role="group">
                  <button type="button"
                          class="btn tn-warning btn-sm"
                          @click="console.log('123')"
                  >{{k}}</button>
                </td>
              </tr>
            </div>
          </td>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      courses: [],
      week_items: [{}],
      curr_site: '',
      wv1: false,
      wv2: false,
      wv3: false,
      wv4: false,
      curr_course: '',
      weeks_numb: 0,
      addBookForm: {
        title: '',
      },
      message: '',
      showSites: true,
      showCourses: false,
      showCourse: false,
    };
  },
  components: {
  },
  methods: {
    getCourses() {
      const path = 'http://localhost:5000/';
      axios.get(path)
        .then((res) => {
          this.courses = res.data.sites;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    goCourses(site) {
      this.showCourses = true;
      this.showSites = false;
      let path = 'http://localhost:5000/';
      path += site;
      this.curr_site = site;
      axios.get(path)
        .then((res) => {
          this.courses = res.data;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    goCourse(index) {
      this.showCourses = false;
      this.showSites = false;
      this.showCourse = true;
      let path = 'http://localhost:5000/';
      path += this.curr_site;
      path += '/';
      path += this.curr_course;
      path += '/';
      path += index;
      axios.get(path)
        .then((res) => {
          this.week_items = res.data;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
  created() {
    this.getCourses();
  },
};
</script>
<style>
@import url(https://fonts.googleapis.com/icon?family=Material+Icons);
</style>
