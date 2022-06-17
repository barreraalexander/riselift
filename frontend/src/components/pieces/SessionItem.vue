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

<style lang="scss">
@import "@/assets/scss/pieces/SessionItem.scss"
</style>