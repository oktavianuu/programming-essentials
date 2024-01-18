# evaluating BMI and converting imperial units to metric units
'''
We must pay attention when dealing with imperial measurements since not all countries use metric units.
So we need to write functions to convert imperial units to metric ones.
'''
# It is well-known fact that 1 lb = 0.45359237 kg, we can make functio to convert lb to kg.
def lb_to_kg(lb):
    return lb * 0.45359237

# print(lb_to_kg(1)) 

# feet to inches, 1 ft = 0.3048 m, 1 in = 2.54 cm = 0.0254 m
def ft_and_inch_to_m(ft, inch=0.0):
    return ft * 0.3048 + inch * 0.0254
# print(ft_and_inch_to_m(1, 1))
# print(ft_and_inch_to_m(6, 0))

def bmi(weight, height):
    if height < 1.0 or height > 2.5 or weight < 20 or weight > 200:
        return None
    
    return weight/height ** 2

print(bmi(weight=lb_to_kg(176), height=ft_and_inch_to_m(5, 7)))