"""""Omimplementerade funktioner till lab 8A"""

def start_time(ts):
    "span -> time"
    if is_time_span(ts):
        return strip_tag(ts)[0]

def end_time(ts):
    "span -> time"
    if is_time_span(ts):
        return strip_tag(ts)[1]

def overlap(ts1,ts2):
    "span x span -> span"
    if are_overlapping(ts1,ts2):
        min1 = latest_time(start_time(ts2), start_time(ts1))
        min2 = earliest_time(end_time(ts2), end_time(ts1))
        hour1 = strip_tag(get_hour(min1))
        hour2 = strip_tag(get_hour(min2))
        minute1 = strip_tag(get_minute(min1))
        minute2 = strip_tag(get_minute(min2))
        print ("hour1",hour1)
        print ("hour2", minute1)
        return ('span', (('time', (('hour', hour1), ('minute', minute1))), \
            ('time', (('hour', hour2), ('minute', minute2)))))


def new_duration(hour, minute):
    "hour x minute -> duration"
    if is_hour(hour) and is_minute(minute):
        return ('duration', (('hour', hour[1] + minute[1] // 60), ('minute', minute[1] % 60)))


def length_of_span(ts):
    "span -> duration"
    duration = (strip_tag(strip_tag(end_time(ts))[0]) - \
    strip_tag(strip_tag(start_time(ts))[0]),strip_tag(strip_tag(end_time(ts))[1]) - \
    strip_tag(strip_tag(start_time(ts))[1]))
    mins = duration[0]*60 + duration[1]
    return ('duration', (('hour', mins//60), ('minute', mins%60)))
