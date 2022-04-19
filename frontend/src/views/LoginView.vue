<template>
  <div class="login">
    <input v-model="userId" placeholder="IDを入力してください。"/>
  </div>
  <div>
    <input v-model="password" placeholder="PWを入力してください。"/>
  </div>
  <div>
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
        this.$router.push({path: '/home'});
      })
      .catch(response => {
        console.log(response)
        console.log("error")
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