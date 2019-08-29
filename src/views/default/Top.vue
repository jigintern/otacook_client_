<template>
<div>
    <v-card class="ma-4" height="40vh">
        <v-card-title>ここにサービスの概要みたいなの入れたい</v-card-title>
    </v-card>
    <v-row class="ma-2">
        <v-col>
            <ContestYokoku v-if="isActiveContestYokoku === true"/>
        </v-col>
        <v-col>
            <ContestResult v-if="isActiveContestResult === true"/>
        </v-col>
    </v-row>
</div>
</template>

<script>
import ContestYokoku from "./components/ContestYokoku"
import ContestResult from "./components/ContestResult"

export default {
    components: {
        ContestYokoku,
        ContestResult
    },
    data: function(){
        return {
            isActiveContestYokoku: true,
            isActiveContestResult: false,
        }
    },
}
</script>