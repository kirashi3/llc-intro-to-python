# Remember, we get a string from raw_input, but we need an int to compare it
weather = int(raw_input("What temperature is it now? (as a number, please): "))
sunshine = raw_input("Is it sunny out? ").lower()

if sunshine == "yes" or sunshine == "y" or sunshine == "1" or sunshine == "true":
    sunshine = bool(True)
else:
    sunshine = bool(False)
# if the weather is greater than or equal to 25 degrees
if weather >= 25 and sunshine:
    print("Go to the beach!")
# the weather is less than 25 degrees AND greater than 15 degrees
#
# if (weather < 25 and > 15):
#
elif weather < 25 and weather > 15:
    # Still warm enough for ice cream!
    print("sudo make me an ice cream cone")
else:
    # Wear a sweater and dream of beaches.
    print("Grab your sweater and a PSL.")
