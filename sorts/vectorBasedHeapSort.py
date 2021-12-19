class vectorBasedHeapSort:
    def __init__(self,inputSequence):
        self.inputSequence = inputSequence
        self.sortedSequence = []
        self.vectorHeap = [0] * (len(self.inputSequence) + 1)
        self.insertionIndex = 0

    def heapSort(self):
        # print("Input Sequence : " + str(self.inputSequence))
        for i in range(len(self.inputSequence)):
            self.insertElm(self.inputSequence[i])
        for j in range(len(self.vectorHeap) - 1):
            minElm = self.removeMin()
            self.sortedSequence.append(minElm)
        return self.sortedSequence

    # Method to add one element at a time in min-heap
    def insertElm(self,item):
        self.insertionIndex = self.insertionIndex + 1
        self.vectorHeap[self.insertionIndex] = item
        # Upheap to satisfy heap property
        counter = self.insertionIndex
        while(counter > 1 and self.vectorHeap[counter//2] > self.vectorHeap[counter]):
            self.vectorHeap[counter//2],self.vectorHeap[counter] = self.vectorHeap[counter],self.vectorHeap[counter//2]
            counter = counter//2
       
    # Method to remove smallest element from vector 
    def removeMin(self):
        minElm = self.vectorHeap[1]
        self.vectorHeap[1] = self.vectorHeap[self.insertionIndex]
        self.insertionIndex = self.insertionIndex -1 
        counter = 1
        while counter < self.insertionIndex:
            if((2 * counter) + 1) <= self.insertionIndex:
                if(self.vectorHeap[counter] <= self.vectorHeap[2 * counter] and self.vectorHeap[counter] <= self.vectorHeap[(2 * counter) + 1]):
                    # no need for downheap;
                    return minElm
                else:
                    if self.vectorHeap[2 * counter] < self.vectorHeap[(2 * counter) + 1]:
                        j = 2 * counter
                        self.vectorHeap[j],self.vectorHeap[counter] = self.vectorHeap[counter],self.vectorHeap[j]
                        counter = j
                    else:
                        j = (2 * counter) + 1
                        self.vectorHeap[j],self.vectorHeap[counter] = self.vectorHeap[counter],self.vectorHeap[j]
                        counter = j 
            else:
                if(2 * counter) <= self.insertionIndex:
                    if self.vectorHeap[counter] > self.vectorHeap[2 * counter]:
                        self.vectorHeap[2 * counter],self.vectorHeap[counter] = self.vectorHeap[counter],self.vectorHeap[2 * counter]
                        
                return minElm



        return minElm

    