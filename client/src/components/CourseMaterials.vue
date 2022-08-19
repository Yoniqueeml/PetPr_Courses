<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1 class="col-md-6 mb-4 wow zoomIn">MOOCs</h1>
        <hr><br>
        <router-link to="/"><button class="btn btn-primary">
Вернуться к ресурсам</button></router-link>
        <span v-if="errorMessage" class="error-position alert alert-danger">
        {{errorMessage}}
        </span>
        <div style="padding-right:100px; padding-top:20px">
          <ul role="button" class="list-group" style="padding-left:25px">
            <details open v-for="(week, index)
in courseMaterial.weeks_info" :key="index">
            <summary class="btn bg-dark text-white">
{{week.week_title}}</summary>
                <h2 class="list-group" style="padding-left: 61px;">
                  <li v-for="(video, j) in week.videos" :key="j">
                  <button class="btn bg-secondary text-white"
                  v-on:click="getVideo(week.week_title, video)"> {{ video }} </button></li>
                </h2>
            </details>
          </ul>
        </div>
      </div>
<ul class="video_move">
<Transition name="video_transition" mode="out-in">
        <video class="embed-responsive-item outline-secondary"
        v-if="video" :key="video" controls width="600" height="500">
        <source :src="video">
        </video>
</Transition>
</ul>
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
      errorMessage: '',
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
      const path = `/${this.constructedString}/${weekTitle}/${videoTitle}`;
      console.log(path);
      if (path === this.video) {
        this.video = '';
        return;
      }
      const xhr = new XMLHttpRequest();
      xhr.open('HEAD', path, false);
      xhr.send();
      if (xhr.status === 404) {
        this.errorMessage = 'Sorry, video is not found';
        this.video = '';
      } else {
        this.video = path;
        this.errorMessage = '';
      }
    },
  },
  created() {
    this.constructedString = `${this.$route.params.site}/${this.$route.params.acronym}`;
    this.getCourseMaterial(this.$route.params.site, this.$route.params.acronym);
  },
};
</script>

<style>
.video_move {
  position: absolute;
  bottom: 230px;
  left: 910px;
}
.video_transition-enter-active,
.video_transition-leave-active {
  transition: opacity 0.6s ease;
}
.video_transition-enter,
.video_transition-leave-to {
  opacity: 0;
}
.error-position {
  position: absolute;
  bottom: 0px;
  left: 100px;
}
</style>
