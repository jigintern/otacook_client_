<template lang="pug">
div
    v-card.ma-4.pb-1
        v-card-title.headline {{ title }}
        .text-center.body.mx-4 {{ comment }}
        v-card.ma-6
            ol.ml-6.py-4
                li.body-1(v-for="line in list") {{ line }}
</template>

<script>
export default {
    props:{
        title: String,
        comment: String,
        list: Array
    }
}
</script>