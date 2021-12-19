import matplotlib.pyplot as plt

# x axis values
x = [1000, 2000, 3000, 5000, 10000, 20000, 30000, 40000, 50000, 60000]
x1 = [1000, 2000, 3000, 5000, 10000, 20000]
# corresponding y axis values
# Random integers
# insertion-sort
y = [0.16, 0.60, 1.36, 4.27, 15.07, 59.18, 147.45, 266.17, 448.47, 634.38]
# merge sort
y1 = [0.01,0.04,0.06,0.10,0.21,0.60,1.00,1.59,2.56,3.66]
# heap sort
y2 = [0.02,0.05,0.11,0.15,0.31,0.70,1.25,1.62,2.35,2.35]
# modified quick sort
y3 = [0.01,0.02,0.03,0.04,0.09,0.21,0.40,0.46,0.60,0.91]
#in place quick sort
y4 = [0.01,0.02,0.03,0.05,0.09,0.21,0.37,0.43,0.60,0.79]




#Sorted sequence
#Insertion sort 
# y = [0.00,0.00,0.00,0.01,0.01,0.02,0.02,0.03,0.05,0.05]
# # Merge sort
# y1 = [0.01,0.03,0.06,0.14,0.19,0.55,0.89,1.42,2.06,2.79]
# #heap sort 
# y2 = [0.02,0.05,0.11,0.14,0.19,0.55,0.89,1.42,2.12,2.44]
# # Modified quick sort 
# y3 = [0.00,0.01,0.02,0.05,0.05,0.12,0.19,0.23,0.29,0.38]
# #in place quick sort
# y4 = [0.15,0.66,1.38,3.78,15.18,60.84]
# plotting the points

# Reverse Sorted sequence
#Insertion sort 
# y = [0.27,1.12,2.75,7.14,35.51,124.11,303.14,615.46,951.24,1441.78]
# Merge sort
# y1 = [ 0.01,0.03,0.05,0.08,0.27,0.60,0.91,1.61,2.49,3.15]
#heap sort 
# y2 = [0.03,0.08,0.12,0.20,0.46,1.06,1.47,2.52,2.91,4.03]
# Modified quick sort 
# y3 = [0.01,0.02,0.02,0.04,0.08,0.17,0.22,0.37,0.45,0.59]
#in place quick sort
# y4 = [0.16,0.64,1.38,3.63,15.22,61.44]


# plotting the points
plt.plot(x, y,label = "Insertion sort")
plt.plot(x, y1,label = "Merge sort")
plt.plot(x, y2,label = "Heap sort")
plt.plot(x, y3,label = "Modified quick sort")
#plt.plot(x1, y4,label = "Quick sort")            
plt.plot(x, y4,label = "Quick sort")            
# naming the x axis
plt.xlabel('Input size')
# naming the y axis
plt.ylabel('Time(seconds)')
            
# giving a title to my graph
plt.title('Algorithm Analysis: Random Sequence')
# function to show the plot
plt.legend()
plt.show()