def assign_ticket(ticket, staff_name):
    """
    F3 — ASSIGN: Assign a ticket to a non-empty staff member name.
    """
    if not staff_name or not staff_name.strip():
        raise ValueError("Staff name cannot be blank.")
    
    if ticket.get("status") == "resolved":
        raise ValueError("Cannot assign a resolved ticket. Reopen it first.")

    ticket["assigned_to"] = staff_name.strip()
    return ticket


def update_status(ticket, new_status):
    """
    F4 — WORKFLOW: open -> in_progress -> resolved.
    - Cannot move unassigned ticket to in_progress.
    - Resolved tickets require explicit reopening.
    """
    valid_statuses = ["open", "in_progress", "resolved"]
    if new_status not in valid_statuses:
        raise ValueError(f"Invalid status '{new_status}'. Must be one of {valid_statuses}")

    current_status = ticket.get("status", "open")

    if current_status == "resolved" and new_status != "open":
        raise ValueError("Ticket is resolved. Reopen to 'open' before making changes.")

    if new_status == "in_progress" and not ticket.get("assigned_to"):
        raise ValueError("Cannot move unassigned ticket to in_progress. Assign a staff member first.")

    ticket["status"] = new_status
    return ticket


def get_work_queue(tickets):
    """
    F5 — WORK QUEUE: Order open/in_progress tickets by priority 
    (critical -> high -> medium -> low) and break ties with ticket ID.
    """
    priority_weights = {
        "critical": 1,
        "high": 2,
        "medium": 3,
        "low": 4
    }
    
    active_tickets = [t for t in tickets if t.get("status") in ["open", "in_progress"]]

    return sorted(
        active_tickets,
        key=lambda t: (priority_weights.get(t.get("priority", "low"), 4), t.get("id", ""))
    )
