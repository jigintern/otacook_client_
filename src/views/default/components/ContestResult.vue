<template lang="pug">
    v-card
        v-card-title 前回コンテスト結果

        .text-center.ma-4.pb-4
          v-btn.title(color="#FFB618" @click="torankingpage") 結果を見る
</template>

<script>
import axios from 'axios'

export default {
  methods:{
    torankingpage: function(){
      this.$router.push("/rankingpage")
    },
  }
}
</script>