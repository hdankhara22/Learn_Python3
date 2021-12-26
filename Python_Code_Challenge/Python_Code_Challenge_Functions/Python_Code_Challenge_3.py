# Write your win_percentage function here:

# Uncomment these function calls to test your win_percentage function:
#print(win_percentage(5, 5))
# should print 50
#print(win_percentage(10, 0))
# should print 100
def win_percentage(wins, losses):
  games = wins + losses
  won = wins / games
  return won * 100