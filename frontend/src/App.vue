<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <h1>Trump AI Tweets</h1>
    <div id="tweet">{{ tweet }}</div>
    <button @click="getTweet">Get New Tweet</button>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'App',
  data() {
      return {
          tweet: ""
      }
  },
  methods: {
      getTweet() {
        const path = 'http://localhost:5000/api/tweet';
        axios.get(path)
          .then((res) => {
            this.tweet = res.data.tweet;
          })
          .catch((error) => {
            console.error(error);
          });
      }
  },
  mounted () {
    this.getTweet();
  },
}
</script>
