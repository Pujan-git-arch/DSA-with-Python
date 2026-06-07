# nyc_weather.csv contains new york city weather for first few days in the month of January. Write a program that can answer following,
# What was the temperature on Jan 9?
# What was the temperature on Jan 4?
# Figure out data structure that is best for this problem

weather_dict = {}
with open("nyc_weather.csv","r") as f:
    for line in f:
        tokens = line.split(",")
        try:
            date = tokens[0]
            temperature = int(tokens[1])
            weather_dict[date] = temperature
        except:
            print("Error in converting temperature to integer for line: ", line)
            
print(weather_dict)
print("Temperature on Jan 9:", weather_dict.get("Jan 9", "Data not available")) # Using get method to handle case where date might not be present in the dictionary
print("Temperature on Jan 4:", weather_dict.get("Jan 4", "Data not available")) # Using get method to handle case where date might not be present in the dictionary
print("Data structure used: Dictionary")