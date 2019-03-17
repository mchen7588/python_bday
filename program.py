import datetime


def header():
    print('------------------------')
    print('----------bday----------')
    print('------------------------')


def get_bday():
    print('bday??')
    year = int(input('year [YYYY]: '))
    month = int(input('month [MM]: '))
    day = int(input('day [DD]: '))

    return datetime.date(year, month, day)


def calculate_days(bday, today):
    this_year_bday = datetime.date(year=today.year, month=bday.month, day=bday.day)

    return (this_year_bday - today).days


def print_bday_info(days):
    if days < 0:
        print('{} days ago'.format(-days))
    elif days > 0:
        print('{} days to go'.format(days))
    else:
        print('happy bday!!!')


def main():
    header()
    bday = get_bday()
    today = datetime.date.today()
    days = calculate_days(bday, today)
    print_bday_info(days)


main()
