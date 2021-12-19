from random import randint
from random import seed
import time
import copy
import sys
import insertionSort
import mergeSort
import vectorBasedHeapSort
import inPlaceQuickSort
import modifiedQuickSort


class sortMain:
    sys.setrecursionlimit(5000)

    # Method to generate random numbers for input seq of size n
    def randomNumberGenerator(self,input_size):
        inputSeq = []
        # seed value chosen to be 1
        seed(1)
        for _ in range(input_size):
            value = randint(0, 10000)
            inputSeq.append(value)

        return inputSeq

    # Drivers code
    def process(self,input_size,input_choice):
        print("Inside process")
        inputSeq = []
        run_time_insertion =[0,0,0]
        run_time_merge =[0,0,0]
        run_time_heap =[0,0,0]
        run_time_quick =[0,0,0]
        run_time_modified_quick =[0,0,0]

        # generate random integers
        inputSeq = self.randomNumberGenerator(input_size) 
        
        if input_choice == 1:
            for run in range(3):
                print("------Run %s-------" % (run+1))

                # Insertion sort
                inputData = copy.deepcopy(inputSeq)
                print("Running insertion sort for input size: " +str(input_size))
                start_time = time.time()
                insertionSortInput = insertionSort.insertionSort(inputData)
                sortedSequence = insertionSortInput.sort(inputData)
                # print("Sorted sequence: " + str(sortedSequence))
                total_time = time.time() - start_time
                print("Total Time : --- %.2f seconds ---" %total_time)
                run_time_insertion[run] = total_time

                # Merge sort
                inputData = copy.deepcopy(inputSeq)
                print("Running merge sort for input size: " +str(input_size))
                start_time = time.time()
                mergeSortInput = mergeSort.mergeSort(inputData)
                mergeSortInput.mergeSort() 
                # print("Sorted sequence: " + str(inputData))
                total_time = time.time() - start_time
                print("Total Time : --- %.2f seconds ---" %total_time)
                run_time_merge[run] = total_time

                # Heap sort
                inputData = copy.deepcopy(inputSeq)
                print("Running heap sort for input size: " +str(input_size))
                start_time = time.time()
                heapSortInput = vectorBasedHeapSort.vectorBasedHeapSort(inputData)
                sortedSequence = heapSortInput.heapSort()
                # print("Sorted sequence: " + str(sortedSequence))
                total_time = time.time() - start_time
                print("Total Time : --- %.2f seconds ---" %total_time)
                run_time_heap[run] = total_time

                # Quick sort
                inputData = copy.deepcopy(inputSeq)
                print("Running in place quick sort for input size: " +str(input_size))
                start_time = time.time()
                q = inPlaceQuickSort.QuickSort(inputData)
                sortedSequence = q.inPlaceQuickSort(inputData,0,len(inputData)- 1)
                # print("Sorted sequence: " + str(sortedSequence))
                total_time = time.time() - start_time
                print("Total Time : --- %.2f seconds ---" %total_time)
                run_time_quick[run] = total_time

                #Modified quick sort
                inputData = copy.deepcopy(inputSeq)
                print("Running modified quick sort for input size: " +str(input_size))
                start_time = time.time()
                q = modifiedQuickSort.EnhancedQuickSort()
                sortedSequence = q.quickSort(inputData,0,len(inputData) - 1)
                # print("Sorted sequence: " + str(sortedSequence))
                total_time = time.time() - start_time
                print("Total Time : --- %.2f seconds ---" %total_time)
                run_time_modified_quick[run] = total_time
            
            print("Average time taken by insertion sort: %.2f seconds " %(sum(run_time_insertion)/len(run_time_insertion)))
            print("Average time taken by merge sort: %.2f seconds " %(sum(run_time_merge)/len(run_time_merge)))
            print("Average time taken by heap sort: %.2f seconds " %(sum(run_time_heap)/len(run_time_heap)))
            print("Average time taken by quick sort: %.2f seconds " %(sum(run_time_quick)/len(run_time_quick)))
            print("Average time taken by modified quick sort: %.2f seconds " %(sum(run_time_modified_quick)/len(run_time_modified_quick)))
            
        
        elif input_choice == 2:
            for run in range(3):
                print("------Run %s-------" % (run+1))

                # Insertion sort
                inputData = copy.deepcopy(inputSeq)
                inputData.sort()
                print("Running insertion sort for sorted input size: " +str(input_size))
                start_time = time.time()
                insertionSortInput = insertionSort.insertionSort(inputData)
                sortedSequence = insertionSortInput.sort(inputData)
                # print("Sorted sequence: " + str(sortedSequence))
                total_time = time.time() - start_time
                print("Total Time : --- %.2f seconds ---" %total_time)
                run_time_insertion[run] = total_time

                # Merge sort
                inputData = copy.deepcopy(inputSeq)
                inputData.sort()
                print("Running merge sort for sorted input size: " +str(input_size))
                start_time = time.time()
                mergeSortInput = mergeSort.mergeSort(inputData)
                mergeSortInput.mergeSort() 
                # print("Sorted sequence: " + str(inputData))
                total_time = time.time() - start_time
                print("Total Time : --- %.2f seconds ---" %total_time)
                run_time_merge[run] = total_time

                # Heap sort
                inputData = copy.deepcopy(inputSeq)
                inputData.sort()
                print("Running heap sort for sorted input size: " +str(input_size))
                start_time = time.time()
                heapSortInput = vectorBasedHeapSort.vectorBasedHeapSort(inputData)
                sortedSequence = heapSortInput.heapSort()
                # print("Sorted sequence: " + str(sortedSequence))
                total_time = time.time() - start_time
                print("Total Time : --- %.2f seconds ---" %total_time)
                run_time_heap[run] = total_time

                # Quick sort
                if len(inputData) >= 3000:
                    print("Python will throw RecursionError: maximum recursion depth exceeded in comparison and will stop execution")
                else :
                    inputData = copy.deepcopy(inputSeq)
                    inputData.sort()
                    print("Running in place quick sort for sorted input size: " +str(input_size))
                    start_time = time.time()
                    q = inPlaceQuickSort.QuickSort(inputData)
                    sortedSequence = q.inPlaceQuickSort(inputData,0,len(inputData)- 1)
                    # print("Sorted sequence: " + str(sortedSequence))
                    total_time = time.time() - start_time
                    print("Total Time : --- %.2f seconds ---" %total_time)
                    run_time_quick[run] = total_time

                #Modified quick sort
                inputData = copy.deepcopy(inputSeq)
                inputData.sort()
                print("Running modified quick sort for sorted input size: " +str(input_size))
                start_time = time.time()
                q = modifiedQuickSort.EnhancedQuickSort()
                sortedSequence = q.quickSort(inputData,0,len(inputData) - 1)
                # print("Sorted sequence: " + str(sortedSequence))
                total_time = time.time() - start_time
                print("Total Time : --- %.2f seconds ---" %total_time)
                run_time_modified_quick[run] = total_time
            
            print("Average time taken by insertion sort: %.2f seconds " %(sum(run_time_insertion)/len(run_time_insertion)))
            print("Average time taken by merge sort: %.2f seconds " %(sum(run_time_merge)/len(run_time_merge)))
            print("Average time taken by heap sort: %.2f seconds " %(sum(run_time_heap)/len(run_time_heap)))
            print("Average time taken by quick sort: %.2f seconds " %(sum(run_time_quick)/len(run_time_quick)))
            print("Average time taken by modified quick sort: %.2f seconds " %(sum(run_time_modified_quick)/len(run_time_modified_quick)))
            

        else:
            for run in range(3):
                print("------Run %s-------" % (run+1))

                # Insertion sort
                inputData = copy.deepcopy(inputSeq)
                inputData.sort()
                inputData = inputData[::-1]
                print("Running insertion sort for reverse sorted input size: " +str(input_size))
                start_time = time.time()
                insertionSortInput = insertionSort.insertionSort(inputData)
                sortedSequence = insertionSortInput.sort(inputData)
                # print("Sorted sequence: " + str(sortedSequence))
                total_time = time.time() - start_time
                print("Total Time : --- %.2f seconds ---" %total_time)
                run_time_insertion[run] = total_time

                # Merge sort
                inputData = copy.deepcopy(inputSeq)
                inputData.sort()
                inputData = inputData[::-1]
                print("Running merge sort for reverse sorted input size: " +str(input_size))
                start_time = time.time()
                mergeSortInput = mergeSort.mergeSort(inputData)
                mergeSortInput.mergeSort() 
                # print("Sorted sequence: " + str(inputData))
                total_time = time.time() - start_time
                print("Total Time : --- %.2f seconds ---" %total_time)
                run_time_merge[run] = total_time

                # Heap sort
                inputData = copy.deepcopy(inputSeq)
                inputData.sort()
                inputData = inputData[::-1]
                print("Running heap sort for reverse sorted input size: " +str(input_size))
                start_time = time.time()
                heapSortInput = vectorBasedHeapSort.vectorBasedHeapSort(inputData)
                sortedSequence = heapSortInput.heapSort()
                # print("Sorted sequence: " + str(sortedSequence))
                total_time = time.time() - start_time
                print("Total Time : --- %.2f seconds ---" %total_time)
                run_time_heap[run] = total_time

                # Quick sort
                if len(inputData) >= 3000:
                    print("Python will throw RecursionError: maximum recursion depth exceeded in comparison and will stop execution")
                else :
                    inputData = copy.deepcopy(inputSeq)
                    inputData.sort()
                    inputData = inputData[::-1]
                    print("Running in place quick sort for reverse sorted input size: " +str(input_size))
                    start_time = time.time()
                    q = inPlaceQuickSort.QuickSort(inputData)
                    sortedSequence = q.inPlaceQuickSort(inputData,0,len(inputData)- 1)
                    # print("Sorted sequence: " + str(sortedSequence))
                    total_time = time.time() - start_time
                    print("Total Time : --- %.2f seconds ---" %total_time)
                    run_time_quick[run] = total_time

                #Modified quick sort
                inputData = copy.deepcopy(inputSeq)
                inputData.sort()
                inputData = inputData[::-1]
                print("Running modified quick sort for reverse sorted input size: " +str(input_size))
                start_time = time.time()
                q = modifiedQuickSort.EnhancedQuickSort()
                sortedSequence = q.quickSort(inputData,0,len(inputData) - 1)
                # print("Sorted sequence: " + str(sortedSequence))
                total_time = time.time() - start_time
                print("Total Time : --- %.2f seconds ---" %total_time)
                run_time_modified_quick[run] = total_time
            
            print("Average time taken by insertion sort: %.2f seconds " %(sum(run_time_insertion)/len(run_time_insertion)))
            print("Average time taken by merge sort: %.2f seconds " %(sum(run_time_merge)/len(run_time_merge)))
            print("Average time taken by heap sort: %.2f seconds " %(sum(run_time_heap)/len(run_time_heap)))
            print("Average time taken by quick sort: %.2f seconds " %(sum(run_time_quick)/len(run_time_quick)))
            print("Average time taken by modified quick sort: %.2f seconds " %(sum(run_time_modified_quick)/len(run_time_modified_quick)))

    



def main():
    helper = sortMain()
    input_size = int(input("Enter input size: "))
    print("Choose Input Type: ")
    input_choice = int(input("1.Random integers \n2.Sorted Sequence \n3.Reverse Sorted Sequence \n"))
    helper.process(input_size,input_choice)


if __name__ == '__main__':
    main()