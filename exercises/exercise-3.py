# exercise-03 Calculate Dog Years

# Write the code that:
# 1. Prompts the user to enter a dog's age in human years like this:
#      Input a dog's age in human years: 
# 2. Calculates the equivalent dog years, where:
#      - The first two years count as 10 years each
#      - Any remaining years count as 7 years each
# 3. Prints the answer in the following format:
#      The dog's age in dog years is xx

# Hint:  Use the int() function to convert the string returned from input() into an integer

dogs_human_age = float(input("Input a dog's age in human years: "))
dogs_dog_age = 0
if dogs_human_age <= 2:
    dogs_dog_age = dogs_human_age * 10
else:
    dogs_dog_age = 20 + (dogs_human_age - 2) * 7

print(dogs_dog_age)

print(f"The dog's age in dog years is {dogs_dog_age}")