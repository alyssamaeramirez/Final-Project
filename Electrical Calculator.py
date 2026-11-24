
# ==========================================
# ELECTRICAL CALCULATOR
# General kWh Consumption and Bill Estimator
# ==========================================

# Lists for storing appliance information
appliance_names = []
appliance_consumptions = []


# FUNCTION 1: Validate numeric input
def get_valid_number(prompt, minimum, maximum=None):
    while True:
        try:
            number = float(input(prompt))

            if number < minimum:
                print("Invalid input! Value is too low.")

            elif maximum is not None and number > maximum:
                print("Invalid input! Value is too high.")

            else:
                return number

        except ValueError:
            print("Invalid input! Please enter a number.")


# FUNCTION 2: Validate whole number input
def get_valid_integer(prompt, minimum):
    while True:
        number = get_valid_number(prompt, minimum)

        if number.is_integer():
            return int(number)
        else:
            print("Please enter a whole number.")


# FUNCTION 3: Calculate appliance consumption
def calculate_kwh(watts, hours):
    kwh = (watts * hours) / 1000
    return kwh


# FUNCTION 4: Calculate combined daily consumption
def calculate_total(consumption_list):
    total = 0

    for consumption in consumption_list:
        total += consumption

    return total


# FUNCTION 5: Calculate monthly consumption and bill
def calculate_monthly_bill(daily_kwh, rate):
    monthly_kwh = daily_kwh * 30
    bill = monthly_kwh * rate

    return monthly_kwh, bill


# FUNCTION 6: Add appliances
def add_appliances(names, consumptions):
    count = get_valid_integer(
        "\nHow many appliances will you add? ", 1
    )

    for i in range(1, count + 1):
        print("\nAppliance", i)

        name = input("Enter appliance name: ")

        while name.strip() == "":
            print("Appliance name cannot be empty.")
            name = input("Enter appliance name: ")

        watts = get_valid_number(
            "Enter wattage (W): ", 0.01
        )

        hours = get_valid_number(
            "Hours of use per day (0-24): ", 0, 24
        )

        # Calculate consumption and store it in the list
        kwh = calculate_kwh(watts, hours)

        names.append(name)
        consumptions.append(kwh)

        print("Appliance successfully added!")

    return count


# FUNCTION 7: Display appliance names
def display_appliances(names):
    if len(names) == 0:
        print("\nNo appliances recorded yet.")

    else:
        print("\n========== APPLIANCE LIST ==========")

        for i in range(len(names)):
            print(i + 1, ".", names[i])


# ==========================================
# MAIN PROGRAM / MENU
# ==========================================

while True:

    print("\n================================")
    print("       ELECTRICAL CALCULATOR")
    print("================================")
    print("1. Add Appliances")
    print("2. Calculate Total Consumption and Bill")
    print("3. View Appliance List")
    print("4. Exit")
    print("================================")

    choice = input("Enter your choice: ")

    if choice == "1":
        added = add_appliances(
            appliance_names,
            appliance_consumptions
        )
        print("\nTotal appliances added:", added)

    elif choice == "2":

        if len(appliance_names) == 0:
            print("\nPlease add appliances first.")

        else:
            # Get the combined daily consumption
            daily_total = calculate_total(
                appliance_consumptions
            )

            rate = get_valid_number(
                "\nEnter electricity rate per kWh (PHP): ",
                0
            )

            monthly_kwh, bill = calculate_monthly_bill(
                daily_total, rate
            )

            print("\n====== ELECTRICITY BILL SUMMARY ======")
            print("Number of Appliances:", len(appliance_names))
            print("Total Daily Consumption:",
                  round(daily_total, 3), "kWh")
            print("Monthly Consumption:",
                  round(monthly_kwh, 3), "kWh")
            print("Electricity Rate: PHP", round(rate, 2))
            print("Estimated Monthly Bill: PHP",
                  round(bill, 2))

    elif choice == "3":
        display_appliances(appliance_names)

    elif choice == "4":
        print("\nThank you for using Electrical Calculator!")
        break

    else:
        print("\nInvalid choice! Please select 1-4.")
