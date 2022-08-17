<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>MOOCs</h1>
        <hr><br>
        <router-link to="/"><button>Вернуться к ресурсам</button></router-link>
        <div>
        <video class="embed-responsive-item"
        v-if="video" :key="video" controls width="500" height="400">
        <source :src="video">
        </video>
          <ul role="button" class="list-group">
            <details open v-for="(week, index) in courseMaterial.weeks_info" :key="index">
            <summary class="font-weight-bold">{{week.week_title}}</summary>
                <ul class="list-group">
                  <li v-for="(video, j) in week.videos" :key="j">
                  <button class="list-group-item list-group-item-action"
                  v-on:click="getVideo(week.week_title, video)"> {{ video }} </button></li>
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
      currentPath: window.location.hash,
      video: '',
      courseMaterial: [],
      constructedString: '',
    };
  },
  methods: {
    getCourseMaterial(moocTitle, courseTitle) {
      const path = `http://localhost:5000/${moocTitle}/${courseTitle}`;
      console.log(path);
      axios.get(path)
        .then((res) => {
          console.log(res);
          this.courseMaterial = res.data.courseMaterial;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.$router.push('/notfound');
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
    this.constructedString = `${this.$route.params.site}/${this.$route.params.acronym}`;
    this.getCourseMaterial(this.$route.params.site, this.$route.params.acronym);
  },
};
</script>
