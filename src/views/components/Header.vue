<template lang="pug">
div
    v-toolbar(color="#ffb618")
        //v-btn(text @click="totop").title オタクック                                                                                                                                                                           
        //v-divider.mx-4(vertical)
        router-link(to="/")
            v-img(:src="img_src"
                max-height="40"
                max-width="130"
                )
        .flex-grow-1
        v-toolbar-items
            //v-divider.mx-4(vertical)
            div(v-if="isLoggingin" class="my-auto header white--text")
                v-btn(text @click="tomypage").white--text MyPage
                v-btn(text @click="tosignout").white--text SignOut
            div(v-else class="my-auto header white--text")
                v-btn(text @click="tosignin").white--text SignIn
                v-btn(text @click="tosignup").white--text SignUp
            //router-link(to="signin")
</template>

<script>
export default {
    data(){
        return {
            img_src: require("../../assets/header_logo.png")
        }
    },
    methods: {
        tosignin: function(){
            this.$router.push("/signin")
        },
        tosignup: function(){
            this.$router.push("/signup")
        },
        tosignout: function(){
            this.$emit('signout')
        },
        tomypage: function(){
            this.$router.push("/mypage")
        },
        totop: function(){
            this.$router.push("/")
        }
    },
    props: {
        isLoggingin: Boolean
    },
}
</script>

<style>
    .header{
        font-family: 'ヒラギノ丸ゴ ProN','Hiragino Maru Gothic ProN',sans-serif;
    }
</style>