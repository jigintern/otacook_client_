<template lang="pug">
div(color="#F7F3E8")
  v-container
    v-card(class="ma-4")
      //料理の名前を入れる##
      div.headline.ml-2.mb-1 {{ time }}
      div.display-1.ml-4.font-weight-bold お題: {{ recipetitle }}

      div.headline.ma-8.mb-0 料理名
      v-text-field.ma-8.mt-0(
        :counter="30"
        value=""
        v-model="title"
        :rules="[rules.required, rules.namemax]"
        label="料理名を入力！"
        required)

      div.headline.ma-8.mb-0 コメント
      v-textarea.ma-8.mt-0(
        :counter="140"
        value=""
        v-model="comment"
        :rules="[rules.required, rules.commentmax]"
        label="料理について自由に書いてください！")
        required

      div.headline.ma-8.mb-0 写真
      v-file-input.ma-8.mt-0(
        accept="image/*"
        label="写真を選択してください！")

      .text-center.pt-10.pb-12
        //div.text-color 投票済みです
        div(v-if="isLoggingin == true")
          v-btn.title(color="#FFB618" @click="toquestion") 送信
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
      title: "",
      comment: "",
      rules: {
        required: value => !!value || '入力必須項目です。',
        namemax: v => v.length <= 30 || '30文字以内でオナシャス',
        commentmax: v => v.length <= 140 || '140文字以内でオナシャス',
      },
    }
  },
  props:{
    isLoggingin: Boolean,
    userid: Number
  },
  methods: {
    toquestion: function(){
      this.$router.push("/questionpage")
    },
    tologin: function(){
      this.$router.push("/loginpage")
    },
  }
}
</script>