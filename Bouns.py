weight = float(input("Enter your weight (kg): "))
height = float(input("Enter your height (cm): ")) /100

bmi = weight / (height ** 2)

if bmi < 18.5:
    print("You are underweight. Watch your health.")
elif bmi <= 24.9:
    print("You are fit & healthy.")
else:
    print("You are overweight you need to work out more and watch your diet.")
