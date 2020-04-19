import Vue from 'vue'
import Router from 'vue-router'
// import HelloWorld from '@/components/HelloWorld'
import Index from '../views/Index'
import Todo from '../views/Todo'
import Md from '../views/Md'
import Article from '../views/Article'
import Conclusion from '../views/Conclusion'
import Forum from '../views/Forum'
import Personal from '../views/Personal'
import Userinfo from '../views/Userinfo'


Vue.use(Router)

const routerPush = Router.prototype.push
Router.prototype.push = function push(location) {
  return routerPush.call(this, location).catch(error=> error)
}

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Index',
      component: Index
    },
    {
      path: '/todo',
      name: 'Todo',
      component: Todo
    },
    {
      path: '/md',
      name: 'Md',
      component: Md
    },
    {
      path: '/article',
      name: 'Article',
      component: Article
    },
    {
      path: '/conclusion',
      name: 'Conclusion',
      component: Conclusion,
      children:[
        {
          path: 'forum',
          name: 'Forum',
          component: Forum
        },
        {
          path: 'personal',
          name: "Personal",
          component: Personal
        }
      ]
    },
    {
      path: '/userinfo',
      name: 'Userinfo',
      component: Userinfo
    }
  ]
})
