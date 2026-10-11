1. Responsibility

Engineer B is responsible for the ticket workflow and reporting features of CampusFlow.

Responsibilities include:

Ticket assignment

Ticket status transitions

Reopening resolved tickets

Open-ticket work queue

Ticket reportsgit switch -c feature/engineer-b-workflow

Unit tests for these features

Reviewing Engineer A's pull request

Implementation files

workflow.py

queue_manager.py

reports.py

Test files

tests/test_workflow.py

tests/test_queue_manager.py

tests/test_reports.py

2. Shared Ticket Structure

Every ticket must preserve the following eight fields:

Field

Description

id

Unique ticket reference

title

Short description of the issue

category

Type of issue reported

urgency

Reported urgency

affected_users

Number of users affected

priority

Calculated ticket priority

status

Current workflow state

assigned_to

Staff member responsible for the ticket

Engineer B must use the same ticket dictionary structure as Engineer A. Field names must not be renamed or changed without agreement.

Engineer B should normally modify only assigned_to and status. Priority calculation remains Engineer A's responsibility.

3. Ticket Assignment

Function

assign_ticket(tickets, ticket_id, assigned_to)

This function assigns an existing ticket to a staff member.

Success conditions

The ticket exists.

The staff member's name is a nonblank string.

Surrounding whitespace is removed from the staff member's name.

The ticket's assigned_to field is updated.

Failure conditions

The ticket ID does not exist.

The staff member's name is blank or is not a string.

The ticket is resolved and has not been reopened.

Return value

Successful operations return (True, message).

Failed operations return (False, message).

The function must not modify the ticket when an assignment request fails.

4. Ticket Status Workflow

Function

update_ticket_status(tickets, ticket_id, new_status)

Valid statuses are:

open

in_progress

resolved

Permitted transitions

Normal ticket progression is:

open → in_progress → resolved

Rules:

A ticket must have an assignee before moving to in_progress.

A ticket cannot skip directly from open to resolved.

Invalid statuses must be rejected.

Status input should be stripped of surrounding whitespace and converted to lowercase before validation.

A resolved ticket cannot be modified through the normal status update function.

Failed transitions must not change the ticket's status.

Reopening resolved tickets

Function:

reopen_ticket(tickets, ticket_id)

Only a resolved ticket may be reopened. Reopening changes its status to open.

Both status functions return (success, message), where success is a Boolean and message explains the outcome.

5. Open-Ticket Work Queue

Function

get_work_queue(tickets)

The work queue displays tickets waiting to be started.

The function must:

Include only tickets whose status is open.

Sort tickets by priority in this order: critical, high, medium, low.

Sort tickets within the same priority by the numeric part of the ticket ID.

Return a new sorted list without changing the original ticket collection.

For example, T002 must appear before T010 when both tickets have the same priority.

Unknown priorities should sort after recognized priorities. Malformed ticket IDs should sort after correctly formatted IDs within the same priority.

The function returns a list of ticket dictionaries.

6. Ticket Reports

Function

generate_report(tickets)

This function generates a summary of the ticket collection.

The returned dictionary must contain:

total_tickets: total number of ticket records.

status_counts: counts for open, in_progress, and resolved.

priority_counts: counts for critical, high, medium, and low.

Every supported status and priority must appear in the report, even when its count is zero.

The function must also support an empty ticket list.

Example output

{
    "total_tickets": 2,
    "status_counts": {
        "open": 1,
        "in_progress": 1,
        "resolved": 0
    },
    "priority_counts": {
        "critical": 1,
        "high": 1,
        "medium": 0,
        "low": 0
    }
}

7. Error-Handling Convention

Assignment and status operations use the following return convention:

(True, message) indicates success.

(False, message) indicates failure.

The work queue returns a list.

The report function returns a dictionary.

The CLI must inspect each operation's return value and display an appropriate message instead of assuming every operation succeeds.

Failed operations must not leave the ticket collection in an invalid or partially updated state.

8. Testing

Engineer B uses Python's built-in unittest framework.

Run all project tests from the repository root:

python3 -m unittest discover -s tests -v

Tests should cover:

Successful The work queue displays tickets waiting to be started.

The function must:

Include only tickets whose status is open.

Sort tickets by priority in this order: critical, high, medium, low.

Sort tickets within the same priority by the numeric part of the ticket ID.

Return a new sorted list without changing the original ticket collection.

For example, T002 must appear before T010 when both tickets have the same priority.

Unknown priorities should sort after recognized priorities. Malformed ticket IDs should sort after correctly formatted IDs within the same priority.

The function returns a list of ticket dictionaries.

6. Ticket Reports

Function

generate_report(tickets)

This function generates a summary of the ticket collection.

The returned dictionary must contain:

