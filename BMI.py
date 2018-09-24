#BMI
import math
weight = float(input('Input weight by \"kg\"\n'))
height = float(input('Input Height by \"cm\"\n'))/100
bmi = float(weight / math.pow(height,2))
if bmi < 18.5:
    print('Your BMI is',bmi, ': You\'re too fucking skinny')
elif bmi >= 18.5 and bmi < 24:
    print('Your BMI is',bmi, ': You look great!')
elif bmi >= 24 and bmi < 27:
    print('Your BMI is',bmi, ': You\'re fat!')
elif bmi >= 27 and bmi < 30:
    print('Your BMI is',bmi, ': You might have some problem.')
elif bmi >= 30 and bmi < 35:
    print('Your BMI is',bmi, ': I think you have to go see the doctor.')
else :
    print('Your BMI is',bmi, ': You should buy you a TOMB')