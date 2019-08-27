<template>
    <v-container>
        <Usercard class="ma-4" />
        <Skilltreecard class="ma-4"/>
        <Ratecard class="ma-4" />
    </v-container>
</template>

<script>
import Usercard from '..//components/Usercard'
import Skilltreecard from '..//components/Skilltreecard'
import Ratecard from '..//components/Ratecard'

export default {
    components: {
        Usercard,
        Skilltreecard,
        Ratecard
    }
}
</script>