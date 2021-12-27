# Write your substring_between_letters function here:

# Uncomment these function calls to test your function:
#print(substring_between_letters("apple", "p", "e"))
# should print "pl"
#print(substring_between_letters("apple", "p", "c"))
# should print "apple"
def substring_between_letters(word, start, end):
  si = word.find(start)
  ei = word.find(end)
  if -1 < si < len(word) and -1 < ei < len(word):
    return(word[si+1:ei])
  else:
    return word