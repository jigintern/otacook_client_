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
    created: function(){
        if(this.isLoggingin == true){
            this.$router.push("/")
        }
    },
    props: {
        isLoggingin: Boolean,
        redirectto: String
    },
    methods:{
        signin: function(sessionid, userid){
            this.$emit('signin', sessionid, userid)
        }
    }
}
</script>