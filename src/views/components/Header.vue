<template lang="pug">
div
    v-toolbar(color="#ffb618")
        v-btn(text @click="totop").title オタクック
        v-divider.mx-4(vertical)
        .flex-grow-1
        v-text-field(single-line hide-details)
            v-icon mdi-anchor
        v-toolbar-items
            v-divider.mx-4(vertical)
            div(v-if="isLoggingin" class="my-auto")
                v-btn(text @click="tomypage") MyPage
                v-btn(text @click="tosignout") SignOut
            div(v-else class="my-auto")
                v-btn(text @click="tosignin") SignIn
                v-btn(text @click="tosignup") SignUp
            //router-link(to="signin")
</template>

<script>
export default {
    methods: {
        tosignin: function(){
            this.$router.push("/signin")
        },
        tosignup: function(){
            this.$router.push("/signup")
        },
        tosignout: function(){
            this.$emit('signout')
            this.$router.push("/")
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