curWeather = raw_input("Go outside. Check weather. Return safely.\nReport current conditions: ")
print
if curWeather == "cold" : print("Chilly eh? Grab a Parka.")
elif curWeather == "rain" : print("Yellow umbrella time.")
elif curWeather == "tornado" : print("Batten down the hatches.")
elif curWeather == "snow" : print("Time to swap your tires.")
else: print("Err. Weather not in database...\nBecause there is no database.\nCannot provide any advice.")