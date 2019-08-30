<template lang="pug">
div(color="#F7F3E8")
  v-container
    v-card(class="ma-4")
      //料理の名前を入れる##
      div.headline.ml-2.mb-1 {{ time }}
      div.display-1.ml-4.font-weight-bold お題: {{ recipetitle }}
      div.body-2.mr-4.text-right {{ total_member }}人が参加しています
      .text-right.ma-4
        v-btn.title(color="#FFB618" @click="tovote") 投票ページへ
      
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

      
      .text-center.pt-10.pb-12
        div(v-if="isLoggingin == true")
          v-btn.title(color="#FFB618" @click="toanswer") コンテストに提出する
        div(v-else)
          div コンテスト参加にはログインが必要です。
          v-btn.title(color="#FFB618" @click="tologin") ログイン

</template>

<script>
import Recipe from '..//components/Recipe'
import Materials from '..//components/Materials'

export default{
  components: {
    Recipe,
    Materials
  },
  data: function(){
    return{
      time: "7:00 ~ 8:00",
      recipetitle:'冷やしキムチラーメン',
      total_member: 1,
      jsonmaterials: '[{"name":"タピオカ","serving":"1kg"},{"name":"天気の子","serving":"10000"},{"name":"肉","serving":"焼肉"},{"name":"あは","serving":"いひ"}]',
      jsonrecipes: '[{"message":"肉を焼く"},{"message":"食べる"},{"message":"炒める"},{"message":"あは"}]',
    }
  },
  props: {
    isLoggingin: Boolean,
    userid: Number
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
    },
  methods: {
    tovote: function(){
      this.$router.push("/votepage")
    },
    toanswer: function(){
      this.$router.push("/answerpage")
    },
    tologin: function(){
      this.$router.push("/signin")
    }
  }
}
</script>