<template>
<v-card>
<form>
    <v-text-field
        class="mx-4 pt-5"
        :rules="[rules.required]"
        label="ユーザー名"
        required
    ></v-text-field>
    <v-text-field
        class="mx-4"
        :rules="[rules.required]"
        label="メールアドレス"
        required
    ></v-text-field>
    <v-text-field
        class="mx-4"
        v-model="password"
        :rules="[rules.required, rules.min]"
        :type="passwordarea ? 'text' : 'password'"
        label="パスワード"
        hint="八文字以上でオナシャス"
        required
        @click:append="passwordarea = !passwordarea"
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
            if(this.redirectto == null){
                this.$router.push("/")
            }else{
                this.$router.push(this.redirectto)
            }
        }
    },
    props:{
        redirectto: String
    },
    data () {
        return {
            rules: {
                required: value => !!value || '入力必須',
                min: v => v.length >= 8 || '八文字以上でオナシャス',
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