# Read, search and append data to a contacts.txt file. Handle missing file, invalid user options
# and write errors.
def read_contacts():
    try:
        with open("contacts.txt", "r") as file:
            print("\n--- Contact List ---")
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("Error: contacts.txt file not found.")


def search_contact():
    name = input("Enter name to search: ").strip().lower()
    found = False

    try:
        with open("contacts.txt", "r") as file:
            for line in file:
                parts = line.strip().split(",")
                if len(parts) == 2 and parts[0].lower() == name:
                    print("Contact Found:", line.strip())
                    found = True
                    break
    except FileNotFoundError:
        print("Error: contacts.txt file not found.")

    if not found:
        print("Contact not found.")


def add_contact():
    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()

    try:
        with open("contacts.txt", "a") as file:
            file.write(f"{name},{phone}\n")
        print("Contact added successfully.")
    except PermissionError:
        print("Error: Permission denied while writing to file.")
    except Exception as e:
        print("Write error:", e)


# -------- Main Menu --------
while True:
    print("\n1. Read Contacts")
    print("2. Search Contact")
    print("3. Add Contact")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        read_contacts()
    elif choice == "2":
        search_contact()
    elif choice == "3":
        add_contact()
    elif choice == "4":
        print("Exiting program.")
        break
    else:
        print("Invalid option! Please choose 1-4.")
