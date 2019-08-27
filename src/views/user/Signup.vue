<template lang="pug">
v-container
    //v-layout
    v-flex
        //コンテストレシピを表示するコンポーネント
        #SignupCardArea
            Signupcard
</template>

<script>
import Signupcard from '..//components/Signupcard'

export default{
    components: {
        Signupcard
    }
}
</script>