<template>
<v-card>
<form>
    <v-text-field
        :rules="[rules.required]"
        class="mx-4 pt-5"
        label="メールアドレス"
        required
    ></v-text-field>
    <v-text-field
        :rules="[rules.required]"
        class="mx-4"
        label="パスワード"
        hint="八文字以上の文字列です."
        required
    ></v-text-field>
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
        submit: function(userid){
            //useridをこいつに入れる
            this.$emit('signin', 1)
            if(this.redirectto == null){
                this.$router.push("/")
            }else{
                this.$router.push(this.redirectto)
            }
        },
    },
    props: {
        redirectto: String,
        userid: Number
    },
    data () {
        return {
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