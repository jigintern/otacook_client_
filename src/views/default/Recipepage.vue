<template lang="pug">
div(color="#F7F3E8")
    v-container
        v-card(class="ma-4")

            div.display-1.pt-4.ma-4.font-weight-bold {{ recipetitle }}
            
            v-divider.ma-4

            v-layout.ma-4
                div.ml-6.my-auto.caption Tags: 
                div(v-for="list in tagslist")
                    v-btn.ma-1.caption(@click="totagpage" small rounded color="#FFCC51") {{list.message}}

            div.mx-4
                v-card.mx-12
                    v-img(
                        :src="topimg"
                        max-height="40vh"
                    )

            //材料を表示するコンポーネント
            #materialsArea
                Materials(
                    class="ma-10 my-4 pb-4"
                    :list= "materiallist"
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
    computed: {
        materiallist: function(){
            var array = JSON.parse(this.jsonmaterials)
            return array
        },
        recipelist: function(){
            var array = JSON.parse(this.jsonrecipes)
            return array
        },
        tagslist: function(){
            var array = JSON.parse(this.jsontags)
            return array
        }
    },
    data: function(){
        return{
            recipetitle:'冷やしキムチラーメン',
            topimg: "https://imgfp.hotp.jp/IMGH/21/64/P028842164/P028842164_480.jpg",
            jsonmaterials: '[{"name":"タピオカ","serving":"1kg"},{"name":"天気の子","serving":"10000"},{"name":"肉","serving":"焼肉"},{"name":"あは","serving":"いひ"}]',
            jsonrecipes: '[{"message":"肉を焼く"},{"message":"食べる"},{"message":"炒める"},{"message":"あは"}]',
            jsontags: '[{"message":"天気の子"},{"message":"タピオカ"},{"message":"焼肉"}]',
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