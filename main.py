
"""CampusFlow command-line helpdesk application."""

from campusflow.tickets import create_ticket, find_ticket
from workflow import assign_ticket, update_ticket_status, reopen_ticket
from queue_manager import get_work_queue
from reports import generate_report
from storage import load_tickets, save_tickets


def display_ticket(ticket):
    """Display all fields of one ticket."""
    print("\n--- Ticket Details ---")
    print(f"ID:             {ticket.get('id')}")
    print(f"Title:          {ticket.get('title')}")
    print(f"Category:       {ticket.get('category')}")
    print(f"Urgency:        {ticket.get('urgency')}")
    print(f"Affected users: {ticket.get('affected_users')}")
    print(f"Priority:       {ticket.get('priority')}")
    print(f"Status:         {ticket.get('status')}")
    print(f"Assigned to:    {ticket.get('assigned_to') or 'Unassigned'}")


def display_tickets(tickets):
    """Display tickets, or a message if the list is empty."""
    if not tickets:
        print("\nNo tickets found.")
        return

    for ticket in tickets:
        display_ticket(ticket)


def save_changes(tickets):
    """Save ticket changes and report storage errors."""
    try:
        save_tickets(tickets)
        print("Changes saved.")
        return True
    except OSError as error:
        print(f"Could not save tickets: {error}")
        return False
    except ValueError as error:
        print(f"Could not save tickets: {error}")
        return False


def create_new_ticket(tickets):
    """Collect input and create a ticket."""
    print("\n--- Create Ticket ---")
    title = input("Ticket title: ")
    category = input("Category (Network/Hardware/Software/Other): ")
    urgency = input("Urgency (low/medium/high): ")
    affected_users_input = input("Number of affected users: ").strip()

    try:
        affected_users = int(affected_users_input)
    except ValueError:
        print("Error: affected users must be a whole number.")
        return

    ticket, error = create_ticket(
        title=title,
        category=category,
        urgency=urgency,
        affected_users=affected_users,
        ticket_list=tickets,
    )

    if error:
        print(f"Ticket was not created: {error}")
        return

    print(f"Ticket {ticket['id']} created successfully.")
    display_ticket(ticket)
    save_changes(tickets)


def search_for_ticket(tickets):
    """Find and display one ticket by ID."""
    ticket_id = input("Enter ticket ID to search for: ")
    ticket = find_ticket(ticket_id, tickets)

    if ticket is None:
        print("Ticket not found.")
    else:
        display_ticket(ticket)


def assign_existing_ticket(tickets):
    """Assign a ticket to a staff member."""
    ticket_id = input("Enter ticket ID: ")
    staff_name = input("Enter staff member's name: ")

    success, message = assign_ticket(tickets, ticket_id, staff_name)
    print(message)

    if success:
        save_changes(tickets)


def change_ticket_status(tickets):
    """Change a ticket's status using the workflow rules."""
    ticket_id = input("Enter ticket ID: ")
    new_status = input("New status (in_progress/resolved): ")

    success, message = update_ticket_status(tickets, ticket_id, new_status)
    print(message)

    if success:
        save_changes(tickets)


def reopen_resolved_ticket(tickets):
    """Reopen a previously resolved ticket."""
    ticket_id = input("Enter ticket ID: ")

    success, message = reopen_ticket(tickets, ticket_id)
    print(message)

    if success:
        save_changes(tickets)


def display_work_queue(tickets):
    """Display open tickets in priority order."""
    queue = get_work_queue(tickets)
    print("\n--- Open-Ticket Work Queue ---")
    display_tickets(queue)


def display_reports(tickets):
    """Display ticket totals, statuses, and priorities."""
    report = generate_report(tickets)

    print("\n--- Ticket Report ---")
    print(f"Total tickets: {report['total_tickets']}")

    print("\nStatus counts:")
    for status, count in report["status_counts"].items():
        print(f"  {status}: {count}")

    print("\nPriority counts:")
    for priority, count in report["priority_counts"].items():
        print(f"  {priority}: {count}")


def display_menu():
    """Print the main menu."""
    print("\n========== CampusFlow ==========")
    print("1. Create a ticket")
    print("2. List all tickets")
    print("3. Search for a ticket")
    print("4. Assign a ticket")
    print("5. Update ticket status")
    print("6. Reopen a resolved ticket")
    print("7. View open-ticket work queue")
    print("8. View ticket reports")
    print("9. Exit")
    print("================================")


def main():
    """Load saved tickets and run the menu until the user exits."""
    try:
        tickets = load_tickets()
    except (ValueError, OSError) as error:
        print(f"Could not load saved tickets: {error}")
        print("Please correct the storage problem before restarting CampusFlow.")
        return

    print(f"Welcome to CampusFlow. Loaded {len(tickets)} ticket(s).")

    while True:
        display_menu()
        choice = input("Choose an option (1-9): ").strip()

        if choice == "1":
            create_new_ticket(tickets)
        elif choice == "2":
            display_tickets(tickets)
        elif choice == "3":
            search_for_ticket(tickets)
        elif choice == "4":
            assign_existing_ticket(tickets)
        elif choice == "5":
            change_ticket_status(tickets)
        elif choice == "6":
            reopen_resolved_ticket(tickets)
        elif choice == "7":
            display_work_queue(tickets)
        elif choice == "8":
            display_reports(tickets)
        elif choice == "9":
            print("Thank you for using CampusFlow. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 9.")


if __name__ == "__main__":
    main()

