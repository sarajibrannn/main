# Repo Link https://github.com/sarajibrannn/main.git
class Ticket:
    ticket_counter = 2000  # Counter for assigning unique ticket numbers
    tickets = []  # List to store all created ticket objects

    def __init__(self, staff_id, creator_name, contact_email, description):
        self.ticket_number = Ticket.ticket_counter  # Assign a unique ticket number
        Ticket.ticket_counter += 1  # Increment the ticket counter for the next ticket
        self.staff_id = staff_id
        self.creator_name = creator_name
        self.contact_email = contact_email
        self.description = description
        self.response = "Not Yet Provided"  # Initial response is set to a default value
        self.status = "Open"  # Initial status is set to "Open"
        Ticket.tickets.append(self)  # Add the created ticket object to the list

    # Methods for interacting with tickets
    # ...

    @staticmethod
    def ticket_stats():
        # Calculate and return ticket statistics
        total_tickets = len(Ticket.tickets)
        resolved_tickets = sum(1 for ticket in Ticket.tickets if ticket.status == "Closed")
        open_tickets = total_tickets - resolved_tickets
        return total_tickets, resolved_tickets, open_tickets


class Main:
    # Methods for user interaction and system functionality
    # ...

    @staticmethod
    def main():
        while True:
            # Display menu options for the help desk system
            # ...


if __name__ == "__main__":
    Main.main()  # Start the main program loop when the script is executed
