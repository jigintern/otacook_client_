<template>
<div>
<v-card class="ma-4 py-1">
    <v-card class="ma-4">
        <div class="text-center">
            <v-img
                :src="require('../../assets/top.png')"
            ></v-img>
        </div>
    </v-card>
    <h1 class="ma-4 font-logotype font-weight-bold">
        日本中の人と料理の腕前を比べよう！！
    </h1>
    <div class="font-harenosora">
        <div class= "mx-8 body-2">
            オタクックは料理を作り、対戦しながら学べるサービスです。
        </div>
        <div class= "mx-8 body-2">
            コンテストでは、日本中の人が同じ料理を作り対戦することができます。また、ほかの人が同じテーマで何を作ったかを見ることができます。
        </div>
        <div class= "mx-8 body-2">
            コンテストの結果からレートが出るので、日本中の人と対戦しながら料理の腕前を上げることができます。
        </div>
    </div>
    
        <ContestResult
            class="ma-4"
            v-if="isActiveContestResult === true"
            :contestid="contestid"
        />
        <ContestNow
            class="ma-4" 
            v-if="isActiveContestNow === true"
            :contestid="contestid"
        />
        <ContestYokoku 
            class="ma-4" 
            v-if="isActiveContestYokoku === true"
            :contestid="contestid"
        />
</v-card>
</div>
</template>

<script>
import ContestYokoku from "./components/ContestYokoku"
import ContestNow from "./components/ContestNow"
import ContestResult from "./components/ContestResult"
import axios from 'axios'

export default {
    mounted: function(){
        let self = this
        //実行中のコンテストのIDを取得
        //実行中から結果発表までがnow
        console.log("いたずらしようとしているなら今すぐやめましょう")
        console.log("いやだよって人は住所を教えてください")
        console.log("物理的に永久バンします")
        console.log("- - - - - - - - - - - - - - - - - - - -")
        console.log("ガバガバAPIだから叩かないでね泣")
        axios.get('https://t1.intern.jigd.info/flask/api/contest/now')
        .then(function (response) {
            var data = response.data
            //console.log(data["contestid"])
            //console.log(data["status"])
            self.contestid = data["contestid"]
            self.status = data["status"]
            if(self.status == "0"){
                self.isActiveContestYokoku = true
            }
            if(self.status == "1" || self.status == "2"){
                self.isActiveContestNow = true
            }
            //2は投票中
            if(self.status == "3"){
                self.isActiveContestResult = true
            }
        })
    },
    components: {
        ContestYokoku,
        ContestNow,
        ContestResult
    },
    data: function(){
        return {
            contestid: 0,
            status: 0,
            isActiveContestYokoku: false,
            isActiveContestNow: false,
            isActiveContestResult: false,
        }
    },
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