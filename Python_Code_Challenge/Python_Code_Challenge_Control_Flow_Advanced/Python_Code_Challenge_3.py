# Write your always_false function here:

# Uncomment these function calls to test your always_false function:
#print(always_false(0))
# should print False
#print(always_false(-1))
# should print False
#print(always_false(1))
# should print False
def always_false(num):
  if num > 0 and num < 0:
    return True
  else:
    return False 