<script setup>
defineProps(['name', 'id'])
defineEmits(['remove'])
</script>

<template>
    <li>
        <p>
            {{id}}
        </p>
        <p>
            {{name}}
        </p>
        <button id="update_button" @click="$emit('update')">UPDATE</button>
        <button id="remove_button" @click="$emit('remove')">REMOVE</button>
    </li>

</template>

<style scoped>
#update_button{
    background: blue;
    /* width: 30em; */
}
#remove_button{
    background: red;
    /* width: 30em; */
}

</style>