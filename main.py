import sys
from campusflow.storage import load_tickets, save_tickets
from campusflow.workflow import assign_ticket, update_status, get_work_queue
from campusflow.reports import generate_report

def print_menu():
    print("\n" + "="*40)
    print("      CAMPUSFLOW HELPDESK SYSTEM")
    print("="*40)
    print("1. Create Ticket (Engineer A)")
    print("2. View All Tickets")
    print("3. Assign Ticket")
    print("4. Update Ticket Status")
    print("5. View Work Queue")
    print("6. View Summary Report")
    print("7. Exit")
    print("="*40)

def main():
    tickets = load_tickets()
    print(f"Loaded {len(tickets)} ticket(s) from storage.")

    while True:
        print_menu()
        choice = input("Select an option (1-7): ").strip()

        if choice == "1":
            print("\n[Ticket Creation is assigned to Engineer A]")

        elif choice == "2":
            if not tickets:
                print("\nNo tickets available.")
            else:
                print("\n--- ALL TICKETS ---")
                for t in tickets:
                    print(f"[{t.get("id")}] {t.get("title")} | Priority: {t.get("priority")} | Status: {t.get("status")} | Assigned: {t.get("assigned_to")}")

        elif choice == "3":
            tid = int(input("Enter Ticket ID to assign: ").strip())
            target = next((t for t in tickets if t.get("id") == tid), None)
            if not target:
                print(f"Error: Ticket '{tid}' not found.")
                continue
            name = input("Enter staff member name: ").strip()
            try:
                assign_ticket(target, name)
                save_tickets(tickets)
                print(f"Success: Ticket {tid} assigned to {name}.")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == "4":
            tid = int(input("Enter Ticket ID to update: ").strip())
            target = next((t for t in tickets if t.get("id") == tid), None)
            if not target:
                print(f"Error: Ticket '{tid}' not found.")
                continue
            status = input("Enter new status (open, in_progress, resolved): ").strip().lower()
            try:
                update_status(target, status)
                save_tickets(tickets)
                print(f"Success: Ticket {tid} status changed to '{status}'.")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == "5":
            queue = get_work_queue(tickets)
            if not queue:
                print("\nWork queue is empty!")
            else:
                print("\n--- WORK QUEUE (Sorted by Priority & ID) ---")
                for t in queue:
                    print(f"[{t.get("id")}] {t.get("title")} | Priority: {t.get("priority")} | Status: {t.get("status")} | Assigned: {t.get("assigned_to")}")

        elif choice == "6":
            report = generate_report(tickets)
            print("\n--- CAMPUSFLOW SUMMARY REPORT ---")
            print(f"Total Tickets: {report["total"]}")
            print("By Status:", report["by_status"])
            print("By Priority:", report["by_priority"])

        elif choice == "7":
            save_tickets(tickets)
            print("\nSaved changes. Goodbye!")
            sys.exit(0)

        else:
            print("Invalid selection. Please enter a number between 1 and 7.")

if __name__ == "__main__":
    main()
