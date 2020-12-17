sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]

scoops_sold = 0

for location in sales_data:
  for dollars in location:
    scoops_sold += dollars

print(scoops_sold)

heights = [161, 164, 156, 144, 158, 170, 163, 163, 157]

can_ride_coaster = [height for height in heights if height > 161]

print(can_ride_coaster)

celsius = [0, 10, 15, 32, -5, 27, 3]

fahrenheit = [(temp * 9/5) + 32 for temp in celsius]

print(fahrenheit)
