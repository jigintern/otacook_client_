<template lang="pug">
div
    v-card
        v-card-title.headline.text-weight-light.text-weight-italic 材料リスト
        
        div.mx-6.pb-4
            v-simple-table(dense)
                thead
                    tr
                        th.text-center 材料
                        th.text-center 分量
                tbody
                    tr(v-for="item in list")
                        td.text-center.body-2 {{ item.name }}
                        td.text-center.body-2 {{ item.serving }}
            v-divider
            //ul.ml-6.pb-4
                li.body-1(v-for="line in list") {{ line.message }}
</template>

<script>
export default {
    props:{
        list: Array
    }
}
</script>

<style>
</style>
