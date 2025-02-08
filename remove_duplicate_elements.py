import heapq
def  removeDuplicatesK(arr):
   output=[]
   for item in arr:
       if item not in output:
           output.append(item)
   return output

# Driver code
if __name__ == '__main__':
#Example1
    array1= [2, 2, 2, 2, 2]
    output1=removeDuplicatesK(array1)
    print("Output Array 1:",*output1)

#Example2
    array2 = [1, 2, 2, 3, 4, 4, 4, 5, 5]
    output2 = removeDuplicatesK(array2)
    print("Output Array 2:", *output2)