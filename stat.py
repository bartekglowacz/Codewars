"""
You are the "computer expert" of a local Athletic Association (C.A.A.). Many teams of runners come to compete.
Each time you get a string of all race results of every team who has run.
For example here is a string showing the individual results of a team of 5 runners:

"01|15|59, 1|47|6, 01|17|20, 1|32|34, 2|3|17"

Each part of the string is of the form: h|m|s where h, m, s (h for hour, m for minutes, s for seconds)
are positive or null integer (represented as strings) with one or two digits. Substrings in the input string are separated by ,  or ,.

To compare the results of the teams you are asked for giving three statistics; range, average and median.

Range : difference between the lowest and highest values. In {4, 6, 9, 3, 7} the lowest value is 3, and the highest is 9, so the range is 9 − 3 = 6.

Mean or Average : To calculate mean, add together all the numbers and then divide the sum by the total count of numbers.

Median : In statistics, the median is the number separating the higher half of a data sample from the lower half.
The median of a finite list of numbers can be found by arranging all the observations from the lowest value to the highest value and picking the middle one
(e.g., the median of {3, 3, 5, 9, 11} is 5) when there is an odd number of observations.
If there is an even number of observations, then there is no single middle value;
the median is then defined to be the mean of the two middle values (the median of {3, 5, 6, 9} is (5 + 6) / 2 = 5.5).

Your task is to return a string giving these 3 values. For the example given above, the string result will be

"Range: 00|47|18 Average: 01|35|15 Median: 01|32|34"

of the form: "Range: hh|mm|ss Average: hh|mm|ss Median: hh|mm|ss"`

where hh, mm, ss are integers (represented by strings) with each 2 digits.
"""
import datetime
import math
import statistics


def stat(strg):
    # strg = "01|15|59, 1|47|16, 01|17|20, 1|32|34, 2|17|17, 3|22|54, 01|13|1"
    record_list = strg.split(",")
    times_list = []
    # print(record_list)
    for x in range(0, len(record_list), 1):
        x = record_list[x].split("|")
        time = int(x[0]) * 3600 + int(x[1]) * 60 + int(x[2])
        # print(time)
        times_list.append(time)
    # print(times_list)
    Range = max(times_list) - min(times_list)
    Average = statistics.mean(times_list)
    Median = statistics.median(times_list)
    Range = str(datetime.timedelta(seconds=Range)).replace(":", "|")
    Average = str(datetime.timedelta(seconds=Average)).replace(":", "|")
    Median = str(datetime.timedelta(seconds=Median)).replace(":", "|")
    # print(Range, Average, Median)
    Range_splitted = Range.split("|")
    Average_splitted = Average.split("|")
    Median_splitted = Median.split("|")
    # print(Range_splitted, Average_splitted, Median_splitted)
    Range_result = [str("%02d" % float(x)) for x in Range_splitted]
    Average_result = [str("%02d" % float(x)) for x in Average_splitted]
    Median_result = [str("%02d" % float(x)) for x in Median_splitted]
    Range_result = "Range: " + Range_result[0] + "|" + Range_result[1] + "|" + Range_result[2]
    Average_result = "Average: " + Average_result[0] + "|" + Average_result[1] + "|" + Average_result[2]
    Median_result = "Median: " + Median_result[0] + "|" + Median_result[1] + "|" + Median_result[2]
    return f"{Range_result}, {Average_result}, {Median_result}"


print(stat("01|15|59, 1|47|6, 01|17|20, 1|32|34, 2|3|17"))
