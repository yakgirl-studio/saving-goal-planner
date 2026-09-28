    # Saving Goal Planner
def goal_set():
    # Ask the user for the savings goal
    goal = float(input("Enter your savings goal: "))

    # Variable to store the total savings per year
    total_yearly_savings = 0

    while True:

        # Ask for the name of the savings source
        source = input("Enter the name of your savings source: ")

        # Ask for the amount saved each time
        amount = float(input("Enter the amount saved each time: "))

        # Ask how many times the saving is made per year
        times = int(input("How many times do you make this saving in a year? "))

        # Calculate the yearly saving from this source
        yearly_saving = amount * times

        # Add it to the total yearly savings
        total_yearly_savings = total_yearly_savings + yearly_saving

        # Ask if the user wants to add another savings source
        another = input("Do you want to add another savings source? (yes/no): ")

        if another.lower() == "no":
            break

    # Calculate the number of years needed
    years = goal / total_yearly_savings

    # Convert the answer to an integer
    years = int(years)

    # Display the result
    print("Your total savings per year is:", total_yearly_savings)
    print("It will take you", years, "years to reach your savings goal.")

    print("Do you want to set another goal?   press (1) for yes , press(2) for no")
    get_response=int(input())

    if  get_response == 1:
        goal_set()
    elif  get_response == 2:
        quit()
    else:
        print("Invalid Input")

goal_set()
