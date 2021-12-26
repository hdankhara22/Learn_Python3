#Write your function here


#Uncomment the line below when your function is done
#print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))
def combine_sort(lst1, lst2):
  n_lst = lst1 + lst2
  n_lst.sort()
  return n_lst