from datetime import datetime, timedelta

def get_upcoming_birthdays(users: list) -> list:
    """
    Determines which colleagues have birthdays in the next 7 days and adjusts
    the congratulation date if the birthday falls on a weekend.

    Args:
        users: A list of dictionaries, where each dictionary contains a user's
               name and birthday.
               Format: [{'name': 'John Doe', 'birthday': '1985.01.23'}, ...]

    Returns:
        A list of dictionaries containing the names of users to be congratulated
        and their corresponding congratulation dates.
        Format: [{'name': 'Jane Smith', 'congratulation_date': '2025.10.20'}]
    """
    today = datetime.today().date()
    upcoming_birthdays = []

    for user in users:
        birthday_date = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        
        birthday_this_year = birthday_date.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        delta_days = (birthday_this_year - today).days

        is_upcoming_birthday = delta_days >= 0 and delta_days < 7

        if is_upcoming_birthday:
            congratulation_date = birthday_this_year
            
            if congratulation_date.weekday() >= 5:
                days_to_monday = 7 - congratulation_date.weekday()
                congratulation_date += timedelta(days=days_to_monday)

            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
            })
            
    return upcoming_birthdays

users = [
    {"name": "John Doe", "birthday": "1985.10.14"},
    {"name": "Jane Smith", "birthday": "1990.10.18"}
]

upcoming_birthdays = get_upcoming_birthdays(users)

print("Congradulations list for the current week:", upcoming_birthdays)
