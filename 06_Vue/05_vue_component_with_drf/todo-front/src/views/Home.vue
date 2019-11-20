<template>
  <div class="home">
    <h1>Todo with Django</h1>
    <TodoInput @createTodo="createTodo"/>
    <TodoList :todos="todos"/>
  </div>
</template>

<script>
import router from "../router"
import TodoList from "@/components/TodoList"
import TodoInput from "@/components/TodoInput"

import axios from 'axios'
// Object destructuring
import { mapGetters } from 'vuex'
// import jwtDecode from 'jwt-decode' // auth.js에 위치함

export default {
  name: 'home',
  components: {
    TodoList,
    TodoInput,
  },
  data() {
    return {
      todos: []
    }
  },
  computed: {
    ...mapGetters([
      'isLoggedIn',
      'requestHeader',
      'userId'
    ])
  },
  methods: {
    checkLoggedIn() {
      // this.$session.start()
      // if ( !this.$session.has('jwt') ) {
      
      if (!this.isLoggedIn) {
        router.push('/login')
      }
    },
    getTodos() {
      // this.$session.start()
      // const token = this.$session.get('jwt')
      // console.log(token)
      // const requestHeader = {
      //   headers: {
      //     Authorization: 'JWT ' + token
      //   }
      // }
      // const user_id = jwtDecode(token).user_id
      // console.log(jwtDecode(token))

      
      axios.get(`http://127.0.0.1:8000/api/v1/users/${this.userId}/`, this.requestHeader) // user_id -> this.userId, requestHeader -> this.requestHeader
      .then(res => {
        this.todos = res.data.todo_set
        console.log(res)
      })
      .catch(err => {
        console.log(err)
      })
    },
    createTodo(title) {
      // this.$session.start()
      // const token = this.$session.get('jwt')
      // const requestHeader = {
      //   headers: {
      //     Authorization: 'JWT ' + token
      //   }
      // }
      // const user_id = jwtDecode(token).user_id


      // requestForm -> blank Object
      const requestForm = new FormData()
      requestForm.append('user', this.userId) // user_id -> this.userId
      requestForm.append('title', title)

      axios.post('http://127.0.0.1:8000/api/v1/todos/', requestForm, this.requestHeader)
      .then(res => {
        this.todos.push(res.data)
      })
      .catch(err => {
        console.log(err)
      })
    }
  },
  mounted() {
    this.checkLoggedIn()
    this.getTodos()
  }
}
</script>
