def add_greetings(names):
  greeting_list = []
  for name in names: 
    greeting_list.append("Hello, " + name)
  return greeting_list

#Uncomment the line below when your function is done
print(add_greetings(["Owen", "Max", "Sophie"]))

# Slicing lists with while loop based on parameters

def delete_starting_evens(lst):
  while len(lst) > 0 and lst[0] % 2 == 0:
    lst = lst[1:]
  return lst


print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
print(delete_starting_evens([4, 8, 10]))

#Loop through list and return is based on index of elements

def odd_indices(lst):
  odd_nums = []
  for index in range(1, len(lst), 2):
    odd_nums.append(lst[index])
  return odd_nums


print(odd_indices([4, 3, 7, 10, 11, -2]))

# Take a base and raise it to a specific power using a for loop

def exponents(bases, powers):
  new_lst = []
  for base in bases:
    for power in powers:
      new_lst.append(base ** power)
  return new_lst

print(exponents([2, 3, 4], [1, 2, 3]))

#Loop through each list and take the one that is larger

def larger_sum(lst1,lst2):
  sum1 = 0
  sum2 = 0
  for num1 in range(0, len(lst1)):
    sum1 += lst1[num1]
  for num2 in range(0, len(lst2)):
    sum2 += lst2[num2]
  if sum1 > sum2:
    return lst1
  elif sum1 == sum2:
    return lst1
  else:
    return lst2 

# Alternative (probably better) method

def larger_sum(lst1, lst2):
  sum1 = 0
  sum2 = 0
  for number in lst1:
    sum1 += number
  for number in lst2:
    sum2 += number
  if sum1 >= sum2:
    return lst1
  else: 
    return lst2

# Add numbers from lst until sum is greater than 9000.

def over_nine_thousand(lst):
  sum = 0
  for number in lst:
    sum += number
    if (sum > 9000):
      break
  return sum

print(over_nine_thousand([8000, 900, 120, 5000]))

# Find maximum number in a list 

def max_num(nums):
  maximum = nums[0]
  for number in nums:
    if number > maximum:
      maximum = number
  return maximum

print(max_num([50, -10, 0, 75, 20]))
