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
        Materials(
          class="ma-10 my-4 pb-4"
          :list= "mateliallist"
        )
      //コンテストレシピを表示するコンポーネント
      #ResipeArea
        Resipe(
          class="ma-10 my-4 pb-10"
          :list="resipelist"
        )

      .text-center.pt-10.pb-12
        v-btn.title(color="#FFB618" @click="toanswer") コンテストに提出する
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
      total_member: 1,
      mateliallist: [
        { message: 'お肉' },
        { message: '野菜' },
        { message: '魚' },
      ],
      resipelist: [
        { message: '肉を焼く' },
        { message: '野菜を炒める' },
        { message: '魚を焼く' },
      ]
    }
  },
  methods: {
    tovote: function(){
      this.$router.push("/votepage")
    },
    toanswer: function(){
      this.$router.push("/answerpage")
    }
  }
}
</script>