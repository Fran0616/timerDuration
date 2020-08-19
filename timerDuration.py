#Simple code to evaluate the end time of a period of time, given as a number of minutes.
#the start time is given as a pair of hours (0..23) and minutes (0.59). The results will be printed to the console. 


hour = int(input("Starting time (hours): ")) #this variable will hold the hour value
mins = int(input("Starting time (minutes): ")) #this variable will hold the minutes
dura = int(input("Event duration (minutes): ")) # this variable will hold the duration or elapse time 

# put your code here

endMinCalculator = (mins + dura) #adds the minute to the duration 
endMin = endMinCalculator%60 #find the remainder of the minute, this will be the value for minute

endHourB = (mins + dura)// (60) #add the  minutes and duration and then calculate the hour = 60
endHourCalculator = endHourB + hour 
endHour = endHourCalculator%24

    
#print(endHour)
print(endHour, end=":")
print(endMin)
