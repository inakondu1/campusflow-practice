import unittest
from campusflow.workflow import assign_ticket, update_status, get_work_queue

class TestWorkflow(unittest.TestCase):

    def setUp(self):
        self.ticket = {
            "id": "T001",
            "title": "Wi-Fi down",
            "status": "open",
            "assigned_to": None
        }

    def test_assign_ticket_success(self):
        assign_ticket(self.ticket, "Amina")
        self.assertEqual(self.ticket["assigned_to"], "Amina")

    def test_assign_ticket_blank_name_rejected(self):
        with self.assertRaises(ValueError):
            assign_ticket(self.ticket, "   ")

    def test_unassigned_cannot_move_to_in_progress(self):
        with self.assertRaises(ValueError):
            update_status(self.ticket, "in_progress")

    def test_assigned_can_move_to_in_progress(self):
        assign_ticket(self.ticket, "Amina")
        update_status(self.ticket, "in_progress")
        self.assertEqual(self.ticket["status"], "in_progress")

    def test_resolved_ticket_cannot_change_without_reopen(self):
        assign_ticket(self.ticket, "Amina")
        update_status(self.ticket, "in_progress")
        update_status(self.ticket, "resolved")
        
        with self.assertRaises(ValueError):
            update_status(self.ticket, "in_progress")

    def test_work_queue_sorting_by_priority_and_id(self):
        tickets = [
            {"id": "T003", "status": "open", "priority": "high"},
            {"id": "T001", "status": "resolved", "priority": "critical"},
            {"id": "T002", "status": "open", "priority": "critical"},
            {"id": "T004", "status": "in_progress", "priority": "high"}
        ]
        
        queue = get_work_queue(tickets)
        ids = [t["id"] for t in queue]
        
        self.assertEqual(ids, ["T002", "T003", "T004"])

if __name__ == "__main__":
    unittest.main()
