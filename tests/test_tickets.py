
import unittest

from campusflow.tickets import (
    calculate_priority,
    validate_ticket_data,
    generate_ticket_id,
    create_ticket,
    list_tickets,
    find_ticket,
)


class TestCalculatePriority(unittest.TestCase):

    def test_critical_priority(self):
        self.assertEqual(calculate_priority("high", 10), "critical")

    def test_high_urgency(self):
        self.assertEqual(calculate_priority("high", 2), "high")

    def test_high_affected_users(self):
        self.assertEqual(calculate_priority("low", 10), "high")

    def test_medium_urgency(self):
        self.assertEqual(calculate_priority("medium", 1), "medium")

    def test_medium_affected_users(self):
        self.assertEqual(calculate_priority("low", 3), "medium")

    def test_low_priority(self):
        self.assertEqual(calculate_priority("low", 1), "low")

    def test_urgency_is_case_insensitive(self):
        self.assertEqual(calculate_priority("HIGH", 10), "critical")


class TestTicketValidation(unittest.TestCase):

    def test_valid_data(self):
        valid, _ = validate_ticket_data(
            "Wi-Fi issue", "Network", "high", 5
        )
        self.assertTrue(valid)

    def test_title_cannot_be_empty(self):
        for title in ("", "   ", None):
            with self.subTest(title=title):
                valid, _ = validate_ticket_data(
                    title, "Network", "low", 1
                )
                self.assertFalse(valid)

    def test_invalid_category(self):
        valid, _ = validate_ticket_data(
            "Wi-Fi issue", "Food", "low", 1
        )
        self.assertFalse(valid)

    def test_invalid_urgency(self):
        valid, _ = validate_ticket_data(
            "Wi-Fi issue", "Network", "urgent", 1
        )
        self.assertFalse(valid)

    def test_affected_users_must_be_positive_integer(self):
        for value in (0, -1, True, False, 3.5, "5", None):
            with self.subTest(value=value):
                valid, _ = validate_ticket_data(
                    "Wi-Fi issue", "Network", "low", value
                )
                self.assertFalse(valid)

    def test_category_and_urgency_case_are_accepted(self):
        valid, _ = validate_ticket_data(
            "Wi-Fi issue", "network", "HIGH", 2
        )
        self.assertTrue(valid)


class TestTicketCreationAndSearch(unittest.TestCase):

    def setUp(self):
        self.test_tickets = []

    def test_first_id(self):
        self.assertEqual(generate_ticket_id(self.test_tickets), "T001")

    def test_next_id_uses_largest_existing_number(self):
        self.test_tickets.extend([
            {"id": "T001"},
            {"id": "T002"},
            {"id": "T004"},
        ])
        self.assertEqual(generate_ticket_id(self.test_tickets), "T005")

    def test_create_ticket(self):
        ticket, error = create_ticket(
            " Wi-Fi issue ", "network", "HIGH", 10, self.test_tickets
        )

        self.assertIsNone(error)
        self.assertIsNotNone(ticket)
        self.assertEqual(ticket["id"], "T001")
        self.assertEqual(ticket["title"], "Wi-Fi issue")
        self.assertEqual(ticket["category"], "Network")
        self.assertEqual(ticket["urgency"], "high")
        self.assertEqual(ticket["affected_users"], 10)
        self.assertEqual(ticket["priority"], "critical")
        self.assertEqual(ticket["status"], "open")
        self.assertIsNone(ticket["assigned_to"])
        self.assertEqual(len(self.test_tickets), 1)

    def test_invalid_ticket_is_not_added(self):
        ticket, error = create_ticket(
            "", "Network", "low", 1, self.test_tickets
        )

        self.assertIsNone(ticket)
        self.assertIsNotNone(error)
        self.assertEqual(len(self.test_tickets), 0)

    def test_created_ids_are_unique(self):
        first, _ = create_ticket(
            "Wi-Fi issue", "Network", "low", 1, self.test_tickets
        )
        second, _ = create_ticket(
            "Broken laptop", "Hardware", "medium", 3, self.test_tickets
        )

        self.assertNotEqual(first["id"], second["id"])

    def test_list_tickets(self):
        create_ticket(
            "Wi-Fi issue", "Network", "low", 1, self.test_tickets
        )
        self.assertEqual(len(list_tickets(self.test_tickets)), 1)

    def test_find_ticket(self):
        create_ticket(
            "Wi-Fi issue", "Network", "low", 1, self.test_tickets
        )

        found = find_ticket("t001", self.test_tickets)
        self.assertIsNotNone(found)
        self.assertEqual(found["title"], "Wi-Fi issue")

    def test_missing_ticket_returns_none(self):
        self.assertIsNone(find_ticket("T999", self.test_tickets))


if __name__ == "__main__":
    unittest.main()
