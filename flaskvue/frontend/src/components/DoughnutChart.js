import {Doughnut, mixins} from 'vue-chartjs'
const {reactiveProp} = mixins

export default({
  extends: Doughnut,
  mixins: [reactiveProp],
  props: ['options'],
  mounted () {
    this.renderChart({
      labels: ['blues', 'classical', 'country', 'disco', 'hiphop', 'jazz', 'metal', 'pop', 'reggae', 'rock'],
      datasets: [
        {
          label: 'Current Genre Distribution of Database',
          borderColor: 'white',
          borderWidth: 1,
          backgroundColor: [
            'blue',
            'green',
            'yellow',
            'white',
            'grey',
            'pink',
            'red',
            'purple',
            'teal',
            'orange'
          ],
          data: this.chartData
        }
      ]
    }, {responsive: true, maintainAspectRatio: false})
  }
})
