<template lang="pug">
    v-card.py-1
        v-card-title 現在開催中のコンテスト
        .title.mx-8 {{title}}
        .subtitle-1.mx-8 開催時間: {{time}}
        .subtitle-1.mx-8 投票時間: {{votetime}}

        .subtitle-2.mx-8 以下コンテストに必要な材料の目安です
        Materials.ma-4(
            :list="materiallist"
        )
        .text-center.ma-4
          v-btn.title(color="#FFB618" @click="toquestion") 問題ページへ

</template>
<script>
import Materials from "../../components/Materials"
import Cookies from 'js-cookie'
import axios from 'axios'

export default {
    components: {
        Materials
    },
    props: {
        contestid: String
    },
    data: function(){
        return {
            title: "お題: ",
            time: "",
            votetime: "",
            jsonlist:'[]',
        }
    },
    mounted: function(){
        let self = this
        axios.get('https://t1.intern.jigd.info/flask/api/contest/info/'+String(this.contestid))
        .then(function (response) {
            var data = response.data
            console.log(data["title"])
            console.log(data["time"])
            console.log(data["votetime"])
            self.title = "お題:"+data["title"]
            self.time = data["time"]
            self.votetime = data["votetime"]
        })

        axios.get('https://t1.intern.jigd.info/flask/api/contest/materialsinfo/'+String(this.contestid))
        .then(function (response) {
            self.jsonlist = "[" + response.data + "]"
        })
    },
    computed: {
        materiallist: function(){
            var array = JSON.parse(this.jsonlist)
            return array
        },
    },
    methods: {
        toquestion: function(){
            Cookies.set('contestid', String(this.contestid))
            this.$router.push('/questionpage')
        }
    },
}
</script>