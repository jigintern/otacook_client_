<template lang="pug">
div
    v-card
        v-card-title.headline レシピ
        ol.ml-6.pb-4
            li.body-1(v-for="line in list") {{ line.message }}
</template>

<script>
export default {
    data: function(){
        return{
            list: [
                { message: '肉を焼く' },
                { message: '野菜を炒める' },
                { message: '魚を焼く' }
            ]
        }
    }
}
</script>

<style>
</style>
