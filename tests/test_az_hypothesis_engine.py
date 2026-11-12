"""Candidate-index tests; checks records and reproducible topic coverage."""
import json
import sys
import unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"research"/"discovery_engine"))
from az_hypothesis_engine import CANDIDATES,read_topics,candidates,audit_registry

class IndexTests(unittest.TestCase):
    def test_complete_candidate_receipts(self):
        self.assertTrue(audit_registry(CANDIDATES))
    def test_curated_inventory_is_explicitly_not_full(self):
        self.assertGreaterEqual(len(read_topics()),20)
        self.assertLess(len(read_topics()),342)  # never falsely claim unimported 342
    def test_ready_candidates_have_fields(self):
        for c in candidates():
            self.assertEqual(c["ready_for_formulation"],not c["missing_fields"])
    def test_missing_topics_downgrade_candidates(self):
        for c in candidates({"geometry"}):
            self.assertFalse(c["ready_for_formulation"])
            self.assertLess(c["priority_score"],10)
    def test_deterministic(self):
        self.assertEqual(json.dumps(candidates(),sort_keys=True),json.dumps(candidates(),sort_keys=True))

if __name__=="__main__":
    unittest.main()
