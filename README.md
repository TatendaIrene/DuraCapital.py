# DuraCapital.py
A calculator in Python which takes a vehicle number plate and counts the number of vehicles registered before that car. 

For example, if you input the number plate AAA0000 in the calculator it should output, “The car with number plate AAA0000 is the first car, and 0 cars were registered before the car.”

Another example, if you input the number plate AAA0099 in the calculator it should output, “The car with number plate AAA0099 is the 100th car and 99 cars were registered before the car.”


In this code, the function count_vehicles() takes the number plate as input and calculates the count of vehicles registered before it. The calculation is based on the assumption that the number plate consists of three uppercase letters followed by four digits.

The function includes a validation step to ensure the number plate meets the specified format. It checks if the length of the number plate is exactly 7 characters and verifies that the first three characters are letters and the last four characters are digits. It also converts the letters in the number plate to uppercase using the .upper() method.

Next, the function converts the first three letters of the number plate into a numeric value by mapping each letter to a range of values from 0 to 25 (A=0, B=1, …, Z=25). Then, it multiplies this value by 26^2, 26, and 1 respectively, to obtain a unique numeric representation for the combination of letters.

After that, the function multiplies the numeric representation of the letters by 10,000 and adds the numeric value of the four digits to get the final count.

The main part of the code prompts the user to enter a number plate, calls the count_vehicles() function, and displays the output based on the count calculated. If the number plate is invalid, it displays a message indicating that a valid number plate should be entered.
