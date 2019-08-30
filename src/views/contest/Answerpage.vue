<template lang="pug">
div(color="#F7F3E8")
  v-container
    v-card(class="ma-4")
      //料理の名前を入れる##
      div.headline.ml-2.mb-1 {{ time }}
      div.display-1.ml-4.font-weight-bold お題: {{ resipetitle }}

      div.headline.ma-8.mb-0 料理名
      v-text-field.ma-8.mt-0(
        :counter="30"
        value=""
        v-model="name"
        :rules="[rules.required, rules.namemax]"
        label="料理名を入力！"
        required)

      div.headline.ma-8.mb-0 コメント
      v-textarea.ma-8.mt-0(
        :counter="140"
        value=""
        v-model="outline"
        :rules="[rules.required, rules.commentmax]"
        label="料理について自由に書いてください！")
        required

      div.headline.ma-8.mb-0 写真
      //input(
        type="file"
      //)
      v-file-input.ma-8.mt-0(
        @change="selectfile"
        accept="image/*"
        label="写真を選択してください！"
        )

      .text-center.pt-10.pb-12
        div(v-if="isLoggingin == true")
          div.red--text.mb-4 {{ error }}
          v-btn.title(color="#FFB618" @click="toquestion") 送信
        div(v-else)
          div コンテスト参加にはログインが必要です。
          v-btn.title(color="#FFB618" @click="tologin") ログイン
</template>

<script>
import Recipe from '..//components/Recipe'
import Materials from '..//components/Materials'
import axios from 'axios'

export default{
  components: {
    Recipe,
    Materials
  },
  data: function(){
    return{
      time: "7:00 ~ 8:00",
      resipetitle:'冷やしキムチラーメン',
      total_member: 1,
      uploadFile: null,
      name: "",
      outline: "",
      error: "",
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
  created: function(){
    //useridをサーバーに送って投票状況を確認する？
  },
  methods: {
    selectfile :function(e){
      console.log(e)
      var file = e.data
      this.uploadFile = file
    },
    toquestion: function(){
      if(this.name=="" || this.outline==""){
        this.error="すべての項目を入力してから送信してください！"
      }else{
        this.error = ""
        const params = new URLSearchParams()
        params.append('qi', 1)
        params.append('ui', 3)
        params.append('cn', this.name)
        params.append('co', this.outline)
        axios.post('http://localhost:8080/answer/insert', params)
          .catch(error => {
            this.error = "送信に失敗しました"
            window.alert("送信に失敗しました")
          })
          .then(Response => {
            this.$router.push('/')
          })  
      }
    },
    tologin: function(){
      this.$router.push("/loginpage")
    },
  }
}
</script>