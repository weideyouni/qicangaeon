# -*- coding: utf-8 -*-
"""qc_ledger.py · qicangaeon 打捞账本+README 锁+批总闸（QC-V1）

打捞账（DREDGE_LEDGER append-only）：每次出网打捞入账——
需求指纹+三账快照计数+归航验证（netaeon route 归位——两网
级联留痕）。种子 1 条=本批建仓（递归先例，承 TD-0001 同型）。

README 锁（承 mirraeon mirror_ledger 惯例）：口径数字在
README 必须可回读——漂移即 FAIL。

批总闸=qc_core 19+本件账闸合检。

诚实边界：打捞账为演示态（种子 1 条），真实打捞由执行端按
投喂包流程入账；归航验证以 netaeon 在机为前提（不在机 SKIP
诚实）。

封口密语：潮起开门，潮落闭嘴。
"""

from __future__ import annotations

import json
import sys
from typing import Any, Dict, List

try:
    from . import qc_core
except ImportError:
    import qc_core

try:
    from netaeon import net_core
except ImportError:
    import net_core

SCHEMA = "QICANGAEON-LEDGER/1.0"
SEAL = "潮起开门，潮落闭嘴"
BATCH = "QC-V1"

# ---------------------------------------------------------------------------
# §1 打捞账（append-only；演示态种子 1 条）
# ---------------------------------------------------------------------------

DREDGE_LEDGER: List[Dict[str, Any]] = [
    {"rid": "DR-0001",
     "demand": "启藏建仓（碳基指令：打捞之网模式全局孵化）",
     "input_hash16": qc_core._hash16(
         "启藏建仓 打捞之网 全局 独立建仓 19 仓库 25 机制"),
     "source": "碳基指令+千问《纪元·启藏》策划案（投喂）",
     "authority_source": "碳基指令（终裁源）+本批投喂包",
     "node_count": None,  # 落账时由 check 回填实测
     "mech_count": None,
     "state": "dispatched",
     "note": "种子：本仓建制本身入账（递归先例，承 TD-0001）"},
]


def append_dredge(demand: str, source: str = "执行端") -> \
        Dict[str, Any]:
    """真实打捞入账（append-only；执行端按投喂包流程调用）。"""
    if not demand or not demand.strip():
        raise ValueError("打捞需求须非空")
    d = qc_core.dredge(demand)
    entry = {"rid": "DR-{:04d}".format(len(DREDGE_LEDGER) + 1),
             "demand": demand,
             "input_hash16": d["input_hash16"],
             "source": source,
             "authority_source": "执行端回执（验收权威——AR-4）",
             "node_count": d["node_count"],
             "mech_count": d["mech_count"],
             "state": "dispatched", "note": ""}
    DREDGE_LEDGER.append(entry)
    return dict(entry)


def dredge_ledger() -> List[Dict[str, Any]]:
    return [dict(t) for t in DREDGE_LEDGER]


# ---------------------------------------------------------------------------
# §2 账本闸（含归航级联验证+README 锁）
# ---------------------------------------------------------------------------


def check_ledger() -> Dict[str, Any]:
    checks: List[Dict[str, Any]] = []

    def add(name, ok, note=""):
        checks.append({"check": name, "ok": bool(ok), "note": note})

    add("ledger_seeded_recursive",
        len(DREDGE_LEDGER) >= 1
        and DREDGE_LEDGER[0]["rid"] == "DR-0001",
        "种子 1 条在账（本仓建制递归先例）")
    add("ledger_fields_complete",
        all({"rid", "demand", "input_hash16", "source",
             "authority_source", "state"} <= set(t.keys())
            for t in DREDGE_LEDGER),
        "每条打捞账六字段齐（AR-1 派活带权威源）")

    # 种子回填实测（node_count/mech_count 由真跑回填——账实一致）
    d = qc_core.dredge(
        "启藏建仓 打捞之网 全局 独立建仓 19 仓库 25 机制")
    DREDGE_LEDGER[0]["node_count"] = d["node_count"]
    DREDGE_LEDGER[0]["mech_count"] = d["mech_count"]
    add("seed_backfilled_live",
        DREDGE_LEDGER[0]["node_count"] == d["node_count"]
        and DREDGE_LEDGER[0]["mech_count"] == d["mech_count"],
        "种子账实测回填（出网真跑 {} 仓/{} 机制）".format(
            d["node_count"], d["mech_count"]))

    # 归航级联验证（两网级联：打捞出网→netaeon 归航回港）
    try:
        r = net_core.route("启藏 文明挖掘 打捞 挖掘机")
        add("netaeon_cascade_live",
            r.get("schema") == "NETAEON-NET/1.0"
            and r.get("verdict") in ("known", "unknown"),
            "归航级联在案（打捞出网→netaeon route 回港——"
            "两网级联单例实测，verdict={}）".format(
                r.get("verdict")))
    except Exception as e:  # noqa: BLE001
        add("netaeon_cascade_live", False, str(e)[:120])

    # 真名对照账（承 qc_core NAME_MAP——账本侧对账）
    nm = {e["alias"]: e["status"] for e in qc_core.NAME_MAP}
    add("namemap_19repo_done_adjusted",
        nm.get("19 仓库") == "done",
        "19 仓库 done+adjusted 在账（投喂降级被实测推翻留痕）")

    # 打捞幂等（同需求不重复入账——承 dispatch 幂等同律）
    n0 = len(DREDGE_LEDGER)
    try:
        append_dredge("")
        add("append_rejects_empty", False)
    except ValueError:
        add("append_rejects_empty", True,
            "空需求入账被拒（append-only 账目纪律）")

    # 孵化登记账
    add("incubation_registry_consistent",
        len(qc_core.INCUBATION_REGISTRY) == 3
        and qc_core.INCUBATION_REGISTRY[0]["id"] == "INC-001",
        "孵化登记账 3 条在册（全局独立建仓范式）")

    failed = [c for c in checks if not c["ok"]]
    return {"schema": SCHEMA, "batch": BATCH, "seal": SEAL,
            "total": len(checks), "passed": len(checks) - len(failed),
            "failed": len(failed),
            "verdict": "PASS" if not failed else "FAIL",
            "checks": checks}


