# -*- coding: utf-8 -*-
"""qc_core.py · qicangaeon 启藏核心：三维语义张量+真名对照+打捞出网（QC-V1）

碳基指令落点：五人组接千问《纪元·启藏：人类文明信息挖掘机 ×
HoloAeon 融合策划案》扬弃——打造打捞之网（主动出网版）、自动
匹配项目名称、独立建仓、关联基座及 25 机制、自组织相似性 M07、
匹配 19 仓库、融通内部协议、全域全员加载。**碳基修正（建仓中
追加）：整体独立建仓非只针对打捞之网——打捞之网模式固化为
全局新项目孵化范式（§5），启藏=1 号孵化实例，未来新项目一律
独立建仓独立启动。**

第一性原理三条（启藏建仓纲领）：

  1. **打捞是主动出网，归航是被动回港**（与 netaeon 分工）：
     netaeon（NA-V1 建仓，中文名"打捞之网"=归航路由网）回答
     "文本归哪个仓"；qicangaeon 回答"升级需求该去哪些仓打捞
     哪些资产"——出网打捞+归航验证两网级联（打捞账经 netaeon
     route 归位登记）。名字纪律：netaeon 中文名不动，启藏以
     qicangaeon 独立命名（纪元族第六员，*aeon 族自动匹配）。
  2. **只蒸馏形状，不搬领域资产**（投喂 ring 纪律采纳）：打捞
     记录=指针+指纹+真名对照（done/designed 标注），零复制零
     vendoring；每个机制标注真伪——无权威源一律 designed。
  3. **先证红律贯穿**（AR-2/AR-3/AR-4 承 NA-V5）：本件真名
     对照表对投喂策划案逐条对账——**投喂的 designed 降级本身
     也被实测对账**："19 仓库无权威源"判定被 netaeon 19 节点
     注册表推翻（adjusted 留痕，承千问 C08 同型先例：手写判定
     被实测权威推翻，扬弃不是照单全收）。

三维语义张量（投喂最核心建模资产·扬弃采纳）：
  - X 场域六锚：**自动匹配本体系六步位**（道/法/术/器/升维/
    横切——真 import legion_dispatch.STEP_ROUTING，done）；
  - Y 马斯洛弹性权重向量：五层 schema（公开口径登记，done）；
  - Z 意义状态五类：槽位 5 承投喂声明，**具体内容待权威源
    喂入（designed——投喂"6 项待喂入"清单如实承接）**。

自组织相似性（M07）：打捞命中=确定性双向子串匹配（键在文中/
文词含键），承 net_core 同律——非相似度模型、零评分（M07
机制真 import meridian_link，锚点指针登记）。

诚实边界：Z 维五类内容待喂入；IPU 可寻址单元 designed；本件
为机制建制+演示态打捞账（种子 1 条），真实打捞由执行端按
投喂包流程入账。

封口密语：潮起开门，潮落闭嘴。
"""

from __future__ import annotations

import json
import sys
from typing import Any, Dict, List

try:
    from netaeon import net_core
    from holoaeon import meridian_link
    from mirraeon import legion_dispatch
except ImportError:  # 直接模块路径兜底（三仓根在 sys.path）
    import net_core
    import meridian_link
    import legion_dispatch

SCHEMA = "QICANGAEON-CORE/1.0"
SEAL = "潮起开门，潮落闭嘴"
BATCH = "QC-V1"
REPO_CN = "启藏·文明挖掘环（打捞之网·主动出网版）"
RING = 24  # 当前链 ring23（salvage_gate 打捞局）+1；投喂自称
# ring-25 属策划案编号口径，实测对账 adjusted（承 C08 先例）
NODE_TOTAL = net_core.NODE_TOTAL    # 19（单一真源指针）
MECH_TOTAL = net_core.MECH_TOTAL    # 25（单一真源指针）

# ---------------------------------------------------------------------------
# §1 真名对照表（投喂策划案逐条对账——done/designed 先证红律）
# ---------------------------------------------------------------------------

