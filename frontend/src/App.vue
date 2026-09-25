<template>
  <div class="app-shell">
    <aside class="app-side">
      <h1 class="app-title">地质勘探钻孔编录平台</h1>
      <nav class="nav-list">
        <RouterLink v-for="item in navItems" :key="item.path" :to="item.path" class="nav-item">
          {{ item.label }}
        </RouterLink>
      </nav>
    </aside>
    <main class="app-main">
      <header class="app-head">
        <span class="head-desc">面向地质勘探项目的钻孔布置、岩心编录、地层划分、取样送检与封孔验收的一体化勘探管理后台。</span>
        <span class="head-user">当前值班：{{ store.operator }} · {{ store.shiftLabel }}</span>
      </header>
      <RouterView />
    </main>
  </div>
</template>

<script setup lang="ts">
import { useSessionStore } from '@/stores/session'

const store = useSessionStore()

const navItems = [{ label: "运营概览", path: "/" }, { label: "勘探项目", path: "/project" }, { label: "钻孔", path: "/drillhole" }, { label: "岩心", path: "/core" }, { label: "地层划分", path: "/stratum" }, { label: "取样送检", path: "/sample" }, { label: "地球物理测井", path: "/logging" }, { label: "水文观测", path: "/hydro" }, { label: "孔内测试", path: "/test" }, { label: "钻孔编录", path: "/record" }, { label: "封孔验收", path: "/seal" }, { label: "剖面测量", path: "/section" }, { label: "地质点", path: "/point" }, { label: "钻机设备", path: "/rig" }, { label: "钻探班报", path: "/shiftlog" }, { label: "岩矿鉴定", path: "/assess" }, { label: "安全隐患", path: "/hazard" }, { label: "成果验收", path: "/accept" }, { label: "资料归档", path: "/archive" }]
</script>
