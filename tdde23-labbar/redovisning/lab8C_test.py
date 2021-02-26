from calendar import *

def test_8C():

    cal_name = "result"
    day = 13
    month = 'jun'
    start = "13:00"
    end = "16:00"
    subject = "watch a movive"
    create(cal_name)
    book(cal_name,day,month,start,end,subject)

    start2 = "17:00"
    end2 = "18:00"
    subject2 = "cook food"
    book(cal_name,day,month,start2,end2,subject2)

    show(cal_name,day,month)

    remove (cal_name,day,month,start)

    start3 = "14:00"
    end3 = "16:00"
    subject3 = "Dont want to watch a movie anymore"
    book(cal_name,day,month,start3,end3,subject3)

    result = show(cal_name,day,month)

    cal_name2 = "expected"
    create(cal_name2)
    book(cal_name2,day,month,start2,end2,subject2)
    book(cal_name2,day,month,start3,end3,subject3)
    expected = show(cal_name2,day,month)

    assert(result == expected)
    print("Passed the test")
