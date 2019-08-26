<template lang="pug">
v-conteiner
  v-card(class="ma-4")
    //料理の名前を入れる##
    div.headline.ml-2.mb-1 {{ time }}
    div.display-1.ml-4.font-weight-bold お題: {{ resipetitle }}
    div.body-2.mr-2.text-right {{ total_member }}人が参加しています
    
    //コンテストレシピを表示するコンポーネント
    #ContestResipeArea
      Contestresipe(class="ma-4")

        //サーバーで生成したHTML埋め込み
        //iframe(
          width="90%"
          height="1000px"
          crolling="no"
          src="http://localhost:8080/#/"
        //)
</template>

<script>
import Contestresipe from './components/Contestresipe'

export default{
  components: {
    Contestresipe
  },
  data: function(){
    return{
      time: "7:00 ~ 8:00",
      resipetitle:'冷やしキムチラーメン',
      total_member: 1
    }
  }
}
</script>