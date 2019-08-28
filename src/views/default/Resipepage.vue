<template lang="pug">
div(color="#F7F3E8")
    v-container
        v-card(class="ma-4")

            div.display-1.pt-4.ma-4.font-weight-bold {{ resipetitle }}
            
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
            #ResipeArea
            Resipe(
                class="ma-10 my-4 pb-10"
                :list="resipelist"
            )

            .text-center.pt-10.pb-12
                v-btn.title(color="#FFB618" @click="toback") 戻る
</template>

<script>
import Resipe from '..//components/Resipe'  
import Materials from '..//components/Materials'

export default{
    components: {
        Resipe,
        Materials
    },
    data: function(){
        return{
        resipetitle:'冷やしキムチラーメン',
        topimg: "https://imgfp.hotp.jp/IMGH/21/64/P028842164/P028842164_480.jpg",
        mateliallist: [
            { message: 'お肉' },
            { message: '野菜' },
            { message: '魚' },
        ],
        resipelist: [
            { message: '肉を焼く' },
            { message: '野菜を炒める' },
            { message: '魚を焼く' },
        ],
        tags: ['天気の子', 'あは', 'あはは']
        }
    },
    methods: {
        toback: function(){
            this.$router.push("/votepage")
        },
        totagpage: function(){
            this.$router.push("/tagpage")
        }
    }
}
</script>