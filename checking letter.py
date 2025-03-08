def is_alphabet(char):
    if char.isalpha():
        return True
    return False

def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

# Example usage
char = input("Enter a character: ")
if is_alphabet(char):
    print(f"{char} is an alphabet.")
else:
    print(f"{char} is not an alphabet.")

weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))
bmi = calculate_bmi(weight, height)
print(f"Your BMI is: {bmi:.2f}")