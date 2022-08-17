<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>MOOCs</h1>
        <hr><br>
        <router-link to="/"><button>Вернуться к ресурсам</button></router-link>

        <table class="table table-hover table-bordered">
          <thead>
            <tr>
              <th class="text-center" scope="col" colspan="100%">Доступные курсы</th>
            </tr>
          </thead>
          <tbody>
            <tr class="text-center" v-for="(course, index) in courses" :key="index">
              <td>
              <router-link :to="{ name: 'CourseMaterials', params: { site: $route.params.site,
                                                                    acronym: course.acronym }}">
                 <button class="list-group-item list-group-item-action" :value="course.acronym">
                    {{course.acronym}} : {{ course.title }}
                 </button>
              </router-link>
              </td>
              <td class="text-center" v-for="(week, j) in course.weeks" :key="j">{{week}}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script type="text/javascript">
import axios from 'axios';

export default {
  data() {
    return {
      courses: [],
    };
  },
  methods: {
    getCourses(moocTitle) {
      const path = `http://localhost:5000/${moocTitle}`;
      console.log(path);
      axios.get(path)
        .then((res) => {
          console.log(res);
          this.courses = res.data.courses;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.$router.push('/notfound');
        });
    },
  },
  created() {
    this.getCourses(this.$route.params.site);
  },
};
</script>
