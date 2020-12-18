# Create a function called every_three_nums that has one parameter named start

#The function should return a list of every third number between start and 100 (inclusive)

#If start is greater than 100, the function should return an empty list.

def every_three_nums(start):
  if start > 100:
    return list()
  else:
    return list(range(start, 101, 3))

print(every_three_nums(4))


# The function should return a list where all elements in lst with an index between
# start and end (inclusive) have been removed.

def remove_middle(lst, start, end):
  del lst[start:end + 1]
  return lst

print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))

# alternative method
def remove_middle(lst, start, end):
  return lst[:start] + lst[end+1:]

# Return the item that appears more frequently

def more_frequent_item(lst,item1,item2):
  if lst.count(item1) > lst.count(item2):
    return item1
  elif lst.count(item1) < lst.count(item2):
    return item2
  else:
    return item1

print(more_frequent_item([2, 3, 3, 2, 3, 2, 3, 2, 3], 2, 3))


def double_index(lst, index):
  # Checks to see if index is too big
  if index >= len(lst):
    return lst
  else:
    # Gets the original list up to index
    new_lst = lst[0:index]
 # Adds double the value at index to the new list 
  new_lst.append(lst[index]*2)
  #  Adds the rest of the original list
  new_lst = new_lst + lst[index+1:]
  return new_lst

#If there are an odd number of elements in lst, the function should return the
# middle element. If there are an even number of elements, the function should
# return the average of the middle two elements

def middle_element(lst):
  if len(lst) % 2 == 0:
    sum = lst[int(len(lst)/2)] + lst[int(len(lst)/2) - 1]
    return sum / 2
  else:
    return lst[int(len(lst)/2)]
print(middle_element([5, 2, -10, -4, 4, 5]))
