<template lang="pug">
div
    v-card
        v-card-title.font-logotype レシピ
        ol.ml-6.pb-4
            li.font-harenosora(v-for="line in list") {{ line.message }}
</template>

<script>
export default {
    props:{
        list: Array
    }
}
</script>

<style>
    @font-face {
        font-family: 'LogoType';
        src: url('../../fonts/07LogoTypeGothic7.ttf') format('TrueType');
    }

    @font-face {
        font-family: 'Harenosora';
        src: url('../../fonts/Harenosora.otf') format('OpenType');
    }

    .font-logotype{
        font-family: 'LogoType';
    }
    .font-harenosora{
        font-family: 'Harenosora';
    }
</style>