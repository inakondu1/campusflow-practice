import sys
import json

# Adjust this import to match your find output:
# from YOUR_MODULE import assign_ticket, update_status

def main():
    try:
        with open("data/tickets.json", "r") as f:
            tickets = json.load(f)
        print(f"Loaded {len(tickets)} ticket(s) from storage.\n")
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        tickets = {}

    while True:
        print("=" * 40)
        print("      CAMPUSFLOW HELPDESK SYSTEM")
        print("=" * 40)
        print("1. Create Ticket (Engineer A)")
        print("2. View All Tickets")
        print("3. Assign Ticket")
        print("4. Update Ticket Status")
        print("5. View Work Queue")
        print("6. View Summary Report")
        print("7. Exit")
        print("=" * 40)
        
        choice = input("Select an option (1-7): ").strip()

        if choice == "3":
            raw_id = input("Enter Ticket ID to assign: ").strip()
            try:
                tid = int(raw_id)
            except ValueError:
                print(f"Error: '{raw_id}' is not a valid numeric Ticket ID.\n")
                continue

            assignee = input("Enter staff member name: ").strip()
            if not assignee:
                print("Error: Staff name cannot be empty.\n")
                continue

            assign_ticket(tickets, tid, assignee)

        elif choice == "4":
            raw_id = input("Enter Ticket ID to update: ").strip()
            try:
                tid = int(raw_id)
            except ValueError:
                print(f"Error: '{raw_id}' is not a valid numeric Ticket ID.\n")
                continue

            print("Valid statuses: open, in_progress, resolved")
            new_status = input("Enter new status: ").strip().lower()
            valid_statuses = {"open", "in_progress", "resolved"}

            if new_status not in valid_statuses:
                print(f"Error: '{new_status}' is not a valid status.\n")
                continue

            update_status(tickets, tid, new_status)

        elif choice == "7":
            print("Exiting CampusFlow. Goodbye!")
            sys.exit(0)

if __name__ == "__main__":
    main()
