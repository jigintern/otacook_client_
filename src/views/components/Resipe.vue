<template lang='pug'>
div
    v-simple-table
        thead
            tr
                th.text-center 材料
                th.text-center 分量
        tbody
            tr(v-for="item in items" :key="item.name")
                td.text-center {{item.name}}
                td.text-center {{item.amount}}
</template>

<script>
export default {
    data:function(){
        items: [
            {
                name:'玉ねぎ',
                amount:'一本'
            }
        ]
    }
}
</script>