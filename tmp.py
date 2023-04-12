"""
1. Rok można w ogóle olać - zrób listę rekordów z pominięciem roku
2. Sprawdzany format jest postaci: yyyy-mm-dd
3. Sprawdź czy
"""


def check_dates(records):
    for records in records:
        print(records[0][5:7] + "\t" + records[0][8:10])
        # print(records[0].replace(records[0][5:6], records[0][8:9]))

    return [0, 0, 0]


records_to_analyze = [
    ["2015-04-04", "2015-05-13"],  # correct
    ["2013-06-18", "2013-08-05"],  # correct
    ["2001-02-07", "2001-03-01"],  # correct
    ["2011-10-08", "2011-08-14"],  # recoverable
    ["2009-08-21", "2009-04-12"],  # recoverable
    ["1996-01-24", "1996-03-09"],  # uncertain
    ["2000-10-09", "2000-11-20"],  # uncertain
    ["2002-02-07", "2002-12-10"]]  # uncertain

check_dates(records_to_analyze)
