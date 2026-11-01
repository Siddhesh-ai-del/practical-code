from collections import *


class EventQueue:
    def __init__(self):
        self.events = deque()

    # Add an event
    def add_event(self, event):
        self.events.append(event)
        print("Event added:", event)

    # Process the next event
    def process_event(self):
        if self.events:
            event = self.events.popleft()
            print("Event processed:", event)
        else:
            print("No pending events")

    # Display pending events
    def display_events(self):
        if self.events:
            print("Pending events:", list(self.events))
        else:
            print("No pending events")

    # Cancel an event
    def cancel_event(self, event):
        if event in self.events:
            self.events.remove(event)
            print("Event cancelled:", event)
        else:
            print("Event not found")


# Main program
queue = EventQueue()

while True:
    print("\n----- EVENT MENU -----")
    print("1. Add an Event")
    print("2. Process the Next Event")
    print("3. Display Pending Events")
    print("4. Cancel an Event")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        event = input("Enter event name: ")
        queue.add_event(event)
    elif choice == "2":
        queue.process_event()
    elif choice == "3":
        queue.display_events()
    elif choice == "4":
        event = input("Enter event to cancel: ")
        queue.cancel_event(event)
    elif choice == "5":
        print("Program ended.")
        break
    else:
        print("Invalid choice")
