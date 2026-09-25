# 地质勘探钻孔编录平台

面向地质勘探项目的钻孔布置、岩心编录、地层划分、取样送检与封孔验收的一体化勘探管理后台。

这是一个前后端分离的管理平台：前端 Vue 3 + Vite + TypeScript，后端 FastAPI（Python）。
两边各自独立启动，前端 dev server 已关掉自动打开页面，启动后按终端打印的地址手工打开。

## 目录结构

```text
.
├── frontend/                 Vue 3 + Vite + TypeScript 前端
│   ├── src/views/            每个业务模块一个页面
│   ├── src/api/              统一请求封装
│   ├── src/stores/           会话与筛选状态
│   └── vite.config.ts        dev server 配置（open: false）
├── backend/                  FastAPI（Python） 后端
│   ├── app/routers/          每个业务模块一组接口
│   ├── app/services/         业务规则与状态流转
│   └── app/store.py          内存数据仓库与示例数据
├── .gitignore
└── docker-compose.yml
```

## 启动

### 后端

```bash
cd backend
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
./run.sh
```

健康检查：`curl http://127.0.0.1:8000/api/health`

### 前端

```bash
cd frontend
npm install
npm run dev
```

前端默认监听 `http://127.0.0.1:5173/`，dev server 不会自动打开浏览器，
需要自己访问。`/api` 由 vite 代理到后端 `http://127.0.0.1:8000`。

## 业务模块

| 模块 | 目录 | 业务对象 | 主要字段 |
| --- | --- | --- | --- |
| 勘探项目 | `project` | 勘探项目 | 项目编号、项目名称、勘探阶段 |
| 钻孔 | `drillhole` | 钻孔 | 钻孔孔号、所属项目、孔口坐标 |
| 岩心 | `core` | 岩心 | 岩心编号、所属钻孔、起止深度 |
| 地层划分 | `stratum` | 地层分层 | 分层编号、所属钻孔、顶板深度 |
| 取样送检 | `sample` | 取样样品 | 样品编号、所属钻孔、取样深度 |
| 地球物理测井 | `logging` | 测井记录 | 测井编号、所属钻孔、测井方法 |
| 水文观测 | `hydro` | 水文观测记录 | 观测编号、所属钻孔、观测项目 |
| 孔内测试 | `test` | 孔内测试单 | 测试编号、所属钻孔、测试项目 |
| 钻孔编录 | `record` | 编录记录 | 编录编号、所属钻孔、编录日期 |
| 封孔验收 | `seal` | 封孔单 | 封孔编号、所属钻孔、封孔方式 |
| 剖面测量 | `section` | 地质剖面 | 剖面编号、剖面名称、起点坐标 |
| 地质点 | `point` | 地质观察点 | 点位编号、点位类型、坐标位置 |
| 钻机设备 | `rig` | 钻探设备 | 设备编号、设备类型、钻机型号 |
| 钻探班报 | `shiftlog` | 钻探班报 | 班报编号、所属钻孔、班组名称 |
| 岩矿鉴定 | `assess` | 岩矿鉴定单 | 鉴定编号、样品编号、鉴定项目 |
| 安全隐患 | `hazard` | 安全隐患 | 隐患编号、所属项目、隐患类型 |
| 成果验收 | `accept` | 成果验收单 | 验收编号、所属项目、验收内容 |
| 资料归档 | `archive` | 归档资料 | 归档编号、所属项目、资料类型 |

## 约定

- 每个模块的前端页面在 `frontend/src/views/<模块>/index.vue`，后端接口在
  `backend/app/routers/<模块>.py`，业务规则在 `backend/app/services/<模块>.py`。
- 列表接口统一返回 `{ items, total, page, size }`，动作接口统一返回 `{ ok, message }`。
- 状态流转只允许在 `app/services` 里改，路由层不做业务判断。
