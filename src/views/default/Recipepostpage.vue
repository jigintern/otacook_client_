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
                v-model="recipetitle"
                :rules="[rules.required, rules.namemax]"
                label="料理名を入力！"
                required)

        v-card.ma-4
            .headline.ma-8.mb-0.pt-4 材料リスト
            v-row(v-for="list in materials")
                v-text-field.ml-12.mr-4(
                    :counter="30"
                    value=""
                    v-model="list.name"
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
                v-btn.mr-4(@click="materiallistdell" color="#FFB618") リストリセット
                v-btn(@click="materiallistadd" color="#FFB618") リスト追加

        //材料を表示するコンポーネント
        #materialsArea
            Materials(
                class="ma-10 my-4 pb-4"
                :list= "materiallist"
        )
        div {{this.jsonmaterials}}

        v-card.ma-4
            .headline.ma-8.mb-0.pt-4 レシピ
            
            div(v-for="list in recipes")
                v-text-field.mx-8.mt-0(
                    :counter="50"
                    v-model="list.message"
                    :rules="[rules.required]"
                    label="レシピ"
                    required
                )
            .text-right.mt-6.mr-12.pb-4
                v-btn.mr-4(@click="recipelistdell" color="#FFB618") レシピリセット
                v-btn(@click="recipelistadd" color="#FFB618") レシピ追加

        v-card.ma-4
            div.headline.ma-8.mb-0.pt-4 写真
            v-file-input.ma-8.mt-0(
                accept="image/*"
                label="写真を選択してください！")

        v-card.ma-4
            .headline.ma-8.mb-0.pt-4 タグ
            div(v-for="list in tags")
                v-text-field.mx-8.mt-0(
                    :counter="50"
                    v-model="list.message"
                    :rules="[rules.required]"
                    label="タグ"
                    required
                )
            .text-right.mt-6.mr-12.pb-4
                v-btn.mr-4(@click="taglistdell" color="#FFB618") タグリセット
                v-btn(@click="taglistadd" color="#FFB618") タグ追加

        .text-center.pt-10.pb-12
            div(v-if="isLoggingin == true")
                v-btn.title(color="#FFB618" @click="totop") 送信
            div(v-else)
                div レシピ投稿にはログインが必要です。
                v-btn.title(color="#FFB618" @click="tologin") ログイン
</template>

<script>
import Materials from '..//components/Materials'
import { returnStatement } from 'babel-types';
export default{
    components: {
        Materials
    },
    data: function(){
        return{
        recipetitle:"",
        materials: [
            { name: "", serving: ""}
        ],
        recipes: [
            {message: ""}
        ],
        tags: [
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
    computed: {
        jsonmaterials: function(){
            var jsontext = JSON.stringify(this.materials)
            //console.log(jsontext)
            return jsontext
        },
        jsonrecipes: function(){
            var jsontext = JSON.stringify(this.recipes)
            //console.log(jsontext)
            return jsontext
        },
        jsontags: function(){
            var jsontext = JSON.stringify(this.tags)
            //console.log(jsontext)
            return jsontext
        },
        materiallist: function(){
            var array = JSON.parse(this.jsonmaterials)
            return array
        },
    },
    methods: {
        totop: function(){
            this.$router.push("/")
        },
        tologin: function(){
        this.$router.push("/loginpage")
        },
        
        materiallistadd: function(){
            this.materials.push(
                {name:"", serving: ""}
            )
        },
        materiallistdell: function(){
            this.materials = [{name:"", serving: ""}]
        },
        recipelistadd: function(){
            this.recipes.push(
                {message: ""}
            )
        },
        recipelistdell: function(){
            this.recipes = [{message: ""}]
        },
        taglistadd: function(){
            this.tags.push(
                {message: ""}
            )
        },
        taglistdell: function(){
            this.tags = [{message: ""}]
        },
    }
}
</script>