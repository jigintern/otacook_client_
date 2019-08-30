<template>
  <v-app>
    <!--<v-app-bar app>
      <v-toolbar-title class="headline text-uppercase">
        <span>Vuetify</span>
        <span class="font-weight-light">MATERIAL DESIGN</span>
      </v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn
        text
        href="https://github.com/vuetifyjs/vuetify/releases/latest"
        target="_blank"
      >
        <span class="mr-2">Latest Release</span>
      </v-btn>
    </v-app-bar>-->
    <Headercontent :isLoggingin="AppisLoggingin" @signout="logout" />
    <v-content class="master">
      <router-view :isLoggingin="AppisLoggingin" :userid="Appuserid" @signin="login" />
    </v-content>
    <Footer />
  </v-app>
</template>

<script>
import Headercontent from "./views/components/Header";
import Footer from "./views/components/Footer";
import Cookies from "js-cookie";
import axios from "axios";

export default {
  name: "App",
  components: {
    Headercontent,
    Footer
  },
  data: function() {
    return {
      AppisLoggingin: false,
      Appuserid: -1,
      Appsessionid: -1
    };
  },
  computed: {},
  //初回読み込み時にクッキーからセッションID呼び出し
  created: function() {
    const sessionid = Cookies.get("sessionid");
    if (sessionid == -1) {
      this.AppisLoggingin = false;
    } else if (sessionid == undefined) {
      this.AppisLoggingin = false;
    } else {
      //ここでセッションIDをサーバーに送ってログイン状態を確認
      //true なら以下のプロパティをセット
      //false ならCookieのsessionidを-1に
      //Applogginginはfalseにする
      this.Appuserid = 1; //取得したuseridを入れる
      this.Appsessionid = sessionid;
      this.AppisLoggingin = true;
    }
  },
  methods: {
    login: function(sessionid, userid) {
      this.AppisLoggingin = true;
      this.Appuserid = userid;
      this.Appsessionid = sessionid;
      Cookies.set("sessionid", sessionid);
    },
    logout: function() {
      //セッションIDをサーバーに送る
      this.AppisLoggingin = false;
      Cookies.set("sessionid", -1);
    }
  }
};
</script>

<style scoped>
.master {
  background-color: #f7f3e8;
}
</style>