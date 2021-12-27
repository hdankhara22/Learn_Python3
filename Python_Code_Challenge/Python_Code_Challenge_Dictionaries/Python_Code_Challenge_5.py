# Write your max_key function here:

# Uncomment these function calls to test your  function:
#print(max_key({1:100, 2:1, 3:4, 4:10}))
# should print 1
#print(max_key({"a":100, "b":10, "c":1000}))
# should print "c"
def max_key(my_dictionary):
  k = float("-inf")
  v = float("-inf")
  for key, value in my_dictionary.items():
    if value > v:
      v = value
      k = key
  return k