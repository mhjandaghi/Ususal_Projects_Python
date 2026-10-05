# global vars and imports


# getting user inputs as height and weight
def get_user_inputs():
    weight = float(input("enter ur weight (kg): "))
    height = float(input("enter ur height (m): "))
    return weight, height


# calculate bmi
def calculate_bmi(weight, height):
    bmi = weight // (height**2) #  (//) for float and (/) for int
    return bmi


# get the bmi result
def get_bmi_result(bmi):
    print(f"bmi :{bmi}\nresult")
    if bmi <= 18.5:
        print("under weight")
    elif 25 > bmi > 18.5:
        print("normal")
    elif 30 > bmi >= 25:
        print("Over Weight")
    elif 35 > bmi >= 30:
        print("Obese")
    else:
        print("Fat!")

        
# create main func for run
def main():
    weight, height = get_user_inputs()
    bmi = calculate_bmi(weight, height)
    get_bmi_result(bmi)
    
    
if __name__ == "__main__":
    main()