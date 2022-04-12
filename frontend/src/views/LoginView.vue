<template>
  <div class="login">
    <input v-model="userId" />
    <input v-model="password" />

    <button @click="login()" :disabled="!userId">ログイン</button>
  </div>
</template>

<script>
export default {
  data () {
    return {
      userId: '',
      password: ''
    }
  },
  methods: {
    login () {
      this.$store.commit('setUserId', this.userId) // (1)
      this.$store.commit('setPassword', this.password) 
      this.$router.push(this.$route.query.redirect) // (2)
    }
  }
}
</script>