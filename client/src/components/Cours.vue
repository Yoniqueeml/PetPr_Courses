<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1 class="col-md-6 mb-4 wow zoomIn">MOOCs</h1>
        <hr><br>
        <button type="button" class="btn btn-primary"
           v-if="showCourses || showCourseMaterial" v-on:click="getMoocs">Вернуться к ресурсам
        </button>
        <table v-if="showMoocs" class="table table-dark">
          <thead>
          <tr>
            <th class="text-center" scope="col" colspan="100%" >Названия ресурсов</th>
          </tr>
          </thead>
          <tbody>
          <tr v-for="(mooc, index) in moocs" :key="index">
            <td><button type="button" class="btn btn-light btn-outline-secondary btn-block"
                        v-on:click="getCourses(mooc)" :value="mooc">{{ mooc }}
            </button></td>
          </tr>
          </tbody>
        </table>
        <table v-if="showCourses" class="table table-hover table-bordered table-dark">
          <thead>
          <tr>
            <th class="text-center" scope="col" colspan="100%">Доступные курсы</th>
          </tr>
          </thead>
          <tbody>
          <tr class="text-center" v-for="(course, index) in courses" :key="index">
            <td>
              <button class="btn btn-light btn-outline-secondary"
                      v-on:click="getCourseMaterial(course.acronym)" :value="course.acronym">
                {{course.acronym}} : {{ course.title }}
              </button>
            </td>
            <td class="text-center" v-for="(week, j) in course.weeks" :key="j">{{week}}</td>
          </tr>
          </tbody>
        </table>

        <div v-if="showCourseMaterial">
          <h1 role="button" class="list-group" style="padding-left: 16px;">
            <details open v-for="(week, index) in courseMaterial.weeks_info" :key="index">
              <summary class="btn bg-dark text-white">{{week.week_title}}</summary>
              <h2 class="list-group" style="padding-left: 24px;">
                <li v-for="(video, j) in week.videos" :key="j">
                  <button class="btn bg-secondary text-white"
                          v-on:click="getVideo(week.week_title, video)"> {{ video }} </button></li>
              </h2>
            </details>
            <ul class="video_move">
              <video class="embed-responsive-item outline-secondary"
                     v-if="video" :key="video" controls width="700" height="600">
                <source :src="video">
              </video>
            </ul>
          </h1>
        </div>
      </div>
    </div>
  </div>
</template>

<script type="text/javascript">
import axios from 'axios';

export default {
  data() {
    return {
      video: '',
      moocs: [],
      courses: [],
      courseMaterial: [],
      showMoocs: true,
      showCourses: false,
      showCourseMaterial: false,
      constructedString: '',
    };
  },
  methods: {
    getMoocs() {
      const path = 'http://localhost:5000/';
      axios.get(path)
        .then((res) => {
          console.log(res);
          this.moocs = res.data.moocs;
          this.showMoocs = true;
          this.showCourses = false;
          this.showCourseMaterial = false;
          this.constructedString = '';
          this.video = '';
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    getCourses(moocTitle) {
      const path = `http://localhost:5000/${moocTitle}`;
      console.log(path);
      axios.get(path)
        .then((res) => {
          console.log(res);
          this.courses = res.data.courses;
          this.showMoocs = false;
          this.showCourses = true;
          this.showCourseMaterial = false;
          this.constructedString = moocTitle;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    getCourseMaterial(courseTitle) {
      const path = `http://localhost:5000/${this.constructedString}/${courseTitle}`;
      console.log(path);
      axios.get(path)
        .then((res) => {
          console.log(res);
          this.courseMaterial = res.data.courseMaterial;
          this.showMoocs = false;
          this.showCourses = false;
          this.showCourseMaterial = true;
          this.constructedString += `/${courseTitle}`;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    getVideo(weekTitle, videoTitle) {
      const path = `./${this.constructedString}/${weekTitle}/${videoTitle}`;
      const xhr = new XMLHttpRequest();
      xhr.open('HEAD', path, false);
      xhr.send();
      if (xhr.status === 404) {
        console.log('sorry, file not found');
      } else {
        this.video = path;
      }
    },
  },
  created() {
    this.getMoocs();
  },
};
</script>

<style>
@import './Home.scss';
@import './BirthdayCake.scss';

.video_move {
  position: absolute;
  bottom: -55px;
  left: 580px;
}
</style>
