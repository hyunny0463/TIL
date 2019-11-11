# Vue.js



기존에는

링크(a tag)를 사용해서 새로운 페이지를 받아온다

모든 리소스를 (HTML, CSS, JS, Image)를 서버에서 가져온다



AJAX(비동기 처리 라이브러리)

비동기 요청

: 앞의 수행이 뒤의 수행을 막지 않는다!

요청을 보내 응답이 올 때까지 기다렸다가 응답이 오면 **그-때** 처리한다. <콜백함수의 핵심>



왜 ?

사용자가 언제 이벤트를 발생 시킬 지 알 수 없다.



모든 페이지가 아닌 특정 부분(좋아요)만 비동기 요청으로 처리



SPA(Single Page Application)

: 모든 정적 리소스는 **최초 1번**만 받음

새로운 페이지 요청시 페이지 갱신에 **필요한 데이터만** 전달 받음



장점

사용자 경험(UX) 극대화

불필요한 서버 자원 사용x



SPA

구글에서 angular.js

페이스북에서 react.js

두 개의 장점을 합해 만든 것이 Vue.js



Django -> MVC(MTV)

Vue js -> MVVM(Model View(눈으로 보는 DOM) View Model)



![image](https://user-images.githubusercontent.com/22102664/68168447-27480580-ffac-11e9-91d5-72f102bf3b69.png)



시작하기

```html
<body>
    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
    <script>
        // Vue 코드가 작성될 곳
    </script>
</body>
```



DOM 과 vue instance가 binding 되어있다. 마운트가 되었다라고도 말한다.



Vue Styling

```html
<body>
    <div v-bind:style="{ color:activeColor, fontSize:fontSize + 'px' }">
    Styling Test
	<script>
        data: {
            activeColor: 'red',
        }
	</script>
</body>
```



todo list

```html
<li v-for="todo in todos" v-bind:class="{ completed: todo.completed }">
    <input type="checkbox" v-model=todo.completed>
    <span>{{ todo.content }}</span>
</li>
<script>
    const app = new Vue({
      // DOM(View)와 Vue instance(View-Model)을 연결(mount)
      el: '#app',
      data: {
        todos: [
          {
            content: '점심 메뉴 고민하기',
            completed: true,
          },
        ]
      }
    })
</script>
```



```
v-if : 조건에 맞지 않으면 랜더링 조차 하지않음
v-show : 일단 랜더링 하고 false 옵션이면 display: none 속성을 넣어줌
```



```
# shortcut
v-bind 는 : 만 찍음
v-on 은 @ 만 찍고 사용가능
```





this 키워드

function 은 전역을 가리킨다, nested 하면 window를 가리킨다.

arrow function 에서의 this는 상위 스코프를 가리킨다.



전역에서 호출하면 this는 window를 반환한다.

```javascript
const greeting = function() {
	console.log(this)
}

greeting()
=> Window {parent: Window, postMessage: ƒ, blur: ƒ, focus: ƒ, close: ƒ, …}
```



you 라는 object 안에서 호출되므로 you를 가리킨다.

```javascript
const you = {
	name: 'justin',
	greeting
}

you.greeting()
=> {name: "justin", greeting: ƒ}
```



arrow function 을 쓰면 this는 상위 객체를 가리킨다.

```javascript
const arrowGreeting = () => {
	console.log(this)
}
const me = {
	name: 'me',
	arrowGreeting
}
```

```javascript
arrowGreeting()
=> window {parent: Window, postMessage: ƒ, blur: ƒ, focus: ƒ, close: ƒ, …}
me.arrowGreeting()
=> window {parent: Window, postMessage: ƒ, blur: ƒ, focus: ƒ, close: ƒ, …}
```



```javascript
const num = {
	numbers: [1],
	print: function() {
		console.log(this)
		console.log(this.numbers)
		this.numbers.forEach(function(num) {
			console.log(num)
			console.log(this)
        })
    }
}

num.print()
=> {numbers: Array(1), print: ƒ}
=> [1]
=> 1
=> Window {parent: Window, postMessage: ƒ, blur: ƒ, focus: ƒ, close: ƒ, …}
```





```javascript
const num2 = {
	numbers: [1],
	print: function() {
		console.log(this)
		console.log(this.numbers)
		this.numbers.forEach( num => {
			console.log(num)
			console.log(this)
        })
    }
}

num2.print()
=> {numbers: Array(1), print: ƒ}
=> [1]
=> 1
=> {numbers: Array(1), print: ƒ}
```



## webpack

node.js 를 사용할 때 많은 패키지를 관리해주는 친구 npm (node package manager)

```
$ npm init
```



```
$ npm install vue
```



커맨드 라인에서 디벨로퍼 기능을 사용하도록 웹팩을 설치

```
$ npm i webpack webpack-cli -D
```



웹팩을 설정하는 파일 - webpack.config.js 설정

```
$ touch webpack.config.js
```

```js
const VueLoaderPlugin = require('vue-loader/lib/plugin')
const path = require('path')

module.exports = {
  // entry: 여러 개의 js 파일의 시작점. (웹팩이 파일을 읽기 시작하는 지점)
  entry: {
    app: path.join(__dirname, 'src', 'main.js')
  },
  // module: 웹팩은 js만 변환이 가능하기 때문에 html, css 같으 모듈을 통해서 웹팩이 이해할 수 있는 것으로 변환을 해주는 곳.
  module: {
    rules: [
      {
        test: /\.vue$/,
        use: 'vue-loader',
      }
    ]
  },
  // plugins: 웹팩을 통해서 번들된 결과물을 추가적으로 처리하는 부분(옵션)
  plugins: [
    new VueLoaderPlugin(),
  ],
  // 여러 개의 js 파일을 하나로 만들어낸 결과물
  output: {
    filename: 'app.js',
    path: path.join(__dirname, 'dist')
  },
}
```



```
$ npm install vue-loader vue-template-compiler -D
```

```js
// main.js
// Vue instanace 를 최종적으로 만드는 파일
// 연결되어 있는 모든 JS 파일의 최상단에 존재하는 파일

// 1. npm install vue -> 추가(내가 만든 파일 아님)
import Vue from 'vue'
// 2. 최상위 컴포넌트 App.vue를 추가(내가 만들 파일)
import App from './App.vue'

// 3. Vue instance 를 만들어 DOM 에 연결
new Vue({
  render: h => h(App),
}).$mount('#app')

/*
new Vue({
  render: function(createElement) {
    return createElement(App)
  }
})
*/
```



package.json에 webpack 추가

```json
"scripts": {
    "build": "webpack"
},
```



빌드하기

```
$ npm run build
```



.vue 파일에서 사용할 css, vue-style 로더 설치

```
$ npm install vue-style-loader css-loader -D
```



webpack.config.js 파일에서 등록

```js
module: {
    rules: [
      {
        test: /\.css$/,
        use: ['vue-style-loader', 'css-loader']
      }
    ]
  },
```



Webpack은 이렇게 할게 많지만 정리할 필요가 없었따! 안쓸거니깐



## CLI(Command Line Interface)

설치하기

```
$ npm i -g @vue/cli
```



프로젝트 만들기(default 선택)

```
$ vue create todo-vue-cli

Vue CLI v4.0.5
? Please pick a preset:
> default (babel, eslint)
  Manually select features
```



프로젝트로 이동한 후 실행

```
$ cd todo-vue-cli
$ npm run serve
```





## YouTube Project

![image](https://user-images.githubusercontent.com/12672315/68556376-60351e00-0475-11ea-9ac9-a01e3de03e92.png)

![image](https://user-images.githubusercontent.com/12672315/68556359-527f9880-0475-11ea-9ca7-9fd04034c530.png)

등록한다

```vue
<!-- SearchBar.vue -->
<script>
    export default {
        name: 'SearchBar',
    }
</script>
```



불러온다

```vue
<!-- App.vue -->
<script>
    import SearchBar from "./components/SearchBar"
    
    export default {
        name: 'app',
        components: {
            SearchBar,
        }
    }
</script>
```



사용자 컴포넌트를 사용한다

```vue
<!-- App.vue -->
<template>
	<div>
        <search-bar></search-bar>
    </div>
</template>
```



console.log를 찍고 싶은데 에러가 난다?

```json
"eslintConfig": {
    "rules": {
      "no-console": "off" <<< 추가
    },
    "parserOptions": {
      "parser": "babel-eslint"
    }
  }
}
```



자식에서 부모로 데이터를 올려주는 emitting event

```vue
<!-- SearchBar.vue -->
<script>
export default {
  name: 'SearchBar',
  methods: {
    onInput(e) {
      this.$emit('inputChange', e.target.value)
    }
  },
}
</script>
```



부모에서 올려주는 데이터 받기

```vue
<!-- App.vue -->
<template>
	<div>
        <search-bar @inputChange="onInputChange"></search-bar>
    </div>
</template>

<script>
import SearchBar from "./components/SearchBar"

export default {
  name: 'app',
  components: {
    SearchBar,
  },
  methods: {
    onInputChange(inputValue) {
      console.log(inputValue)
    }
  }
}
</script>
```



google api 사용하기

```
https://console.developers.google.com
```

으로 이동 후 youtube data api v3 사용하기



사용자 인증 정보 만들기

해당 키를 App.vue 에서 `const API_KEY = ''` 에 넣어줌



axios 설치하기

```
$npm i axios
```



axios 모듈 import

```
import axios from 'axios'
```



youtube 검색 데이터 받기

```vue
export default {
  methods: {
    onInputChange(inputValue) {
      axios.get(API_URL, {
        params: {
          // 1. (required) 위에서 가져온 키
          key: API_KEY,
          // 2. (option) 특정 리소스 유형만 검색(channel, playlist, video)
          type: 'video',
          // 3. (required) API 응답이 포함하는 search 리소스 속성
          part: 'snippet',
          // 4. (option) string -> 검색어(사용자에게 받은 input value)
          q: inputValue
        }
      })
      .then((response) => {
        // console.log(response)
        this.videos = response.data.items
      })
    }
  }
}
```



key 나누기

```
.env.local
VUE_APP_YOUTUBE_API_KEY=''
```



```vue
<!-- 환경변수 파일의 데이터 불러오기 -->
<!-- App.vue -->
const API_KEY = process.env.VUE_APP_YOUTUBE_API_KEY

```



App.vue에서 VideoList로 데이터 내려주기

```
<video-list :videos="videos"></video-list>
```



VideoList에서 데이터 받기

```vue
<!-- VideoList.vue -->
export default {
  name: 'VideoList',
  props: {
    videos: {
      type: Array,
      required: true,
    }
  }
}
```

