#Write your function here


#Uncomment the line below when your function is done
#print(larger_sum([1, 9, 5], [2, 3, 7]))
def larger_sum(lst1, lst2):
  s1 = 0
  s2 = 0
  for i in lst1:
    s1 += i
  for i in lst2:
    s2 += i
  if s1 >= s2:
    return lst1
  else: 
    return lst2