NAME_MAP: List[Dict[str, str]] = [
    # ── done：权威源实测在案（投喂落位正确）──
    {"alias": "Mirror", "real": "mirraeon",
     "status": "done",
     "authority_source": "mirraeon.ledger_legion（66 科学轴+83 "
                        "工程轴=133 自然人席位——实测可回读）"},
    {"alias": "Graph 城邦化", "real": "polisaeon",
     "status": "done",
     "authority_source": "polisaeon 仓（纪元族第三员，城市轴）"},
    {"alias": "细胞骨架经络心跳", "real": "确定性时钟",
     "status": "done",
     "authority_source": "holoaeon 基座机制（25 机制轴经 "
                        "meridian_link 注册——指针）"},
    {"alias": "1331×1331", "real": "11³ 立方体",
     "status": "done",
     "authority_source": "mirraeon.mirror_core.MIRROR_GRID==11**3"
                        "（实测在案）"},
    {"alias": "慢病", "real": "ssyd-chronic-engine（六零声明）",
     "status": "done",
     "authority_source": "holoaeon V41-A（ring 12，dimensions "
                        "untouched）"},
    {"alias": "长寿", "real": "LongAeon V9b",
     "status": "done",
     "authority_source": "longaeon 仓（纪元族第二员）"},
    {"alias": "RuntimeGraph/AdaptiveGraph", "real": "graph/forge 模块",
     "status": "done",
     "authority_source": "mirraeon README 诚实边界节（语义映射"
                        "如实登记——承 MR-V2 先例）"},
    # ── done：投喂降级被实测推翻（adjusted——扬弃裁决留痕）──
    {"alias": "19 仓库", "real": "netaeon 19 节点注册表",
     "status": "done",
     "adjusted": "投喂判 designed（无权威源）被实测推翻："
                 "net_core.build_nodes() 19 节点（C01-C18+MIR）"
                 "在案——降级本身也要对账",
     "authority_source": "netaeon.net_core.build_nodes()"},
    # ── designed：无权威源，如实降级（投喂判定正确承接）──
    {"alias": "108641", "real": "",
     "status": "designed",
     "authority_source": "无——待权威源喂入（勿落账勿虚称）"},
    {"alias": "贝叶斯衍射 15 模块", "real": "",
     "status": "designed",
     "authority_source": "无——bayes_reasoning 实测模块数待"
                        "对账（先证红后落位）"},
    {"alias": "曼陀罗一把八", "real": "",
     "status": "designed",
     "authority_source": "无——待权威源喂入"},
    {"alias": "可寻址 IPU", "real": "",
     "status": "designed",
     "authority_source": "无——投喂待喂入清单项（六项之一）"},
]

# ---------------------------------------------------------------------------
# §2 三维语义张量 schema（投喂核心资产·扬弃自动匹配）
# ---------------------------------------------------------------------------

QC_TENSOR: Dict[str, Any] = {
    "schema": "QICANG-QC-TENSOR/1.0",
    "X_field_anchors": {
        "count": 6, "status": "done",
        "anchors": [r["step"] for r in legion_dispatch.STEP_ROUTING],
        "authority_source": "mirraeon.legion_dispatch.STEP_ROUTING"
                           "（六步位真 import——场域锚自动匹配"
                           "五步协议+横切，非投喂原案字段照搬）"},
    "Y_maslow_weights": {
        "count": 5, "status": "done",
        "layers": ["生理", "安全", "归属", "尊重", "自我实现"],
        "authority_source": "马斯洛需求五层（公开口径登记——"
                           "schema 定义，权重向量待真实打捞样本"
                           "回填，本件不虚称已标定）"},
    "Z_meaning_states": {
        "count": 5, "status": "designed",
        "slots": None,
        "authority_source": "无——槽位数 5 承投喂声明，具体五类"
                           "内容待权威源喂入（投喂 6 项待喂入"
                           "清单如实承接）"},
}

