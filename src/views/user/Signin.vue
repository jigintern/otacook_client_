<template lang="pug">
v-container
    //v-layout
    v-flex
        //コンテストレシピを表示するコンポーネント
        #SigninCardArea
            Signincard(
                :redirectto="redirectto"
            )
</template>

<script>
import Signincard from '..//components/Signincard'

export default{
    components: {
        Signincard
    },
    props:{
        redirectto: String
    }
}
</script>