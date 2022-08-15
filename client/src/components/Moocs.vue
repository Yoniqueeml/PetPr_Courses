<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>MOOCs</h1>
        <hr><br>
        <button v-if="showCourses || showCourseMaterial" v-on:click="getMoocs">Вернуться к ресурсам
        </button>
        <table v-if="showMoocs" class="table table-hover">
          <thead>
            <tr>
              <th class="text-center" scope="col" colspan="3" >Названия ресурсов</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(mooc, index) in moocs" :key="index">
              <td><button v-on:click="getCourses(mooc)" :value="mooc">{{ mooc }}
              </button></td>
            </tr>
          </tbody>
        </table>

        <table v-if="showCourses" class="table table-hover">
          <thead>
            <tr>
              <th class="text-center" scope="col" colspan="3">Доступные курсы</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(course, index) in courses" :key="index">
              <td><button v-on:click="getCourseMaterial(course.acronym)" :value="course.acronym" >
                    {{course.acronym}} : {{ course.title }}</button>
              </td>
              <td v-for="(week, j) in course.weeks" :key="j">{{week}}</td>
            </tr>
          </tbody>
        </table>

        <div v-if="showCourseMaterial">
        <video v-if="video" :key="video" controls>
        <source :src="video">
        </video>
          <ul>
            <details open v-for="(week, index) in courseMaterial.weeks_info" :key="index">
            <summary>{{week.week_title}}</summary>
                <ul>
                  <li v-for="(video, j) in week.videos" :key="j">
                  <button v-on:click="getVideo(week.week_title, video)"> {{ video }} </button></li>
                </ul>
            </details>
          </ul>
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
