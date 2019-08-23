<template>
<v-app>
        <v-card width='800' class="mx-auto mt-5" outlined>
            <v-container class="justify-center">
                <v-list>
                    <div class="display-1 text-center">
                        レシピ
                    </div>
                    <v-divider/>
                    <v-content>
                        <Resipe/>
                    </v-content>
                </v-list>
            </v-container>
        </v-card>
</v-app>
</template>

<script>
import Resipe from './Resipe'
export default {
    components: {
        Resipe
    }
}
</script>

<style>
</style>
