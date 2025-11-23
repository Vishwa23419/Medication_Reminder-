med_list = []

def add_med():
    name = input("Medice name:")
    time = input("Time (HH:MM): ")

    med_list.append([name, time])
    print("\n Medicine added.\n")

def view_med():
    if not med_list:
        print("\nNo medicines added.\n")
        return
    
    print("\n Medice LIst:")
    for m in med_list:
        print(f"- {m[0]} at {m[1]}")
    print()

def check_due():
    now = input("Enter current time (HH:MM:")

    print("\n Status:")
    for m in med_list:
        if now > m[1]:
            print(f"Missed: {m[0]} (was due at) {m[1]}")
        else:
            print(f"Upcoming: {m[0]} (due at {m[1]})")
    print()

def med_menu():
    while True:
        print(".. Medicine Reminder ..")
        print("1. Add Medicine")
        print("2. View Medicines")
        print("3. Check Missed Doses")
        print("4. Back")
        ch = input("Choice: ")

        if ch == "1": add_med()
        elif ch == "2": view_med()
        elif ch == "3": check_due()
        elif ch == "4": break
        else: print("Invalid\n")

med_menu()
