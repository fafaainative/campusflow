"""CampusFlow command-line helpdesk application."""

from campusflow.tickets import create_ticket, find_ticket
from workflow import assign_ticket, update_ticket_status, reopen_ticket
from queue_manager import get_work_queue
from reports import generate_report
from storage import load_tickets, save_tickets
from campusflow.auth import authenticate



# ─────────────────── 🎫 TICKET DISPLAY ───────────────────

def display_ticket(ticket):
    """Display one ticket with aligned labels and values."""
    fields = [
        ("🆔 Ticket ID", ticket.get("id")),
        ("📌 Title", ticket.get("title")),
        ("📁 Category", ticket.get("category")),
        ("🚨 Urgency", ticket.get("urgency")),
        ("👥 Affected Users", ticket.get("affected_users")),
        ("⚡ Priority", ticket.get("priority")),
        ("🔄 Status", ticket.get("status")),
        ("👤 Assigned To", ticket.get("assigned_to") or "Unassigned"),
    ]

    print("\n" + "═" * 60)
    print("🎫 TICKET DETAILS".center(60))
    print("═" * 60)

    for label, value in fields:
        print(f"{label:<24} : {value}")

    print("═" * 60)


def display_tickets(tickets):
    """Display all tickets or an empty-list message."""
    if not tickets:
        print("\n📭 No tickets found.")
        return

    print(f"\n📋 TOTAL TICKETS: {len(tickets)}")
    for ticket in tickets:
        display_ticket(ticket)


# ─────────────────── 💾 STORAGE ───────────────────

def save_changes(tickets):
    """Save ticket changes and report storage errors."""
    try:
        save_tickets(tickets)
        print("💾 Changes saved successfully.")
        return True
    except (OSError, ValueError) as error:
        print(f"❌ Could not save tickets: {error}")
        return False


# ─────────────────── 🎫 CREATE TICKET ───────────────────

def create_new_ticket(tickets):
    """Collect input and create a ticket."""
    print("\n" + "═" * 45)
    print("🎫 CREATE NEW TICKET")
    print("═" * 45)

    title = input("📌 Ticket title: ")

    # 📁 Category selection
    print("\n📁 SELECT CATEGORY")
    print("─" * 30)
    print("  1. 🌐 Network")
    print("  2. 💻 Hardware")
    print("  3. 🧩 Software")
    print("  4. 📦 Other")

    category_choice = input("👉 Choose category (1-4): ").strip()

    categories = {
        "1": "Network",
        "2": "Hardware",
        "3": "Software",
        "4": "Other",
    }

    if category_choice not in categories:
        print("❌ Invalid category choice. Please select 1-4.")
        return

    category = categories[category_choice]

    # 🚨 Urgency selection
    print("\n🚨 SELECT URGENCY")
    print("─" * 30)
    print("  1. 🟢 Low")
    print("  2. 🟡 Medium")
    print("  3. 🔴 High")

    urgency_choice = input("👉 Choose urgency (1-3): ").strip()

    urgencies = {
        "1": "low",
        "2": "medium",
        "3": "high",
    }

    if urgency_choice not in urgencies:
        print("❌ Invalid urgency choice. Please select 1-3.")
        return

    urgency = urgencies[urgency_choice]

    # 👥 Validate affected users
    affected_users_input = input(
        "\n👥 Number of affected users: "
    ).strip()

    try:
        affected_users = int(affected_users_input)
    except ValueError:
        print("❌ Error: affected users must be a whole number.")
        return

    # 🎫 Create the ticket using your existing function
    ticket, error = create_ticket(
        title=title,
        category=category,
        urgency=urgency,
        affected_users=affected_users,
        ticket_list=tickets,
    )

    if error:
        print(f"❌ Ticket was not created: {error}")
        return

    print(f"\n✅ Ticket {ticket['id']} created successfully!")
    display_ticket(ticket)
    save_changes(tickets)

# ─────────────────── 🔍 SEARCH TICKET ───────────────────

def search_for_ticket(tickets):
    """Find and display one ticket by ID."""
    print("\n🔍 SEARCH FOR A TICKET")
    ticket_id = input("🆔 Enter ticket ID: ").strip()
    ticket = find_ticket(ticket_id, tickets)

    if ticket is None:
        print("❌ Ticket not found.")
    else:
        display_ticket(ticket)


# ─────────────────── 👤 ASSIGN TICKET ───────────────────

def assign_existing_ticket(tickets):
    """Assign a ticket to a selected staff member."""

    staff_members = {
        "1": "Mr. Kingsley",
        "2": "Mr. God'swill",
        "3": "Mr Gabriel",
        "4": "Mr Emmanuel",
        "5": "Mr. Ayuba",
        "6": "Mr Onche",
    }

    print("\n" + "═" * 45)
    print("👤 ASSIGN TICKET TO STAFF")
    print("═" * 45)

    ticket_id = input("🆔 Enter ticket ID: ").strip()

    print("\n👨‍💼 SELECT STAFF MEMBER")
    print("─" * 35)

    for number, name in staff_members.items():
        print(f"  {number}. {name}")

    print("─" * 35)

    staff_choice = input("👉 Choose staff member (1-6): ").strip()

    if staff_choice not in staff_members:
        print("❌ Invalid selection. Please choose 1-6.")
        return

    staff_name = staff_members[staff_choice]

    success, message = assign_ticket(
        tickets, ticket_id, staff_name
    )

    print(("✅ " if success else "❌ ") + message)

    if success:
        save_changes(tickets)

