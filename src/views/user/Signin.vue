<template lang="pug">
v-container
    //v-layout
    v-flex
        //コンテストレシピを表示するコンポーネント
        #SigninCardArea
            Signincard(
                :redirectto="redirectto"
                @signin="signin"
            )
</template>

<script>
import Signincard from '..//components/Signincard'

export default{
    components: {
        Signincard
    },
    props:{
        redirectto: String,
        sessionid: Number,
        userid: Number
    },
    methods:{
        signin: function(sessionid, userid){
            this.$emit('signin', sessionid, userid)
        }
    }
}
</script>