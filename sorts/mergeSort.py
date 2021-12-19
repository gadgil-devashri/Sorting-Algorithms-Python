from random import randint
from random import seed
import time

class mergeSort:
    def __init__(self,inputArray):
        self.inputArray = inputArray
        # print("Input sequence: "+ str(self.inputArray))
        self.sortedQueue = []

    def mergeSort(self):
        self.sortedQueue = self.partitionSequence(self.inputArray)

    # Method to devide sequence nto subsequences 
    def partitionSequence(self,arrayForPartition):
        if len(arrayForPartition) > 1:
            half = len(arrayForPartition) // 2
            left = arrayForPartition[:half]
            right = arrayForPartition[half:]
            left = self.partitionSequence(left)
            right = self.partitionSequence(right)
            arrayForPartition = self.mergeSequence(left,right)
        return arrayForPartition


    # Method to merge subsequences 
    def mergeSequence(self,queueOne,queueTwo):
        sortedQueue = []
        while len(queueOne) > 0 and len(queueTwo) > 0:
            if queueOne[0] < queueTwo[0]: 
                sortedQueue.append(queueOne.pop(0))
            else:
                sortedQueue.append(queueTwo.pop(0))
        while len(queueOne) > 0:
            sortedQueue.append(queueOne.pop(0))
        while len(queueTwo) > 0:
            sortedQueue.append(queueTwo.pop(0))
        # print(sortedQueue)
        return sortedQueue
       