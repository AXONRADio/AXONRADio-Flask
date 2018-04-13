<template lang="html">
  <div>
  <v-container>
    <p>Please choose a genre</p>
    <p>Now playing {{this.radios}}</p>
    <p>{{this.videoId}}</p>
    <youtube :video-id="videoId" ref="youtube" @playing="playing"></youtube>
    <v-btn @click="getVideo()">play</v-btn>
    <v-radio-group v-model="radios" :mandatory="false">
        <v-divider></v-divider>
        <v-radio label="Jazz" value="jazz"></v-radio>
        <v-divider></v-divider>
        <v-radio label="Rock" value="rock"></v-radio>
        <v-divider></v-divider>
        <v-radio label="Blues" value="blues"></v-radio>
        <v-divider></v-divider>
        <v-radio label="Pop" value="pop"></v-radio>
        <v-divider></v-divider>
        <v-radio label="Reggae" value="reggae"></v-radio>
        <v-divider></v-divider>
        <v-radio label="Hiphop" value="hiphop"></v-radio>
        <v-divider></v-divider>
        <v-radio label="Disco" value="disco"></v-radio>
        <v-divider></v-divider>
        <v-radio label="Country" value="country"></v-radio>
        <v-divider></v-divider>
        <v-radio label="Classical" value="classical"></v-radio>
        <v-divider></v-divider>
        <v-radio label="Metal" value="metal"></v-radio>
        <v-divider></v-divider>
      </v-radio-group>
  </v-container>
  <v-container>
      <v-btn v-on:click="getVideo()">Play</v-btn>

      <p>{{songs}}</p>
      <p>{{videoId}}</p>
      <div v-for="song in songs" :key="song.id">
        <div>
          <p>{{song.name}}</p>
          <p>{{song.genre}}</p>
          <p>{{song.url}}</p>
          <p>{{song.vidID}}</p>
          <v-divider></v-divider>
        </div>
      </div>
    </v-container>
  </div>
</template>

<script>
// import axios from 'axios'
export default {
  data () {
    return {
      radios: 'jazz',
      songs: [],
      videoId: ''
    }
  },
  methods: {/*
    getSongs() {
      axios
        .get("http://127.0.0.1:5000/api/song/" + this.radios + "/")
        .then(response => {
          this.songs = response.data;
          console.log(response);
          console.log(this.videoId);
        })
        .catch(error => {
          console.log(error);
        });
    },
    getVideo() {
      axios
        .get("http://127.0.0.1:5000/api/video/" + this.radios + "/")
        .then(response => {
          this.videoId = response.data;
          console.log(response);
          console.log(this.videoId);
        })
        .catch(error => {
          console.log(error);
        });
    },
    getRandomInt(max) {
      return Math.floor(Math.random() * Math.floor(max));
    },
    playVideo() {
      this.player.playVideo();
    },
    playing() {
      console.log("o/ we are watching!!!");
    }
  },
  computed: {
    player() {
      return this.$refs.youtube.player;
    }
  */}
}
</script>

<style lang="css">

</style>
