<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>MOOCs</h1>
        <hr><br>
        <table class="table table-hover table-bordered">
          <thead>
            <tr>
              <th class="text-center" scope="col" colspan="100%" >Названия ресурсов</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(mooc, index) in moocs" :key="index">
              <td>
              <router-link :to="{ name: 'Courses', params: { site: mooc }}">
                <button class="list-group-item list-group-item-action" :value="mooc">{{ mooc }}
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
