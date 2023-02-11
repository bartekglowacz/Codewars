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
import math
import statistics


def stat(strg):
    record = "01|15|59, 1|47|16, 01|17|20, 1|32|34, 2|17|17, 3|22|54 01|13|1"
    # record = "01|15|59, 1|47|6, 01|17|20, 1|32|34, 2|3|17"
    # print("oryginalna forma: ", record)
    record_list = record.split(",")
    # print("jako lista: ", record_list)

    for count, x in enumerate(record_list):
        # print(f"record: {count} = {x}")
        record_list[count] = x.split("|")
    # print("lista rekordów sformatowana: ", record_list)

    record_1 = record_list[0]
    record_2 = record_list[1]
    record_3 = record_list[2]
    record_4 = record_list[3]
    record_5 = record_list[4]

    time1 = int(record_1[0]) * 3600 + int(record_1[1]) * 60 + int(record_1[2])
    time2 = int(record_2[0]) * 3600 + int(record_2[1]) * 60 + int(record_2[2])
    time3 = int(record_3[0]) * 3600 + int(record_3[1]) * 60 + int(record_3[2])
    time4 = int(record_4[0]) * 3600 + int(record_4[1]) * 60 + int(record_4[2])
    time5 = int(record_5[0]) * 3600 + int(record_5[1]) * 60 + int(record_5[2])
    # print(time1, time2, time3, time4, time5)

    times_list = [time1, time2, time3, time4, time5]

    Range = max(time1, time2, time3, time4, time5) - min(time1, time2, time3, time4, time5)
    # Mean = (time1 + time2 + time3 + time4 + time5)/5
    # Median = times_list.sort()
    # Median = times_list[math.floor(len(times_list)/2)]
    Mean_stat = statistics.mean(times_list)
    Mean_stat = math.floor(Mean_stat)
    Median_stat = statistics.median(times_list)
    # print(f"{Range = }\n{Mean_stat = }\n{Median_stat = }")

    if Range / 3600 < 1:
        hours = "00"
        minutes = math.floor(Range / 60)
        seconds = Range - math.floor(Range / 60) * 60
        Range_result = "Range: " + str(hours) + "|" + str(minutes) + "|" + str(seconds)
        # print(Range_result)
    else:
        hours = math.floor(Range / 3600)
        minutes = math.floor((Range - hours * 3600) / 60)
        seconds = math.floor(Range - hours * 3600 - minutes * 60)
        Range_result = "Range: " + str("%02d" % hours) + "|" + str("%02d" % minutes) + "|" + str("%02d" % seconds)
        # print(Range_result)

    if Mean_stat / 3600 < 1:
        hours = "00"
        minutes = math.floor(Mean_stat / 60)
        seconds = Mean_stat - math.floor(Mean_stat / 60) * 60
        Mean_stat_result = "Mean_stat: " + str(hours) + "|" + str(minutes) + "|" + str(seconds)
        # print(Mean_stat_result)
    else:
        hours = math.floor(Mean_stat / 3600)
        minutes = math.floor((Mean_stat - hours * 3600) / 60)
        seconds = math.floor(Mean_stat - hours * 3600 - minutes * 60)
        Mean_stat_result = "Average: " + str("%02d" % hours) + "|" + str("%02d" % minutes) + "|" + str("%02d" % seconds)
        # print(Mean_stat_result)

    if Median_stat / 3600 < 1:
        hours = "00"
        minutes = math.floor(Median_stat / 60)
        seconds = Median_stat - math.floor(Median_stat / 60) * 60
        Median_stat_result = "Median_stat: " + str(hours) + "|" + str(minutes) + "|" + str(seconds)
        # print(Median_stat_result)
    else:
        hours = math.floor(Median_stat / 3600)
        minutes = math.floor((Median_stat - hours * 3600) / 60)
        seconds = math.floor(Median_stat - hours * 3600 - minutes * 60)
        Median_stat_result = "Median: " + str("%02d" % hours) + "|" + str("%02d" % minutes) + "|" + str(
            "%02d" % seconds)
        # print(Median_stat_result)
    print(f"{Range_result} {Mean_stat_result} {Median_stat_result}")
    return Range_result, Mean_stat_result, Median_stat_result


stat(strg=0)
