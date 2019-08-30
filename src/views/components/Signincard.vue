<template>
<v-card>
<form>
    <v-text-field
        :rules="[rules.required]"
        v-model="email"
        class="mx-4 pt-5"
        label="メールアドレス"
        required
    ></v-text-field>
    <v-text-field
        :rules="[rules.required]"
        :type="passwordarea ? 'text' : 'password'"
        v-model="password"
        class="mx-4"
        label="パスワード"
        hint="八文字以上の文字列です."
        required
        @click:append="passwordarea = !passwordarea"
    ></v-text-field>
    <div class="text-right mr-4 red--text"> {{error}} </div>
    <v-layout justify-space-around="">
        <v-layout class="tosignup">
            <div class="moji ml-4">会員登録をされていない方</div>
            <v-btn class="ma-4" @click="tosignup">サインアップページへ</v-btn>
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
            if(this.email == "" || this.password == ""){
                this.error = "入力していない項目があります"
            }else{
                //ここでメールアドレスとパスワードをサーバーに送って
                //sessionidとuseridを取得する
                this.sessionid = 1
                this.userid = 1
                this.$emit('signin', this.sessionid, this.user)
                this.$router.back()
                if(this.redirectto == null){
                    this.$router.push("/")
                }else{
                    this.$router.push(this.redirectto)
                }
            }
        },
    },
    props: {
        redirectto: String,
    },
    data () {
        return {
            error: "",
            email: "",
            password: "",
            userid: "",
            sessionid: "",
            passwordarea: "",
            rules: {
                required: value => !!value || '入力必須',
            },
        }
    },
}
</script>

<style scoped>
.moji{
    position: relative;
    top: 23px
}
</style>