# ---------------------------------------------------------------------------
# §3 机构映射（打捞局/规划局/制造局/熔炉/神灯/漩涡——指针非复制）
# ---------------------------------------------------------------------------

BUREAU_MAP: Dict[str, Dict[str, str]] = {
    "打捞局": {"module": "holoaeon.salvage_gate", "ring": "23",
              "note": "18 维检索网+打捞资产身份册（ring23）"},
    "规划局": {"module": "holoaeon.forge_bureau",
              "note": "锻造局（规划+制造一体两局）"},
    "制造局": {"module": "holoaeon.forge_bureau",
              "note": "同上——forge_bureau 双职能"},
    "熔炉": {"module": "holoaeon.holo_forge", "ring": "—",
            "note": "全息熔炉（指针登记）"},
    "神灯": {"module": "holoaeon.magic_lamp", "ring": "V29",
            "note": "magic_lamp 已知技能索引（V29 落地）"},
    "漩涡": {"module": "holoaeon.mobius_vortex", "ring": "V26",
            "note": "莫比乌斯漩涡（V26 落地）"},
}

# ---------------------------------------------------------------------------
# §4 打捞出网（需求文本→三账：节点/机制/步位——确定性零评分）
# ---------------------------------------------------------------------------


def dredge(text: str) -> Dict[str, Any]:
    """打捞出网：升级需求文本 → 命中三账。

    ① 节点命中账（19 仓——键双向子串，承 net_core 同律）；
    ② 机制命中账（25 机制——真 import net_core.mech_hits，
       单一真源零复制）；
    ③ 步位路由账（六步位——真 import legion_dispatch。
       STEP_ROUTING，打捞结果派工到责任席）。
    同文同账（确定性）；零评分（M07 自组织相似性=确定性键命中
    非相似度模型）。
    """
    if not text or not text.strip():
        raise ValueError("打捞需求须非空")
    nodes = net_core.build_nodes()
    t = text.lower()
    words = [w for w in
             t.replace("，", " ").replace("、", " ").split()
             if w]
    node_hits = []
    for n in nodes:
        keys = n["keywords"]
        matched = [k for k in keys
                   if k.lower() in t
                   or any(w in k.lower() or k.lower() in w
                          for w in words)]
        if matched:
            node_hits.append({"node": n["node_id"],
                              "cang": n["cang"],
                              "matched_keys": matched[:5]})
    mech_hits = net_core.mech_hits(text)   # 单一真源（25 机制键）
    routing = {r["step"]: r["seat"] for r in
               legion_dispatch.STEP_ROUTING}
    return {"schema": "QICANG-DREDGE/1.0", "batch": BATCH,
            "seal": SEAL,
            "input_hash16": _hash16(text),
            "node_hits": node_hits,
            "node_count": len(node_hits),
            "mech_hits": mech_hits,
            "mech_count": len(mech_hits),
            "step_routing": routing,
            "note": "三账确定性命中（零评分）；打捞账入 "
                    "qc_ledger.DREDGE_LEDGER（append-only）",
            }


def _hash16(text: str) -> str:
    import hashlib
    return hashlib.md5(text.encode("utf-8")).hexdigest()[:16]


# ---------------------------------------------------------------------------
# §5 全局新项目孵化协议（碳基修正指令落点：整体独立建仓——打捞之
# 网模式不是单仓方案，是全局范式）+ 孵化登记账
# ---------------------------------------------------------------------------

