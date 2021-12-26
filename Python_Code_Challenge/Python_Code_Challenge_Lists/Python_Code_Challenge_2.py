#Write your function here


#Uncomment the line below when your function is done
#print(append_sum([1, 1, 2]))
def append_sum(lst):
  for i in range(3):
    lst.append(lst[-1] + lst[-2])
  return lst