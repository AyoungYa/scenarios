import datetime


def date_flip(date_str: str) -> str:
    """Flip the day and month of a date string.

    Args:
        date_str (_type_): like "2020-10-01"

    Returns:
        _type_: like "01-10-2020"
    """
    date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d")
    new_date_str = date_obj.strftime("%d-%m-%Y")
    return new_date_str
