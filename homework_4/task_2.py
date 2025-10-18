from random import sample

def get_numbers_ticket(min, max, quantity):
    """
    Generates a sorted list of unique random numbers for a lottery ticket.

    This function validates the input parameters to ensure they are within the
    lotterys rules (min >= 1, max <= 1000, and quantity is a valid number
    to choose from the range).

    Args:
        min (int): The minimum possible number (must be at least 1).
        max (int): The maximum possible number (must be at most 1000).
        quantity (int): The number of unique numbers to generate.

    Returns:
        list: An ordered list of unique random numbers.
              Returns an empty list if the input parameters are invalid.
    """
    is_min_valid = min > 0 and min < max
    is_max_valid = max <= 1000 and max > min
    is_quantity_valid = quantity <= (max - min + 1) and quantity > 0

    valid = is_min_valid and is_max_valid and is_quantity_valid 

    if not valid :
        return []

    numbers = sample(range(min, max + 1), quantity)
    
    return sorted(numbers)

print(get_numbers_ticket(50, 49, 6))
print(get_numbers_ticket(1, 49, 6))