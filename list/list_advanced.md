### Multidimensional Nature of List: Advanced Application

In two-dimensional list, we must use two coordinates when we access an element:

* a vertical one (row number)
* and a horizontal one (column header)

To get a deeper understanding about two-dimensional list, let's study the following scenario:

Imagine that we want to develop a piece of software for an automatic weather station. The device records the air temperature on and hourly basis and does it throughout the month. This gives us a total of 24 x 31 = 744 values. We must be able to design a list that capable of storing all these results. The following is the steps of how we design the application:

1. First we have to decide which data type would be adequate for this application. In this case, a ``float`` would be best, since the thermometer we're using is able to measure the temperature with an accuracy of 0.1 degree Celsius.
2. Then we take an arbitrary decision that the rows will record the readings every hour (sho the row will have 24 elements) and each of the row will be assigned to one day of the month (let's assume that each month has 31 days, so we need 31 rows). Here's the appropriate pair of comprehension (```h``` is for hour and ```d``` is for day):

```python
temps = [[0.0 for h in range(24)] for d in range(31)]
```

3. The whole matrix is filled with zero. We can imagine that it will be updated automatically using special hardware agents. We just need to wait for the list to be updated with the measurements from our devices. 
4. It's time to determine the monthly average of noon temperature. Add up all 31 recorded at noon and divide the sum by 31. We can assume that the midnight temperature is stored first. Here's the relevant code:
```python
temps = [[0.0 for h in range(24)] for d in range(31)]
#
# The matrix is updated here
#

total = 0.0 

for day in temps:
    total += day[11]

average = total/31

print("Average temperature at noon: ", average)
```

