from random import randint
from random import seed

class EnhancedQuickSort():

    def quickSort(self,inputSeq,low,high):
        #print("InputSeq : " +str(inputSeq))
        # Decide sorting mechanism
        if low + 10 >= high:
            #Perform insertion sort
            self.insertionSort(inputSeq,low,high)

        else:
            # Perform quick sort
            if low >= high:
                return 
            # calculate pivot based on median of three
            middleIndex = (low+high) // 2
            arrayForMedian = [inputSeq[low],inputSeq[middleIndex],inputSeq[high]]
            inputSeq[low] = min(arrayForMedian)
            arrayForMedian.remove(min(arrayForMedian))
            inputSeq[high] = max(arrayForMedian)
            arrayForMedian.remove(max(arrayForMedian))
            inputSeq[middleIndex] = arrayForMedian[0]
            # Pivot selection
            pivot = inputSeq[middleIndex]
            # swap with elm at high -1 
            temp = pivot
            inputSeq[middleIndex] = inputSeq[high - 1]
            inputSeq[high - 1] = temp

            # Inplace quick sort
            i = low
            j = high - 2
            while i <= j:
                while i <= j and inputSeq[i] <= pivot:
                    i = i + 1
                while i <= j and inputSeq[j] >= pivot:
                    j = j - 1
                if i < j:
                    inputSeq[i],inputSeq[j] = inputSeq[j],inputSeq[i]
            
            inputSeq[high - 1],inputSeq[i] = inputSeq[i],inputSeq[high - 1]

            self.quickSort(inputSeq,low,i-1)
            self.quickSort(inputSeq,i+1,high)

        return inputSeq


    def insertionSort(self,inputSeq,low,high):
        for i in range(low+1,high+1):
            key = inputSeq[i]
            j = i -1
            while(j >= low and inputSeq[j] > key):
                inputSeq[j+1] = inputSeq[j]
                j -= 1
            inputSeq[j+1] = key
