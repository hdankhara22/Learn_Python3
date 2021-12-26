#Write your function here


#Uncomment the line below when your function is done
#print(append_size([23, 42, 108]))
def append_size(lst):
  lst.append(len(lst))
  return lst