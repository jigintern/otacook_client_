<template lang="pug">
div(color="#F7F3E8")
    v-container
        v-card(class="ma-4")
            div.display-2.pt-4.ma-4 チュートリアル
            v-divider.ma-4
            
            .text-center ここでは、料理の基本的な知識や技術が学べる。
            div(v-if="isLoggingin == true")

                div.ma-4
                    div.display-1 チュートリアル一覧
                
                    Tutorialcard(
                        :title="cuttitle"
                        :comment="cutcomment"
                        :list="cuttutoriallist"
                    )

                    Tutorialcard(
                        :title="tyourititle"
                        :comment="tyouricomment"
                        :list="tyouritutoriallist"
                    )
            div(v-else)
                .text-center.pt-10.pb-12
                    div.ma-4 この機能はログインが必要です
                    v-btn.title(color="#FFB618" @click="tologin") ログイン

            .text-center.pt-10.pb-12
                v-btn.title(color="#FFB618" @click="totop") トップページへ

</template>

<script>
import Tutorialcard from '..//components/Tutorialcard'

export default{
    components: {
        Tutorialcard
    },
    data: function(){
        return{
            time: "7:00 ~ 8:00",
            total_member: 1,
            cuttitle:'包丁 ( 0 % )',
            cutcomment: "包丁の使い方を学習できるよ！",
            cuttutoriallist: ["基本的な使い方", "ざく切り", "輪切り"],
            tyourititle:'調理 ( 0 % )',
            tyouricomment: "調理の工程を学習できるよ！",
            tyouritutoriallist: ["調理器具", "計量・計り方"],
        }
    },
    props: {
        isLoggingin: Boolean,
        userid: Number
    },
    methods: {
        totop: function(){
        this.$router.push("/")
        },
        tologin: function(){
        this.$router.push("/signin")
        }
    }
}
</script>