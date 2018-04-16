<template lang="html">
  <div>
  <v-container grid-list-md>
    <v-container>
    <h2>Now playing: {{song_name}}</h2>
    <h3>genre: {{this.radios}}</h3>
    <v-divider></v-divider>
    </v-container>
    <v-layout  d-flex row wrap>

    <youtube :video-id="vid_id" ref="youtube" @playing="playing" @ended="getVideo()" :player-vars="{autoplay:1}"></youtube>

    <v-flex d-flex xs12 sm6 md4>
    <v-radio-group v-model="radios" :mandatory="false">

        <v-radio label="Jazz" value="jazz"></v-radio>

        <v-radio label="Rock" value="rock"></v-radio>

        <v-radio label="Blues" value="blues"></v-radio>

        <v-radio label="Pop" value="pop"></v-radio>

        <v-radio label="Reggae" value="reggae"></v-radio>

        <v-radio label="Hiphop" value="hiphop"></v-radio>

        <v-radio label="Disco" value="disco"></v-radio>

        <v-radio label="Country" value="country"></v-radio>

        <v-radio label="Classical" value="classical"></v-radio>

        <v-radio label="Metal" value="metal"></v-radio>
        <v-btn @click="getVideo()">New Video</v-btn>
      </v-radio-group>
    </v-flex>
    <v-flex  d-flex xs12 sm6 md4>
        <bar-chart v-if="loaded" :chart-data="this.mean"></bar-chart>
    </v-flex>
    <v-flex>
      <p class="text-md-center">Distribution of Current Song DB</p>
    </v-flex>
    <v-divider></v-divider>
        <doughnut-chart v-if="loaded" :chart-data="this.db_data"></doughnut-chart>
  </v-layout>
  </v-container>
  </div>
</template>

<script>
/* eslint-disable */
import axios from 'axios'
import BarChart from '@/components/BarChart.js'
import LineChart from '@/components/LineChart.js'
import DoughnutChart from '@/components/DoughnutChart.js'
export default {
  name: 'app',
  components: {
    BarChart,
    LineChart,
    DoughnutChart
  },
  data(){
    return{
      radios: 'jazz',
      song_name: '',
      vid_id: '',
      mean: {},
      loaded: false,
      db_data: {}
    }
  },
  beforeMount(){
    this.getVideo()
    this.getDbData()
  },
  mounted(){
    this.getVideo()
    this.getDbData()
  },
  methods: {
    resetState(){
      this.loaded = false
    },
    getVideo(){
      this.resetState()
      axios.get('http://127.0.0.1:5000/api/video/' + this.radios + '/')
      .then(response => {
        this.song_name = response.data.name
        this.vid_id = response.data.vidID
        this.mean = response.data.mean
        this.loaded = true
        console.log(response.data.name)
      })
      .catch(error => {
        console.log(error)
      });
    },
    getDbData (){
      this.resetState ()
      axios.get('http://127.0.0.1:5000/api/data/')
      .then (response => {
        this.db_data = response.data
        console.log(response.data)
      })
      .catch(error => { console.log(error) })
      this.loaded = true
    },
    playVideo () {
      this.player.playVideo()
    },
    playing () {
      console.log('we are watching!!!')
    }
  },
  computed: {
    player () {
      return this.$refs.youtube.player
    }
  }

}

</script>

<style lang="css">

</style>
