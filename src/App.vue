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
      <Headercontent :isLoggingin="isLoggingin"/>
    <v-content class="master">
        <router-view
          :isLoggingin="isLoggingin"
          :userid="userid"
        />
    </v-content>
    <Footer/>
  </v-app>
</template>

<script>
import Headercontent from './views/components/Header'
import Footer from './views/components/Footer'

export default {
  name: 'App',
  components: {
    Headercontent,
    Footer
  },
  data: function(){
    return{
      isLoggingin: true,
      userid: 0,
    }
  },
};
</script>

<style scoped>
.master{
  background-color: #f7f3e8
}
</style>