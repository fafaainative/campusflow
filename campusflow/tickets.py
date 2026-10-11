
"""Engineer A: CampusFlow ticket creation, validation and search."""

tickets = []

VALID_CATEGORIES = ("Network", "Hardware", "Software", "Other")
VALID_URGENCIES = ("low", "medium", "high")


def calculate_priority(urgency, affected_users):
    """Return the priority determined by urgency and user impact."""
    urgency = urgency.strip().lower() if isinstance(urgency, str) else urgency

    if (
        urgency == "high"
        and isinstance(affected_users, int)
        and not isinstance(affected_users, bool)
        and affected_users >= 10
    ):
        return "critical"

    if urgency == "high" or (
        isinstance(affected_users, int)
        and not isinstance(affected_users, bool)
        and affected_users >= 10
    ):
        return "high"

    if urgency == "medium" or (
        isinstance(affected_users, int)
        and not isinstance(affected_users, bool)
        and affected_users >= 3
    ):
        return "medium"

    return "low"


def validate_ticket_data(title, category, urgency, affected_users):
    """Return (True, message) or (False, error_message)."""
    if not isinstance(title, str) or not title.strip():
        return False, "Title must not be empty."

    if not isinstance(category, str):
        return False, "Category must be text."

    category = category.strip().lower()
    allowed_categories = {item.lower() for item in VALID_CATEGORIES}

    if category not in allowed_categories:
        return False, "Invalid category."

    if not isinstance(urgency, str):
        return False, "Urgency must be text."

    if urgency.strip().lower() not in VALID_URGENCIES:
        return False, "Invalid urgency."

    if isinstance(affected_users, bool) or not isinstance(affected_users, int):
        return False, "Affected users must be a whole number."

    if affected_users <= 0:
        return False, "Affected users must be greater than zero."

    return True, "Ticket data is valid."


def generate_ticket_id(ticket_list=None):
    """Generate the next ID after the largest existing numeric suffix."""
    if ticket_list is None:
        ticket_list = tickets

    largest_number = 0

    for ticket in ticket_list:
        ticket_id = ticket.get("id", "")

        if (
            isinstance(ticket_id, str)
            and ticket_id.startswith("T")
            and ticket_id[1:].isdigit()
        ):
            largest_number = max(largest_number, int(ticket_id[1:]))

    return f"T{largest_number + 1:03d}"


def create_ticket(title, category, urgency, affected_users, ticket_list=None):
    """
    Return (ticket, None) on success or (None, error_message) on failure.
    The optional ticket_list supports shared storage and isolated tests.
    """
    if ticket_list is None:
        ticket_list = tickets

    valid, message = validate_ticket_data(
        title, category, urgency, affected_users
    )

    if not valid:
        return None, message

    title = title.strip()
    category = next(
        item for item in VALID_CATEGORIES
        if item.lower() == category.strip().lower()
    )
    urgency = urgency.strip().lower()

    new_ticket = {
        "id": generate_ticket_id(ticket_list),
        "title": title,
        "category": category,
        "urgency": urgency,
        "affected_users": affected_users,
        "priority": calculate_priority(urgency, affected_users),
        "status": "open",
        "assigned_to": None,
    }

    ticket_list.append(new_ticket)
    return new_ticket, None


def list_tickets(ticket_list=None):
    """Return a new list containing the tickets."""
    if ticket_list is None:
        ticket_list = tickets

    return list(ticket_list)


def find_ticket(ticket_id, ticket_list=None):
    """Return a matching ticket or None if it does not exist."""
    if ticket_list is None:
        ticket_list = tickets

    if not isinstance(ticket_id, str):
        return None

    ticket_id = ticket_id.strip().upper()

    for ticket in ticket_list:
        if str(ticket.get("id", "")).upper() == ticket_id:
            return ticket

    return None
