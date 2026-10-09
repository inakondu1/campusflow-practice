import unittest
from campusflow.reports import generate_report

class TestReports(unittest.TestCase):

    def test_report_empty_tickets(self):
        report = generate_report([])
        self.assertEqual(report["total"], 0)
        self.assertEqual(report["by_status"]["open"], 0)

    def test_report_breakdown_counts(self):
        tickets = [
            {"id": "T001", "status": "open", "priority": "critical"},
            {"id": "T002", "status": "in_progress", "priority": "high"},
            {"id": "T003", "status": "resolved", "priority": "critical"}
        ]
        report = generate_report(tickets)
        self.assertEqual(report["total"], 3)
        self.assertEqual(report["by_status"]["open"], 1)
        self.assertEqual(report["by_status"]["in_progress"], 1)
        self.assertEqual(report["by_status"]["resolved"], 1)
        self.assertEqual(report["by_priority"]["critical"], 2)
        self.assertEqual(report["by_priority"]["high"], 1)

if __name__ == "__main__":
    unittest.main()
