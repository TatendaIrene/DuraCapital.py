# Registered vehicle counter

# Check if the number plate has 7 characters
def count_vehicles(plate_number):
    if len(plate_number) != 7:
        # Return none values if the number plate is invalid
        return None, None

# Extract the first 3 characters (letters) and convert them to uppercase
    plate_letters = number_plate[:3].upper()
    # Extract the remaining characters (numbers)
    plate_numbers = number_plate[3:]

# Check if the letters are alphabetic and numbers are digits
    if not plate_letters.isalpha() or not plate_numbers.isdigit():
        # Return none values if the number plate is invalid
        return None, None

# Calculate the count based on the letters and number plates
    count = (ord(plate_letters[0]) - ord('A')) * 26 * 26
    count += (ord(plate_letters[1]) - ord('A')) * 26
    count += ord(plate_letters[2]) - ord('A')
    count *= 10000
    count += int(plate_numbers)

# Return the count and the previous count
    return count, count - 1


# Prompt the user to enter a number plate
number_plate = input("Enter the number plate: ")
# Call the count_vehicles function with the given number plate
plate_count, previous_count = count_vehicles(number_plate)

# Check if the count is none, indicating an invalid number plate
if plate_count is None:
    print("The number plate is invalid. Please enter a valid number plate.")
else:
    # Print the information for the first car
    if plate_count == 1:
        print(f"Car with number plate {number_plate} is the first car, and 0 cars were registered before the car.")
    else:
        print(f"Car with number plate {number_plate} is the {plate_count}th car and {previous_count} cars were "
              f"registered before the car.")
