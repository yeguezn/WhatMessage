<script setup lang="ts">
  import { RouterView } from 'vue-router'
  import { useAuthStore } from '@/stores/auth'
  import NavBar from "@/components/navBar/NavBar.vue"

  const { initializeStore, setAuthorizationHeader} = useAuthStore()

  initializeStore()

  setAuthorizationHeader()

</script>

<template>
  <v-app>
    <NavBar></NavBar>
    <v-container>
      <v-main>
        <RouterView />
      </v-main>
    </v-container>

  </v-app>
</template>