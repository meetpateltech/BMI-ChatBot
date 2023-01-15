def bmi_chatbot():
    print("Welcome to the BMI chatbot!")
    height = float(input("Please enter your height in meters: "))
    weight = float(input("Please enter your weight in kilograms: "))
    bmi = weight / (height ** 2)
    if bmi < 18.5:
        print("Your BMI is {:.2f}, which is considered underweight.".format(bmi))
    elif bmi >= 18.5 and bmi < 25:
        print("Your BMI is {:.2f}, which is considered healthy.".format(bmi))
    elif bmi >= 25 and bmi < 30:
        print("Your BMI is {:.2f}, which is considered overweight.".format(bmi))
    else:
        print("Your BMI is {:.2f}, which is considered obese.".format(bmi))
    print("Thank you for using the BMI chatbot!")

bmi_chatbot()
