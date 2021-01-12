
#Iterate through a list in search of what you want, break loop once found

dog_breeds_available_for_adoption = ['french_bulldog', 'dalmatian', 'shihtzu', 'poodle', 'collie']
dog_breed_I_want = 'dalmatian'

for want in dog_breeds_available_for_adoption:
  print(want)
  if want == dog_breed_I_want:
    print("They have the dog I want!")
    break

# Example of the continue command. Print ages unless under 21

ages = [12, 38, 34, 26, 21, 19, 67, 41, 17]

for drink in ages:
  if drink < 21:
    continue
  print(drink) 
