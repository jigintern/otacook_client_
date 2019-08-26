<template lang="pug">
  v-container
      //v-layout
      v-flex
        //料理の名前を入れる##
        div.display-1.mt-1 料理名: {{ resipetitle }}
          v-divider
        //コンテストレシピを表示するコンポーネント
        //#ContestResipeArea
          Contestresipe
        //サーバーで生成したHTML埋め込み
        iframe(
          width="90%"
          height="1000px"
          crolling="no"
          src="http://localhost:8080/#/"
        )
</template>

<script>
import Contestresipe from './components/Contestresipe'

export default{
  components: {
    Contestresipe
  },
  data: function(){
    return{
      resipetitle:'冷やしキムチラーメン'
    }
  }
}
</script>