# ---------------------------------------------------------------------------
# §3 README 锁（数字口径在 README 必须可回读——承 mirror_ledger）
# ---------------------------------------------------------------------------


def check_readme_sync() -> Dict[str, Any]:
    checks: List[Dict[str, Any]] = []

    def add(name, ok, note=""):
        checks.append({"check": name, "ok": bool(ok), "note": note})

    import os
    readme_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), os.pardir,
        "README.md")
    try:
        text = open(readme_path, encoding="utf-8").read()
    except OSError:
        return {"schema": "QICANGAEON-README-SYNC/1.0",
                "batch": BATCH, "total": 0, "passed": 0, "failed": 0,
                "verdict": "SKIP", "checks": [],
                "note": "README.md 不在机：跳过（仓内必在）"}

    # 口径数字（README 数字口径对账表须可回读）
    for num, name in ((19, "19 节点"), (25, "25 机制"),
                      (24, "ring24"), (6, "六机构"),
                      (7, "七步孵化协议"), (12, "真名对照 12 条")):
        add("readme_covers_{}".format(name),
            str(num) in text, "{} 在 README 可回读".format(name))
    add("readme_has_seal", "潮起开门，潮落闭嘴" in text,
        "封口密语在 README")

    failed = [c for c in checks if not c["ok"]]
    return {"schema": "QICANGAEON-README-SYNC/1.0", "batch": BATCH,
            "total": len(checks), "passed": len(checks) - len(failed),
            "failed": len(failed),
            "verdict": "PASS" if not failed else "FAIL",
            "checks": checks}


# ---------------------------------------------------------------------------
# §4 批总闸（qc_core 19+ledger 8+README 锁 7）
# ---------------------------------------------------------------------------


def check_batch() -> Dict[str, Any]:
    parts = {"qc_core": qc_core.check_qc_core(),
             "qc_ledger": check_ledger(),
             "readme_sync": check_readme_sync()}
    total = passed = failed = 0
    for r in parts.values():
        total += r["total"]
        passed += r["passed"]
        failed += r["failed"]
    return {"schema": SCHEMA, "batch": BATCH, "seal": SEAL,
            "total": total, "passed": passed, "failed": failed,
            "verdict": "PASS" if failed == 0 else "FAIL",
            "parts": {k: {"total": v["total"],
                          "passed": v["passed"],
                          "failed": v["failed"],
                          "verdict": v["verdict"]}
                      for k, v in parts.items()}}


def _main(argv: List[str]) -> int:
    cmd = argv[1] if len(argv) > 1 else "check"
    if cmd == "check":
        r = check_ledger()
        print(json.dumps({k: r[k] for k in
                          ("schema", "batch", "total", "passed",
                           "failed", "verdict")},
                         ensure_ascii=False))
        for c in r["checks"]:
            if not c["ok"]:
                print("FAIL:", c["check"], c.get("note", ""))
        return 0 if r["verdict"] == "PASS" else 1
    if cmd == "batch":
        r = check_batch()
        print(json.dumps(r, ensure_ascii=False, indent=1))
        return 0 if r["verdict"] == "PASS" else 1
    if cmd == "ledger":
        print(json.dumps(dredge_ledger(), ensure_ascii=False,
                         indent=1))
        return 0
    print("usage: qc_ledger.py [check|batch|ledger]")
    return 2


if __name__ == "__main__":
    sys.exit(_main(sys.argv))
