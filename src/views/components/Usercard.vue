<template lang="pug">  
    v-card(height="190px")
        v-card-title ユーザー情報
        v-divider
        v-layout
            v-avatar(class="ma-4" size="36")
                img(src="https://vuetifyjs.com/apple-touch-icon-180x180.png" alt="avatar")
            
            div.usercardcontent
                div.subtitle-2 ユーザー名
                div.title {{ username }}
        v-divider
        div.usercardmailarea
            div.subtitle-2 メールアドレス
            div.title {{ email }}
</template>

<script>
export default {
    data: function(){
        return{
            username:'ぴPI',
            email: "ahahanoha@gmail.com"
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
</style>
