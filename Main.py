import csv  # Importing the csv module to read and write CSV files

# Global list to store all expense records
expenses = []
# Variable to store the user's monthly budget
monthly_budget = 0.0

# Function to add a new expense
def add_expense():
    # Prompt the user for the date of the expense
    date = input("Enter the date (YYYY-MM-DD): ")
    # Ask for the category of the expense, such as Food or Travel
    category = input("Enter the category (e.g., Food, Travel): ")
    # Ask for the amount spent
    amount = float(input("Enter the amount spent: "))
    # Ask for a brief description of the expense
    description = input("Enter a brief description: ")
    
    # Create a dictionary to hold all details of this expense
    expense = {
        'date': date,
        'category': category,
        'amount': amount,
        'description': description
    }
    # Append the expense dictionary to the list of expenses
    expenses.append(expense)
    print("Expense added successfully.")

# Function to view all recorded expenses
def view_expenses():
    # Print the table headers
    print("Date\t\tCategory\tAmount\tDescription")
    print("-" * 50)
    # Loop through each expense in the expenses list
    for expense in expenses:
        # Check that all fields in the expense dictionary have values
        if all(expense.values()):
            # Print each field in the expense in a formatted way
            print(f"{expense['date']}\t{expense['category']}\t${expense['amount']:.2f}\t{expense['description']}")
        else:
            # Message to indicate an incomplete entry
            print("Incomplete entry found. Skipping...")

# Function to set the monthly budget
def set_budget():
    global monthly_budget  # Make sure we're updating the global variable
    monthly_budget = float(input("Enter your monthly budget: "))
    print(f"Budget set to ${monthly_budget:.2f}.")

# Function to track the budget without requiring the user to set it each time
def track_budget():
    if monthly_budget == 0.0:
        print("Budget is not set. Please set the budget first.")
    else:
        # Calculate the total amount spent so far by summing amounts in expenses
        total_spent = sum(expense['amount'] for expense in expenses)
        # Calculate the remaining balance by subtracting total spent from the budget
        remaining_balance = monthly_budget - total_spent
        # Print the total amount spent
        print(f"Total spent: ${total_spent:.2f}")
        # Check if the total spent exceeds the monthly budget
        if total_spent > monthly_budget:
            print("Warning: You have exceeded your budget!")
        else:
            # Show the remaining balance if budget is not exceeded
            print(f"You have ${remaining_balance:.2f} left for the month.")

# Function to save all expenses to a CSV file
def save_expenses():
    # Open 'expenses.csv' in write mode
    with open('expenses.csv', mode='w', newline='') as file:
        # Define the CSV writer with headers for each column
        writer = csv.writer(file)
        writer.writerow(['Date', 'Category', 'Amount', 'Description'])
        # Write each expense as a row in the CSV file
        for expense in expenses:
            writer.writerow([expense['date'], expense['category'], expense['amount'], expense['description']])
    print("Expenses saved to expenses.csv.")

# Function to load expenses from a CSV file at the start of the program
def load_expenses():
    try:
        # Open 'expenses.csv' in read mode
        with open('expenses.csv', mode='r') as file:
            # Read the CSV data into a dictionary format
            reader = csv.DictReader(file)
            # Loop through each row in the CSV file and add it to expenses
            for row in reader:
                expenses.append({
                    'date': row['Date'],
                    'category': row['Category'],
                    'amount': float(row['Amount']),
                    'description': row['Description']
                })
        print("Expenses loaded from expenses.csv.")
    except FileNotFoundError:
        # Message if no saved expenses file is found
        print("No saved expenses found. Starting fresh.")

# Function to display the interactive menu options
def display_menu():
    # Display the options for the expense tracker
    print("\nPersonal Expense Tracker")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Set Budget")
    print("4. Track Budget")
    print("5. Save Expenses")
    print("6. Exit")
    
    # Prompt user for their choice and return it
    choice = input("Enter your choice (1-6): ")
    return choice

# Main function to control the flow of the program
def main():
    # Load expenses from file when the program starts
    load_expenses()
    
    # Loop until the user chooses to exit
    while True:
        # Show the menu and get the user's choice
        choice = display_menu()
        # Call the appropriate function based on the user's choice
        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            set_budget()
        elif choice == '4':
            track_budget()
        elif choice == '5':
            save_expenses()
        elif choice == '6':
            # Save expenses before exiting
            save_expenses()
            print("Exiting the program. Goodbye!")
            break
        else:
            # Message for invalid choices
            print("Invalid choice. Please try again.")

# Run the main function if this file is executed
if __name__ == "__main__":
    main()
