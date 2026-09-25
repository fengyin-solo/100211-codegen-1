"""接口出入参模型：列表分页、动作结果与各模块的明细结构。"""
from __future__ import annotations

from typing import Any, Generic, TypeVar

from pydantic import BaseModel, Field

T = TypeVar("T")


class PageResult(BaseModel, Generic[T]):
    items: list[T]
    total: int
    page: int = 1
    size: int = 20


class ActionResult(BaseModel):
    ok: bool
    message: str
    entry: dict[str, Any] | None = None


class EntryPayload(BaseModel):
    """登记或修改一条业务记录时提交的字段集合。"""

    values: dict[str, Any] = Field(default_factory=dict)
    remark: str | None = None



class ProjectEntry(BaseModel):
    """勘探项目明细结构。"""

    field_0: str | None = None  # 项目编号
    field_1: str | None = None  # 项目名称
    field_2: str | None = None  # 勘探阶段
    field_3: str | None = None  # 委托单位
    field_4: str | None = None  # 勘探面积
    field_5: str | None = None  # 设计孔数
    field_6: str | None = None  # 开工日期
    field_7: str | None = None  # 项目状态

class DrillholeEntry(BaseModel):
    """钻孔明细结构。"""

    field_0: str | None = None  # 钻孔孔号
    field_1: str | None = None  # 所属项目
    field_2: str | None = None  # 孔口坐标
    field_3: str | None = None  # 设计孔深
    field_4: str | None = None  # 实际孔深
    field_5: str | None = None  # 开孔日期
    field_6: str | None = None  # 终孔日期
    field_7: str | None = None  # 钻孔状态

class CoreEntry(BaseModel):
    """岩心明细结构。"""

    field_0: str | None = None  # 岩心编号
    field_1: str | None = None  # 所属钻孔
    field_2: str | None = None  # 起止深度
    field_3: str | None = None  # 岩心长度
    field_4: str | None = None  # 采取率
    field_5: str | None = None  # 岩性描述
    field_6: str | None = None  # 装箱编号
    field_7: str | None = None  # 岩心状态

class StratumEntry(BaseModel):
    """地层分层明细结构。"""

    field_0: str | None = None  # 分层编号
    field_1: str | None = None  # 所属钻孔
    field_2: str | None = None  # 顶板深度
    field_3: str | None = None  # 底板深度
    field_4: str | None = None  # 地层代号
    field_5: str | None = None  # 岩性名称
    field_6: str | None = None  # 分层厚度
    field_7: str | None = None  # 分层状态

class SampleEntry(BaseModel):
    """取样样品明细结构。"""

    field_0: str | None = None  # 样品编号
    field_1: str | None = None  # 所属钻孔
    field_2: str | None = None  # 取样深度
    field_3: str | None = None  # 样品类型
    field_4: str | None = None  # 送检单位
    field_5: str | None = None  # 送检日期
    field_6: str | None = None  # 检测项目
    field_7: str | None = None  # 样品状态

class LoggingEntry(BaseModel):
    """测井记录明细结构。"""

    field_0: str | None = None  # 测井编号
    field_1: str | None = None  # 所属钻孔
    field_2: str | None = None  # 测井方法
    field_3: str | None = None  # 测量井段
    field_4: str | None = None  # 测量日期
    field_5: str | None = None  # 仪器型号
    field_6: str | None = None  # 解释结论
    field_7: str | None = None  # 测井状态

class HydroEntry(BaseModel):
    """水文观测记录明细结构。"""

    field_0: str | None = None  # 观测编号
    field_1: str | None = None  # 所属钻孔
    field_2: str | None = None  # 观测项目
    field_3: str | None = None  # 水位埋深
    field_4: str | None = None  # 观测日期
    field_5: str | None = None  # 观测人员
    field_6: str | None = None  # 稳定时长
    field_7: str | None = None  # 观测状态

class TestEntry(BaseModel):
    """孔内测试单明细结构。"""

    field_0: str | None = None  # 测试编号
    field_1: str | None = None  # 所属钻孔
    field_2: str | None = None  # 测试项目
    field_3: str | None = None  # 测试深度
    field_4: str | None = None  # 测试值
    field_5: str | None = None  # 标准要求
    field_6: str | None = None  # 测试结论
    field_7: str | None = None  # 测试状态

