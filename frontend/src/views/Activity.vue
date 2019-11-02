<template>
  <v-container class="mt-12">
    <v-row justify="center">
      <v-col cols="4" xl="3">
        <h2 class="date-title">Выберете дату</h2>
        <v-date-picker
          v-model="picker"
          year-icon="mdi-calendar-blank"
          prev-icon="mdi-skip-previous"
          next-icon="mdi-skip-next"
          locale="ru"
          min="2019-05-01"
          max="2019-12-31"
          full-width
        ></v-date-picker>
        <v-row justify="center">
          <v-btn
            color="primary"
            height="55"
            class="mt-5 white--text"
            @click="refreshLogs"
          >
            Обновить данные
            <v-icon right dark>mdi-cloud-upload</v-icon>
          </v-btn>
        </v-row>
      </v-col>
      <v-col cols="6" xl="4">
        <h2 class="table-title mb-3">Отчет</h2>
        <Table :picker="picker" />
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import Table from '@/components/Table.vue'

export default {
  name: 'App',

  components: {
    Table
  },

  data () {
    return {
      picker: '2019-10-29'
    }
  },

  async created () {
    await this.$store.dispatch('getActivityLogs', {
      date: '2019-10-29'
    })
  },

  watch: {
    picker (newDate) {
      this.$store.dispatch('getActivityLogs', {
        date: newDate
      })
    }
  },

  methods: {
    async refreshLogs () {
      await this.$store.dispatch('getActivityLogs', {
        date: this.picker
      })
    }
  }

}
</script>

<style lang='scss' scoped>
  .date-title{
    text-align: center;
    margin-bottom: 0.5em;
  }

  .hour-title{
    text-align: center;
    margin: 0.5em 0;
  }

  .table-title{
    text-align: center;
  }
</style>