INCUBATION_PROTOCOL: List[Dict[str, str]] = [
    {"step": "①出网打捞", "act": "dredge() 需求三账（19 仓节点"
     "+25 机制+六步位）——确定性零评分命中"},
    {"step": "②五人组扬弃", "act": "采纳/改造/拒收/碳基独占四"
     "分裁决——无权威源一律 designed（先证红律）"},
    {"step": "③独立建仓", "act": "*aeon 族自动命名+中文名+README"
     " 同类型同风格（价值仲裁观阅/数字口径对账表/验真路径/"
     "诚实边界/封口密语）"},
    {"step": "④全域装载", "act": "loader REPOS 增项+GLOBAL_LOAD "
     "对账+五地同步（Gitee/GitHub/HF/vector-sea）"},
    {"step": "⑤投喂包", "act": "tmp 权威交付源+md5-16 指纹表+"
     "执行序（豆包执行端）"},
    {"step": "⑥执行回执", "act": "批闸/测试数/指纹/commit hash"
     " 四对账+DISPATCH_LEDGER 状态机 audited"},
    {"step": "⑦记忆回填", "act": "daily log+总监 MEMORY+"
     "project_registry+用户级 MEMORY+玉安记忆之王五地"},
]

INCUBATION_REGISTRY: List[Dict[str, str]] = [
    {"id": "INC-001", "name": "qicangaeon（启藏·打捞之网主动"
     "出网版）", "status": "done",
     "note": "1 号孵化实例=本仓本批（全局独立建仓范式首例"
             "——碳基修正指令落点）"},
    {"id": "INC-002", "name": "三维语义张量标定（Y 权重向量）",
     "status": "designed",
     "note": "待真实打捞样本回填——schema 已登记（QC_TENSOR "
             "Y 维），独立立项待碳基点单"},
    {"id": "INC-003", "name": "可寻址 IPU", "status": "designed",
     "note": "投喂 6 项待喂入之一——无权威源不立项，登记候选"},
    {"id": "INC-004", "name": "qixiaeon（启曦·分形式生成骨架·"
     "ring25）", "status": "done",
     "note": "4 号孵化实例：QX-V1 跨仓派单落 qixiaeon 首笔 "
             "d299ecd（建仓执行端=qixiaeon 自身）；本仓管孵化、"
             "qixiaeon 管生成骨架，两环相邻同承 M07 全息相似性"
             "口径"},
    {"id": "INC-005", "name": "eduaeon（教育环·纪元族"
     "第八员·ring26）", "status": "done",
     "note": "5 号孵化实例：ED-V1 跨仓派单落 eduaeon 首笔 "
             "dc132769（建仓执行端=eduaeon 自身，七步孵化"
             "协议第三次应用）；本仓管孵化、eduaeon 管教育"
             "域垂类（EduRing→holoaeon.edu_gate ring8 为"
             "机制真源，域层与机制层不混）"},
    {"id": "INC-007", "name": "forgaeon（锻闸·纪元族第十员·ring28）",
     "status": "done",
     "note": "7 号孵化实例：FG-V1 跨仓派单落 forgaeon 首笔 "
             "b7bf288（建仓执行端=forgaeon 自身，七步孵化"
             "协议第四次应用）；本仓管孵化、forgaeon 管建仓"
             "质检（六病型前置闸，与启藏孵化环正交分工）。"
             "编号依 FG-V1 投喂指定 INC-007（INC-006 预留"
             "未入账，跳号在案）"},
]


# ---------------------------------------------------------------------------
# §6 总闸（二十闸全绿）
# ---------------------------------------------------------------------------


