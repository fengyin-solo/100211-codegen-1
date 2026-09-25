import { createRouter, createWebHistory } from 'vue-router'

import Dashboard from '@/views/Dashboard.vue'
const Project = () => import('@/views/project/index.vue')
const Drillhole = () => import('@/views/drillhole/index.vue')
const Core = () => import('@/views/core/index.vue')
const Stratum = () => import('@/views/stratum/index.vue')
const Sample = () => import('@/views/sample/index.vue')
const Logging = () => import('@/views/logging/index.vue')
const Hydro = () => import('@/views/hydro/index.vue')
const Test = () => import('@/views/test/index.vue')
const Record = () => import('@/views/record/index.vue')
const Seal = () => import('@/views/seal/index.vue')
const Section = () => import('@/views/section/index.vue')
const Point = () => import('@/views/point/index.vue')
const Rig = () => import('@/views/rig/index.vue')
const Shiftlog = () => import('@/views/shiftlog/index.vue')
const Assess = () => import('@/views/assess/index.vue')
const Hazard = () => import('@/views/hazard/index.vue')
const Accept = () => import('@/views/accept/index.vue')
const Archive = () => import('@/views/archive/index.vue')

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/', name: 'dashboard', component: Dashboard },
    { path: '/project', name: 'project', component: Project },
    { path: '/drillhole', name: 'drillhole', component: Drillhole },
    { path: '/core', name: 'core', component: Core },
    { path: '/stratum', name: 'stratum', component: Stratum },
    { path: '/sample', name: 'sample', component: Sample },
    { path: '/logging', name: 'logging', component: Logging },
    { path: '/hydro', name: 'hydro', component: Hydro },
    { path: '/test', name: 'test', component: Test },
    { path: '/record', name: 'record', component: Record },
    { path: '/seal', name: 'seal', component: Seal },
    { path: '/section', name: 'section', component: Section },
    { path: '/point', name: 'point', component: Point },
    { path: '/rig', name: 'rig', component: Rig },
    { path: '/shiftlog', name: 'shiftlog', component: Shiftlog },
    { path: '/assess', name: 'assess', component: Assess },
    { path: '/hazard', name: 'hazard', component: Hazard },
    { path: '/accept', name: 'accept', component: Accept },
    { path: '/archive', name: 'archive', component: Archive },
  ],
})

export default router
