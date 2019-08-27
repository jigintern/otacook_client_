<template lang="pug">
div(color="#F7F3E8")
  v-container
    v-card(class="ma-4")
      //料理の名前を入れる##
      div.headline.ml-2.mb-1 {{ time }}
      div.display-1.ml-4.font-weight-bold お題: {{ resipetitle }}
      div.body-2.mr-2.text-right {{ total_member }}人が参加しています
      .text-right.ma-4
        v-btn.title(color="#FFB618" @click="tovote") 投票ページへ
      
      //コンテスト材料を表示するコンポーネント
      #MatelialsArea
        Materials(class="ma-10 my-4 pb-4")
      //コンテストレシピを表示するコンポーネント
      #ResipeArea
        Resipe(class="ma-10 my-4 pb-10")

      .text-center.pt-10.pb-12
        v-btn.title(color="#FFB618" @click="toanswer") コンテストに提出する

        //サーバーで生成したHTML埋め込み
        //iframe(
          width="90%"
          height="1000px"
          crolling="no"
          src="http://localhost:8080/#/"
        //)
</template>

<script>
import Resipe from '..//components/Resipe'
import Materials from '..//components/Materials'

export default{
  components: {
    Resipe,
    Materials
  },
  data: function(){
    return{
      time: "7:00 ~ 8:00",
      resipetitle:'冷やしキムチラーメン',
      total_member: 1
    }
  },
  methods: {
    tovote: function(){
      this.$router.push("/vote")
    },
    toanswer: function(){
      this.$router.push("/answer")
    }
  }
}
</script>