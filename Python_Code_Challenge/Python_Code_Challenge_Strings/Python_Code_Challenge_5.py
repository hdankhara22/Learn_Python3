# Write your x_length_words function here:

# Uncomment these function calls to test your tip function:
#print(x_length_words("i like apples", 2))
# should print False
#print(x_length_words("he likes apples", 2))
# should print True
def x_length_words(sentence, x):
  lst = sentence.split()
  for i in lst:
    if len(i) >= x:
      return True
    else:
      return False