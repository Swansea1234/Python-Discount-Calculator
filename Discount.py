# --- Discount.py ---

def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount.
    
    The discount is applied only if it is 20% or higher.

    Args:
        price (float): The original price of the item.
        discount_percent (float): The discount percentage (e.g., 20 for 20%).

    Returns:
        float: The final price after the discount, or the original price if no discount was applied.
    """
    # Check if the discount percentage is 20 or greater
    if discount_percent >= 20:
        # If the condition is met, calculate the discount amount
        discount_amount = price * (discount_percent / 100)
        # Subtract the discount amount from the original price to get the final price
        final_price = price - discount_amount
        # Return the discounted price
        return final_price
    else:
        # If the condition is not met, return the original price without any changes
        return price
