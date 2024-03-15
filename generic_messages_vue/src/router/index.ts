import { createRouter, createWebHistory } from 'vue-router' 
import { useAuthStore } from '@/stores/auth'
import NotFoundView from "@/views/NotFoundView.vue"

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: () => import('../views/HomeView.vue')
    },

    {
      path: '/new-contact',
      name: 'new-contact',
      component: () => import('../views/CreateContactView.vue'),
      meta:{
        requireLogin:true
      }
    },

    {
      path: '/get-contacts',
      name: 'get-contacts',
      component: () => import('../views/ContactsView.vue'),
      meta:{
        requireLogin:true
      }
    },

    {
      path: '/signup',
      name: 'signup',
      component: () => import('../views/SignUpView.vue')
    },

    {
      path: '/login',
      name: 'login',
      component: () => import('../views/LogInView.vue')
    },

    {
      path: '/send-message',
      name: 'send-message',
      component: ()=> import('../views/SendMessageView.vue'),
      meta:{
        requireLogin:true
      }
    },

    {
      path: '/history',
      name: 'history',
      component: ()=> import('../views/HistoryView.vue'),
      meta:{
        requireLogin:true
      }
    },

    {
      path: '/edit-contact/:contactId',
      name: 'edit-contact',
      component: ()=> import('../views/EditContactView.vue'),
      meta:{
        requireLogin:true
      }
    },

    {
      path: '/:pathMatc(.*)*',
      name: 'not-found',
      component:NotFoundView,
    },
  
  ]
})

router.beforeEach((to, from, next)=>{
  const { isAuthenticated } = useAuthStore()
  
  if (to.matched.some(record => record.meta.requireLogin) && !isAuthenticated){

    next({name:"login", query:{ to: to.path }})
    
  }

  else if (to.path ==="/login" && isAuthenticated){

    next({name:"send-message"})
    
  }

  else if(to.path === "/" && isAuthenticated){

    next({name:"send-message"})

  }

  else if (to.path ==="/signup" && isAuthenticated){

    next({name:"send-message"})
    
  }
  
  else{
    next()
  }
  
})

export default router