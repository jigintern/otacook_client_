<template>
<v-card>
<form>
    <v-text-field
        class="mx-4 pt-5"
        v-model="username"
        :rules="[rules.required]"
        label="ユーザー名"
        required
    ></v-text-field>
    <v-text-field
        class="mx-4"
        v-model="email"
        :rules="[rules.required]"
        label="ユーザーID"
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
    <div class="text-right mr-4 red--text"> {{error}} </div>
    <div class="moji ma-4">会員の方は</div>
    <v-layout justify-space-around="">
        <v-layout class="tosignup">
            <!-- <div class="moji ml-4">会員の方は</div> -->
            <v-btn class="ma-4" @click="tosignin">ログインページへ</v-btn>
        </v-layout>
        <v-btn class="ma-4" @click="submit" color="#FFB618">サインアップ</v-btn>
    </v-layout>
</form>
</v-card>
</template>

<script>
import axios from 'axios'
export default {
    methods: {
        tosignin: function(){
            this.$router.push("/signin")
        },
        submit: function(){
            if(this.email == "" || this.password == "" || this.username == ""){
                this.error = "入力していない項目があります"
            }else{
                //mail, userid, passwordをサーバーに送信する
                //会員登録をサーバーで処理して
                //sessionid, useridを取得する
                let self = this
                axios.post('https://t1.intern.jigd.info/flask/api/signup',{
                    email: this.email,
                    password: this.password,
                    username: this.username
                })
                .then(function (response) {
                    console.log(response.data);
                    if(response.data == "-1"){
                        self.error = "使用されているユーザーIDです"
                    }else{
                        //var data = JSON.parse(response.data)
                        var data = response.data
                        //console.log(data["userid"])
                        //console.log(data["sessionid"])
                        self.userid = Number(data["userid"])
                        self.sessionid = Number(data["sessionid"])
                        self.$emit('signin', self.sessionid, self.userid)
                        self.$router.push("/")
                    }
                })
            }
        },
        loginmethod: function(id){
            this.$emit('signin', id)
        }
    },
    props:{
        redirectto: String
    },
    data () {
        return {
            error: "",
            username: "",
            email:"",
            password:"",
            passwordarea: "",
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
    top: 23px;
    font-size: 10pt;
}
</style>