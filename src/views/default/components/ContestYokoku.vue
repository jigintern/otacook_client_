<template lang="pug">
    v-card.py-1
        v-card-title {{title}}
        .subtitle-1.mx-8 開催時間: {{time}}
        .subtitle-1.mx-8 投票時間: {{votetime}}

        .subtitle-2.mx-8 以下コンテストに必要な材料の目安です
        Materials.ma-4(
            :list="materiallist"
        )
</template>
<script>
import Materials from "../../components/Materials"
export default {
    components: {
        Materials
    },
    data: function(){
        return {
            title: "次回開催予定のコンテスト",
            time: "7:00~8:00",
            votetime: "8:00~9:00",
            jsonlist:'[{"name":"タピオカ","serving":"1kg"},{"name":"天気の子","serving":"10000"},{"name":"肉","serving":"焼肉"},{"name":"あは","serving":"いひ"}]',
        }
    },
    computed: {
        materiallist: function(){
            var array = JSON.parse(this.jsonlist)
            return array
        },
    },
}
</script>