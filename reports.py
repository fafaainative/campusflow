"""CampusFlow ticket reports."""

VALID_STATUSES = ("open", "in_progress", "resolved")
VALID_PRIORITIES = ("critical", "high", "medium", "low")


def generate_report(tickets):
    """Return total, status counts, and priority counts."""
    status_counts = {status: 0 for status in VALID_STATUSES}
    priority_counts = {priority: 0 for priority in VALID_PRIORITIES}

    for ticket in tickets:
        status = ticket.get("status")
        priority = ticket.get("priority")

        if status in status_counts:
            status_counts[status] += 1

        if priority in priority_counts:
            priority_counts[priority] += 1

    return {
        "total_tickets": len(tickets),
        "status_counts": status_counts,
        "priority_counts": priority_counts,
    }