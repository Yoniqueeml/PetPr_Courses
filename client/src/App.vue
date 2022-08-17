<template>
  <div id="app">
    <vue-page-transition name="fade">
      <particles-bg type="square" :canvas="{backgroundColor:'#888'}" :bg="true"/>
    <router-view/>
    </vue-page-transition>
  </div>
</template>

<script>
import { ParticlesBg } from "particles-bg-vue";

export default {
  name: "App",
  components: {
    ParticlesBg
  }
};
</script>

<style>
#app {
  margin-top: 60px
}
/* Global transition declaration*/
.slide-fade-enter-active {
  transition: all .8s ease;
}
.slide-fade-leave-active {
  transition: all .8s cubic-bezier(1.0, 0.5, 0.8, 1.0);
}
.slide-fade-enter, .slide-fade-leave-to {
  transform: translateX(10px);
  opacity: 0;
}
</style>
