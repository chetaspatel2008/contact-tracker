import json
import os

FILE = "contacts.json"

def read_contacts():
    if not os.path.exists(FILE):
        return []
    
    with open(FILE, "r") as file:
        contacts = json.load(file)
    return contacts


def add_contacts():

    name = input("\nEnter the name: ")
    phone = input("\nEnter the phone number: ")
    email = input("\nEnter the email id: ")

    contacts = read_contacts()

    contacts.append({
        "name" : name,
        "phone": phone,
        "email": email
    })

    with open(FILE, "w") as file:
        json.dump(contacts, file, indent=4)
    print("\nContact saved!!\n")


def show_contacts():
    contacts = read_contacts()
    if not contacts:
        print("\nNo contacts found")
        return

    for contact in contacts:
        print("-----------------------------------------------")
        print("Name:", contact["name"])
        print("Phone No.:", contact["phone"])
        print("Email:", contact["email"])
    print("-----------------------------------------------")

def search_contacts():
    name = input("\nEnter name to search : ")

    contacts = read_contacts()

    for contact in contacts:
        if contact["name"].lower() == name.lower():
            print("-----------------------------------------------")
            print("Name:", contact["name"])
            print("Phone No.:", contact["phone"])
            print("Email:", contact["email"])
            print("-----------------------------------------------")
            return
    print("\nContacts not found!\n")


while True:
    print("-----------------------")
    print("1. - Add contacts")
    print("2. - Show contacts")
    print("3. - Search contacts")
    print("4. - Exit")
    print("-----------------------")

    print()

    choice = int(input("\nEnter choice : "))

    if choice == 1:
        add_contacts()
    elif choice == 2:
        show_contacts()
    elif choice == 3:
        search_contacts()
    elif choice == 4:
        break
    else:
        print("\nInvalid character!!\n")