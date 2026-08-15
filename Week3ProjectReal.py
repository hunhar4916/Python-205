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


def convertData(data):
    """
    convertData(data): takes one numerical argument (data), the
    temperature in Fahrenheit, and returns it converted to Celsius
    using (F - 32) * 5/9. Returns a float.
    """
    return (data - 32) * 5 / 9


def getInput():
    num_entries = int(input("How many entries are you inputting? "))

    for i in range(num_entries):
        entry_date = input("\nEnter a date: ")
        print()
        highest_temp = float(input("Enter the highest temp for the inputted date: "))

        # Calling convertData(highest_temp): passes the Fahrenheit value
        # to be converted; returns the converted Celsius value (float)
        converted_value = convertData(highest_temp)

        print(f"The following was saved at {datetime.now()} :")
        print(f"{entry_date},{highest_temp},{converted_value}")


def current_data():
    print("viewing current data... (feature coming soon)")


def generate_report():
    print("generating report... (feature coming soon)")


def exit_program():
    print("Goodbye!")


while True:
    menu_options()
    # The next line retrieves the inputted option and stores into the
    # variable called choice.
    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        print(f"You selected {choice} at {datetime.now()}")
        getInput()
    else:
        print("Error: The chosen functionality is not implemented yet")
