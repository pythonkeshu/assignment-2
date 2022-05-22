#Q1. write a python program to get a list,sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.

 
final_list = list(tuple(map(int,input().split()))
for r in range(int(input('enter no of rows : '))))  
print("List of tuple before sorting : ",final_list) 
listLen = len(final_list); 
for i in range(0, listLen):
    for j in range(0, listLen - i - 1):
        if(final_list[j][-1] > final_list[j + 1][-1]):
            swap = final_list[j]
            final_list[j] = final_list[j + 1]
            final_list[j + 1] = swap
print("List of Tuple after sorting : " ,(final_list))
 





