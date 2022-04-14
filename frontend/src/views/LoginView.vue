<template>
  <div class="login">
    <input v-model="userId" />
    <input v-model="password" />

    <button @click="login()" :disabled="!userId">ログイン</button>
  </div>
</template>

<script>
import axios from 'axios'

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
  },
  mounted() {
    console.log("mounted");
    axios.request("/login2")
      .then(response => console.log(response))
      .catch(error => console.log(error))
    //    fetch('http://localhost:8081/sample/demo')
    console.log(this.users);
  }
}
</script>