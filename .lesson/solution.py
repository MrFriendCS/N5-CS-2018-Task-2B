# Title: Mobile Wifi
# Author: Mr Friend
# Date: 18 Nov 2021

# Declare variables and data structures
rawReading = 0.0
roundedReading = 0
readings = [0] * 5
signalPattern= ""

# Loop 5 times
for index in range(5):

    # Get valid reading
    rawReading =float(input("Enter the reading: "))

    while rawReading < 0 or rawReading > 100:
        print("Reading must be from 0 to 100")
        rawReading =float(input("Enter the reading: "))
    
    # Round reading to zero decimal places
    roundedReading = round(rawReading)

    # Store the reading
    readings[index] = roundedReading

    # Is reading greater than 80?
    if roundedReading > 80:
        # Add "S" on to signal pattern
        signalPattern = signalPattern + "S"
    
    # Is reading less than 30?
    elif roundedReading < 30:
        # Add "P" on to signal pattern
        signalPattern = signalPattern + "P"

    else:
        # Add "M" on to signal pattern
        signalPattern = signalPattern + "M"

# Display signal pattern with message
print("The signal pattern is: " + signalPattern)

# Loop 5 times
for index in range(5):

    # Display rounded reading with message
    print("Reading " + str(index + 1) + " - " + str(readings[index]))
