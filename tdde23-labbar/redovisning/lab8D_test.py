from calendar import *

def test_8D():
        cal_name = "result"
        day = 22
        month = 'sep'
        start = "11:00"
        end = "13:00"
        subject = "drink beer"
        create(cal_name)
        book(cal_name,day,month,start,end,subject)

        test_range_start = "08:00"
        test_range_end = "16:00"
        result = show_free(cal_name,day,month,test_range_start,test_range_end)

        print()

        span1 = ('span',(('time',(('hour', 8), ('minute', 0))), ('time',(('hour', 11), ('minute', 0)))))
        span2 = ('span',(('time',(('hour', 13), ('minute', 0))), ('time',(('hour', 16), ('minute', 0)))))
        time_spans = ('time_spans', [span1,span2])
        wanted = show_time_spans(time_spans)
        assert(result == wanted)
        print("Passed the test")
