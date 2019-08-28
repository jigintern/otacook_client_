<template lang="pug">
v-container
    //v-layout
    v-flex
        //コンテストレシピを表示するコンポーネント
        #SignupCardArea
            Signupcard(
                :redirectto="redirectto"
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
    }
}
</script>