
#function
def findsecLarge(numbers):
    
    #loop to go through all elements of the array
    for i in numbers:
        
        #check if there are enough elements in the array to function
        if len(numbers) < 2:

            return("There are not enough elements in the array.")

        #check if all elements in array are equal
        elif all(i == numbers[0] for i in numbers):
            return("All numbers in array are the same.")
            
        #if array is not all equal run function for second largest
        else:  
            
            #find initial max and second max from first two values
            for i in numbers:
                if numbers[0] >= numbers[1]:
                    firstLargest = numbers[0]
                    secondLargest = numbers[1]
                else:
                    firstLargest = numbers[1]
                    secondLargest = numbers[0]
            
                #use previously found values to run through the rest of the array
                for i in range(2,len(numbers)):
                    if numbers[i] > firstLargest:
                        secondLargest = firstLargest
                        firstLargest = numbers[i]
                    elif numbers[i] > secondLargest and numbers[i] != firstLargest:
                        secondLargest = numbers[i]
                return secondLargest


#Calling Function
numbers1 = [5, 2, 8, 1, 9, 3]
print(findsecLarge(numbers1))    
numbers2 = [4, 4, 4, 4]
print(findsecLarge(numbers2))
numbers3 = [10, 5, 10, 20, 20, 15]
print(findsecLarge(numbers3))