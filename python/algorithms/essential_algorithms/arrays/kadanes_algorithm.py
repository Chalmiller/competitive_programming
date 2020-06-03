# kadanes algorithm is used to look for all positive contiguous segments of the array and keep track of the 
# max sum segment.

from sys import maxint 
def maxSubArraySum(a,size): 
       
    max_so_far = -maxint - 1
    max_ending_here = 0
       
    for i in range(0, size): 
        max_ending_here = max_ending_here + a[i] 
        if (max_so_far < max_ending_here): 
            max_so_far = max_ending_here 
  
        if max_ending_here < 0: 
            max_ending_here = 0   
    return max_so_far 

    # def maxSubArraySum(a,size): 
      
    # max_so_far =a[0] 
    # curr_max = a[0] 
      
    # for i in range(1,size): 
    #     curr_max = max(a[i], curr_max + a[i]) 
    #     max_so_far = max(max_so_far,curr_max) 
          
    # return max_so_far 