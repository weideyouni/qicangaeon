# -*- coding: utf-8 -*-
"""test_qc1_core.py · qicangaeon QC-V1 套件（真 unittest）

四组（启藏建仓批·逐点验收）：
  一、真源接线（19 节点/25 机制/六步位/M07 真 import）
  二、真名对照+三维张量（done/designed/adjusted 先证红律）
  三、打捞出网（deterministic/命中/空拒/级联归航）
  四、孵化协议+账本+批总闸 33（全绿闭环——设计即账）

R2 惯例：本套件锁当批精确值（33/19/7），历史批下限化由各旧
套件自持。
"""

import os
import sys
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)

from qicangaeon import qc_core as qc       # noqa: E402
from qicangaeon import qc_ledger as ql     # noqa: E402

try:
    from netaeon import net_core
    from holoaeon import meridian_link
    from mirraeon import legion_dispatch
except ImportError:  # 三仓根须在 sys.path（README 三步验收注明）
    import net_core
    import meridian_link
    import legion_dispatch


class T1TrueSources(unittest.TestCase):
    """一、真源接线——三仓指针非复制。"""

    def test_nodes_19_live(self):
        """19 节点真 import（netaeon 单一真源——打捞网域）。"""
        self.assertEqual(len(net_core.build_nodes()), 19)

    def test_mechs_25_live(self):
        """25 机制真 import（holoaeon meridian_link）。"""
        self.assertEqual(
            len(meridian_link.KERNEL_MECHANISMS), 25)

    def test_routing_six_live(self):
        """六步位真 import（mirraeon legion_dispatch）。"""
        self.assertEqual(len(legion_dispatch.STEP_ROUTING), 6)

    def test_m07_similarity_anchor(self):
        """M07 自组织相似性在案（打捞命中的机制锚）。"""
        m07 = [m for m in meridian_link.KERNEL_MECHANISMS
               if m.get("id") == "M07"]
        self.assertEqual(
            (len(m07), m07[0]["name"]), (1, "自组织相似性"))

    def test_bureau_six_pointers(self):
        """六机构指针登记（打捞局/规划局/制造局/熔炉/神灯/漩涡）。"""
        self.assertEqual(len(qc.BUREAU_MAP), 6)
        for v in qc.BUREAU_MAP.values():
            self.assertTrue(v["module"].startswith("holoaeon."))


class T2NameMapTensor(unittest.TestCase):
    """二、真名对照+三维张量——先证红律。"""

    def test_namemap_12_entries(self):
        """真名对照 12 条（8 done+4 designed）。"""
        self.assertEqual(len(qc.NAME_MAP), 12)
        self.assertEqual(
            sum(1 for e in qc.NAME_MAP
                if e["status"] == "done"), 8)
        self.assertEqual(
            sum(1 for e in qc.NAME_MAP
                if e["status"] == "designed"), 4)

    def test_namemap_done_all_have_authority(self):
        """done 条目全带 authority_source（AR-1）。"""
        for e in qc.NAME_MAP:
            if e["status"] == "done":
                self.assertTrue(e["authority_source"])

    def test_namemap_designed_no_real_value(self):
        """designed 条目不落 real 值（不虚称落位）。"""
        for e in qc.NAME_MAP:
            if e["status"] == "designed":
                self.assertEqual(e["real"], "")

    def test_namemap_19repo_adjusted(self):
        """19 仓库条 adjusted 在案（投喂降级被实测推翻——
        扬弃不是照单全收）。"""
        e = next(x for x in qc.NAME_MAP
                 if x["alias"] == "19 仓库")
        self.assertEqual(e["status"], "done")
        self.assertIn("推翻", e["adjusted"])

    def test_namemap_grid_11c3(self):
        """1331×1331→11³ 对照（mirror_core 实测）。"""
        e = next(x for x in qc.NAME_MAP
                 if x["alias"] == "1331×1331")
        self.assertEqual(e["real"], "11³ 立方体")

    def test_tensor_x_six_done(self):
        """X 场域六锚=六步位自动匹配（真 import done）。"""
        x = qc.QC_TENSOR["X_field_anchors"]
        self.assertEqual((x["count"], x["status"]), (6, "done"))
        self.assertEqual(x["anchors"],
                         ["道", "法", "术", "器", "升维", "横切"])

    def test_tensor_y_five_done(self):
        """Y 马斯洛五层 schema（公开口径登记）。"""
        y = qc.QC_TENSOR["Y_maslow_weights"]
        self.assertEqual((y["count"], y["status"]), (5, "done"))
        self.assertEqual(len(y["layers"]), 5)

    def test_tensor_z_five_designed(self):
        """Z 意义状态五类槽位待喂入（designed——不虚称）。"""
        z = qc.QC_TENSOR["Z_meaning_states"]
        self.assertEqual((z["count"], z["status"]),
                         (5, "designed"))
        self.assertIsNone(z["slots"])


