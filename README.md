# DAA_Handson4  
Problem 0    
code:[fibonaci output](./fibonacci.py)
output:[output]   
Problem 1     
code:[merge_k_sorted arrays](./merge_k_sortedarrays.py)    
output:[output](./merge_k_sortedarrays.png)  
**Time complexity  
Heap tracks the smallest elements from K arrays  
Initially, inserting the first element of each array into the heap takes O(K log K) time  
After that, algortithms continue to popout the smallest element & push corresponding element from array  
for  K * N elements, it take O(log K) time  
So, overall  Time complexity of O(K * N log K).  

**Space complexity **
output:[output]  
Problem 2  
code:[remove_duplicate_elements](./remove_duplicate_elements.py)  
output:[output](./remove_duplicate_elements.png)  
**Time complexity **
The time complexity of the removeDuplicatesK function is O(N^2) because for each element in the input array, it checks whether the item is already in the output list, which takes O(M) time where M is the size of the output list. This results in an overall complexity of O(N^2), where N is the number of elements in the input array. To optimize, using a set for checking duplicates can reduce the time complexity to O(N). 

**Space complexity **
