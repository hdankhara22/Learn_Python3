#Write your function here


#Uncomment the line below when your function is done
#print(odd_indices([4, 3, 7, 10, 11, -2]))
def odd_indices(lst):
  n_lst = []
  for i in range(1, len(lst), 2):
    n_lst.append(lst[i])
  return n_lst