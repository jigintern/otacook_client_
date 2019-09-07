<template lang="pug">
div(color="#F7F3E8")
    v-container
        v-card(class="ma-4")
            //料理の名前を入れる##
            v-row.mx-4
                //div.headline.ml-0.pt-1 {{ date }}
                div.headline.pt-2 {{ time }}
            h1.ma-4.font-logotype お題: {{ recipetitle }}
            v-divider.my-2.mx-4

            .text-center.ma-4.body-1.font-harenosora 下の5つの料理から「おいしそうだな～」「食べたいな～」と思う順に、1位〜3位まで選んでください！

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
import Cookies from 'js-cookie'
import axios from 'axios'

export default{
    components: {
        Contestresultcard
    },
    data: function(){
        return{
            error: "",
            //date: "2019/8/24",
            time: "",
            recipetitle:'',
            jsonmember: [],//jsonで取得して配列に変換する
            //member: [
            //    { number: 1, title: "タピオカミルクティー風カレーライスの南蛮漬け", name: "ぴ", icon: "https://vuetifyjs.com/apple-touch-icon-180x180.png", img: "https://imgfp.hotp.jp/IMGH/21/64/P028842164/P028842164_480.jpg", comment: "タピオカミルクティーの風味が効いていてとても美味しいです。"},
            //    { number: 2, title: "タピオカカルピスソーダ風カレーライスの南蛮漬け", name: "ぴ", icon: "https://vuetifyjs.com/apple-touch-icon-180x180.png", img: "https://imgfp.hotp.jp/IMGH/21/64/P028842164/P028842164_480.jpg", comment: "タピオカミルクティーの風味が効いていてとても美味しいです。"},
            //    { number: 3, title: "タピオカオレンジシューズ風カレーライスの南蛮漬け", name: "ぴ", icon: "https://vuetifyjs.com/apple-touch-icon-180x180.png", img: "https://imgfp.hotp.jp/IMGH/21/64/P028842164/P028842164_480.jpg", comment: "タピオカミルクティーの風味が効いていてとても美味しいです。"},
            //    { number: 4, title: "タピオカ野菜じゅーず風カレーライスの南蛮漬け", name: "ぴ", icon: "https://vuetifyjs.com/apple-touch-icon-180x180.png", img: "https://imgfp.hotp.jp/IMGH/21/64/P028842164/P028842164_480.jpg", comment: "タピオカミルクティーの風味が効いていてとても美味しいです。"},
            //    { number: 5, title: "タピオカコヒー風カレーライスの南蛮漬け", name: "ぴ", icon: "https://vuetifyjs.com/apple-touch-icon-180x180.png", img: "https://imgfp.hotp.jp/IMGH/21/64/P028842164/P028842164_480.jpg", comment: "タピオカミルクティーの風味が効いていてとても美味しいです。"},
            //],
            member: "",
            groopid: "",
            selected1: "",
            selected2: "",
            selected3: "",
            no1: 0,
            no2: 0,
            no3: 0,
        }
    },
    mounted: function(){
        let self = this
        axios.get('https://t1.intern.jigd.info/flask/api/contest/getrandomgroopid')
        .then(function (response) {
            //console.log(response.data)
            self.groopid = Number(response.data)
            self.getlist()
        })

        axios.get('https://t1.intern.jigd.info/flask/api/contest/info/'+String(self.contestid))
        .then(function (response) {
            var data = response.data
            ////console.log(data["title"])
            ////console.log(data["time"])
            ////console.log(data["votetime"])
            self.recipetitle = data["title"]
            //self.time = data["time"]
            self.time = data["votetime"]
        })
    },
    computed: {
        contestid: function(){
            var contestid = Cookies.get('contestid')
            return contestid
        },
        titles1: function(){
            let newArray = []
            let title = ""
            this.member.forEach((e) => {
                title = e.number + ". " +e.title
                if(title != this.selected2 && title != this.selected3){
                    newArray.push(title)
                }
                if(title == this.selected1){
                    this.no1 = e.number
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
                if(title == this.selected2){
                    this.no2 = e.number
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
                if(title == this.selected3){
                    this.no3 = e.number
                }
            })
            return newArray
        },
    },
    methods: {
        getlist: function(){
            let self = this
            axios.get('https://t1.intern.jigd.info/flask/api/contest/memberlistfromgroop/'+String(this.groopid))
            .then(function (response) {
                //console.log(response.data)
                self.jsonmember = "[" + response.data + "]"
                var array = JSON.parse(self.jsonmember)
                self.member = array
            })
        },
        toquestion: function(){
            let self = this
            if(this.selected1 == "" || this.selected2 == "" || this.selected3 == ""){
                this.error = "選択していない項目があります"
            }else{
                //サーバーに選択内容を送信する
                axios.post('https://t1.intern.jigd.info/flask/api/contest/vote',{
                    groopid:this.groopid,
                    no1: this.no1,
                    no2: this.no2,
                    no3: this.no3
                })
                .then(function (response) {
                    //console.log(response.data);
                    if(response.data == "0"){
                        self.$router.push("/questionpage")
                    }
                })
            }
        },
    }
    }
</script>

<style>
    @font-face {
        font-family: 'LogoType';
        src: url('../../fonts/07LogoTypeGothic7.ttf') format('TrueType');
    }

    @font-face {
        font-family: 'Harenosora';
        src: url('../../fonts/Harenosora.otf') format('OpenType');
    }

    .font-logotype{
        font-family: 'LogoType';
    }
    .font-harenosora{
        font-family: 'Harenosora';
    }
</style>