import unittest

from workflow import assign_ticket, update_ticket_status, reopen_ticket


def make_ticket(ticket_id="T001", status="open", assigned_to=None):
    return {
        "id": ticket_id,
        "title": "Wi-Fi issue",
        "category": "Network",
        "urgency": "high",
        "affected_users": 5,
        "priority": "high",
        "status": status,
        "assigned_to": assigned_to,
    }


class TestAssignment(unittest.TestCase):
    def setUp(self):
        self.tickets = [make_ticket()]

    def test_assign_ticket(self):
        success, _ = assign_ticket(self.tickets, "T001", "Ada")
        self.assertTrue(success)
        self.assertEqual(self.tickets[0]["assigned_to"], "Ada")

    def test_blank_staff_name_is_rejected(self):
        success, _ = assign_ticket(self.tickets, "T001", "   ")
        self.assertFalse(success)
        self.assertIsNone(self.tickets[0]["assigned_to"])

    def test_missing_ticket_is_rejected(self):
        success, _ = assign_ticket(self.tickets, "T999", "Ada")
        self.assertFalse(success)
        self.assertIsNone(self.tickets[0]["assigned_to"])