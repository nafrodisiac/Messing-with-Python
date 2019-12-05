gallons = input("Gallons? ")
 
#5 grams of megacrop per 1 gallon of water 
mc = 5 * int(gallons)
#2 grams per gallon of cal mag (1.1 / 2.2)
cm = 2 * int(gallons)
#find out how many grams of each needed
print("you need " + str(mc) + " grams of megacrop")
print ("you need " + str(cm) + " grams of calmag")  


