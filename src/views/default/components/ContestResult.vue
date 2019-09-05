<template lang="pug">
    v-card(elevation="0")
        //v-card-title.font-logotype 前回コンテスト結果

        .text-center.ma-4.pb-4
          v-btn.title(color="#FFB618" @click="torankingpage") 前回のコンテスト結果を見る
</template>

<script>
import axios from 'axios'
import Cookies from 'js-cookie'

export default {
  methods:{
    torankingpage: function(){
      Cookies.set('contestid', String(this.contestid))
      this.$router.push("/rankingpage")
    }
  },
  props: {
    contestid: String
  }
}
</script>

<style>
    @font-face {
        font-family: 'LogoType';
        src: url('../../../fonts/07LogoTypeGothic7.ttf') format('TrueType');
    }

    @font-face {
        font-family: 'Harenosora';
        src: url('../../../fonts/Harenosora.otf') format('OpenType');
    }

    .font-logotype{
        font-family: 'LogoType';
    }
    .font-harenosora{
        font-family: 'Harenosora';
    }
</style>