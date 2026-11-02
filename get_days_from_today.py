from datetime import datetime


def get_days_from_today(date):
    try:
        given_date = datetime.strptime(date, "%Y-%m-%d").date()
        today = datetime.today().date()

        return (today - given_date).days

    except (ValueError, TypeError):
        return None


print("Перевірка першого завдання:")

print(get_days_from_today("2020-10-09"))
print(get_days_from_today("2026-12-25"))
print(get_days_from_today("2026-11-01"))
print(get_days_from_today("неправильна дата"))
print(get_days_from_today("2025-02-30"))
