# Calculate the avegrage temperaturw

# ask the user how many days

numberOfDays = int(input("How many days's temperature? :"))
total = 0

for i in range(1, numberOfDays+1):
    nextDay = int(input(str(i) + " Day's Highest Temmperatue? : "))
    total +=nextDay

avg = (total/numberOfDays)

print("The average temp of " +str(numberOfDays) + " days is : " + str(avg))

