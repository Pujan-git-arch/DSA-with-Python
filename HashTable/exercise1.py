# nyc_weather.csv contains new york city weather for first few days in the month of January. Write a program that can answer following,
# What was the average temperature in first week of Jan
# What was the maximum temperature in first 10 days of Jan
# Figure out data structure that is best for this problem

arr = []
with open("nyc_weather.csv","r") as f:
    for line in f:
        tokens = line.split(",")
        try:
            temperature = int(tokens[1])
            arr.append(temperature)
        except:
            print("Error in converting temperature to integer for line: ", line)    
            
print(arr)
print("Average temperature in first week of Jan:", sum(arr[:7])/7)  
print("Maximum temperature in first 10 days of Jan:", max(arr[:10]))