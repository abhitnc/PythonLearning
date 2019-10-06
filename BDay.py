from datetime import timedelta, time, datetime, date
def main():
    today=date.today()
    bday=date(today.year,5,26)

    if bday<today:
        print("Bday already went by %d days ago" %((today-bday).days))
        bday=bday.replace(year=today.year+1)

    time_to_bday=bday-today
    print("It's just ",time_to_bday.days,"Days until next bday")

main()
