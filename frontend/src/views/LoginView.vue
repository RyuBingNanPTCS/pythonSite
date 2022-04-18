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
      console.log("login");
      console.log(this.userId);
      axios.post("/login/login", {
        "username": this.userId,
        "password": this.password
      })
      .then(response => {
        console.log("response")
        console.log(response)
        this.$router.push({path: '/login/manage'});
      })
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