<template lang="pug">
div
    v-card
        v-card-title.headline.text-weight-light.text-weight-italic 材料
        ul.ml-6.pb-4
            li.body-1(v-for="line in list") {{ line.message }}
</template>

<script>
export default {
    props:{
        list: Array
    }
}
</script>

<style>
</style>
