"""Implentation av time spans lab 8B"""

# --- Primitiva funktioner till time spans ---
def new_time_spans():
    "-> time_spans"
    return attach_tag("time_spans",[])


def is_time_spans(object):
    "Python-object -> Bool"
    return get_tag(object) == 'time_spans'


def is_empty_time_spans(ts):
    "time_spans -> Bool"
    ensure(ts,is_time_spans)
    return not strip_tag(ts)


def insert_span(ts,time_spans):
    "time_span x time_spans -> time_spans"

    def add_time_span(tl, ts):
        if not tl or precedes(start_time(ts),
                              start_time(tl[0])):

            return [ts] + tl
        else:

            return [tl[0]] + add_time_span(tl[1:], ts)

    ensure(ts, is_time_span)
    ensure(time_spans, is_time_spans)

    return attach_tag('time_spans', add_time_span(strip_tag(time_spans),ts))


def first_time_span(time_spans):
    "time_spans -> time_span"
    ensure(time_spans,is_time_spans)
    if is_empty_time_spans(time_spans):
        raise Exception('Empty time spans.')
    else:
        return strip_tag(time_spans)[0]


def rest_time_spans(time_spans):
    "time_spans -> time_spans"
    ensure(time_spans, is_time_spans)
    if is_empty_time_spans(time_spans):
        return time_spans
    else:
        return attach_tag('time_spans',strip_tag(time_spans)[1:])

# --- Utskriftsfunktion ---
def show_time_spans(time_spans):
    "time_spans -> free_spans"

    def show_time_span(span):
        show_span(span)
        print()
    if is_empty_time_spans(time_spans):
        print("No free time available")
    else:
        for_each_time_span(time_spans, show_time_span)
