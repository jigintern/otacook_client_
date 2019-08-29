<template lang="pug">
div(color="#F7F3E8")
  v-container
    v-card(class="ma-4")

        div.display-2.ma-4.pt-4 レシピ投稿

        v-card.ma-4
            div.headline.ma-8.mb-0.pt-4 料理名
            v-text-field.ma-8.mt-0.pb-4(
                :counter="30"
                value=""
                v-model="resipetitle"
                :rules="[rules.required, rules.namemax]"
                label="料理名を入力！"
                required)

        v-card.ma-4
            .headline.ma-8.mb-0.pt-4 材料リスト
            v-row(v-for="list in matelials" v-bind="list")
                v-text-field.ml-12.mr-4(
                    :counter="30"
                    value=""
                    v-model="list.material"
                    :rules="[rules.required]"
                    label="材料"
                    required
                )
                v-text-field.mr-12.ml-4(
                    :counter="30"
                    value=""
                    v-model="list.serving"
                    :rules="[rules.required]"
                    label="分量"
                    required
                )
            .text-right.mt-6.mr-12.pb-4
                v-btn.mr-4(@click="mateliallistdell" color="#FFB618") リストリセット
                v-btn(@click="mateliallistadd" color="#FFB618") リスト追加

            div(v-for="list in matelials" v-bind="list") {{list.material}} {{list.serving}}
        
        v-card.ma-4
            .headline.ma-8.mb-0.pt-4 レシピ
            
            div(v-for="list in resipe")
                v-text-field.mx-8.mt-0(
                    :counter="50"
                    v-model="list.message"
                    :rules="[rules.required]"
                    label="レシピを入力！"
                    required
                )
            .text-right.mt-6.mr-12.pb-4
                v-btn.mr-4(@click="resipelistdell" color="#FFB618") レシピリセット
                v-btn(@click="resipelistadd" color="#FFB618") レシピ追加

        v-card.ma-4
            div.headline.ma-8.mb-0.pt-4 写真
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

export default{
  data: function(){
    return{
      resipetitle:"",
      matelials: [
          { matelial: "", serving: ""}
      ],
      resipe: [
          {message: ""}
      ],
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
    mateliallistadd: function(){
        this.matelials.push(
            {material:"", serving: ""}
        )
    },
    mateliallistdell: function(){
        this.matelials = [{material:"", serving: ""}]
    },
    resipelistadd: function(){
        this.resipe.push(
            {message: ""}
        )
    },
    resipelistdell: function(){
        this.resipe = [{message: ""}]
    }
  }
}
</script>