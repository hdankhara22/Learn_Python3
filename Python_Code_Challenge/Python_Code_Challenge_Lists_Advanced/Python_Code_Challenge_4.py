#Write your function here


#Uncomment the line below when your function is done
#print(double_index([3, 8, -10, 12], 2))
def double_index(lst, index):
  if index >= len(lst):
    return lst
  else:
    n_lst = lst[0:index] 
  n_lst.append(lst[index]*2)
  n_lst += lst[index+1:]
  return n_lst