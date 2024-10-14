# BMI Calculator.
height = float(input("Enter your height: "))
weight = float(input("Enter your weight: "))
bmi = weight/height**2
if bmi>25:
    print("BMI:",bmi,"\nYou have over weight",)
elif bmi>15:
    print("BMI:",bmi,"\nYou have normal weight",)
else:
    print("BMI:",bmi,"\nYou have under weight",)
