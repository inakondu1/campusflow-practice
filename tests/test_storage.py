import unittest
import os
import shutil
import tempfile
from campusflow.storage import save_tickets, load_tickets

class TestStorage(unittest.TestCase):

    def setUp(self):
        # Create a isolated temporary directory for test files
        self.test_dir = tempfile.mkdtemp()
        self.test_file = os.path.join(self.test_dir, "test_tickets.json")

    def tearDown(self):
        # Clean up temporary directory after test runs
        shutil.rmtree(self.test_dir)

    def test_load_non_existent_file_returns_empty_list(self):
        tickets = load_tickets(self.test_file)
        self.assertEqual(tickets, [])

    def test_save_and_load_tickets_roundtrip(self):
        sample_tickets = [
            {"id": "T001", "title": "Wi-Fi down", "status": "open", "priority": "high"}
        ]
        save_tickets(sample_tickets, self.test_file)
        loaded = load_tickets(self.test_file)
        self.assertEqual(loaded, sample_tickets)

    def test_corrupted_json_raises_value_error(self):
        os.makedirs(self.test_dir, exist_ok=True)
        with open(self.test_file, "w") as f:
            f.write("{ invalid json content ...")

        with self.assertRaises(ValueError):
            load_tickets(self.test_file)

if __name__ == "__main__":
    unittest.main()
