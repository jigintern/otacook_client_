<template lang="pug">
div(color="#F7F3E8")
    v-container
        v-card(class="ma-4")
            //料理の名前を入れる##
            div.display-2.pt-4.ml-4 ランキング
            v-divider.my-2.mx-4
            div.display-1.mx-4 お題: {{ resipetitle }}
            v-row.mx-4
                div.headline.ml-2.mb-1 {{ date }}
                div.headline.ml-2.mb-1 {{ time }}

            div.ma-4.ml-8.headline(v-for="line in ranking") {{ line.rank }}位
                Contestresultcard(
                    :title="line.title"
                    :name="line.name"
                    :img="line.img"
                    :icon="line.icon"
                    :comment="line.comment"
                )
            .text-center.pt-10.pb-12
                v-btn.title(color="#FFB618" @click="totop") トップページへ
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
            ranking: [
                { rank: 1, title: "タピオカミルクティー風カレーライスの南蛮漬け", name: "ぴ", icon: "https://vuetifyjs.com/apple-touch-icon-180x180.png", img: "https://imgfp.hotp.jp/IMGH/21/64/P028842164/P028842164_480.jpg", comment: "タピオカミルクティーの風味が効いていてとても美味しいです。"},
                { rank: 2, title: "タピオカミルクティー風カレーライスの南蛮漬け", name: "ぴ", icon: "https://vuetifyjs.com/apple-touch-icon-180x180.png", img: "https://imgfp.hotp.jp/IMGH/21/64/P028842164/P028842164_480.jpg", comment: "タピオカミルクティーの風味が効いていてとても美味しいです。"},
                { rank: 3, title: "タピオカミルクティー風カレーライスの南蛮漬け", name: "ぴ", icon: "https://vuetifyjs.com/apple-touch-icon-180x180.png", img: "https://imgfp.hotp.jp/IMGH/21/64/P028842164/P028842164_480.jpg", comment: "タピオカミルクティーの風味が効いていてとても美味しいです。"},
                { rank: 4, title: "タピオカミルクティー風カレーライスの南蛮漬け", name: "ぴ", icon: "https://vuetifyjs.com/apple-touch-icon-180x180.png", img: "https://imgfp.hotp.jp/IMGH/21/64/P028842164/P028842164_480.jpg", comment: "タピオカミルクティーの風味が効いていてとても美味しいです。"},
                { rank: 5, title: "タピオカミルクティー風カレーライスの南蛮漬け", name: "ぴ", icon: "https://vuetifyjs.com/apple-touch-icon-180x180.png", img: "https://imgfp.hotp.jp/IMGH/21/64/P028842164/P028842164_480.jpg", comment: "タピオカミルクティーの風味が効いていてとても美味しいです。"},
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