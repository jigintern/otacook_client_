<template lang="pug">
div(color="#F7F3E8")
    v-container
        v-card(class="ma-4")
            //料理の名前を入れる##
            div.display-2.pt-4.ml-4 ランキング
            v-divider.my-2.mx-4
            div.display-1.mx-4 お題: {{ recipetitle }}
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
                    :isnameshow="true"
                )
            .text-center.pt-10.pb-12
                div.red--text.mb-4 {{error}}
                div(v-if="isloggingin == false")
                    v-btn.title(color="#FFB618" @click="tologin") ログイン
                div(v-else)
                    v-btn.title(color="#FFB618" @click="totop") トップページへ
</template>

<script>
import Contestresultcard from '..//components/Contestresultcard'
import Cookies from 'js-cookie'
import axios from 'axios'

export default{
    components: {
        Contestresultcard
    },
    data: function(){
        return{
            error: "",
            date: "",
            time: "",
            recipetitle:'',
            jsonmember: [],
            ranking: "",
            isloggingin: false,
            //ranking: [
            //    { rank: 1, title: "タピオカミルクティー風カレーライスの南蛮漬け", name: "ぴ", icon: "https://vuetifyjs.com/apple-touch-icon-180x180.png", img: "https://imgfp.hotp.jp/IMGH/21/64/P028842164/P028842164_480.jpg", comment: "タピオカミルクティーの風味が効いていてとても美味しいです。"},
            //    { rank: 2, title: "タピオカミルクティー風カレーライスの南蛮漬け", name: "ぴ", icon: "https://vuetifyjs.com/apple-touch-icon-180x180.png", img: "https://imgfp.hotp.jp/IMGH/21/64/P028842164/P028842164_480.jpg", comment: "タピオカミルクティーの風味が効いていてとても美味しいです。"},
            //    { rank: 3, title: "タピオカミルクティー風カレーライスの南蛮漬け", name: "ぴ", icon: "https://vuetifyjs.com/apple-touch-icon-180x180.png", img: "https://imgfp.hotp.jp/IMGH/21/64/P028842164/P028842164_480.jpg", comment: "タピオカミルクティーの風味が効いていてとても美味しいです。"},
            //    { rank: 4, title: "タピオカミルクティー風カレーライスの南蛮漬け", name: "ぴ", icon: "https://vuetifyjs.com/apple-touch-icon-180x180.png", img: "https://imgfp.hotp.jp/IMGH/21/64/P028842164/P028842164_480.jpg", comment: "タピオカミルクティーの風味が効いていてとても美味しいです。"},
            //    { rank: 5, title: "タピオカミルクティー風カレーライスの南蛮漬け", name: "ぴ", icon: "https://vuetifyjs.com/apple-touch-icon-180x180.png", img: "https://imgfp.hotp.jp/IMGH/21/64/P028842164/P028842164_480.jpg", comment: "タピオカミルクティーの風味が効いていてとても美味しいです。"},
            //]
        }
    },
    props:{
        userid: Number
    },
    mounted: function(){
        let self = this
        const sessionid = Cookies.get('sessionid')

        if(sessionid == -1){
            this.isloggingin = false
            self.error = "ログインしてください"
        }else{
            axios.get('https://t1.intern.jigd.info/flask/api/contest/info/'+String(self.contestid))
            .then(function (response) {
                var data = response.data
                self.recipetitle = data["title"]
                self.date = data["date"]
                self.time = data["time"]
            })

            this.isloggingin = true
            axios.get('https://t1.intern.jigd.info/flask/api/contest/rankingmemberlistfromuser/'+String(this.userid))
            .then(function (response) {
                console.log(response.data)
                self.jsonmember = "[" + response.data + "]"
                var array = JSON.parse(self.jsonmember)
                self.ranking = array
            })
            .catch(function(){
                self.error = "コンテストに参加していないかマッチング可能人数に達していなかったため表示できません"
            })
        }
    },
    computed: {
        contestid: function(){
            var contestid = Cookies.get('contestid')
            return contestid
        },
    },
    methods: {
        totop: function(){
            this.$router.push("/")
        },
        tologin: function(){
            this.$router.push("/signin")
        },
    }
    }
</script>