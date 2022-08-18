<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1 class="col-md-6 mb-4 wow zoomIn">MOOCs</h1>
        <hr><br>
        <table class="table table-dark">
          <thead>
            <tr>
              <th class="text-center" scope="col" colspan="100%" >Названия ресурсов</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(mooc, index) in moocs" :key="index">
              <td>
              <router-link :to="{ name: 'Courses', params: { site: mooc }}">
                <button type="button"
class="btn btn-light btn-outline-secondary btn-block" :value="mooc">{{ mooc }}
                </button>
              </router-link>
              </td>
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
      moocs: [],
    };
  },
  methods: {
    getMoocs() {
      const path = 'http://localhost:5000/';
      axios.get(path)
        .then((res) => {
          console.log(res);
          this.moocs = res.data.moocs;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.$router.push('/notfound');
        });
    },
  },
  created() {
    this.getMoocs();
  },
};
</script>
