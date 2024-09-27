from datetime import datetime, timedelta

def display_current_datetime():
    
    current_date = datetime.now()
    
    # Format and display the date and time in "YYYY-MM-DD HH:MM:SS"
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")

# Part 2: Calculate a Future Date
def calculate_future_date():
    try:
       
        days_to_add = int(input("Enter the number of days to add to the current date: "))
        
        # Calculate the future date
        future_date = datetime.now() + timedelta(days=days_to_add)
        
        # Format and display the future date in "YYYY-MM-DD"
        formatted_future_date = future_date.strftime("%Y-%m-%d")
        print(f"Future date: {formatted_future_date}")
    
    except ValueError:
        print("Invalid input. Please enter an integer value for the number of days.")

# Main execution
if __name__ == "__main__":
    # Display the current date and time
    display_current_datetime()
    
    # Calculate and display the future date
    calculate_future_date()
