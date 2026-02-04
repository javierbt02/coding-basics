print("Welcome to the temperature converter.")

while True :

    scale = input("Please, write down what temperature scale you want to convert to (c for celcius/f for farenheith/x to exit): \n")

    if len(scale) != 1 or scale.lower() not in ["c", "f", "x"]:
        print ("Please try again.")
        
    elif scale.lower() == "c": 
        farenheith = input("Now write the temperature you want to convert in Farenheith degrees: \n")
        result_ftoc = (int(farenheith) - 32)*(5/9)
        print(f"The temperature you inserted in Farenheith degrees: {farenheith}. \nConvertion to Celcius degrees: {result_ftoc}.")

    elif scale.lower() == "f": 
        celcius = input("Now write the temperature you want to convert in Celcius degrees: \n")
        result_ctof = (int(celcius) * 9/5)+32
        print(f"The temperature you inserted in Celcius degrees: {celcius}. \nConvertion to Farenheith degrees: {result_ctof}.")

    elif scale.lower() == "x":
        print ("Thank you for using this program.")
        break