<template lang="pug">
div
    v-toolbar(color="#ffb618")
        v-btn(text @click="totop").title オタクック
        //v-divider.mx-4(vertical)
        .flex-grow-1
        v-toolbar-items
            //v-divider.mx-4(vertical)
            div(v-if="isLoggingin" class="my-auto")
                v-btn(text @click="tomypage") My Page
                v-btn(text @click="tosignout") Sign Out
            div(v-else class="my-auto")
                v-btn(text @click="tosignin") Sign In
                v-btn(text @click="tosignup") Sign Up
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