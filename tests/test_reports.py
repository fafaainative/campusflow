import unittest

from reports import generate_report


def make_ticket(ticket_id, status, priority):
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


class TestReports(unittest.TestCase):
    def test_empty_report(self):
        report = generate_report([])

        self.assertEqual(report["total_tickets"], 0)

        self.assertEqual(
            report["status_counts"],
            {"open": 0, "in_progress": 0, "resolved": 0},
        )

        self.assertEqual(
            report["priority_counts"],
            {"critical": 0, "high": 0, "medium": 0, "low": 0},
        )

    def test_report_counts(self):
        tickets = [
            make_ticket("T001", "open", "critical"),
            make_ticket("T002", "in_progress", "high"),
            make_ticket("T003", "resolved", "high"),
            make_ticket("T004", "open", "low"),
        ]

        report = generate_report(tickets)

        self.assertEqual(report["total_tickets"], 4)

        self.assertEqual(
            report["status_counts"],
            {"open": 2, "in_progress": 1, "resolved": 1},
        )

        self.assertEqual(
            report["priority_counts"],
            {"critical": 1, "high": 2, "medium": 0, "low": 1},
        )