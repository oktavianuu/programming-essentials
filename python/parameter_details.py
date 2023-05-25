# what if in a function, one argument is frequently used compare to the other. lets say we have to put default value for one of our paramters.
# yes we can do it, for example we want to count circle area, pi value is constant all the time which is 3.14
def circlearea(r, pi = 3.14):
    print("Okay, this is your circle area based on our calculation", pi * r**2, "cm.")

radius = int(input("Enter the circle radius in cm: "))
circlearea(radius)
