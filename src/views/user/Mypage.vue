<template>
    <v-container>
        <Usercard :userid="userid" class="ma-4" />
        <!--<Skilltreecard class="ma-4"/>-->
        <Ratecard :userid="userid" class="ma-4" />
    </v-container>
</template>

<script>
import Usercard from '..//components/Usercard'
import Skilltreecard from '..//components/Skilltreecard'
import Ratecard from '..//components/Ratecard'

export default {
    props:{
        userid: Number
    },
    components: {
        Usercard,
        Skilltreecard,
        Ratecard
    }
}
</script>