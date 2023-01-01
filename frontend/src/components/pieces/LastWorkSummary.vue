<template>
    <div class="last_work_summary">
        <!-- <h1>
            Most Recent 
        </h1>
        <p>
            {{most_recent.id}}
        </p>
        <p>
            {{most_recent.name}}
        </p>
 -->

        <ul>
            <!-- <li
                v-for="worksession in worksessions"
                :key="worksession.id"
            >
                {{worksession.name}}
            </li> -->
        </ul>
    </div>
</template>

<script lang="ts">
import axios from 'axios'

export default {
    data () {
        return {
            worksessions: [],
            most_recent : ''
        }
    },
    methods : {
        async getWorksessions(){
            let result = await axios.get('http://localhost:5000/worksessions')
            if (result.data){
                return result.data
            }
        }
    },
    mounted: async function(){
        // let worksessions = await this.getWorksessions()

        // this.worksessions = worksessions

        // this.most_recent = worksessions[0]



    }
}

</script>

<style lang="scss">


.last_work_summary{
    background: yellow;
}

</style>