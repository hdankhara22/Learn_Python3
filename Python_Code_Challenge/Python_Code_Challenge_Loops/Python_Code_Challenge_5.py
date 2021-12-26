#Write your function here


#Uncomment the line below when your function is done
#print(exponents([2, 3, 4], [1, 2, 3]))
def exponents(bases, powers):
  n_lst = []
  for i in bases:
    for j in powers:
      n_lst.append(i ** j)
  return n_lst