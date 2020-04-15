<template>
  <div id="app">
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>
html,body,#app{
  height: 100%;
  margin: 0;
  padding:0;
}
/* body{
  background-color: #f5f5f5;
  min-width: 1000px;
}

body>.container{
  width: 1000px;
  min-width: 1000px;
  margin: 0 auto;
} */
</style>
