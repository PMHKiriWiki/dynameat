<template>
    <v-app>
      <!-- Left Navigation Drawer -->
      <v-navigation-drawer app v-model="drawer">
        <v-list dense>
          <v-list-item v-for="item in menuItems" :key="item.title" @click="navigateTo(item.route)">
            <v-list-item-icon>
              <v-icon>{{ item.icon }}</v-icon>
            </v-list-item-icon>
            <v-list-item-content>
              <v-list-item-title>{{ item.title }}</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </v-list>
      </v-navigation-drawer>
  
      <!-- App Bar -->
      <v-app-bar app>
        <v-app-bar-nav-icon @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
        <v-toolbar-title>Custom Main Page</v-toolbar-title>
      </v-app-bar>
  
      <!-- Main Content -->
      <v-main>
        <!-- Your main content goes here -->
        <router-view></router-view>
      </v-main>
    </v-app>
  </template>
  
  <script>
  export default {
    data() {
      return {
        drawer: true,
        menuItems: [
          { title: 'Dashboard', icon: 'mdi-view-dashboard', route: '/dashboard' },
          // Add more menu items as needed
        ],
      };
    },
    methods: {
      navigateTo(route) {
        // Use the router to navigate to the specified route
        this.$router.push(route)
      },
    },
  };
  </script>
  
  <style scoped>
  /* Add your custom styles here */
  </style>