
## Python Script to Determine the Cheapest Shipping Method based on Weight

## Function for ground costs

def ground_cost(weight):
  if weight <= 2:
    cost_per_pound = 1.5
  elif weight <= 6:
    cost_per_pound = 3
  elif weight <= 10:
    cost_per_pound = 4
  else:
    cost_per_pound = 4.75
  return 20 + (cost_per_pound * weight)  

## Premium ground price is constant

premium_ground = 125

## Test ground_cost function

#print(ground_cost(8.4))


## Function for drone shipping costs

def drone_cost(weight):
  if weight <= 2:
    flight_cost = 4.5
  elif weight <= 6:
    flight_cost = 9
  elif weight <= 10:
    flight_cost = 12
  else:
    flight_cost = 14.25
  return (flight_cost * weight)

## Test drone_cost function

#print(drone_cost(1.5))

## Function that will take a weight input from the user and determine the cheapest shipping cost and method

def print_cheapest_ship_method(weight):

  ground = ground_cost(weight)
  premium = premium_ground
  drone = drone_cost(weight)

  if ground < premium and ground < drone: 
    method = "Standard Ground"
    cost = ground
  elif premium < ground and premium < drone:
    method = "Premium Ground"
    cost = premium
  else:
    method = "Drone"
    cost = drone
  print(
    "The cheapest option available is $%.2f with %s Shipping."
    % (cost, method)
  )

print_cheapest_ship_method(4.8)
print_cheapest_ship_method(41.5)