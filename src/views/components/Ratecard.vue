<template lang="pug">
div
    v-card
        v-card-title.font-logotype レート
        v-layout
            div.ml-8 Your rate is
            div.mx-1.mb-4.font-weight-bold {{rate}}.
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
            self.rate = data["rate"]
        })
    },
    data: function(){
        return{
            rate:""
        }
    }
}
</script>

<style>
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