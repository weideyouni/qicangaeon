# -*- coding: utf-8 -*-
"""test_qc2_defects.py · qicangaeon QC-V2 套件（真 unittest）

四组（QWEN-R16 缺陷修法批·主攻本仓全员升级·逐点验收）：
  一、DF-001 修法（or True 恒真→真断言）
  二、DF-002 修法（重言式闸→只读对账+模块级回填）
  三、DF-003/DF-004 修法（README 口径+CI 在仓）
  四、缺陷修法账+批总闸 36（全绿闭环——设计即账）

R2 惯例：本套件锁当批精确值（36/9/4），历史套件下限化自持。
"""

import os
import sys
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)

from qicangaeon import qc_core as qc       # noqa: E402
from qicangaeon import qc_ledger as ql     # noqa: E402


class T1DefectOne(unittest.TestCase):
    """一、DF-001——or True 恒真装饰拔除（AR-4）。"""

    def test_no_or_true_in_gates(self):
        """源码无 'or True' 恒真装饰（QWEN-R16 缺陷一修法）。"""
        src = open(qc.__file__, encoding="utf-8").read()
        self.assertNotIn("or True", src)

    def test_name_gate_real_assertion(self):
        """命名裁决闸为真断言（两真条件全绿）。"""
        r = qc.check_qc_core()
        gate = next(c for c in r["checks"]
                    if c["check"] == "netaeon_name_conflict_resolved")
        self.assertTrue(gate["ok"])

    def test_qc_core_gates_19(self):
        """核心闸 20/20（QX-V1 增 INC-004 闸；修法不虚拟）。"""
        r = qc.check_qc_core()
        self.assertEqual((r["total"], r["failed"]), (20, 0))


class T2DefectTwo(unittest.TestCase):
    """二、DF-002——重言式闸+检查写账拔除（AR-2 闸只阻断）。"""

    def test_check_does_not_write_ledger(self):
        """check_ledger 不写账（闸只读对账——闸只阻断不重建）。"""
        before = [dict(t) for t in ql.DREDGE_LEDGER]
        ql.check_ledger()
        after = [dict(t) for t in ql.DREDGE_LEDGER]
        self.assertEqual(before, after)

    def test_seed_backfilled_at_load(self):
        """种子实测值模块级回填（建仓真跑入账非 check 自写）。"""
        self.assertIsNotNone(ql.DREDGE_LEDGER[0]["node_count"])
        self.assertIsNotNone(ql.DREDGE_LEDGER[0]["mech_count"])

    def test_seed_account_matches_replay(self):
        """账实对账：重跑出网与账上值一致（确定性）。"""
        d = qc.dredge(ql._SEED_TEXT)
        self.assertEqual(
            ql.DREDGE_LEDGER[0]["node_count"], d["node_count"])
        self.assertEqual(
            ql.DREDGE_LEDGER[0]["mech_count"], d["mech_count"])

    def test_ledger_gates_9(self):
        """账本闸 7→9（缺陷修法账+CI 闸入账）。"""
        r = ql.check_ledger()
        self.assertEqual((r["total"], r["failed"]), (9, 0))


class T3DefectThreeFour(unittest.TestCase):
    """三、DF-003/DF-004——README 口径+CI 在仓。"""

    def test_readme_no_stale_24(self):
        """README 无 'Ran 24 tests' 过时口径（QWEN-R16 缺陷三）。"""
        text = open(os.path.join(ROOT, "README.md"),
                    encoding="utf-8").read()
        self.assertNotIn("Ran 24 tests", text)
        self.assertNotIn("即 FAIL）。", text)

    def test_readme_covers_36(self):
        """README 口径含批总闸实测 36（与 check_batch 对账）。"""
        text = open(os.path.join(ROOT, "README.md"),
                    encoding="utf-8").read()
        self.assertIn("36", text)

    def test_ci_workflow_present(self):
        """CI workflow 在仓（QWEN-R16 8-B 头号结构补齐）。"""
        ci = os.path.join(ROOT, ".github", "workflows", "ci.yml")
        self.assertTrue(os.path.isfile(ci))

    def test_ci_checkout_four_repos(self):
        """CI 四仓同 checkout（三仓真 import 依赖在 CI 复现）。"""
        ci = open(os.path.join(ROOT, ".github", "workflows",
                               "ci.yml"), encoding="utf-8").read()
        for repo in ("holoaeon", "netaeon", "mirraeon",
                     "qicangaeon"):
            self.assertIn(repo, ci)


class T4DefectLedgerBatch(unittest.TestCase):
    """四、缺陷修法账+批总闸 35 全绿闭环。"""

    def test_defect_ledger_four_fixed(self):
        """缺陷修法账 4 条全 fixed（QWEN-R16 三缺陷+CI 结构原因）。"""
        self.assertEqual(len(ql.DEFECT_LEDGER), 4)
        for e in ql.DEFECT_LEDGER:
            self.assertEqual(e["status"], "fixed_qc_v2")
            self.assertTrue(e["fix"])
            self.assertTrue(e["defect"])

    def test_defect_ids_unique(self):
        """四案编号唯一（DF-001..DF-004——可指认）。"""
        self.assertEqual(
            sorted(e["did"] for e in ql.DEFECT_LEDGER),
            ["DF-001", "DF-002", "DF-003", "DF-004"])

    def test_defect_source_qwen_r16(self):
        """修法源=QWEN-R16 十六轮核验（扬弃链路可追溯）。"""
        for e in ql.DEFECT_LEDGER:
            self.assertIn("QWEN-R16", e["source"])

    def test_batch_36_all_pass(self):
        """批总闸 36/36（core 20+ledger 9+README 锁 7）——
        QC-V1 33+缺陷修法 2 闸+QX-V1 INC-004 闸。"""
        r = ql.check_batch()
        self.assertEqual(r["verdict"], "PASS")
        self.assertEqual((r["total"], r["passed"], r["failed"]),
                         (36, 36, 0))

    def test_readme_sync_locked(self):
        """README 锁全绿。"""
        r = ql.check_readme_sync()
        self.assertEqual(r["verdict"], "PASS")


if __name__ == "__main__":
    unittest.main(verbosity=2)
