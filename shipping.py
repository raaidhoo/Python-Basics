weight = int(input("Enter Weight"))
# Ground Shipping
if weight <= 2:
  costground = weight * 1.50 + 20.00
elif weight <= 6:
  costground = weight * 3.00 + 20.00
elif weight <= 10:
  costground = weight * 4.00 + 20.00
else:
  costground = weight * 4.75 + 20.00
print("The Ground shipping cost is ",costground)
# Groud Shipping Premium
costgroundpre = weight + 125.00
print("The Ground Shipping Premium cost is ",costgroundpre)
# Drone Shipping
if weight <= 2:
  costdrone = weight * 4.50
elif weight <= 6:
  costdrone = weight * 9.00
elif weight <= 10:
  costdrone = weight * 12.00
else:
  costdrone = weight * 14.25
print("The Drone Shipping cost is ",costdrone)

