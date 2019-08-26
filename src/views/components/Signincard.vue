<template>
<v-card>
<form>
    <v-text-field
        v-model="email"
        :error-messages="emailErrors"
        class="mx-4"
        label="メールアドレス"
        required
        @input="$v.email.$touch()"
        @blur="$v.email.$touch()"
    ></v-text-field>
    <v-text-field
        v-model="passward"
        :error-messages="selectErrors"
        class="mx-4"
        label="パスワード"
        required
        @input="$v.passward.$touch()"
        @blur="$v.passward.$touch()"
    ></v-text-field>
    <v-layout justify-space-around="">
        <v-layout class="tosignup">
            <div class="moji ml-4">会員登録をされていない方</div>
            <v-btn class="ma-4" @click="tosignup">サインアップ</v-btn>
        </v-layout>
        <v-btn class="ma-4" @click="submit">ログイン</v-btn>
    </v-layout>
</form>
</v-card>
</template>

<script>
export default {
    methods: {
        tosignup: function(){
            this.$router.push("/signup")
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