#Write your function here


#Uncomment the line below when your function is done
#print(middle_element([5, 2, -10, -4, 4, 5]))
def middle_element(lst):
  if len(lst) % 2 == 0:
    s = lst[int(len(lst)/2)] + lst[int(len(lst)/2) - 1]
    return s / 2
  else:
    return lst[int(len(lst)/2)]