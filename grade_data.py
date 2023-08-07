# Data Project Practice
# Factum est a Brandon Ruth
# read in a csv file
# output mean, median, and std dev for fall & spring semesters
# needs at least two functions

import csv
import statistics # needed for mean, median, and standard deviation


# define functions to return mean, median, and mode
def find_mean(input):
    num_mean = statistics.mean(input)
    round_num_mean = format(num_mean, ".2f")
    return round_num_mean

def find_median(input):
    num_median = statistics.median(input)
    round_num_median = format(num_median, ".2f")
    return round_num_median

def find_std(input):
    num_std = statistics.stdev(input)
    round_num_std = format(num_std, ".2f")
    return round_num_std

# open the csv file
with open("sample_grades.csv", "r") as csv_file:
    # specify field names
    field_names = ["Name", "Semester", "Grade"]
    
    csv_reader = csv.DictReader(csv_file, fieldnames=field_names)  # fieldnames parameter tells what the field names are

    # create a list to store the dictionaries
    data = []

    # loop through each row
    for row in csv_reader:
        data.append(row)

# initialize all values    
    fall_grades = []
    spring_grades = []

# loop over dictionary entries in list of data
for entry in data:
    # check values for second key-value pair to see what semester
    sem_value = entry["Semester"]
    # loop to populate lists for grades
    if sem_value == "Fall 2016":
        fall_grades.append(int(entry["Grade"]))
    if sem_value == "Spring 2016":
        spring_grades.append(int(entry["Grade"]))

# output values in chart, ANSI hero
header = "\033[1m{:^12} {:^12} {:^12}\033[0m".format("", "Fall 2016", "Spring 2016")
print(header)
print("\033[1m{:<12}\033[0m {:^12} {:^12}".format("Mean:", find_mean(fall_grades) , find_mean(spring_grades)))
print("\033[1m{:<12}\033[0m {:^12} {:^12}".format("Median:", find_median(fall_grades) , find_median(spring_grades)))
print("\033[1m{:<12}\033[0m {:^12} {:^12}".format("STD:", find_std(fall_grades) , find_std(spring_grades)))

# # output values in chart; spacebar hero
# print(f"            \033[1mFall 2016       Spring 2016\033[0m")
# print(f"\033[1mMean:\033[0m         {find_mean(fall_grades)}            {find_mean(spring_grades)}")
# print(f"\033[1mMedian:\033[0m       {find_median(fall_grades)}            {find_median(spring_grades)}")
# print(f"\033[1mSTD:\033[0m          {find_std(fall_grades)}             {find_std(spring_grades)}")