from calendar import *

"""Implementation av show_free och hjälpfunktioner till lab8D. Körexempel
    finns i lab8D_test.py. Vidare """


def show_free(cal_name, d, m , t1, t2):
    "String x Integer x String x String x String ->"
    day = new_day(d)
    mon = new_month(m)
    start = convert_time(t1)
    end = convert_time(t2)
    cal_day = calendar_day(day, calendar_month(mon,(fetch_calendar(cal_name))))

    show_time_spans(free_spans(cal_day,start,end))


def show_time_spans(time_spans):
    "time_spans -> free_spans"

    def show_time_span(span):
        show_span(span)
        print()
    if is_empty_time_spans(time_spans):
        print("No free time available")
    else:
        for_each_time_span(time_spans, show_time_span)


def free_spans(cal_day,start, end):
    "calendar_day x time x time -> free_spans"

    span = new_time_span(start,end)


    def locate_spans(cal_day,span):
        if is_empty_calendar_day(cal_day):
            return [span]

        if are_overlapping(get_span(first_appointment(cal_day)),span):

            start_time2 = start_time(get_span(first_appointment(cal_day)))
            endtime = end_time(get_span(first_appointment(cal_day)))

            if is_same_time(endtime, end_time(span)) and is_same_time(start_time(span),start_time2):
                return []

            if is_same_time(endtime, end_time(span)) and precedes(start_time2,start_time(span)):
                return []

            if is_same_time(endtime,end_time(span)):
                return [new_time_span(start_time(span), start_time2)]

            if precedes(end_time(span, endtime)):
                if precedes(start_time2,start_time(span)):
                    return []

                elif is_same_time(start_time2, start_time(span)):
                    return []

                else:
                    return [new_time_span(start_time(span),start_time2)]

            upd_time_span = new_time_span(endtime,end_time(span))
            spans = locate_spans(rest_calendar_day(cal_day),upd_time_span)

            if is_same_time(start_time2,start_time(span)):
                return spans

            if precedes(start_time2, start_time(span)):
                return spans

            if precedes(endtime,end_time(span)) and precedes(start_time2,start_time(span)):
                return spans

            else:
                return [new_time_span(start_time(span),start_time2)] + spans

        else:
            return locate_spans(rest_calendar_day(cal_day),span)

    ensure(start,is_time)
    ensure(end,is_time)
    ensure(cal_day,is_calendar_day)

    return attach_tag('time_spans',(locate_spans(cal_day,span)))


def for_each_time_span(time_spans,time_span_fn):
    "time_spans x (time_span ->) -> "
    if not is_empty_time_spans(time_spans):
        time_span_fn(first_span(time_spans))
        for_each_time_span(rest_time_spans(time_spans),time_span_fn)
