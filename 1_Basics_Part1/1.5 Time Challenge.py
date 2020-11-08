##Estimated time
##15-20 minutes
##
##Level of difficulty
##Easy
##
##Objectives
##improving the ability to use numbers, operators, and arithmetic operations in Python;
##using the print() function's formatting capabilities;
##learning to express everyday life phenomena in terms of programming language.
##Scenario
##Your task is to prepare a simple code able to evaluate the end time of a period of time, given as a number of minutes (it could be arbitrarily large). The start time is given as a pair of hours (0..23) and minutes (0..59). The result has to be printed to the console.
##
##For example, if an event starts at 12:17 and lasts 59 minutes, it will end at 13:16
##
##Don't worry about any imperfections in your code - it's okay if it accepts an invalid time – the most important thing is that the code produces valid results for valid input data. Test your code carefully!
##
##Hint: using the % operator may be the key to success!

hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))


# hours at 24 go to 0
# mins at 60 raise hour by one go to 0
# I can use f-strings to print everything nicely with two digits
# Might be easiest to just convert to raw minutes then back to minutes and hours
#1440 mins in day
#could do hours * 60 + mins to conver to min time
#Then add duration
#Then mod 1440 and f-string output
#Let's give a whirl

raw_min = hour * 60 + mins

raw_end = (raw_min + dura) % 1440

end_hour = raw_end // 60

end_min = raw_end % 60

print(f"The event will end at {end_hour:02d}:{end_min:02d}.")
