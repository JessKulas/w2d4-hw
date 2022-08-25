"""
Consecutive Indices
You are given a list of unique integers (arr), and two integers (a and b). 
Your task is to find out whether or not a and b appear consecutively in arr, 
and return a boolean value (True if a and b are consecutive, False otherwise).
It is guaranteed that a and b are both present in arr.
Example:
Input: ([1, 6, 9, -3, 4, -78, 0], -3, 4)
Output: True
Input: ([3,1,0,19], 19, 0)
Output: True 
"""
# if -3 and 4 are next to each other
    #return true
    #if else return false
list_b = [1, 6, 9, -3, 4, -78, 0]
num1 = 4
num2 = -3

def consec(arr, num1, num2):
   
    
    id1 = arr.index(num1)
    id2 = arr.index(num2)
    print (id1, id2)
    if (id1 + 1 == id2) or (id2+ 1 == id1):
        return True
    else:
        return False

consec(list_b, num1, num2)
print(consec(list_b, num1, num2))



#if index(3,4):
  #  return True
#else:
   # return False
# return 

#list_a = ['jimi', 'jimmy', 'downing']

#print(list_a.index('downing'))