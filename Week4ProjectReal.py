from datetime import datetime

print("hunhar4916 - Spreadsheet Automation Menu")
print("It's just a flesh wound!!")


def menu_options():
    """
    menu_options(): prints the main menu options available to the user.
    """
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


def insertData(path, data):
    """
    insertData(path, data): takes a path to a csv file and a comma-separated
    string of data. Opens the file with append permissions (creating the
    file first if it does not already exist) and writes the data as a new
    line. A try-except statement catches any errors that occur while
    writing; if an error occurs, it is reported and re-raised so the
    caller can respond accordingly.
    """
    try:
        with open(path, "a") as file:
            file.write(data + "\n")
    except Exception as e:
        print(f"Error writing to file {path}: {e}")
        raise


def viewData(path):
    """
    viewData(path): takes a path to a csv file, opens it using the minimal
    permissions needed to read (read-only mode), and displays the path of
    the file being read along with its full contents. A try-except
    statement catches any errors that occur while reading, such as the
    file not existing.
    """
    try:
        with open(path, "r") as file:
            print(f"\nReading data from: {path}")
            print(file.read())
    except Exception as e:
        print(f"Error reading file {path}: {e}")


def getInput():
    """
    getInput(): prompts the user for the number of entries to input, then
    for each entry collects a date and a highest Fahrenheit temperature,
    converts the temperature to Celsius via convertData, and attempts to
    save the entry to ZooData.csv using insertData. A try-except statement
    wraps the save so that, on a successful write, a confirmation message
    is displayed showing the current date/time and the data saved; on
    failure, an error message is displayed instead.
    """
    num_entries = int(input("How many entries are you inputting? "))
    for i in range(num_entries):
        entry_date = input("\nEnter a date: ")
        print()
        highest_temp = float(input("Enter the highest temp for the inputted date: "))
        # Calling convertData(highest_temp): passes the Fahrenheit value
        # to be converted; returns the converted Celsius value (float)
        converted_value = convertData(highest_temp)
        data = f"{entry_date},{highest_temp},{converted_value}"

        try:
            insertData("ZooData.csv", data)
            print(f"The following data was saved at {datetime.now()}: {data}.")
        except Exception as e:
            print(f"Failed to save entry: {e}")


def current_data():
    """
    current_data(): placeholder for viewing current data (superseded by
    the viewData function, which is now called directly from the menu).
    """
    print("viewing current data... (feature coming soon)")


def generate_report():
    """
    generate_report(): placeholder for generating a report (feature not
    yet implemented).
    """
    print("generating report... (feature coming soon)")


def exit_program():
    """
    exit_program(): prints a farewell message when the user exits the
    program.
    """
    print("Goodbye!")


while True:
    menu_options()
    # The next line retrieves the inputted option and stores into the
    # variable called choice.
    choice = input("Enter your choice (1-3): ")
    if choice == "1":
        print(f"You selected {choice} at {datetime.now()}")
        getInput()
    elif choice == "2":
        print(f"You selected {choice} at {datetime.now()}")
        viewData("ZooData.csv")
    else:
        print("Error: The chosen functionality is not implemented yet")
