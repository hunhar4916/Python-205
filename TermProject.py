from datetime import datetime

print("hunhar4916 - Spreadsheet Automation Menu")
print("It's just a flesh wound!!")

def menu_options():
    print("\n--MENU--")
    print("1, Input Data")
    print("2, View Currect Data")
    print("3, Generate Report")
    print("0, Exit")

def input_data():
    print("You selected input data")
    print("You made your choice on ",str(datetime.now()))

def current_data():
    print("You selected view current data")
    print("You made your choice on ",str(datetime.now()))

def generate_report():
    print("You selected generate report")
    print("You made your choice on ",str(datetime.now()))

def exit_pro():
    print("Goodbye!")
    print("You made your choice on ",str(datetime.now()))


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
        exit_pro()
        break
    else:
        print("Invalid choice, please choose from options listed.")













    
    
