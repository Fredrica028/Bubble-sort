#array is a variable that stores the values to be sorted
array = [12,32,3,65,24,76,7,78]
swapped = bool

for count in range (len(array)-1):
    swapped = False
    for index in range (len(array)-1):
        if array[index] > array[index + 1]:
            temp = array[index]
            array[index] = array[index + 1]
            array[index + 1] = temp    
            swapped = True
            
if swapped == False:
    print (f"sorted array: {array}")
