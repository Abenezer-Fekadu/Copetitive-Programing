"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
  
"""

class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        
        lst = []
        
        for x in range(1, 1000):
            
            f, y = 1, 1000
            while f <= y:
                mid = f + (y-f)//2
                if customfunction.f(x,mid) == z:
                    lst.append([x,mid])
                    break
                    
                elif customfunction.f(x,mid) > z:
                    y = mid -1
                    
                else:
                    f = mid + 1 
                                
        return lst
        
