<template lang="pug">
div(color="#F7F3E8")
    v-container
        v-card(class="ma-4")

            div.display-1.pt-4.ma-4.font-weight-bold {{ recipetitle }}
            
            v-divider.ma-4

            v-layout.ma-4
                div.ml-6.my-auto.caption Tags: 
                div(v-for="list in tags")
                    v-btn.ma-1.caption(@click="totagpage" small rounded) {{list}}

            div.mx-4
                v-card.mx-12
                    v-img(
                        :src="topimg"
                        max-height="40vh"
                    )

            //材料を表示するコンポーネント
            #MatelialsArea
                Materials(
                    class="ma-10 my-4 pb-4"
                    :list= "mateliallist"
            )
            //レシピを表示するコンポーネント
            #RecipeArea
            Recipe(
                class="ma-10 my-4 pb-10"
                :list="recipelist"
            )

            .text-center.pt-10.pb-12
                v-btn.title(color="#FFB618" @click="toback") 戻る
</template>

<script>
import Recipe from '..//components/Recipe'
import Materials from '..//components/Materials'

export default{
    components: {
        Recipe,
        Materials
    },
    props:{
        recipeid: Number
    },
    data: function(){
        return{
            recipetitle:'冷やしキムチラーメン',
            topimg: "https://imgfp.hotp.jp/IMGH/21/64/P028842164/P028842164_480.jpg",
            mateliallist: [
                { name: 'お肉', serving: "一本"},
                { name: '野菜', serving: "日本"},
                { name: '魚', serving: "三枚"},
            ],
            recipelist: [
                { message: '肉を焼く' },
                { message: '野菜を炒める' },
                { message: '魚を焼く' },
            ],
            tags: ['天気の子', 'あは', 'あはは']
        }
    },
    methods: {
        toback: function(){
        },
        totagpage: function(){
            this.$router.push("/tagpage")
        }
    }
}
</script>