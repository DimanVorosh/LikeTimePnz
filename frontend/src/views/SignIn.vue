<template>
  <v-container class="fill-height" fluid>
    <v-row
      align="center"
      justify="center"
    >
      <v-col
        cols="12"
        sm="8"
        md="4"
        xl="3"
      >
        <v-card class="elevation-12">
          <v-toolbar
            color="primary"
            dark
            flat
          >
            <v-toolbar-title>Авторизация</v-toolbar-title>
            <div class="flex-grow-1"></div>
          </v-toolbar>
          <v-card-text>
            <v-form>
              <v-text-field
                v-model="user.login"
                v-validate="'required|min:3'"
                :error-messages="errors.collect('login')"
                data-vv-name="login"
                required
                outlined
                placeholder="Логин"
                color="primary"
              ></v-text-field>
              <v-text-field
                v-model="user.password"
                v-validate="'required'"
                :error-messages="errors.collect('password')"
                placeholder="Пароль"
                data-vv-name="password"
                required
                type="password"
                outlined
                color="primary"
              ></v-text-field>
            </v-form>
          </v-card-text>
          <v-card-actions>
            <div class="flex-grow-1"></div>
            <v-btn @click="login" color="primary">Войти</v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  $_veeValidate: {
    validator: 'new'
  },

  name: 'Auth',

  data () {
    return {
      user: {
        login: '',
        password: ''
      },
      dictionary: {
        custom: {
          login: {
            required: () => '*Это поле является обязательным'
          },
          password: {
            required: () => '*Это поле является обязательным'
          }
        }
      }
    }
  },

  mounted () {
    this.$validator.localize('en', this.dictionary)
  },

  methods: {
    async login () {
      const valid = await this.$validator.validate()
      if (valid) {
        await this.$store.dispatch('login', this.user)
        await this.$store.dispatch('getCurrentUser')
      }
    }
  }
}
</script>

<style lang='scss' scoped>

</style>
