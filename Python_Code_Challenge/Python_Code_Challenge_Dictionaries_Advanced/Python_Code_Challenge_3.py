# Write your unique_values function here:

# Uncomment these function calls to test your  function:
#print(unique_values({0:3, 1:1, 4:1, 5:3}))
# should print 2
#print(unique_values({0:3, 1:3, 4:3, 5:3}))
# should print 1
def unique_values(my_dictionary):
  v = []
  for value in my_dictionary.values():
    if value not in v:
      v.append(value)
  return len(v)