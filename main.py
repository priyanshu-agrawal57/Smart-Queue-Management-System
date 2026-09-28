#Smart Queue Management System 
# Python Essentials-Evaluated Course Project

waiting = []
tokens_served = []
next_token_number = 1

def generate_token():
    global next_token_number
#Customer name input
    name=input("customer name: ").strip()

    if name== "":
        print("Ivalid Input.")
        return
# Next token number is assigned to the customer and added to the waiting list
    token = {
        "number": next_token_number,
        "name": name,
        "priority": False
    }

    waiting.append(token)
    print(f"\nToken generated successfully")
    print(f"Token Number: {next_token_number}")
    print(f"Customer: {name}")

    next_token_number += 1
#Generates Priority token for the customer and adds it to the waiting list
def generate_priority_token():
    global next_token_number

    name = input("priority customer name: ").strip()

    if name == "":
        print("Invalid Input")
        return

    token = {
        "number": next_token_number,
        "name": name,
        "priority": True
    }

    waiting.insert(0, token)

    print("\nPriority token generated successfully")
    print(f"Token Number: {next_token_number}")
    print(f"Customer: {name}")

    next_token_number += 1

# Displays the current queue of customers waiting to be served, including their token numbers, names, and priority status
def display_queue():
    if len(waiting) == 0:
        print("\nempty.")
        return

    print("\n----------- CURRENT QUEUE ------------")

    for token in waiting:
        if token["priority"]:
            status = "PRIORITY"
        else:
            status = "NORMAL"

        print(
            f"Token: {token['number']} | "
            f"Name: {token['name']} | "
            f"Type: {status}"
        )

    print("--------------------------------------")

# Serves the next customer in the queue by removing their token from the waiting list and adding it to the served list. It also displays the token number and customer name of the served customer.
def serve_next_customer():
    if len(waiting) == 0:
        print("\nNo customers")
        return

    token = waiting.pop(0)
    tokens_served.append(token)

    print("\n========== NOW SERVING ==========")
    print(f"Token Number: {token['number']}")
    print(f"Customer: {token['name']}")
    print("=================================")

# Searches for a token in the waiting list and served list based on the token number provided by the user. If the token is found, it displays the token details; otherwise, it informs the user that the token was not found.
def search_token():
    try:
        number = int(input("Enter token number"))
    except ValueError:
        print("enter a valid number.")
        return

    for token in waiting:
        if token["number"] == number:
            print("\nToken found")
            print(f"Token Number: {token['number']}")
            print(f"Customer: {token['name']}")

            if token["priority"]:
                print("Type: Priority")
            else:
                print("Type: Normal")

            return

    for token in tokens_served:
        if token["number"] == number:
            print("\nThis token is alredy registered")
            print(f"Customer: {token['name']}")
            return

    print("\nToken not found.")

# Your previous funnction ends here
def cancel_token():
    if len(waiting) == 0:
        print("\nno customers")
        return

    try:
        number = int(input("Enter token number to cancel: "))
    except ValueError:
        print("enter a valid token number.")
        return

    for token in waiting:
        if token["number"] == number:
            waiting.remove(token)
            print(f"\nToken {number} has been cancelled successfully.")
            print(f"Customer: {token['name']}")
            return

    print(f"\nToken {number} was not found")


# Shows statistics about the queue, including the total number of tokens generated, the number of customers waiting, the number of customers served, and an estimated waiting time based on the number of customers waiting.
def show_statistics():
    total = len(waiting) + len(tokens_served)
    waiting = len(waiting)
    served = len(tokens_served)

    print("\n--------------- QUEUE STATISTICS --------------")
    print(f"Total tokens generated : {total}")
    print(f"Customers waiting      : {waiting}")
    print(f"Customers served       : {served}")

    if waiting > 0:
        estimated_wait = waiting * 5
        print(f"Estimated waiting time : {estimated_wait} minutes")
    else:
        print("Estimated waiting time : 0 minutes")

    print("----------------------------------------------------")

# Display the main menu and handle user input to perform various actions related to the queue management system. The menu provides options for generating tokens, displaying the queue, serving customers, searching for tokens, showing statistics, and exiting the program.
def main():
    while True:
        print("\n")
        print("--------------------------------------")
        print("       SMART QUEUE MANAGEMENT")
        print("--------------------------------------")
        print("1. Generate Normal Token")
        print("2. Generate Priority Token")
        print("3. Display Queue")
        print("4. Serve Next Customer")
        print("5. Search Token")
        print("6. Show Statistics")
        print("7. Exit")
        print("--------------------------------------")

        choice = input("Enter Input: ")

        if choice == "1":
            generate_token()

        elif choice == "2":
            generate_priority_token()

        elif choice == "3":
            display_queue()

        elif choice == "4":
            serve_next_customer()

        elif choice == "5":
            search_token()

        elif choice == "6":
            show_statistics()

        elif choice == "7":
            print("\nThank you for using Smart Queue Management System!")
            break

        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main()