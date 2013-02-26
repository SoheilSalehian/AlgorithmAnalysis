#!/usr/bin/python
import random
import math
     

def partition(array, pivot, left, right):   
    #get the index of pivot + 1 which is the starting index for all (< pivot) element list (aka. partition index)
    i = array.index(pivot) 
    #walk through the array and make the comparisons
    for j in xrange(left,right):     
        #if the current element is greater than the pivot don't do anything otherwise:          
        if (array[j] <= pivot):
            #swap the element with the partition index element
            array[j], array[i+1] = array[i+1], array[j]
            #now that we have a new element in the (< pivot) list, increment the partition index           
            i += 1
            
	#swap the pivot to its correct position  
    array[array.index(pivot)], array[i] = array[i], array[array.index(pivot)]
    #return the partition index which should be one behind the pivot index   
    return i

               
def choosePivot(array, left, right):
	global pivotmode
	if(pivotmode == 'first'):
		index = left
	elif(pivotmode == 'last'):
		index = right - 1 	
	elif(pivotmode == '3-median'):
		temparray = array[left:right]
		midlist = []
		middleIndex = (right-left)/2 if (right-left)%2 else ((right-left)/2)-1
		midlist = [array[left], temparray[middleIndex], array[right-1]]
		midlist.sort()
		index = array.index(midlist[1])
	return array[index]


def qSort(array,left=None, right=None):
    if left == None: left = 0
    if right == None: right = len(array)
    global comparisons          
    #recursive stopping condition    
    if (right - left <= 1):
        #print "end of the line"
        return array     
    #choose the pivot element
    pivot = choosePivot(array, left, right)
    #print array, pivot
    #swap the pivot with the first element of the array
    array[array.index(pivot)], array[left] = array[left], array[array.index(pivot)]
    #partition the array around pivot
    i =partition(array, pivot, left+1, right)
    #count the number of comparisons
    comparisons += len(array[left:right]) - 1     
    #recursive call to sort the first part (< pivot)
    qSort(array,left,i)   
    #recursive call to sort the second part (< pivot)
    qSort(array,i+1,right)
    	
               
    

comparisons = 0
pivotmode = '3-median'

if __name__ == '__main__':
    
	#TODO: Do elegant testing scheme
	#TODO: Monte Carlo Method
	#TODO: Random Pivot 
	
	
	with open('/home/soheil/Algorithms/quickSort/PA2-Input.txt',"r") as fp:
		flist = fp.readlines()
	unsorted = []
	for i in xrange(len(flist)):
		unsorted.append(int(flist[i]))
	
#	unsorted = []
#	unsorted = sorted(random.sample(range(1,101),100), reverse=True) 
#	unsorted = [2, 8, 9, 3, 7, 5, 10, 1, 6, 4]
	qSort(unsorted)
	print comparisons
	#print unsorted    
    


