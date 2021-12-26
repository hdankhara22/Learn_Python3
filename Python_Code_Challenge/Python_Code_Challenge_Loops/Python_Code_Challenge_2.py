#Write your function here


#Uncomment the line below when your function is done
#print(add_greetings(["Owen", "Max", "Sophie"]))
def add_greetings(names):
  n_list = []
  for i in names:
    n_list.append("Hello, " + i)
  return n_list