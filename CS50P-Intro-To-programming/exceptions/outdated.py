months=[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
while True:
    try:
        date=input('Date: ').strip().title()
        if '/' in date:
            date=date.split('/')
            month,day,year=int(date[0]),int(date[1]),int(date[2])
            if month>12 or day>31:
                continue
            print(f'{year}-{month:02}-{day:02}')
            break
        elif ',' in date:
            date=date.split(' ')
            month, day, year=str(date[0]),str(date[1]),int(date[2])
            day=day.replace(',','')
            if month in months:
                month=months.index(month)
                month=month+1
                month,day,year=int(month),int(day),int(year)
                if month>12 or day>31:
                    continue
                print(f'{year}-{month:02}-{day:02}')
                break
    except ValueError:
        continue
