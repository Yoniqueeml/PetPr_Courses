<template>
    <div class='v-btn' v-on:click='clicked'>
      <p> Coursera </p>
    </div>
</template>

<script>
export default {
  name: "v-btn",
  props:{

  },
  data() {
    return {
      hover: false,
    };
  },
  methods:{
    clicked(){
      console.log('clicked')}
  }
}
</script>
<style scoped>
  .v-btn{
    border-radius: 200px;
    padding: 8px 16px;
    color: black;
    background: darkseagreen;
    cursor: pointer;
  }
</style>