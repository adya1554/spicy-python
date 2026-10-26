# problem 1 simple example 
# age group categarization under 13-18 - teen,19-59 = adult, 60=< senior

age = int(input("entr age : "))
if age < 18:
    print("child")

elif age < 60:
    print("adult")
else:
    print("senior")
print("python ")
