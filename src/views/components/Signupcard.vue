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
      <v-text-field class="mx-4" v-model="email" :rules="[rules.required]" label="メールアドレス" required></v-text-field>
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
      <v-checkbox class="mx-4" label="利用規約に同意する。" required></v-checkbox>
      <div class="text-right mr-4 red--text">{{error}}</div>
      <v-layout justify-space-around>
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
import axios from "axios";
export default {
  data() {
    return {
      error: "",
      username: "",
      email: "",
      password: "",
      passwordarea: "",
      rules: {
        required: value => !!value || "入力必須",
        min: v => v.length >= 8 || "八文字以上でオナシャス"
      }
    };
  },
  methods: {
    tosignin: function() {
      this.$router.push("/signin");
    },
    submit: function() {
      if (this.email == "" || this.password == "" || this.username == "") {
        this.error = "入力していない項目があります";
      } else {
        //mail, userid, passwordをサーバーに送信する
        const params = new URLSearchParams();
        params.append("UserName", this.username);
        params.append("UserMailaddress", this.email);
        params.append("UserPassword", this.password);
        params.append("UserRated", 0);
        axios
          .post("http://localhost:8080/user/insert", params)
          .catch(error => {
            console.log(error);
          })
          .then(Response => {
            this.$router.push("/");
          });
        //会員登録をサーバーで処理して
        //sessionid, useridを取得する
        this.sessionid = 1;
        this.userid = 1;
        this.$emit("signin", this.sessionid, this.userid);
        if (this.redirectto == null) {
          this.$router.push("/");
        } else {
          this.$router.push(this.redirectto);
        }
      }
    },
    loginmethod: function(id) {
      this.$emit("signin", id);
    }
  },
  props: {
    redirectto: String
  }
};
</script>

<style scoped>
.moji {
  position: relative;
  top: 23px;
}
</style>