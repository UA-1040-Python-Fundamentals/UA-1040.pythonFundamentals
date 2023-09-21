def get_day_of_week(number):
    days = ["понеділок", "вівторок", "середа", "четвер", "п'ятниця", "субота", "неділя"]
    if number < 1 or number > 7:
        raise ValueError("Неправильний номер дня тижня")
    return days[number - 1]

try:
    number = int(input("Введіть номер дня тижня (1-7): "))
    day = get_day_of_week(number)
    print(f"Це {day}")
except ValueError as e:
    print(e)
except KeyboardInterrupt:
    print("Ви вийшли з програми")



