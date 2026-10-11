"""CampusFlow ticket assignment and status workflow."""

VALID_STATUSES = ("open", "in_progress", "resolved")


def _find_ticket(tickets, ticket_id):
    """Internal helper: find a ticket by ID, ignoring letter case."""
    if not isinstance(ticket_id, str):
        return None

    ticket_id = ticket_id.strip().upper()

    for ticket in tickets:
        if str(ticket.get("id", "")).upper() == ticket_id:
            return ticket

    return None


def assign_ticket(tickets, ticket_id, assigned_to):
    """Assign an existing, non-resolved ticket to a staff member."""
    ticket = _find_ticket(tickets, ticket_id)

    if ticket is None:
        return False, "Ticket not found."

    if ticket.get("status") == "resolved":
        return False, "Reopen the ticket before modifying its assignment."

    if not isinstance(assigned_to, str) or not assigned_to.strip():
        return False, "Staff name must not be blank."

    ticket["assigned_to"] = assigned_to.strip()

    return True, f"Ticket {ticket['id']} assigned to {assigned_to.strip()}."