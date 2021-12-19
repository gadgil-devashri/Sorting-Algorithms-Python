class QuickSort:
    def __init__(self,inputSeq):
        self.inputSeq = inputSeq
        # print("Input sequence : " +str(self.inputSeq))
    
    def inPlaceQuickSort(self,seq,low,high):
        if low >= high:
            return
        # select pivor as the last element in input sequence
        pivot = seq[high]
        i = low
        # Since pivot is the last element in an input sequence, it is already sorted
        j = high - 1
        while i <= j:
            while i <= j and seq[i] <= pivot:
                i = i + 1
            while i <= j and seq[j] >= pivot:
                j = j - 1
            if i < j:
                # swap elements
                seq[i],seq[j] = seq[j],seq[i]
        
        # swap elements
        seq[high],seq[i] = seq[i],seq[high]

        if i-1-low < high-i-1:
            self.inPlaceQuickSort(seq,low,i-1)
            self.inPlaceQuickSort(seq,i+1,high)
        else:
            self.inPlaceQuickSort(seq,low,i-1)
            self.inPlaceQuickSort(seq,i+1,high)


        return seq