# ─────────────────── 🔄 UPDATE STATUS ───────────────────

def change_ticket_status(tickets):
    """Change a ticket's status using workflow rules."""
    print("\n" + "═" * 45)
    print("🔄 UPDATE TICKET STATUS")
    print("═" * 45)

    ticket_id = input("🆔 Enter ticket ID: ").strip()

    # 🔄 Status selection menu
    print("\n📋 SELECT NEW STATUS")
    print("─" * 30)
    print("  1. ⚙️ In Progress")
    print("  2. ✅ Resolved")

    status_choice = input("👉 Choose status (1-2): ").strip()

    statuses = {
        "1": "in_progress",
        "2": "resolved",
    }

    if status_choice not in statuses:
        print("❌ Invalid status choice. Please select 1 or 2.")
        return

    new_status = statuses[status_choice]

    # 🔄 Apply existing workflow rules
    success, message = update_ticket_status(
        tickets, ticket_id, new_status
    )

    print(("✅ " if success else "❌ ") + message)

    # 💾 Save only when the update succeeds
    if success:
        save_changes(tickets)

# ─────────────────── 🔓 REOPEN TICKET ───────────────────

def reopen_resolved_ticket(tickets):
    """Reopen a previously resolved ticket."""
    print("\n🔓 REOPEN RESOLVED TICKET")
    ticket_id = input("🆔 Enter ticket ID: ").strip()

    success, message = reopen_ticket(tickets, ticket_id)
    print(("✅ " if success else "❌ ") + message)

    if success:
        save_changes(tickets)


# ─────────────────── 📥 WORK QUEUE ───────────────────

def display_work_queue(tickets):
    """Display open tickets in priority order."""
    queue = get_work_queue(tickets)

    print("\n" + "═" * 60)
    print("📥 OPEN-TICKET WORK QUEUE".center(60))
    print("═" * 60)

    if not queue:
        print("📭 No open tickets in the queue.")
        return

    display_tickets(queue)


# ─────────────────── 📊 REPORTS ───────────────────

def display_reports(tickets):
    """Display ticket totals, statuses, and priorities."""
    report = generate_report(tickets)

    print("\n" + "═" * 45)
    print("📊 CAMPUSFLOW TICKET REPORT".center(45))
    print("═" * 45)

    print(f"\n🎫 Total tickets: {report['total_tickets']}")

    print("\n🔄 STATUS COUNTS")
    print("─" * 35)
    print(f"{'Status':<22} {'Count':>8}")
    print("─" * 35)

    for status, count in report["status_counts"].items():
        print(f"{status:<22} {count:>8}")

    print("\n⚡ PRIORITY COUNTS")
    print("─" * 35)
    print(f"{'Priority':<22} {'Count':>8}")
    print("─" * 35)

    for priority, count in report["priority_counts"].items():
        print(f"{priority:<22} {count:>8}")

    print("─" * 35)


# ─────────────────── 🎓 MAIN MENU ───────────────────

def display_menu():
    """Display the main menu."""
    print("\n" + "═" * 60)
    print("🎓 CAMPUSFLOW HELP DESK".center(60))
    print("🏫 Campus Support & Ticket Management".center(60))
    print("═" * 60)

    print("  1. 🎫 Create a new ticket")
    print("  2. 📋 List all tickets")
    print("  3. 🔍 Search for a ticket")
    print("  4. 👤 Assign a ticket to an agent")
    print("  5. 🔄 Update ticket status")
    print("  6. 🔓 Reopen a resolved ticket")
    print("  7. 📥 View open work queue")
    print("  8. 📊 View reports")
    print("  9. 🚪 Exit system")

    print("═" * 60)


# ─────────────────── 🚀 APPLICATION ───────────────────

def main():
    """Load saved tickets and run the menu until exit."""
    try:
        tickets = load_tickets()
    except (ValueError, OSError) as error:
        print(f"❌ Could not load saved tickets: {error}")
        print("⚠️ Please correct the storage problem before restarting.")
        return

    print("\n" + "═" * 60)
    print("👋 Welcome to CampusFlow!")
    print(f"📂 Loaded {len(tickets)} ticket(s).")
    print("═" * 60)

    while True:
        display_menu()
        choice = input("👉 Choose an option (1-9): ").strip()

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
            print("\n👋 Thank you for using CampusFlow. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please enter a number from 1 to 9.")


if __name__ == "__main__":
    main()
