#Write your function here


#Uncomment the line below when your function is done
#print(max_num([50, -10, 0, 75, 20]))
def max_num(nums):
  max = nums[0]
  for i in nums:
    if i > max:
      max = i
  return max