# Write your count_first_letter function here:

# Uncomment these function calls to test your  function:
#print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Lannister": ["Jaime", "Cersei", "Tywin"]}))
# should print {"S": 4, "L": 3}
#print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Sannister": ["Jaime", "Cersei", "Tywin"]}))
# should print {"S": 7}
def count_first_letter(names):
  l = {}
  for key in names:
    k = key[0]
    if k not in l:
      l[k] = 0
    l[k] += len(names[key])
  return l