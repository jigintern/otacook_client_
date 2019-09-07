<template lang="pug">  
    v-card(height="190px")
        v-card-title.font-logotype ユーザー情報
        v-divider
        v-layout
            v-avatar(class="ma-4" size="36")
                img(src="https://t1.intern.jigd.info/files/20190905-020131pi.png" alt="avatar")
            
            div.usercardcontent
                div.subtitle-2.font-logotype ユーザー名
                div.title {{ username }}
        v-divider
        div.usercardmailarea
            div.subtitle-2.font-logotype ユーザーID
            div.title {{ email }}
</template>

<script>
import axios from 'axios'
export default {
    props:{
        userid: Number
    },
    mounted: function(){
        let self = this
        axios.get('https://t1.intern.jigd.info/flask/api/userinfo/'+String(this.userid))
        .then(function (response) {
            var data = response.data
            //console.log(data["username"])
            //console.log(data["email"])
            self.username = data["username"]
            self.email = data["email"]
        })
    },
    data: function(){
        return{
            username:"",
            email: ""
        }
    }
}
</script>

<style scoped>
.usercardcontent{
    position: relative;
    top: 5px
}
.usercardmailarea{
    position: relative;
    top:5px;
    left: 70px
}

@font-face {
    font-family: 'LogoType';
    src: url('../../fonts/07LogoTypeGothic7.ttf') format('TrueType');
}

@font-face {
    font-family: 'Harenosora';
    src: url('../../fonts/Harenosora.otf') format('OpenType');
}

.font-logotype{
    font-family: 'LogoType';
}
.font-harenosora{
    font-family: 'Harenosora';
}
</style>

