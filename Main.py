# --- Main.py ---

# Import the calculate_discount function from the discounts.py file.
# This allows us to use the function in this script.
from Discount import calculate_discount

def main():
    """
    Main function to get user input and run the calculation.
    """
    try:
        # Prompt the user to enter the original price.
        # Use float() to convert the input string to a number that can have decimals.
        original_price = float(input("Enter the original price: "))

        # Prompt the user for the discount percentage.
        discount_percentage = float(input("Enter the discount percentage: "))

        # Call the calculate_discount function imported from discounts.py.
        # This will return the final price based on the discount rules.
        final_price = calculate_discount(original_price, discount_percentage)

        # Print the final result, formatted to two decimal places for currency.
        print(f"The final price is: ${final_price:.2f}")

    except ValueError:
        # This part of the code handles potential errors, such as the user entering text instead of a number.
        print("Invalid input. Please enter a valid number for price and discount.")

# The if __name__ == "__main__": block ensures that the main() function is called
# only when this script is run directly.
if __name__ == "__main__":
    main()