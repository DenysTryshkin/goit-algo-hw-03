from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    today = datetime.today().date()

    greetings = []

    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = birthday.replace(year=today.year)
        
        if birthday_this_year < today:
            birthday_this_year = birthday.replace(year=today.year + 1)

        days_until_birthday = (birthday_this_year - today).days
        
        while birthday_this_year.weekday() <= 5:
            birthday_this_year += timedelta(days=1)
        
        if 0 <= days_until_birthday <= 7:
            greetings.append({"name": user["name"], "greeting_date": birthday_this_year})
    
    return greetings



users = [
    {"name": "John Doe", "birthday": "1985.04.24"},
    {"name": "Jane Smith", "birthday": "1990.05.24"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
