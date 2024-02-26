while True:
    try:
        number = int(input("Enter an int number: "))
        print(5/number)
        break
    except (ValueError, ZeroDivisionError): # specify and handle multiple built-in exceptions within a single except clause
        print("Wrong value or no division by zero rule broken.")
    except:
        print("Sorry, something went wrong...")

