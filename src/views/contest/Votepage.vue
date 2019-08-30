<template lang="pug">
div(color="#F7F3E8")
    v-container
        v-card(class="ma-4")
            //料理の名前を入れる##
            v-row.mx-4
                div.headline.ml-0.pt-1 {{ date }}
                div.headline.pl-4.pt-1 {{ time }}
            div.display-1.ma-4 お題: {{ recipetitle }}
            v-divider.my-2.mx-4

            .text-center.ma-4.body-1 下の5つの料理から「おいしそうだな～」「食べたいな～」と思う順に、1位 ~ 3位まで選んでください！

            div.ma-8(v-for="line in member")
                Contestresultcard(
                    :title="line.title"
                    :number= "line.number"
                    :img="line.img"
                    :comment="line.comment"
                    :isnameshow="false"
                )

            v-row(align="center")
                v-col.pr-10(cols="12" sm="5")
                    .text-right.headline 1位
                v-col(cols="12" sm="4")
                    .text-center
                        v-select(
                            :items="titles1"
                            :menu-props="{ maxHeight: '400' }"
                            label="選択"
                            v-model="selected1"
                            persistent-hint
                        )
            v-row(align="center")
                v-col.pr-10(cols="12" sm="5")
                    .text-right.headline 2位
                v-col(cols="12" sm="4")
                    .text-center
                        v-select(
                            :items="titles2"
                            :menu-props="{ maxHeight: '400' }"
                            label="選択"
                            v-model="selected2"
                            persistent-hint
                        )
            v-row(align="center")
                v-col.pr-10(cols="12" sm="5")
                    .text-right.headline 3位
                v-col(cols="12" sm="4")
                    .text-center
                        v-select(
                            :items="titles3"
                            :menu-props="{ maxHeight: '400' }"
                            label="選択"
                            v-model="selected3"
                            persistent-hint
                        )

            .text-center.pt-10.pb-12
                div.mb-4.red--text {{error}}
                v-btn.title(color="#FFB618" @click="toquestion") 投票する
</template>

<script>
import Contestresultcard from '..//components/Contestresultcard'

export default{
    components: {
        Contestresultcard
    },
    data: function(){
        return{
            error: "",
            date: "2019/8/24",
            time: "7:00 ~ 8:00",
            recipetitle:'冷やしキムチラーメン',
            member: [
                { number: 1, title: "タピオカミルクティー風カレーライスの南蛮漬け", name: "ぴ", icon: "https://vuetifyjs.com/apple-touch-icon-180x180.png", img: "https://imgfp.hotp.jp/IMGH/21/64/P028842164/P028842164_480.jpg", comment: "タピオカミルクティーの風味が効いていてとても美味しいです。"},
                { number: 2, title: "タピオカカルピスソーダ風カレーライスの南蛮漬け", name: "ぴ", icon: "https://vuetifyjs.com/apple-touch-icon-180x180.png", img: "https://imgfp.hotp.jp/IMGH/21/64/P028842164/P028842164_480.jpg", comment: "タピオカミルクティーの風味が効いていてとても美味しいです。"},
                { number: 3, title: "タピオカオレンジシューズ風カレーライスの南蛮漬け", name: "ぴ", icon: "https://vuetifyjs.com/apple-touch-icon-180x180.png", img: "https://imgfp.hotp.jp/IMGH/21/64/P028842164/P028842164_480.jpg", comment: "タピオカミルクティーの風味が効いていてとても美味しいです。"},
                { number: 4, title: "タピオカ野菜じゅーず風カレーライスの南蛮漬け", name: "ぴ", icon: "https://vuetifyjs.com/apple-touch-icon-180x180.png", img: "https://imgfp.hotp.jp/IMGH/21/64/P028842164/P028842164_480.jpg", comment: "タピオカミルクティーの風味が効いていてとても美味しいです。"},
                { number: 5, title: "タピオカコヒー風カレーライスの南蛮漬け", name: "ぴ", icon: "https://vuetifyjs.com/apple-touch-icon-180x180.png", img: "https://imgfp.hotp.jp/IMGH/21/64/P028842164/P028842164_480.jpg", comment: "タピオカミルクティーの風味が効いていてとても美味しいです。"},
            ],
            selected1: "",
            selected2: "",
            selected3: "",
        }
    },
    computed: {
        titles1: function(){
            let newArray = []
            let title = ""
            this.member.forEach((e) => {
                title = e.number + ". " +e.title
                if(title != this.selected2 && title != this.selected3){
                    newArray.push(title)
                }
            })
            return newArray
        },
        titles2: function(){
            let newArray = []
            let title = ""
            this.member.forEach((e) => {
                title = e.number + ". " +e.title
                if(title != this.selected1 && title != this.selected3){
                    newArray.push(title)
                }
            })
            return newArray
        },
        titles3: function(){
            let newArray = []
            let title = ""
            this.member.forEach((e) => {
                title = e.number + ". " +e.title
                if(title != this.selected1 && title != this.selected2){
                    newArray.push(title)
                }
            })
            return newArray
        },
    },
    methods: {
        toquestion: function(){
            if(this.selected1 == "" || this.selected2 == "" || this.selected3 == ""){
                this.error = "選択していない項目があります"
            }else{
                //サーバーに選択内容を送信する
                this.$router.push("/questionpage")
            }
        },
    }
    }
</script>