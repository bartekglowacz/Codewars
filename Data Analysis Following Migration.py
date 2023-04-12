"""
https://www.codewars.com/kata/5bc5cfc9d38567e29600019d/train/python
1. Rok można w ogóle olać - zrób listę rekordów z pominięciem roku
2. Sprawdzany format jest postaci: yyyy-mm-dd
3. Sprawdź czy data startu jest mniejsza od daty końca, jeśli tak to correct_count += 1
3.1. Jeżeli nie to zamień dd z mm w dacie startu i sprawdź ponownie warunek z punktu 3
3.2. Jeżeli data startu jest mniejsza niż data końca to correct_recoverable += 1
3.3. Jeżeli data startu jest większa niż data końca to zamień dd z mm w dacie końca.
3.4. Jeżeli data startu jest mniejsza niż data końca to correct_recoverable += 1
4.
"""
import datetime


def check_dates(records):
    # for records in records:
    #     records_without_year = [records[0][5:10], records[1][5:10]]
    #     print(records_without_year)
    correct_count = 0
    recoverable_count = 0
    uncertain_count = 0
    for records in records:
        if (records[0] < records[1] and (records[0][:4] + "-" + records[0][8:10] + "-" + records[0][5:7]) < records[1]) \
                or (records[0] < records[1] and records[0] < (records[1][:4] + "-" + records[1][8:10] + "-" + records[1][5:7])):
            print("uncertain")
            uncertain_count += 1
        elif (records[0][:4] + "-" + records[0][8:10] + "-" + records[0][5:7]) < records[1] or records[0] < (
                records[1][:4] + "-" + records[1][8:10] + "-" + records[1][5:7]):
            print("recoverable")
            # print(records[0][:4] + "-" + records[0][8:10] + "-" + records[0][5:7])
            recoverable_count += 1
        else:  # records[0] < records[1]:
            print("correct")
            correct_count += 1
    return [correct_count, recoverable_count, uncertain_count]


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
