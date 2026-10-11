"""CampusFlow open-ticket work queue."""

PRIORITY_ORDER = {
    "critical": 0,
    "high": 1,
    "medium": 2,
    "low": 3,
}


def _ticket_number(ticket):
    """Extract the numeric suffix from a ticket ID."""
    ticket_id = str(ticket.get("id", ""))

    if ticket_id.startswith("T") and ticket_id[1:].isdigit():
        return int(ticket_id[1:])

    # Malformed IDs sort after correctly formatted IDs.
    return float("inf")


def get_work_queue(tickets):
    """Return open tickets sorted by priority and numeric ticket ID."""
    open_tickets = [
        ticket for ticket in tickets
        if ticket.get("status") == "open"
    ]

    return sorted(
        open_tickets,
        key=lambda ticket: (
            PRIORITY_ORDER.get(ticket.get("priority"), 99),
            _ticket_number(ticket),
        ),
    )