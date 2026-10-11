
# CampusFlow Design Decisions

## 1. Ticket Data Structure

CampusFlow represents each ticket as a Python dictionary.

Every ticket uses these fields:

- `id`
- `title`
- `category`
- `urgency`
- `affected_users`
- `priority`
- `status`
- `assigned_to`

Both engineers must preserve these field names to maintain compatibility.

## 2. Separation of Responsibilities

- `campusflow/tickets.py` handles creation, validation, priority calculation, ID generation, listing, and searching.
- `workflow.py` handles assignment, status transitions, and reopening.
- `queue_manager.py` builds the open-ticket work queue.
- `reports.py` calculates ticket totals, status counts, and priority counts.
- `storage.py` loads and saves tickets using JSON.
- `main.py` provides the user-facing menu and connects the modules.

This separation keeps the menu, business rules, and file operations easier to test and maintain.

## 3. Workflow Rules

Normal status progression is:

`open` → `in_progress` → `resolved`

A ticket must be assigned before work begins. A resolved ticket must be explicitly reopened before further assignment or status changes.

Failed operations should not partially modify ticket data.

## 4. Work Queue

The queue contains only open tickets.

Tickets are sorted by priority: critical, high, medium, then low. Tickets with the same priority are sorted by the numeric portion of their IDs.

The queue returns a new list without rearranging the original ticket collection.

## 5. JSON Storage

The storage module uses Python's standard-library `json` module.

The default file is `data/tickets.json`.

A missing file represents a fresh start. Malformed JSON is reported as an error rather than silently treated as an empty ticket list.

The menu loads tickets at startup and saves successful changes.

## 6. Testing

The project uses Python's built-in `unittest` framework.

Run all tests with:

`python3 -m unittest discover -s tests -v`

Tests should cover successful operations, rejected input, workflow rules, queue sorting, report counts, and JSON persistence.

## 7. Collaboration

Both engineers must agree on shared ticket fields and function interfaces before changing them.

Each engineer should review the other engineer's pull request, provide substantive feedback, and approve only after reviewing the changes and test evidence.

## 8. Known Limitations

CampusFlow is currently a local command-line application. It does not provide authentication, concurrent multi-user access, or database transactions.
