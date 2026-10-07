# problem 1 
# age group categarization under 13-18 - teen,19-59 = adult, 60=< senior

age = int(input("Enter your age : "))
if age < 13:
    print('you is child')

elif age >= 13 and age <= 18:
    print("Your are an teenager")
elif age >= 19 and age <= 59:
    print("Your are an Adult \n vote for nation devlopement")
elif age >= 60:
    print("Your are an Senior Citizen")
print("Thank You")