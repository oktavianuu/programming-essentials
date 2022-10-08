# make a program that create output like this:
# sample input              # sample output
# x = 1                     # y = 0.6000000000000001
# x = 10                    # y = 0.09901951266867294

# x = float(input("Enter value for x: "))

# y = 1 / (x + (1 / (x + 1 / (x + 1/x))))

# print("y =", y)

# scenario 2
hour = int(input('Starting time (hours): '))
mins = int(input('Starting time (minutes): '))
duration = int(input('Event duration (minutes): '))

rem_mins = duration % 60
total_hour = 23
end_hour = (hour + (duration - rem_mins) / 60) 
total_mins = rem_mins + mins
end_mins = total_mins % 60
print(end_hour,':',end_mins)