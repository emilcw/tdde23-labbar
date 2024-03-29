# =========================================================================
#  The Calendar - Functional and imperative programming in Python
#
#  Modul: booking.py
#  Updated: 2004-07-30 av Peter Dalenius
#  	Translated to Python 2012 by Peter L-G
#	Translated to English 2013 by Anders M.L.
#
#  Dependencies:
#    calendar_abstraction.py
# =========================================================================

# This module contains lower-level calculations and functions for booking
# appointments, finding unallocated time etc. Functions here never
# operate directly on Python objects, but rather go through the primitives
# and functions provided in calendar_abstraction.

from calendar_abstraction import *

# =========================================================================
#  1. Identifying calendar contents
# =========================================================================
# Check if any meeting in the provided calendar day collides with the
# proposed time span.
def is_booked(cal_day, ts):
    "calendar_day x time span -> Bool"
    return some_meeting_satisfies(
        cal_day,
        lambda app: are_overlapping(ts, get_span(app)))

# Does any appointment that given day start at a specific time?
def is_booked_from(cal_day, t):
    "calendar_day x time -> Bool"
    return some_meeting_satisfies(
       cal_day,
       lambda app: is_same_time(t, start_time(get_span(app))))

# =========================================================================
#  2. Making and removing appointments
# =========================================================================
# Adds a new appointment by taking apart a calendar year, inserting the
# appointment into the correct calendar day, and then putting it back together.

# This function does not modify any structures, but rather builds a new one.
# The new calendar year generated by book_appointment is used to replace the
# old one. This replacement is done by the function book (calendar.py) which
# invokes book_appointment.

def book_appointment(cal_year, day, mon, start, end, subject):
    "calendar_year x day x month x time x time x subject -> calendar_year"
    cal_day = calendar_day(day, calendar_month(mon, cal_year))
    app = new_appointment(new_time_span(start, end), subject)
    return insert_calendar_month(
               mon,
               insert_calendar_day(
                   day,
                   insert_appointment(app, cal_day),
                   calendar_month(mon, cal_year)),
               cal_year)


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


def free_spans(cal_year, day, mon, start, end):
        cal_day = calendar_day(day, calendar_month(mon, cal_year))
        return insert_calendar_month(
                   mon,
                   insert_calendar_day(
                       day,
                       show_free_spans(cal_day, start, end),
                       calendar_month(mon, cal_year)),
                   cal_year)