class T3Dredge(unittest.TestCase):
    """三、打捞出网——确定性零评分。"""

    def test_dredge_deterministic(self):
        """同文同账（同输入两次出网一致）。"""
        t = "康复医学 数字分身 认知蒸馏 军团 相似性 聚类"
        d1, d2 = qc.dredge(t), qc.dredge(t)
        self.assertEqual(d1["input_hash16"],
                         d2["input_hash16"])
        self.assertEqual(d1["node_count"], d2["node_count"])
        self.assertEqual(d1["mech_count"], d2["mech_count"])

    def test_dredge_hits_nodes_and_mechs(self):
        """真跑命中（节点账+机制账双非空）。"""
        d = qc.dredge("康复医学 数字分身 认知蒸馏 军团 相似性")
        self.assertGreater(d["node_count"], 0)
        self.assertGreater(d["mech_count"], 0)

    def test_dredge_m07_hit(self):
        """M07 相似性键命中（自组织/相似/聚类键）。"""
        d = qc.dredge("自组织 相似性 聚类 embedding")
        mechs = [h["mech"] for h in d["mech_hits"]]
        self.assertIn("M07", mechs)

    def test_dredge_step_routing_six(self):
        """步位路由六位全在出网账（派工到责任席）。"""
        d = qc.dredge("任意需求")
        self.assertEqual(len(d["step_routing"]), 6)

    def test_dredge_rejects_empty(self):
        """空需求被拒（append-only 账目纪律）。"""
        with self.assertRaises(ValueError):
            qc.dredge("  ")

    def test_netaeon_cascade(self):
        """两网级联：出网打捞→netaeon route 归航回港。"""
        r = net_core.route("启藏 文明挖掘 打捞")
        self.assertEqual(r["schema"], "NETAEON-NET/1.0")
        self.assertIn(r["verdict"], ("known", "unknown"))


class T4IncubationLedgerBatch(unittest.TestCase):
    """四、孵化协议+账本+批总闸 33 全绿闭环。"""

    def test_incubation_protocol_seven(self):
        """七步孵化协议（全局独立建仓范式——碳基修正落点）。"""
        self.assertEqual(len(qc.INCUBATION_PROTOCOL), 7)
        steps = "①②③④⑤⑥⑦"
        for i, p in enumerate(qc.INCUBATION_PROTOCOL):
            self.assertTrue(p["step"].startswith(steps[i]))
            self.assertTrue(p["act"])

    def test_incubation_registry_three(self):
        """孵化登记账 3 条（1 done+2 designed）。"""
        self.assertEqual(len(qc.INCUBATION_REGISTRY), 3)
        self.assertEqual(
            qc.INCUBATION_REGISTRY[0]["status"], "done")
        self.assertEqual(
            qc.INCUBATION_REGISTRY[0]["id"], "INC-001")
        for r in qc.INCUBATION_REGISTRY[1:]:
            self.assertEqual(r["status"], "designed")

    def test_ring24_adjusted(self):
        """ring24 在案（投喂 ring-25 口径 adjusted）。"""
        self.assertEqual(qc.RING, 24)

    def test_ledger_seeded_recursive(self):
        """打捞账种子 1 条（本仓建制递归先例）。"""
        self.assertEqual(len(ql.DREDGE_LEDGER), 1)
        self.assertEqual(ql.DREDGE_LEDGER[0]["rid"], "DR-0001")

    def test_append_rejects_empty(self):
        """空需求入账被拒。"""
        with self.assertRaises(ValueError):
            ql.append_dredge("")

    def test_qc_core_gates_19(self):
        """启藏核心自检闸 19/19。"""
        r = qc.check_qc_core()
        self.assertEqual((r["total"], r["failed"]), (19, 0))

    def test_ledger_gates_7(self):
        """账本闸 7/7——QC-V2 增至 9：下限化（R2 惯例第七例）。"""
        r = ql.check_ledger()
        self.assertGreaterEqual(r["total"], 7)
        self.assertEqual(r["failed"], 0)

    def test_batch_33_all_pass(self):
        """批总闸 33/33——QC-V2 增至 35：下限化（R2 惯例第七例）。"""
        r = ql.check_batch()
        self.assertEqual(r["verdict"], "PASS")
        self.assertGreaterEqual(r["total"], 33)
        self.assertEqual(r["failed"], 0)

    def test_readme_sync_locked(self):
        """README 锁——口径数字全可回读。"""
        r = ql.check_readme_sync()
        self.assertEqual(r["verdict"], "PASS")


if __name__ == "__main__":
    unittest.main(verbosity=2)
