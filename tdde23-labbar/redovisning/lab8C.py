

"""Implementation av remove-funktion i lab8C, körexempel ligger i lab8C_test och
    förklaringar till hur funktionen fungerar ligger i Forklara8C.txt. Var
    Samtliga funktioner hör hemma finns angiver ovanför funktionen"""


    #Denna funktion hör hemma i calendar.py
def remove(cal_name, d, m, t1):
    "String x Integer x String x String"
    day = new_day(d)
    mon = new_month(m)
    start = convert_time(t1)
    cal_day = calendar_day(day, calendar_month(mon, fetch_calendar(cal_name)))

    new_date(day,mon)

    if is_booked_from(cal_day, start):
        insert_calendar(cal_name, remove_appointment(fetch_calendar(cal_name),
                                                    day, mon, start))
        print("The appointment has been removed")
    else:
        print("This person is not booked here")

    #Denna funktion hör hemma i booking.py
def remove_appointment(cal_year, day, mon , start):
    "calendar_year x day x month x time -> calendar_year"
    cal_day = calendar_day(day, calendar_month(mon, cal_year))
    return insert_calendar_month(
               mon,
               insert_calendar_day(
                   day,
                   delete_appointment(cal_day, start),
                   calendar_month(mon, cal_year)),
               cal_year)

   #Denna funktion hör hemma i calendar_abstraction.py
def delete_appointment(cal_day, start):
    "calendar_day x time -> calendar_day"

    def del_app(al,start):

        if is_same_time(start, start_time(get_span(al[0]))):
            return al[1:]
        else:
            return [al[0]] + del_app(al[1:],start)

    ensure(start,is_time)
    ensure(cal_day, is_calendar_day)

    return attach_tag('calendar_day', del_app(strip_tag(cal_day), start))
