"""岩矿鉴定接口：维护岩矿鉴定单，覆盖办理送鉴、提交结论、确认复核等动作。"""
from __future__ import annotations

from typing import Any

from fastapi import APIRouter, HTTPException, Query

from app.schemas import ActionResult, EntryPayload, PageResult
from app.services.assess import AssessService

router = APIRouter(prefix="/api/assess", tags=["岩矿鉴定"])

service = AssessService()

LIST_FIELDS = ["鉴定编号", "样品编号", "鉴定项目", "送鉴日期", "鉴定单位", "鉴定结论", "鉴定人员", "鉴定状态"]
STATUSES = ["待送鉴", "已送鉴", "已出结论", "已复核"]


@router.get("", response_model=PageResult[dict])
def list_entries(
    keyword: str | None = Query(default=None, description="按鉴定编号检索"),
    status: str | None = Query(default=None, description="待送鉴、已送鉴、已出结论、已复核"),
    page: int = 1,
    size: int = 20,
) -> PageResult[dict]:
    """按鉴定编号与状态过滤岩矿鉴定列表；没有数据时返回空页，不报错。"""
    if size > 200:
        raise HTTPException(status_code=400, detail="每页最多 200 条，请缩小分页范围")
    items, total = service.list_entries(keyword=keyword, status=status, page=page, size=size)
    return PageResult(items=items, total=total, page=page, size=size)


@router.get("/{entry_id}", response_model=dict)
def get_entry(entry_id: int) -> dict:
    """读取单条岩矿鉴定单明细；不存在时给出可读的错误说明。"""
    entry = service.get_entry(entry_id)
    if entry is None:
        raise HTTPException(status_code=404, detail=f"岩矿鉴定单 {entry_id} 不存在或已归档")
    return entry


@router.post("", response_model=ActionResult)
def create_entry(payload: EntryPayload) -> ActionResult:
    """登记一条岩矿鉴定单，缺字段时说明原因而不是静默丢弃。"""
    entry, missing = service.create_entry(payload.values)
    if missing:
        return ActionResult(ok=False, message=f"缺少必填字段：{'、'.join(missing)}")
    return ActionResult(ok=True, message="岩矿鉴定单已登记", entry=entry)


@router.post("/{entry_id}/actions", response_model=ActionResult)
def run_action(entry_id: int, payload: EntryPayload) -> ActionResult:
    """对单条岩矿鉴定单执行办理送鉴、提交结论、确认复核；不允许的动作会被拦下并说明原因。"""
    action = str(payload.values.get("action") or "").strip()
    entry, message = service.run_action(entry_id, action)
    if entry is None:
        return ActionResult(ok=False, message=message)
    return ActionResult(ok=True, message=message, entry=entry)


@router.get("/export")
def export_entries() -> dict[str, Any]:
    """导出岩矿鉴定清单：返回当前过滤条件下的全量数据。"""
    items, total = service.list_entries(page=1, size=10000)
    return {"module": "assess", "total": total, "items": items}
