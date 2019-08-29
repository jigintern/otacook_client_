<template lang="pug">
div
    v-card
        v-card-title.headline {{ title }}
        ol.ml-6.pb-4
            li.body-1(v-for="line in list") {{ line.message }}
</template>

<script>
export default {
    props:{
        title: String,
        list: Array
    }
}
</script>