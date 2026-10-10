📘 CampusFlow — Engineer A AI Learning Log

Fellow: IKYAAIBO EPHRAIM AONDOFA
Cohort: July
Campus: Otukpo Campus

Role: Ticket Creation and Validation
Project: CampusFlow — Campus Helpdesk Ticket Management System

Interaction #1 — Python Functions and Ticket Creation

Problem: I needed to understand how to create a ticket using a Python function and store its information in a dictionary.

My initial understanding: I understood that a dictionary stores information using keys and values, but I was not completely sure how to organize ticket creation inside a function.

Prompt to AI: Explain how Python functions and dictionaries can be used to create a campus helpdesk ticket. Guide me step by step without writing the complete project for me.

Useful AI guidance: A function can receive ticket details as parameters, organize them into a dictionary, and return the new ticket. The ticket must follow the agreed CampusFlow dictionary structure.

My independent experiment/test: I implemented or modified my own ticket creation function in tickets.py. I tested it with valid ticket details and checked whether the returned dictionary contained all required keys.

Verification source or result: Record the actual result of my test, including any errors I corrected.

Decision: Accepted and adapted the guidance because functions and dictionaries provide a clear way to organize ticket information.

Related file/commit: tickets.py — create_ticket(); commit: <actual commit SHA or pending>

What I can now explain without AI: I can explain how a function accepts ticket details, creates a dictionary, and returns the ticket for other parts of the application to use.

Interaction #2 — Input Validation and Priority Calculation

Problem: I needed to validate ticket information and calculate priority consistently.

My initial understanding: I knew that if and elif statements could check conditions, but I needed to understand how to apply several priority rules in the correct order.

Prompt to AI: Help me understand how to validate ticket titles, categories, urgency, and affected users, and how to calculate ticket priority using ordered conditions. Give me test cases rather than a complete implementation.

Useful AI guidance: Validate input before creating a ticket. Use the agreed categories and urgency values, require a positive integer for affected users, and check the most specific priority condition first.

My independent experiment/test: I tested different urgency levels and affected-user counts. I also tried invalid categories, empty titles, zero or negative user counts, and Boolean values.

Verification source or result: Record the actual test results. Include at least one boundary case, such as high urgency with 10 affected users producing critical priority.

Decision: Accepted the guidance after checking the priority rules against the project requirements. I changed any implementation details that did not match the requirements.

Related file/commit: tickets.py — validate_ticket_data() and calculate_priority(); tests/test_tickets.py; commit: <actual commit SHA or pending>

What I can now explain without AI: I can explain why validation should happen before ticket creation and why the priority rules must be evaluated in the agreed order.

Interaction #3 — Unique Ticket IDs and Testing

Problem: I needed to generate unique ticket IDs and test the ticket functions independently.

My initial understanding: I understood that ticket IDs identify individual tickets, but I needed to work out how to avoid duplicates when multiple tickets already exist.

Prompt to AI: Explain how to generate IDs such as T001, T002, and T003 from an existing ticket list. Help me design tests for ID generation, listing, searching, and ticket creation without giving me the complete solution.

Useful AI guidance: Examine existing IDs, identify the largest valid numeric suffix, and generate the next ID. Test normal cases, empty lists, existing records, and missing ticket searches.

My independent experiment/test: I tested ID generation with an empty list and a list containing existing tickets. I also searched for an existing ID and a ticket ID that was not present.

Verification source or result: Record the actual results from python3 -m unittest discover -s tests -v, including any failed tests and how I resolved them.

Decision: Accepted the approach after verifying the generated IDs and confirming that the search function handled missing IDs appropriately.

Related file/commit: tickets.py — generate_ticket_id(), list_tickets(), and find_ticket(); tests/test_tickets.py; commit: <actual commit SHA or pending>

What I can now explain without AI: I can explain how unique IDs help identify tickets and how unit tests check that individual functions behave as expected.

🧠 Final Reflection

What I learned:
I learned how to organize ticket information with dictionaries, use functions to separate responsibilities, validate user input, calculate priority, generate ticket IDs, and test individual features.

What I verified independently:
<List the functions and test cases I personally ran and verified.>

What I improved or rejected from AI guidance:
<Describe at least one suggestion I changed, rejected, or improved, and explain why. If I accepted all suggestions, explain how I independently checked them instead.>

What I still need to improve:
<Describe the Python concepts or testing areas I still find difficult.>

Final test result:
<Write the actual number of tests passed and failed.>

Final GitHub branch:
feature/engineer-a-tickets
