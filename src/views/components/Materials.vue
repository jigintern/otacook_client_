<template lang="pug">
div
    v-card
        v-card-title.font-logotype 材料リスト
        
        div.mx-6.pb-4
            v-simple-table(dense)
                thead
                    tr
                        th.text-center 材料
                        th.text-center 分量
                tbody
                    tr(v-for="item in list")
                        td.text-center.body-2.font-harenosora {{ item.name }}
                        td.text-center.body-2.font-harenosora {{ item.serving }}
            v-divider
            //ul.ml-6.pb-4
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