<template lang="pug">
    div
        v-card
            div(v-if="isnameshow === false")
                v-card-title.title {{ number }}. {{title}}
            div(v-else)
                v-card-title.title {{title}}
            div(v-if="isnameshow")
                v-btn(text width="96%").mx-4.pb-4
                    v-layout
                        v-avatar(class="ma-4" size="20")
                            img(:src="icon" alt="avatar")
                        div.body-1.my-auto {{ name }}
            v-img.my-4.mx-10(
                :src="img"
                max-height="50vh"
            )
            div.subtitle-1.ma-6.mb-0 作者コメント
            div.body-1.mx-8.pb-4 {{comment}}
            
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