<template lang="pug">
div(color="#F7F3E8")
    v-container
        v-card(class="ma-4")
            div.display-2.pt-4.ma-4 チュートリアル
            v-divider.ma-4
            
            .text-center ここでは、料理の基本的な知識や技術が学べる。
            div(v-if="isLoggingin == true")

                div.ma-4
                    div.display-1 一覧
                
                    Tutorialcard(
                        :title="tutoriallist.title"
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
        title:'冷やしキムチラーメン',
        total_member: 1,
        tutoriallist: [],
        resipelist: [
            { message: '肉を焼く' },
            { message: '野菜を炒める' },
            { message: '魚を焼く' },
        ]
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