<template>
  <div>
    <v-data-table
    :headers="headers"
    :items="activityLogs"
    disable-sort
    hide-default-footer
    no-data-text="В выбранный час не выполнено никакой работы"
  >
    <template v-slot:item="{ item }">
        <tr>
          <td style="text-align: center;">{{ item.Worker.middle_name + ' ' + item.Worker.name[0] + '.' + item.Worker.surname[0] + '.' }}</td>
          <td style="text-align: center;">{{ item.work_hour }}</td>
          <td style="text-align: center;">{{ String(item.product_kilogramms)[0] }}</td>
        </tr>
      </template>
  </v-data-table>
</div>
</template>

<script>
export default {
  name: 'Table',

  data () {
    return {
      headers: [
        {
          text: 'ФИО',
          align: 'center'
        },
        {
          text: 'Час работы',
          align: 'center'
        },
        {
          text: 'Кол-во килограмм',
          align: 'center'
        }
      ]
    }
  },

  computed: {
    activityLogs () {
      if (this.$store.state.activityLog.logs) {
        return this.$store.state.activityLog.logs
      } else {
        return []
      }
    }
  }
}
</script>

<style lang='scss' scoped>

</style>
