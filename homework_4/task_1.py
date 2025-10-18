from datetime import datetime

def get_days_from_today(date: str) -> int | None:
    """
    This function takes a date string in the format 'YYYY-MM-DD' and returns the number of days from today to that date.
    If the input date is invalid, it returns None.

    :param date: A string representing a date in 'YYYY-MM-DD' format.
    :return: An integer representing the number of days from today to the given date, or None if the input is invalid.
    :raises TypeError: If parameters are not the correct type.
    """
    try:
        today = datetime.today()
        requestedDate = datetime.strptime(date, '%Y-%m-%d')

        return (today - requestedDate).days
    
    except ValueError:
        return None
    
print(get_days_from_today("2020-10-09=wrong"))
print(get_days_from_today("2020-10-09"))