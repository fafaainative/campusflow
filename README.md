
# CampusFlow

CampusFlow is a command-line campus helpdesk ticket manager built with Python.
It allows users to create, assign, track, search, and report helpdesk tickets.

## Features

- Create and validate tickets.
- Generate unique ticket IDs and calculate priority.
- List and search tickets.
- Assign tickets to staff members.
- Update ticket status and reopen resolved tickets.
- Display an open-ticket work queue sorted by priority.
- Generate ticket reports.
- Save and reload tickets using JSON.
- Run automated tests with Python's built-in unittest framework.

## Requirements

- Python 3
- No third-party Python packages required.

## How to Run

From the project root, run:

```bash
python3 main.py
```

Follow the numbered menu options to use CampusFlow. Select option 9 to exit.

## Ticket Rules

- Ticket titles must not be empty.
- Categories: Network, Hardware, Software, Other.
- Urgency: low, medium, high.
- A ticket must have an assignee before it can move to `in_progress`.
- Normal progression is `open` → `in_progress` → `resolved`.
- Resolved tickets must be reopened before further assignment or status changes.
- The work queue contains open tickets, sorted by priority and numeric ticket ID.

## Data Storage

Tickets are stored in `data/tickets.json`.

- On startup, CampusFlow loads previously saved tickets.
- If the JSON file does not exist, the application starts with an empty ticket list.
- Successful ticket changes are saved to JSON.
- If the saved JSON is malformed, CampusFlow displays an error instead of silently discarding the data.

Do not commit personal or test ticket data unless the team explicitly agrees to include sample data.

## Running Tests

From the project root, run:

```bash
python3 -m unittest discover -s tests -v
```

The test suite covers ticket creation, validation, assignment, status transitions, queue ordering, reports, and JSON storage.

## Project Structure

- `main.py` — command-line menu and application integration.
- `campusflow/tickets.py` — ticket creation, validation, IDs, and search.
- `workflow.py` — assignment and status workflow.
- `queue_manager.py` — open-ticket work queue.
- `reports.py` — ticket reports.
- `storage.py` — JSON loading and saving.
- `tests/` — automated tests.
- `data/` — application data.
- `docs/` — engineering documentation and learning logs.

## Team Responsibilities

Engineer A: ticket creation, validation, priority calculation, ticket IDs, listing, and search.

Engineer B: assignment, status transitions, reopening, work queue, and reports.

Both engineers contribute to integration, testing, documentation, and code review.

## Limitations

CampusFlow is a local command-line application. It does not currently provide a graphical interface, user authentication, or a database-backed multi-user service.
# campusflow
CampusFlow is a command-line helpdesk app  with ticket creation, priority calculation, assignment, status changes, queue, reporting, JSON storage, and automated tests.
