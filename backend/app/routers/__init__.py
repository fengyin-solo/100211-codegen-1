"""业务模块路由汇总。

这里统一按别名导入再暴露 ROUTERS：模块名有可能和内置名撞车（某个业务模块就叫 dict、list
这种名字时），按名字直接 import 会把内置类型覆盖掉，函数注解在运行时求值就会报
'module' object is not subscriptable。
"""
from __future__ import annotations

from app.routers import project as router_project
from app.routers import drillhole as router_drillhole
from app.routers import core as router_core
from app.routers import stratum as router_stratum
from app.routers import sample as router_sample
from app.routers import logging as router_logging
from app.routers import hydro as router_hydro
from app.routers import test as router_test
from app.routers import record as router_record
from app.routers import seal as router_seal
from app.routers import section as router_section
from app.routers import point as router_point
from app.routers import rig as router_rig
from app.routers import shiftlog as router_shiftlog
from app.routers import assess as router_assess
from app.routers import hazard as router_hazard
from app.routers import accept as router_accept
from app.routers import archive as router_archive

ROUTERS = [router_project, router_drillhole, router_core, router_stratum, router_sample, router_logging, router_hydro, router_test, router_record, router_seal, router_section, router_point, router_rig, router_shiftlog, router_assess, router_hazard, router_accept, router_archive]
