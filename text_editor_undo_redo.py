class TextEditor:
    def __init__(self):
        self.document = ""
        self.undo_stack = []
        self.redo_stack = []

    def make_change(self):
        new_text = input("Enter new document text: ")
        self.undo_stack.append(self.document)
        self.document = new_text
        self.redo_stack.clear()
        print("Change made successfully.")

    def undo(self):
        if self.undo_stack:
            self.redo_stack.append(self.document)
            self.document = self.undo_stack.pop()
            print("Undo successful.")
        else:
            print("Nothing to undo.")

    def redo(self):
        if self.redo_stack:
            self.undo_stack.append(self.document)
            self.document = self.redo_stack.pop()
            print("Redo successful.")
        else:
            print("Nothing to redo.")

    def display(self):
        print("Current Document:", self.document)


# Menu-driven program
editor = TextEditor()

while True:
    print("\n----- TEXT EDITOR -----")
    print("1. Make a Change")
    print("2. Undo")
    print("3. Redo")
    print("4. Display Document")
    print("5. Exit")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a number from 1 to 5.")
        continue

    if choice == 1:
        editor.make_change()
    elif choice == 2:
        editor.undo()
    elif choice == 3:
        editor.redo()
    elif choice == 4:
        editor.display()
    elif choice == 5:
        print("Exiting...")
        break
    else:
        print("Invalid choice! Please enter 1 to 5.")
