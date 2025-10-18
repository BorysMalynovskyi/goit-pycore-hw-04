import re

import re

def normalize_phone(phone_number: str) -> str:
    """
    Normalizes a phone number to the standard '+38...' Ukrainian format.

    This function first extracts all digits from the string and then
    correctly applies the '+38' international prefix.

    Args:
        phone_number: The input phone number string in various formats.

    Returns:
        A normalized phone number string in the Ukrainian format '+38XXXXXXXXXX'.
    """
    digits = re.sub(r'\D', '', phone_number)
    
    return '+' + digits if digits.startswith('380') else '+38' + digits
    
raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900+",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Normalized phone numbers for SMS campaign:", sanitized_numbers)
