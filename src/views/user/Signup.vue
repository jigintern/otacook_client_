<template lang="pug">
v-container
    //v-layout
    v-flex
        //コンテストレシピを表示するコンポーネント
        #SignupCardArea
            Signupcard(
                :redirectto="redirectto"
                @signin="signin"
            )
</template>

<script>
import Signupcard from '..//components/Signupcard'

export default{
    components: {
        Signupcard
    },
    props: {
        redirectto: String
    },
    methods:{
        signin: function(userid){
            this.$emit('signin', userid)
        }
    }
}
</script>