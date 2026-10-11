# 📚 CampusFlow — Campus Helpdesk Ticket Management System

A simple Python-based command-line application for managing campus helpdesk tickets.

CampusFlow allows students and campus users to report problems, while helpdesk staff can manage, assign, track, and resolve tickets efficiently.

## 🚀 Features

Engineer A is responsible for the following features:

- Create new helpdesk tickets.
- Validate ticket titles, categories, urgency levels, and affected users.
- Generate unique ticket IDs (e.g., `T001`, `T002`).
- Automatically calculate ticket priority (`critical`, `high`, `medium`, or `low`).
- View all available tickets.
- Search for tickets by ticket ID.
- Prevent invalid ticket data and duplicate ticket IDs.

## 🛠️ Technologies Used

- Python 3
- Built-in data structures (`list`, `dict`)
- Conditional statements (`if`, `elif`, `else`)
- Functions
- Input validation
- Python `unittest` framework
- Git and GitHub for version control and collaboration

## 📖 Usage

### 1️⃣ Import the Ticket Functions

Engineer A implements the ticket management functions in `tickets.py`.

The functions can be imported into the main program:

```python
from tickets import (
    create_ticket,
    list_tickets,
    find_ticket,
    calculate_priority,
    validate_ticket_data,
    generate_ticket_id
)
```

### 2️⃣ Ticket Information

Each ticket must use the agreed dictionary structure:

```python
{
    "id": "T001",
    "title": "Campus Wi-Fi is not working",
    "category": "Network",
    "urgency": "high",
    "affected_users": 15,
    "priority": "critical",
    "status": "open",
    "assigned_to": None
}
```

**Important:** Both engineers must use the same dictionary keys and initial values to avoid integration problems.

### 3️⃣ Ticket Categories and Urgency

Valid categories:

- `Network`
- `Hardware`
- `Software`
- `Other`

Valid urgency levels:

- `low`
- `medium`
- `high`

The number of affected users must be a positive integer. Boolean values such as `True` and `False` must be rejected.

### 4️⃣ Ticket Priority Rules

CampusFlow calculates ticket priority using the following rules, in order:

| Condition | Priority |
|---|---|
| High urgency and at least 10 affected users | Critical |
| High urgency or at least 10 affected users | High |
| Medium urgency or at least 3 affected users | Medium |
| None of the above | Low |

### 5️⃣ Example Output

Creating a ticket:

```text
Ticket created successfully.

Ticket ID: T001
Title: Campus Wi-Fi is not working
Category: Network
Urgency: high
Affected Users: 15
Priority: critical
Status: open
Assigned To: None
```

Invalid ticket data:

```text
Invalid ticket data.
Affected users must be a positive integer.
```

The exact messages displayed may depend on how the main program handles the results returned by Engineer A's functions.

## 📂 Project Structure

```text
campusflow/
│
├── tickets.py
├── workflow.py
├── queue_manager.py
├── reports.py
├── storage.py
├── main.py
│
├── tests/
│   ├── test_tickets.py
│   ├── test_workflow.py
│   ├── test_queue_manager.py
│   └── test_reports.py
│
├── docs/
│   ├── ENGINEER_A.md
│   ├── ENGINEER_B.md
│   └── AI_LEARNING_LOG_A.md
│
└── README.md
```

Engineer A primarily works on `tickets.py` and `tests/test_tickets.py`. Shared files such as `main.py`, `storage.py`, and `README.md` must be coordinated with Engineer B.

## 🧪 Testing

Engineer A must test ticket creation, validation, priority calculation, ID generation, listing, and searching.

Run the project's tests from the repository root:

```bash
python3 -m unittest discover -s tests -v
```

Tests should cover:

- Valid ticket creation.
- Invalid or empty titles.
- Invalid categories and urgency levels.
- Zero, negative, non-integer, and Boolean affected-user values.
- Correct priority calculation.
- Unique ticket ID generation.
- Listing and searching for tickets.
- Missing ticket IDs.

## 🤝 Team Responsibilities

**Engineer A — Ticket Creation and Validation**

- Implement ticket creation and validation functions.
- Calculate ticket priorities.
- Generate unique ticket IDs.
- Implement ticket listing and searching.
- Write and maintain ticket-related tests.

**Engineer B — Ticket Workflow and Reporting**

- Assign tickets to helpdesk staff.
- Update ticket statuses.
- Reopen resolved tickets where permitted.
- Manage the open-ticket work queue.
- Generate ticket reports and counts.

**Shared responsibilities**

- Agree on the ticket dictionary structure and function interfaces.
- Integrate the features from both engineers.
- Coordinate changes to shared files.
- Run integration tests.
- Maintain the project README and documentation.
- Use GitHub branches and pull requests for collaboration.

## 📤 GitHub Workflow

Engineer A should work on the branch:

```text
feature/engineer-a-tickets
```

Recommended workflow:

1. Create or switch to the Engineer A branch.
2. Implement the ticket management functions.
3. Run the relevant tests.
4. Commit and push tested changes to GitHub.
5. Open a pull request for review.
6. Coordinate with Engineer B before integration.
7. Run all project tests after integrating approved changes.

## 🔮 Possible Enhancements

- Save and load tickets using JSON files.
- Add ticket filtering by category, urgency, priority, or status.
- Improve error messages and user input handling.
- Add timestamps for ticket creation and resolution.
- Add authentication and role-based access.
- Develop a graphical user interface or web interface.

## 👨‍💻 Author

CampusFlow Development Team

**Engineer A:** Ticket Creation and Validation

**Engineer B:** Workflow, Queue Management, and Reporting
