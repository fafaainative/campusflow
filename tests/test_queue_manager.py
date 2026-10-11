import unittest

from queue_manager import get_work_queue


def make_ticket(ticket_id, priority, status="open"):
    return {
        "id": ticket_id,
        "title": "Test issue",
        "category": "Network",
        "urgency": "medium",
        "affected_users": 2,
        "priority": priority,
        "status": status,
        "assigned_to": None,
    }


class TestWorkQueue(unittest.TestCase):
    def test_filters_to_open_tickets(self):
        tickets = [
            make_ticket("T001", "high", "open"),
            make_ticket("T002", "critical", "resolved"),
            make_ticket("T003", "low", "in_progress"),
        ]

        queue = get_work_queue(tickets)

        self.assertEqual([t["id"] for t in queue], ["T001"])

    def test_priority_order(self):
        tickets = [
            make_ticket("T001", "low"),
            make_ticket("T002", "critical"),
            make_ticket("T003", "high"),
            make_ticket("T004", "medium"),
        ]

        queue = get_work_queue(tickets)

        self.assertEqual(
            [t["id"] for t in queue],
            ["T002", "T003", "T004", "T001"],
        )

    def test_numeric_ticket_id_order(self):
        tickets = [
            make_ticket("T010", "high"),
            make_ticket("T002", "high"),
        ]

        queue = get_work_queue(tickets)

        self.assertEqual(
            [t["id"] for t in queue],
            ["T002", "T010"],
        )

    def test_original_list_order_is_preserved(self):
        tickets = [
            make_ticket("T010", "high"),
            make_ticket("T002", "critical"),
        ]
        original_ids = [ticket["id"] for ticket in tickets]

        get_work_queue(tickets)

        self.assertEqual(
            [ticket["id"] for ticket in tickets],
            original_ids,
        )