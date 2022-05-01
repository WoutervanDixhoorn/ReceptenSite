<script>
import { getAPI } from '../axios-api'
export default {
  name: 'PostComp',
  data() {
    return {  
      APIData: []
    }
  },
  created(){
    getAPI.get('/posts/',)
    .then(response => {
      console.log('Post api has recieved data!');
      this.APIData = response.data;
    })
    .catch(err => {
      console.log(err);
    })
  }
}

</script>

<template>
  <div class='row'>
    <div v-for="posts in APIData" :key="posts.id">
      <a href="#">{{posts.title}}</a>
      <p>{{posts.content}}</p>
    </div>
  </div>
</template>

<style scoped>
a {
  color: #42b983;
}
</style>
