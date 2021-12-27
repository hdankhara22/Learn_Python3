# Write your frequency_dictionary function here:

# Uncomment these function calls to test your  function:
#print(frequency_dictionary(["apple", "apple", "cat", 1]))
# should print {"apple":2, "cat":1, 1:1}
#print(frequency_dictionary([0,0,0,0,0]))
# should print {0:5}
def frequency_dictionary(words):
  f = {}
  for i in words:
    if i not in f:
      f[i] = 0
    f[i] += 1
  return f