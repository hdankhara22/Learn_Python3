#Write your function here

#Uncomment the line below when your function is done
#print(more_frequent_item([2, 3, 3, 2, 3, 2, 3, 2, 3], 2, 3))
def more_frequent_item(lst, item1, item2):
  if lst.count(item1) >= lst.count(item2):
    return item1
  else:
    return item2