#Challenge-1
'''
Let's learn about list comprehensions! You are given three integers x, y and z representing the dimensions of a cuboid along with an integer n. Print a list of all possible coordinates given by (i, j, k) on a 3D grid where the sum of i + j + k is not equal to n. Here, 0 i c; 0 j y; 0 k z. Please use list comprehensions rather than multiple loops, as a learning exercise. Example
All permutations of [i, j, k] are:

Sample Input:
1
1
1
2
Sample Output:
[0, o, 0], [o, o, 1], [0, 1, o, n, o, 0], n, 1, 11]
'''
x = int(input())
y = int(input())
z = int(input())
n = int(input())
result = [[i,j,k]
          for i in range(x+1)
          for j in range(y+1)
          for k in range(z+1)
          if x+y+z!=2
]
print(result)


'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''


'''Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given n scores. Store them in a list and find the score of the runner-up.
Input Format The first line contains n. The second line contains an array of n integers each separated by a space.
Given list is [2, 3, 6, 6, 5]. The maximum score is 6, second maximum is 5. Hence, we print 5 as the runner-up score.'''


n = int(input())
arr = map(int, input().split())
aray = sorted(set(arr),reverse = True)  #First we sort the elements and convert into set to remove all the duplicates. Then we will reverse the list to findout second highest scorer(Runner).
runner = aray[1]
print(runner)