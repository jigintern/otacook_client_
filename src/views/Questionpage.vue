<template lang="pug">
  v-container
      //v-layout
      v-flex
        //料理の名前を入れる##
        div.display-1.mt-1 料理名: {{ resipetitle }}
        //コンテストレシピを表示するコンポーネント
        #ContestResipeArea
          Contestresipe
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