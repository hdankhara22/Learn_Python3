#Write your function here


#Uncomment the line below when your function is done
#print(over_nine_thousand([8000, 900, 120, 5000]))
def over_nine_thousand(lst):
  s = 0
  for i in lst:
    s += i
    if (s > 9000):
      break
  return s