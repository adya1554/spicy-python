activity = ["Go for Walk", "Read a Book", "Build a Snow Man!"]
state = input("Enter weather outside of your home :")

if state == 'sunny':
    print(activity[0])
elif state == 'rainy':
    print(activity[1])
elif state == 'snowy':
    print(activity[2])
