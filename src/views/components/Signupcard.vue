<template>
<v-card>
<form>
    <v-text-field
        class="mx-4"
        label="ユーザー名"
        required
    ></v-text-field>
    <v-text-field
        class="mx-4"
        label="メールアドレス"
        required
    ></v-text-field>
    <v-text-field
        class="mx-4"
        label="パスワード"
        required
    ></v-text-field>
    <v-checkbox
        class="mx-4"
        label="利用規約に同意する。"
        required
    ></v-checkbox>
    <v-layout justify-space-around="">
        <v-layout class="tosignup">
            <div class="moji ml-4">会員の方は</div>
            <v-btn class="ma-4" @click="tosignin">ログインページへ</v-btn>
        </v-layout>
        <v-btn class="ma-4" @click="submit">サインアップ</v-btn>
    </v-layout>
</form>
</v-card>
</template>

<script>
export default {
    methods: {
        tosignin: function(){
            this.$router.push("/signin")
        },
        submit: function(){
            this.$router.push("/")
        }
    }
}
</script>

<style scoped>
.moji{
    position: relative;
    top: 23px
}
</style>