<template lang="pug">
div(color="#F7F3E8")
    v-container
        v-card(class="ma-4")
            //料理の名前を入れる##
            v-row.mx-4
                div.headline.ml-0.pt-1 {{ date }}
                div.headline.ml-0.pt-1 {{ time }}
            div.display-1.ma-4 お題: {{ resipetitle }}
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

            
            .text-center.pt-10.pb-12
                v-btn.title(color="#FFB618" @click="totop") 投票
</template>

<script>
import Contestresultcard from '..//components/Contestresultcard'

export default{
    components: {
        Contestresultcard
    },
    data: function(){
        return{
            date: "2019/8/24",
            time: "7:00 ~ 8:00",
            resipetitle:'冷やしキムチラーメン',
            member: [
                { number: 1, title: "タピオカミルクティー風カレーライスの南蛮漬け", name: "ぴ", icon: "https://vuetifyjs.com/apple-touch-icon-180x180.png", img: "https://imgfp.hotp.jp/IMGH/21/64/P028842164/P028842164_480.jpg", comment: "タピオカミルクティーの風味が効いていてとても美味しいです。"},
                { number: 2, title: "タピオカミルクティー風カレーライスの南蛮漬け", name: "ぴ", icon: "https://vuetifyjs.com/apple-touch-icon-180x180.png", img: "https://imgfp.hotp.jp/IMGH/21/64/P028842164/P028842164_480.jpg", comment: "タピオカミルクティーの風味が効いていてとても美味しいです。"},
                { number: 3, title: "タピオカミルクティー風カレーライスの南蛮漬け", name: "ぴ", icon: "https://vuetifyjs.com/apple-touch-icon-180x180.png", img: "https://imgfp.hotp.jp/IMGH/21/64/P028842164/P028842164_480.jpg", comment: "タピオカミルクティーの風味が効いていてとても美味しいです。"},
                { number: 4, title: "タピオカミルクティー風カレーライスの南蛮漬け", name: "ぴ", icon: "https://vuetifyjs.com/apple-touch-icon-180x180.png", img: "https://imgfp.hotp.jp/IMGH/21/64/P028842164/P028842164_480.jpg", comment: "タピオカミルクティーの風味が効いていてとても美味しいです。"},
                { number: 5, title: "タピオカミルクティー風カレーライスの南蛮漬け", name: "ぴ", icon: "https://vuetifyjs.com/apple-touch-icon-180x180.png", img: "https://imgfp.hotp.jp/IMGH/21/64/P028842164/P028842164_480.jpg", comment: "タピオカミルクティーの風味が効いていてとても美味しいです。"},
            ]
        }
    },
    methods: {
        totop: function(){
        this.$router.push("/")
        },
    }
    }
</script>