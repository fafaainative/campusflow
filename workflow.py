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

def update_ticket_status(tickets, ticket_id, new_status):
    """Update a ticket's status when the transition is valid."""
    ticket = _find_ticket(tickets, ticket_id)

    if ticket is None:
        return False, "Ticket not found."

    if not isinstance(new_status, str):
        return False, "Status must be a string."

    new_status = new_status.strip().lower()

    if new_status not in VALID_STATUSES:
        return False, "Invalid status."

    current_status = ticket.get("status")

    if current_status == "resolved":
        return False, "Reopen the ticket before changing its status."

    if current_status == "open" and new_status == "in_progress":
        if not ticket.get("assigned_to"):
            return False, "Assign the ticket before starting work."

    allowed_transitions = {
        "open": ("in_progress",),
        "in_progress": ("resolved",),
    }

    if new_status not in allowed_transitions.get(current_status, ()):
        return False, "Invalid status transition."

    ticket["status"] = new_status
    return True, f"Ticket {ticket['id']} status updated to {new_status}."


def reopen_ticket(tickets, ticket_id):
    """Reopen a resolved ticket."""
    ticket = _find_ticket(tickets, ticket_id)

    if ticket is None:
        return False, "Ticket not found."

    if ticket.get("status") != "resolved":
        return False, "Only resolved tickets can be reopened."

    ticket["status"] = "open"
    return True, f"Ticket {ticket['id']} reopened."
