<template lang="pug">
v-container
    //v-layout
    v-flex
        //コンテストレシピを表示するコンポーネント
        #SigninCardArea
            Signincard
</template>

<script>
import Signincard from '..//components/Signincard'

export default{
    components: {
        Signincard
    }
}
</script>