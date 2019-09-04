<template lang="pug">
div(color="#F7F3E8")
  v-container
    v-card(class="ma-4")
      //料理の名前を入れる##
      div.headline.ml-2.mb-1 {{ time }}
      div.display-1.ml-4.font-weight-bold お題: {{ title }}
      div.body-2.mr-4.text-right {{ total_member }}人が解答済みです
      .text-right.ma-4
        v-btn.title(
          color="#FFB618"
          @click="tovote"
          v-if="isvoteactive === true"
        ) 投票ページへ
      
      //コンテスト材料を表示するコンポーネント
      #materialsArea
        Materials(
          class="ma-10 my-4 pb-4"
          :list= "materiallist"
        )
      //コンテストレシピを表示するコンポーネント
      #RecipeArea
        Recipe(
          class="ma-10 my-4 pb-10"
          :list="recipelist"
        )

      
      .text-center.pt-10.pb-12(v-if="isansweractive == true")
        div(v-if="isLoggingin == true")
          v-btn.title(color="#FFB618" @click="toanswer") コンテストに提出する
        div(v-else)
          div コンテスト参加にはログインが必要です。
          v-btn.title(color="#FFB618" @click="tologin") ログイン

</template>

<script>
import Recipe from '..//components/Recipe'
import Materials from '..//components/Materials'
import Cookies from 'js-cookie'
import axios from 'axios'

export default{
  components: {
    Recipe,
    Materials
  },
  data: function(){
    return{
      time: "",
      title:'',
      total_member: 'n',
      jsonmaterials: '[]',
      jsonrecipes: '[]',
      status: 0,
      isvoteactive: false,
      isansweractive: false
    }
  },
  props: {
    isLoggingin: Boolean,
    userid: Number,
  },
  computed: {
        materiallist: function(){
            var array = JSON.parse(this.jsonmaterials)
            return array
        },
        recipelist: function(){
            var array = JSON.parse(this.jsonrecipes)
            return array
        },
        contestid: function(){
            var contestid = Cookies.get('contestid')
            return contestid
        }
  },
  mounted: function(){
    let self = this
    //実行中のコンテストの状態を取得
    axios.get('https://t1.intern.jigd.info/flask/api/contest/now')
    .then(function (response) {
      var data = response.data
      console.log(data["status"])
      self.status = data["status"]
      if(self.status == "1"){
          self.isansweractive = true
      }
      if(self.status == "2"){
          self.isvoteactive = true
      }
    })

    //情報取得
    axios.get('https://t1.intern.jigd.info/flask/api/contest/info/'+String(self.contestid))
    .then(function (response) {
        var data = response.data
        console.log(data["title"])
        console.log(data["time"])
        console.log(data["votetime"])
        self.title = data["title"]
        self.time = data["time"]
        self.votetime = data["votetime"]
    })

    //材料リスト
    axios.get('https://t1.intern.jigd.info/flask/api/contest/materialsinfo/'+String(self.contestid))
    .then(function (response) {
        self.jsonmaterials = "[" + response.data + "]"
    })

    axios.get('https://t1.intern.jigd.info/flask/api/contest/getentryusertotal')
    .then(function (response) {
        self.total_member = response.data
    })


    //レシピリスト
    axios.get('https://t1.intern.jigd.info/flask/api/contest/recipesinfo/'+String(self.contestid))
    .then(function (response) {
        self.jsonrecipes = "[" + response.data + "]"
    })
  },
  methods: {
    tovote: function(){
      this.$router.push("/votepage")
    },
    toanswer: function(){
      Cookies.set('contestid', String(this.contestid))
      this.$router.push("/answerpage")
    },
    tologin: function(){
      this.$router.push("/signin")
    }
  }
}
</script>