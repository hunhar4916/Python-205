from datetime import datetime

print("hunhar4916 - Spreadsheet Automation Menu")
print("It's just a flesh wound!!")

def menu_options():
    options = [
        "1. input data",
        "2. Current data",
        "3. Generate report",
        "0. Exit program"
    ]
    print("\n--Menu--")
    for option in options:
        print(option)
        
def input_data():
    print("inputing data... (feature coming soon)")
    

def current_data():
    print("viewing current data... (feature coming soon")
    

def generate_report():
    print("generating report... (feature coming soon)")
    

def exit_program():
    print("Goodbye!")
    


while True:
    menu_options()
    #The next line retrieves the inputted option and stores into the
    #variable called choice.
    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        input_data()
    elif choice == "2":
        current_data()
    elif choice == "3":
        generate_report()
    elif choice == "0":
        exit_program()
        break
    else:
        print("Invalid choice, please choose from options listed.")
        continue

    print("You selected option", choice, "-", str(datetime.now()))
    











    
    
