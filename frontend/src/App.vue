<template>
  <v-app>
      <v-app-bar
        absolute
        dark
        color="primary"
      >
        <v-toolbar-title>LikeTimePnz</v-toolbar-title>
        <v-spacer></v-spacer>
        <div v-if="this.$store.state.user.current">
          <span>
            {{ this.$store.state.user.current.middle_name + ' ' + this.$store.state.user.current.name[0] + '.' + this.$store.state.user.current.surname[0] + '.' }}
          </span>
          <v-btn class="ml-2" @click="logout" color="blue">Выйти</v-btn>
        </div>
      </v-app-bar>
    <keep-alive>
      <router-view />
    </keep-alive>
  </v-app>
</template>

<script>
export default {
  name: 'App',

  methods: {
    async logout () {
      await this.$store.dispatch('logout')
      this.$router.push('/')
    }
  }
}
</script>

<style lang='scss' scoped>

</style>