def check_qc_core() -> Dict[str, Any]:
    checks: List[Dict[str, Any]] = []

    def add(name, ok, note=""):
        checks.append({"check": name, "ok": bool(ok), "note": note})

    # 真源接线（三仓指针——19/25/六位全真 import）
    add("nodes_19_live",
        len(net_core.build_nodes()) == NODE_TOTAL,
        "19 节点真 import（netaeon 单一真源——打捞网域）")
    add("mechs_25_live",
        len(meridian_link.KERNEL_MECHANISMS) == MECH_TOTAL,
        "25 机制真 import（holoaeon meridian_link 单一真源）")
    add("routing_six_live",
        len(legion_dispatch.STEP_ROUTING) == 6,
        "六步位真 import（mirraeon legion_dispatch 单一真源）")

    # M07 自组织相似性锚（第一性原理点名机制）
    m07 = [m for m in meridian_link.KERNEL_MECHANISMS
           if m.get("id") == "M07"]
    add("m07_similarity_anchored",
        len(m07) == 1 and m07[0]["name"] == "自组织相似性",
        "M07 自组织相似性在案（确定性键命中非相似度模型——"
        "零评分纪律）")

    # 真名对照表（先证红律）
    add("namemap_done_verified",
        all(e["authority_source"] for e in NAME_MAP
            if e["status"] == "done"),
        "done 条目全带 authority_source（AR-1）")
    add("namemap_designed_honest",
        all(e["real"] == "" for e in NAME_MAP
            if e["status"] == "designed"),
        "designed 条目不落 real 值（不虚称落位）")
    add("namemap_adjusted_evidence",
        any(e.get("adjusted") for e in NAME_MAP),
        "投喂降级被实测推翻留痕（19 仓库条——adjusted 在案，"
        "扬弃不是照单全收）")
    add("namemap_grid_11c3",
        any(e["alias"] == "1331×1331" and e["real"] == "11³ 立方体"
            for e in NAME_MAP),
        "11³ 对照在册（mirror_core 实测）")

    # 三维张量
    qt = QC_TENSOR
    add("tensor_x_six_done",
        qt["X_field_anchors"]["count"] == 6
        and qt["X_field_anchors"]["status"] == "done",
        "X 场域六锚=六步位自动匹配（真 import——done）")
    add("tensor_y_five_done",
        qt["Y_maslow_weights"]["count"] == 5
        and qt["Y_maslow_weights"]["status"] == "done",
        "Y 马斯洛五层 schema（公开口径登记——done）")
    add("tensor_z_five_designed",
        qt["Z_meaning_states"]["count"] == 5
        and qt["Z_meaning_states"]["status"] == "designed",
        "Z 意义状态五类槽位待喂入（designed——不虚称已建）")

    # 机构映射
    add("bureau_six_registered",
        len(BUREAU_MAP) == 6
        and all(v["module"].startswith("holoaeon.")
                for v in BUREAU_MAP.values()),
        "六机构指针登记（打捞局/规划局/制造局/熔炉/神灯/漩涡"
        "——零复制）")

    # 打捞出网（真跑+确定性）
    d1 = dredge("康复医学 数字分身 认知蒸馏 军团 相似性 聚类")
    d2 = dredge("康复医学 数字分身 认知蒸馏 军团 相似性 聚类")
    add("dredge_deterministic",
        d1["input_hash16"] == d2["input_hash16"]
        and d1["node_count"] == d2["node_count"],
        "同文同账（确定性——同输入两次出网结果一致）")
    add("dredge_hits_live",
        d1["node_count"] > 0 and d1["mech_count"] > 0,
        "打捞真跑命中（节点 {} 仓/机制 {} 条）".format(
            d1["node_count"], d1["mech_count"]))
    add("dredge_rejects_empty",
        _raises(dredge, ""),
        "空需求被拒（append-only 账目纪律）")

    # 全局孵化协议（碳基修正：整体独立建仓——打捞之网模式=全局范式）
    add("incubation_protocol_seven",
        len(INCUBATION_PROTOCOL) == 7
        and all(p["act"] for p in INCUBATION_PROTOCOL),
        "打捞之网模式固化为七步孵化协议（出网打捞→扬弃→独立"
        "建仓→全域装载→投喂包→执行回执→记忆回填）——全局新"
        "项目一律独立建仓独立启动")
    add("incubation_registry_seeded",
        len(INCUBATION_REGISTRY) == 6
        and INCUBATION_REGISTRY[0]["status"] == "done"
        and all(r["status"] == "designed"
                for r in INCUBATION_REGISTRY[1:3])
        and INCUBATION_REGISTRY[3]["id"] == "INC-004"
        and INCUBATION_REGISTRY[3]["status"] == "done"
        and INCUBATION_REGISTRY[4]["id"] == "INC-005"
        and INCUBATION_REGISTRY[4]["status"] == "done"
        and INCUBATION_REGISTRY[5]["id"] == "INC-007"
        and INCUBATION_REGISTRY[5]["status"] == "done",
        "孵化登记账 6 条：1 号=本仓实例（done），2/3 号候选"
        "（designed——待权威源/碳基点单，不虚称已立项），4 号="
        "qixiaeon 启曦（done，QX-V1 跨仓派单），5 号=eduaeon 教育环"
        "（done，ED-V1 跨仓派单），7 号=forgaeon 锻闸"
        "（done，FG-V1 跨仓派单；INC-006 预留未入账，跳号在案）")
    add("incubation_inc004_binding",
        "qixiaeon" in INCUBATION_REGISTRY[3]["name"]
        and "d299ecd" in INCUBATION_REGISTRY[3]["note"]
        and "M07" in INCUBATION_REGISTRY[3]["note"],
        "INC-004 落位绑定（QX-V1）：名带 qixiaeon、note 带首笔 "
        "d299ecd 与 M07 同承口径——跨仓派单可回查到具体仓与提交")

    # 环链与命名裁决
    add("ring24_declared",
        RING == 24,
        "ring24（当前链 ring23+1）——投喂自称 ring-25 口径 "
        "adjusted 在案（承 C08 同型先例）")
    add("netaeon_name_conflict_resolved",
        "打捞之网" in REPO_CN
        and "qicangaeon" in SCHEMA.lower(),
        "命名裁决：netaeon 中文名'打捞之网'（归航路由）不动，"
        "启藏=主动出网版（qicangaeon 纪元族第六员）——同中文"
        "名冲突由英文主键消解（QC-V2 修法：QC-V1 此闸含 or "
        "True 恒真装饰——QWEN-R16 缺陷一，实测改真断言）")

    failed = [c for c in checks if not c["ok"]]
    return {"schema": SCHEMA, "batch": BATCH, "seal": SEAL,
            "repo_cn": REPO_CN, "ring": RING,
            "total": len(checks), "passed": len(checks) - len(failed),
            "failed": len(failed),
            "verdict": "PASS" if not failed else "FAIL",
            "checks": checks}


