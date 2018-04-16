import {Bar, mixins} from 'vue-chartjs'
const {reactiveProp} = mixins

export default({
  extends: Bar,
  mixins: [reactiveProp],
  data () {
    return {
      gradient: null,
      gradient2: null
    }
  },
  props: ['options'],
  mounted () {
    this.gradient = this.$refs.canvas.getContext('2d').createLinearGradient(0, 0, 0, 450)
    this.gradient2 = this.$refs.canvas.getContext('2d').createLinearGradient(0, 0, 0, 450)

    this.gradient.addColorStop(0, 'rgba(255, 0,0, 0.5)')
    this.gradient.addColorStop(0.5, 'rgba(255, 0, 0, 0.25)')
    this.gradient.addColorStop(1, 'rgba(255, 0, 0, 0)')

    this.gradient2.addColorStop(0, 'rgba(0, 231, 255, 0.9)')
    this.gradient2.addColorStop(0.5, 'rgba(0, 231, 255, 0.25)')
    this.gradient2.addColorStop(1, 'rgba(0, 231, 255, 0)')

    this.renderChart({
      labels: ['blues', 'classical', 'country', 'disco', 'hiphop', 'jazz', 'metal', 'pop', 'reggae', 'rock'],
      datasets: [
        {
          label: 'Predicted Genre',
          borderColor: '#FC2525',
          pointBackgroundColor: 'white',
          borderWidth: 1,
          pointBorderColor: 'white',
          backgroundColor: [
            this.gradient2,
            this.gradient2,
            this.gradient2,
            this.gradient2,
            this.gradient2,
            this.gradient2,
            this.gradient2,
            this.gradient2,
            this.gradient2,
            this.gradient2
          ],
          data: this.chartData
        }
      ]
    }, {responsive: true, maintainAspectRatio: false})
  }
})