total_tickets: total number of ticket records.

status_counts: counts for open, in_progress, and resolved.

priority_counts: counts for critical, high, medium, and low.

Every supported status and priority must appear in the report, even when its count is zero.

The function must also support an empty ticket list.

Example output

{
    "total_tickets": 2,
    "status_counts": {
        "open": 1,
        "in_progress": 1,
        "resolved": 0
    },
    "priority_counts": {
        "critical": 1,
        "high": 1,
        "medium": 0,
        "low": 0
    }
}

7. Error-Handling Convention

Assignment and status operations use the following return convention:

(True, message) indicates success.

(False, message) indicates failure.

The work queue returns a list.

The report function returns a dictionary.

The CLI must inspect each operation's return value and display an appropriate message instead of assuming every operation succeeds.

Failed operations must not leave the ticket collection in an invalid or partially updated state.

8. Testing

Engineer B uses Python's built-in unittest framework.

Run all project tests from the repository root:

python3 -m unittest discover -s tests -v

Tests should cover:

Successful ticket assignment.

Rejection of blank staff names.

Rejection of missing ticket IDs.

Valid and invalid status transitions.

The requirement for an assignee before work begins.

Reopening resolved tickets.

Filtering open tickets.

Priority sorting.

Numeric ticket ID sorting.

Preservation of the original ticket list order.

Report counts for statuses and priorities.

Empty report generation.

Failed operations leaving ticket data unchanged.

Engineer B should add further edge-case tests as needed and investigate failures rather than deleting tests to obtain a passing result.

9. Integration with Engineer A

Engineer A owns:

Ticket creation and validation.

Priority calculation.

Ticket ID generation.

Ticket listing and search.

Engineer B owns:

Ticket assignment.

Status transitions and reopening.

Work queue management.

Ticket reports.

Both engineers must agree on shared data structures and function interfaces before integration.

Integration rules:

Use the same ticket dictionaries and field names.

Do not duplicate ticket creation or validation logic.

Do not change Engineer A's function signatures without agreement.

Pass the shared ticket collection to the appropriate functions.

Use the shared CLI in main.py.

Use the shared storage module for loading and saving tickets.

Save changes after successful operations when required by the storage design.

Review each other's pull requests before merging.

Engineer B must not create separate, competing ticket collections in the workflow, queue, report, CLI, or storage modules.

10. Scope and Limitations

Engineer B's modules implement in-memory ticket operations.

They do not independently:

Create the shared CLI menu.

Load or save JSON files.

Implement ticket creation.

Calculate ticket priority.

Manage GitHub integration.

These responsibilities belong to the shared project modules or Engineer A's implementation.

11. GitHub Workflow

Engineer B must work on the feature branch:

feature/engineer-b-workflow

Before committing, run:

git status
git diff
python3 -m unittest discover -s tests -v

Stage Engineer B's files:

git add workflow.py queue_manager.py reports.py
git add tests/test_workflow.py tests/test_queue_manager.py tests/test_reports.py
git add docs/ENGINEER_B.md

Commit the changes:

git commit -m "Implement Engineer B workflow queue and reports"

Push the branch:

git push -u origin feature/engineer-b-workflow

Open a pull request with the following details:

Base branch: main

Compare branch: feature/engineer-b-workflow

Title: Engineer B: Workflow, queue, and reports

Include a brief summary of the implementation and the test command used.

Engineer B must also review Engineer A's pull request and provide at least two substantive, evidence-based review comments. Comments should address actual implementation details, potential problems, or verified behavior.

12. AI Learning Log

Engineer B must maintain an honest learning log at:

docs/AI_LEARNING_LOG.md

The log must contain at least three genuine AI interactions, including one instance in which an AI suggestion was verified, modified, or rejected.

Each entry should record:

Date and topic.

Question asked.

Suggestion received.

What was learned.

What was implemented or tested.

The outcome and supporting evidence.

The log must reflect real work. Do not claim to have run tests, verified behavior, or changed code unless those actions were actually performed.

13. Final Handover Checklist

Before Engineer B's work is considered ready for integration, confirm that:

All Engineer B implementation files are present.

All Engineer B test files are present.

The shared ticket structure is preserved.

Function interfaces and return conventions are agreed upon.

All tests have been run and failures investigated.

At least one additional edge-case test has been added.

The feature branch has been pushed to GitHub.

Engineer B's pull request has been opened.

Engineer A's pull requesrequest has received two substantive review comments.

The CLI and storage integration plan is agreed upon.

The AI learning log contains three genuine interactions.

The shared README and project documentation are up to date.

Documentation status: This document defines Engineer B's responsibilities, expected behavior, testing requirements, integration rules, and Github workflow for the CampusFlow project.