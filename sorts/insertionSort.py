class insertionSort:
    def __init__(self,inputArray):
       self.inputArray = inputArray

    def sort(self,inputArray):
        # print("Input array from insertion sort : " + str(inputArray))
        for i in range(1,len(inputArray)):
            key = inputArray[i]
            j = i -1
            #compare if current element is greater than key then shift the element to  right by one place
            while(j >= 0 and inputArray[j] > key):
                inputArray[j+1] = inputArray[j]
                j -= 1
            inputArray[j+1] = key
        return inputArray
