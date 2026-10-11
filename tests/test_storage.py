
"""Tests for CampusFlow JSON storage."""

import json
import tempfile
import unittest
from pathlib import Path

from campusflow.tickets import create_ticket
from storage import load_tickets, save_tickets


class TestTicketStorage(unittest.TestCase):
    def setUp(self):
        self.temp_directory = tempfile.TemporaryDirectory()
        self.storage_path = Path(self.temp_directory.name) / "tickets.json"

        self.sample_ticket = {
            "id": "T001",
            "title": "Wi-Fi connection failure",
            "category": "Network",
            "urgency": "high",
            "affected_users": 15,
            "priority": "critical",
            "status": "open",
            "assigned_to": None,
        }

    def tearDown(self):
        self.temp_directory.cleanup()

    def test_save_and_reload_ticket(self):
        save_tickets([self.sample_ticket], self.storage_path)

        loaded_tickets = load_tickets(self.storage_path)

        self.assertEqual(loaded_tickets, [self.sample_ticket])

    def test_missing_file_returns_empty_list(self):
        loaded_tickets = load_tickets(self.storage_path)

        self.assertEqual(loaded_tickets, [])

    def test_malformed_json_raises_clear_error(self):
        self.storage_path.write_text(
            '{"id": "T001", invalid JSON}',
            encoding="utf-8",
        )

        with self.assertRaisesRegex(ValueError, "invalid JSON"):
            load_tickets(self.storage_path)

    def test_json_must_contain_a_list(self):
        self.storage_path.write_text(
            json.dumps({"id": "T001"}),
            encoding="utf-8",
        )

        with self.assertRaisesRegex(ValueError, "JSON list"):
            load_tickets(self.storage_path)

    def test_every_item_must_be_a_dictionary(self):
        self.storage_path.write_text(
            json.dumps([self.sample_ticket, "not a ticket"]),
            encoding="utf-8",
        )

        with self.assertRaisesRegex(ValueError, "every item"):
            load_tickets(self.storage_path)

    def test_multiple_tickets_are_preserved(self):
        second_ticket = dict(self.sample_ticket)
        second_ticket["id"] = "T002"
        second_ticket["title"] = "Projector failure"

        original_tickets = [self.sample_ticket, second_ticket]

        save_tickets(original_tickets, self.storage_path)
        loaded_tickets = load_tickets(self.storage_path)

        self.assertEqual(loaded_tickets, original_tickets)
        self.assertEqual(len(loaded_tickets), 2)

    def test_ticket_ids_remain_unique_after_reload(self):
        save_tickets([self.sample_ticket], self.storage_path)
        loaded_tickets = load_tickets(self.storage_path)

        new_ticket, error = create_ticket(
            title="Keyboard failure",
            category="Hardware",
            urgency="medium",
            affected_users=3,
            ticket_list=loaded_tickets,
        )

        self.assertIsNone(error)
        self.assertEqual(new_ticket["id"], "T002")
        self.assertEqual(len(loaded_tickets), 2)

    def test_save_rejects_non_list(self):
        with self.assertRaisesRegex(ValueError, "list"):
            save_tickets(self.sample_ticket, self.storage_path)

    def test_save_rejects_non_dictionary_items(self):
        with self.assertRaisesRegex(ValueError, "dictionary"):
            save_tickets([self.sample_ticket, "invalid"], self.storage_path)


if __name__ == "__main__":
    unittest.main()
