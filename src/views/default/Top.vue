<template>
<div>
<v-card class="ma-4 py-1">
    <v-card class="ma-4" height="40vh">
        <v-img
          :src="require('../../assets/top.png')"
        ></v-img>
    </v-card>
    <h1 class="ma-4">
        Otacookで好きなメシを作ろう！
    </h1>
    <div class= "mx-8 body-2">
        Otacookは料理を作り、対戦しながら学べるサービスです。
    </div>
    <div class= "mx-8 body-2">
        コンテストでは、日本中の人が同じ料理を作り対戦することができます。また、ほかの人がどのように作ったかを見ることができます。
    </div>
    <div class= "mx-8 body-2">
        コンテストの結果からレートが出るので、日本中の人と対戦しながら料理の腕前を上げることができます。
    </div>
        <ContestResult
            class="ma-4"
            v-if="isActiveContestResult === true"
        />
        <ContestNow
            class="ma-4" 
            v-if="isActiveContestNow === true"
        />
        <ContestYokoku 
            class="ma-4" 
            v-if="isActiveContestYokoku === true"
        />
</v-card>
</div>
</template>

<script>
import ContestYokoku from "./components/ContestYokoku"
import ContestNow from "./components/ContestNow"
import ContestResult from "./components/ContestResult"

export default {
    components: {
        ContestYokoku,
        ContestNow,
        ContestResult
    },
    data: function(){
        return {
            isActiveContestYokoku: false,
            isActiveContestNow: true,
            isActiveContestResult: false,
        }
    },
}
</script>