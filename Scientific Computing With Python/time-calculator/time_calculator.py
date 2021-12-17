day_map = {
    "Monday": 0,
    "Tuesday": 1,
    "Wednesday": 2,
    "Thursday": 3,
    "Friday": 4,
    "Saturday": 5,
    "Sunday": 6,
}

week_days = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",  
    6: "Sunday",
}


def add_time(start, duration, day=""):
    [hour, minute] = parse_time(start)
    [ahour, am] = parse_duration(duration)
    minute += am
    hour += ahour
    if minute > 60:
        minute %= 60
        hour += 1
    indicator = "AM"

    n = hour // 24
    if hour > 24:
        hour %= 24

    if hour > 12:
        hour %= 12
        indicator = "PM"

    if hour == 12:
        indicator = "PM"

    if hour == 0:
        hour = 12
        indicator = "AM"

    if day == "":
        if n == 0:
            return "{}:{:02d} {}".format(hour, minute, indicator)
        if n == 1:
            return "{}:{:02d} {} (next day)".format(hour, minute, indicator)

        return "{}:{:02d} {} ({} days later)".format(hour, minute, indicator, n)
    else:
        day = day.lower()
        day = day[0].upper() + day[1:]
        end_day = week_days[(day_map[day] + n) % 7]
        if n == 0:
            return "{}:{:02d} {}, {}".format(hour, minute, indicator, end_day)
        if n == 1:
            return "{}:{:02d} {}, {} (next day)".format(hour, minute, indicator, end_day)

        return "{}:{:02d} {}, {} ({} days later)".format(hour, minute, indicator, end_day, n)


def parse_time(t):
    [hourminute, am] = t.split()
    [hour, minute] = parse_duration(hourminute)
    if am != 'AM':
        hour += 12
    return [hour, minute]


def parse_duration(d):
    return map(lambda s: int(s), d.split(":"))