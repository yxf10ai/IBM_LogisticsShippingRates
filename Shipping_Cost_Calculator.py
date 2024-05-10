#Shipping cost calculator

##Input package weight and shipping rate
weight = float(input("Enter the package weight in kilogramms:  "))
rate = float(input("Enter the shipping rate per kilogram: "))

#Calculate the shipping cost
shipping_cost = weight * rate

#Display the result
print(r"Shipping Cost: {shipping_cost} USD")
