<template lang="pug">
    div
        v-card(elevation="0")
            div(v-if="isnameshow === false")
                v-card-title.font-logotype.font-weight-bold {{ number }}. {{title}}
            div(v-else)
                v-card-title.font-logotype.font-weight-bold {{title}}
            div(v-if="isnameshow")
                v-btn(text width="96%").mx-4.pb-4
                    v-layout
                        v-avatar(class="ma-4" size="20")
                            img(:src="icon" alt="avatar")
                        div.my-auto.font-weight-bold {{ name }}
            v-img.my-4.mx-10(
                :src="img"
                max-height="50vh"
            )
            div.ma-6.mb-0.font-logotype 作者コメント
            div.mx-8.pb-4.font-harenosora {{comment}}
            
</template>

<script>
export default {
    props: {
        title: String,
        name: String,
        img: String,
        icon: String,
        number: String,
        comment: String,
        isnameshow: Boolean
    },
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