<template lang="pug">
div
    v-card
        v-card-title レート
        v-layout
            div.ml-8 Your rate is
            div.mx-1.mb-4 {{rate}}.
</template>

<script>
import axios from 'axios'
export default {
    props:{
        userid: Number
    },
    mounted: function(){
        let self = this
        axios.get('http://localhost:8080/api/userinfo/'+String(this.userid))
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