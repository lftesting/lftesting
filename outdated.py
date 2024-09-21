months = {"January":"1",
          "February":"2",
          "March":"3",
          "April":"4",
          "May":"5",
          "June":"6",
          "July":"7",
          "August":"8",
          "September":"9",
          "October":"10",
          "November":"11",
          "December":"12"
          }
while True:
    date = input("Date: ").strip()
    try:
        if "/" in date:
            month, day, year = date.split("/")
            month = int(month)
            day = int(day)
            year = int(year)
        elif "," in date:
            name_month, day_year = date.split(" ",1)
            day, year = day_year.split(",")
            name_month = name_month.strip()
            day = int(day.strip())
            year = int(year.strip())
            if name_month in months:
                    month = int(months[name_month])
            else:
                 continue
                
        else:
            continue
        if 1 <= month <= 12 and 1 <= day <= 31:
            print(f"{year:04}-{month:02}-{day:02}")
            break
    except (ValueError, KeyError):
        continue