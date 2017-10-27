# Convert kilometers to miles 

kilometers = int(input("Enter kilometers: "))

# Conversion(1km is equal to 0.621371 miles) 
conv = 0.621371

# Calculate miles
miles = kilometers * conv
print("%s kilometers is equal to %s miles" % (kilometers,miles))