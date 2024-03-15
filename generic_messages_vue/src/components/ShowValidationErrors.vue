<script setup lang="ts">

    defineProps<{
        errors:Array<string>
    }>()


</script>

<template>

    <v-alert title="Something went wrong"
    type="error" class="mb-4 mx-auto" icon="em em-scream" width="600">

        <p v-for="message in errors">
            - {{ message }}
        </p>

    </v-alert>

</template>