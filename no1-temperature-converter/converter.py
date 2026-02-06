print("Welcome to the temperature converter.")

while True :

    scale = input("Please, write down what temperature scale you want to convert to (c for celsius/f for fahrenheit/x to exit): \n")
    scale = scale.lower()

    if len(scale) != 1 or scale.lower() not in ["c", "f", "x"]:
        print ("Please try again.")
        
    elif scale == "c": 
        while True :
            try:
                fahrenheit = input("Now write the temperature you want to convert in Fahrenheit degrees: \n")
                result_ftoc = (float(fahrenheit) - 32)*(5/9)
                print(f"The temperature you inserted in Fahrenheit degrees: {fahrenheit}. \nConvertion to Celsius degrees: {result_ftoc}.")
                break
            except ValueError:
                print("Please try again.")
    

    elif scale == "f": 
        while True:
            try:
                celsius = input("Now write the temperature you want to convert in Celsius degrees: \n")
                result_ctof = (float(celsius) * 9/5)+32
                print(f"The temperature you inserted in Celsius degrees: {celsius}. \nConvertion to Fahrenheit degrees: {result_ctof}.")
                break
            except ValueError:
                print("Please try again.")

    elif scale == "x":
        print ("Thank you for using this program.")
        break