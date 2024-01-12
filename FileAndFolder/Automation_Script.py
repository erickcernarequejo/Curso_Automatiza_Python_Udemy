import calendar
from pathlib import Path

monthYear = list(calendar.month_name[1:])
dayWeek = ['Day 1', 'Day 10', 'Day 20', 'Day 30']

for i, month in enumerate(monthYear):
    for day in dayWeek:
        Path(f'2024/{i+1}.{month}/{day}').mkdir(parents=True, exist_ok=True)