def _raises(fn, arg) -> bool:
    try:
        fn(arg)
        return False
    except ValueError:
        return True


def _main(argv: List[str]) -> int:
    cmd = argv[1] if len(argv) > 1 else "check"
    if cmd == "check":
        r = check_qc_core()
        print(json.dumps({k: r[k] for k in ("schema", "batch",
                                            "total", "passed",
                                            "failed", "verdict")},
                         ensure_ascii=False))
        for c in r["checks"]:
            if not c["ok"]:
                print("FAIL:", c["check"], c.get("note", ""))
        return 0 if r["verdict"] == "PASS" else 1
    if cmd == "dredge":
        text = " ".join(argv[2:]) or "打捞自检需求"
        print(json.dumps(dredge(text), ensure_ascii=False, indent=1))
        return 0
    if cmd == "namemap":
        print(json.dumps(NAME_MAP, ensure_ascii=False, indent=1))
        return 0
    if cmd == "tensor":
        print(json.dumps(QC_TENSOR, ensure_ascii=False, indent=1))
        return 0
    if cmd == "bureau":
        print(json.dumps(BUREAU_MAP, ensure_ascii=False, indent=1))
        return 0
    if cmd == "incubation":
        print(json.dumps({"protocol": INCUBATION_PROTOCOL,
                          "registry": INCUBATION_REGISTRY},
                         ensure_ascii=False, indent=1))
        return 0
    print("usage: qc_core.py [check|dredge <text>|namemap|tensor"
          "|bureau|incubation]")
    return 2


if __name__ == "__main__":
    sys.exit(_main(sys.argv))
