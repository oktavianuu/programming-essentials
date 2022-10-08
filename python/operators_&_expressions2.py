# make a program that create output like this:
# sample input              # sample output
# x = 1                     # y = 0.6000000000000001
# x = 10                    # y = 0.09901951266867294

# x = float(input("Enter value for x: "))

# y = 1 / (x + (1 / (x + 1 / (x + 1/x))))

# print("y =", y)

# scenario 2
hour = int(input('Starting time (hours): '))
minutes = int(input('Starting time (minutes): '))
duration = int(input('Event duration (minutes): '))

end_minutes = 60 - minutes
end_hour = hour + 1
print(end_hour,':',end_minutes)