# Write your reverse_string function here:

# Uncomment these function calls to test your  function:
#print(reverse_string("Codecademy"))
# should print ymedacedoC
#print(reverse_string("Hello world!"))
# should print !dlrow olleH
#print(reverse_string(""))
# should print
def reverse_string(word):
  r = ""
  for i in range(len(word)-1, -1, -1):
    r += word[i]
  return r