class RecordEntry(BaseModel):
    """编录记录明细结构。"""

    field_0: str | None = None  # 编录编号
    field_1: str | None = None  # 所属钻孔
    field_2: str | None = None  # 编录日期
    field_3: str | None = None  # 编录人员
    field_4: str | None = None  # 记录段数
    field_5: str | None = None  # 岩性描述
    field_6: str | None = None  # 复核人员
    field_7: str | None = None  # 编录状态

class SealEntry(BaseModel):
    """封孔单明细结构。"""

    field_0: str | None = None  # 封孔编号
    field_1: str | None = None  # 所属钻孔
    field_2: str | None = None  # 封孔方式
    field_3: str | None = None  # 封孔材料
    field_4: str | None = None  # 封孔日期
    field_5: str | None = None  # 施工人员
    field_6: str | None = None  # 验收结论
    field_7: str | None = None  # 封孔状态

class SectionEntry(BaseModel):
    """地质剖面明细结构。"""

    field_0: str | None = None  # 剖面编号
    field_1: str | None = None  # 剖面名称
    field_2: str | None = None  # 起点坐标
    field_3: str | None = None  # 终点坐标
    field_4: str | None = None  # 剖面长度
    field_5: str | None = None  # 测量日期
    field_6: str | None = None  # 测量人员
    field_7: str | None = None  # 剖面状态

class PointEntry(BaseModel):
    """地质观察点明细结构。"""

    field_0: str | None = None  # 点位编号
    field_1: str | None = None  # 点位类型
    field_2: str | None = None  # 坐标位置
    field_3: str | None = None  # 观察日期
    field_4: str | None = None  # 岩性描述
    field_5: str | None = None  # 产状数据
    field_6: str | None = None  # 记录人员
    field_7: str | None = None  # 点位状态

class RigEntry(BaseModel):
    """钻探设备明细结构。"""

    field_0: str | None = None  # 设备编号
    field_1: str | None = None  # 设备类型
    field_2: str | None = None  # 钻机型号
    field_3: str | None = None  # 所属项目
    field_4: str | None = None  # 进场日期
    field_5: str | None = None  # 上次保养日
    field_6: str | None = None  # 运行台时
    field_7: str | None = None  # 设备状态

class ShiftlogEntry(BaseModel):
    """钻探班报明细结构。"""

    field_0: str | None = None  # 班报编号
    field_1: str | None = None  # 所属钻孔
    field_2: str | None = None  # 班组名称
    field_3: str | None = None  # 班次
    field_4: str | None = None  # 本班进尺
    field_5: str | None = None  # 岩心长度
    field_6: str | None = None  # 记录人
    field_7: str | None = None  # 班报状态

class AssessEntry(BaseModel):
    """岩矿鉴定单明细结构。"""

    field_0: str | None = None  # 鉴定编号
    field_1: str | None = None  # 样品编号
    field_2: str | None = None  # 鉴定项目
    field_3: str | None = None  # 送鉴日期
    field_4: str | None = None  # 鉴定单位
    field_5: str | None = None  # 鉴定结论
    field_6: str | None = None  # 鉴定人员
    field_7: str | None = None  # 鉴定状态

class HazardEntry(BaseModel):
    """安全隐患明细结构。"""

    field_0: str | None = None  # 隐患编号
    field_1: str | None = None  # 所属项目
    field_2: str | None = None  # 隐患类型
    field_3: str | None = None  # 隐患等级
    field_4: str | None = None  # 发现日期
    field_5: str | None = None  # 整改措施
    field_6: str | None = None  # 整改期限
    field_7: str | None = None  # 隐患状态

class AcceptEntry(BaseModel):
    """成果验收单明细结构。"""

    field_0: str | None = None  # 验收编号
    field_1: str | None = None  # 所属项目
    field_2: str | None = None  # 验收内容
    field_3: str | None = None  # 验收标准
    field_4: str | None = None  # 验收结论
    field_5: str | None = None  # 验收专家
    field_6: str | None = None  # 验收日期
    field_7: str | None = None  # 验收状态

class ArchiveEntry(BaseModel):
    """归档资料明细结构。"""

    field_0: str | None = None  # 归档编号
    field_1: str | None = None  # 所属项目
    field_2: str | None = None  # 资料类型
    field_3: str | None = None  # 卷册号
    field_4: str | None = None  # 归档日期
    field_5: str | None = None  # 归档人员
    field_6: str | None = None  # 密级
    field_7: str | None = None  # 归档状态
