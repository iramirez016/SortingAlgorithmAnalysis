from time import perf_counter
from matplotlib import pyplot as plt
import random
import numpy as np
import heap

def merge_sort(list):
    merge_sortR(list, 0, len(list) - 1)

# sorts list elements in range of indices sti to endi (inclusive)
def merge_sortR(list, sti, endi):
    if sti >= endi:
        return   # 1 element by itself is already sorted so we are done

    # if sti < endi:
    mididx = (sti + endi) // 2
    merge_sortR(list, sti, mididx)
    merge_sortR(list, mididx + 1, endi)

    # we expect the portions of the list to be sorted from sti to mididx
    # and from mididx+1 to endi

    temp_list = []
    left_i = sti
    right_i = mididx + 1
    while left_i <= mididx and right_i <= endi:
        if list[left_i] < list[right_i]:
            temp_list.append(list[left_i])
            left_i += 1
        else:
            temp_list.append(list[right_i])
            right_i += 1

    # either the left half is exhausted or the right half is
    if left_i > mididx:
        # left half is exhausted
        # so we copy the remainder on the right into list
        temp_list += list[right_i:endi+1]
    else:
        # right half is exhausted
        # so we copy the remainder on the left into list
        temp_list += list[left_i:mididx+1]

    # in list we have to copy all of temp_list into list[sti:endi+1]
    list[sti:endi+1] = temp_list.copy()


def selection_sort(nums):
    for phase in range(0, len(nums) - 1):
        maxidx = 0
        for i in range(1, len(nums) - phase):
            if nums[i] > nums[maxidx]:
                maxidx = i

        # maxidx is the place of the largest value
        # we need swap that value with
        lastidx = len(nums) - phase - 1
        temp = nums[maxidx]
        nums[maxidx] = nums[lastidx]
        nums[lastidx] = temp

def heap_sort(nums):
        myheap = heap.BinaryMaxHeap()
        for n in nums:
            myheap.add(n)
        lasti = len(nums) - 1
        #for n in nums:
        #for lasti in range(len(nums) - 1, -1, -1):
        while not myheap.is_empty():
            tempval = myheap.remove()
            #tempval == lasti
            nums[lasti] = tempval
            lasti -= 1

def insertion_sort(nums):
    insertion_sort_portion(nums, 0, len(nums) - 1)
       
def insertion_sort_portion(nums, start_i, end_i):
    for j in range(start_i + 1, end_i + 1):
        temp = nums[j]
        i = j-1
        while i>=start_i:
            #print(temp, nums[i])
            if temp < nums[i]:
                nums[i+1] = nums[i]
                i -= 1
            else:
                break

        nums[i+1] = temp
        #print(nums, 'after a pass')
    
alist = [9,3,6,2,5,8,4]
print(f'alist before sort {alist}')
# notice the alist portion from index 1 to 4 is 3,6,2,5
insertion_sort_portion(alist, 0, 6)
print(f'alist after sort: {alist}')
# [9, 2, 3, 5, 6, 8, 4]

def quick_sort(list):
    quick_sortR(list, 0, len(list)-1)

def quick_sortR(list, si, ei):

    if si >= ei:
        return

#    if (ei - si + 1) < 15:
#        insertion_sort(list, si, ei)
    
    # determine the median of list[si], list[ei], list[midi]
    # and swap that with list[ei]

    
    #pivoti = random.randint(si, ei)
    # swap list[pivoti] and list[ei]
    # or do median of 3
    
    midi = (si + ei) // 2
    if (list[midi] <= list[si] and list[si] <= list[ei]) or \
       (list[midi] >= list[si] and list[si] >= list[ei]):
        # list[si] is median
        temp = list[si]
        list[si] = list[ei]
        list[ei] = temp
    elif (list[si] <= list[midi] and list[midi] <= list[ei]) or \
         (list[si] >= list[midi] and list[midi] >= list[ei]):
        temp = list[midi]
        list[midi] = list[ei]
        list[ei] = temp

    pivotVal = list[ei]

    i = si
    j = ei-1

    while True:

        while list[i] < pivotVal:
            i += 1

        while j >= si and list[j] >= pivotVal:
            j -= 1

        if i < j:
            # swap the ith and jth elements
            temp = list[i]
            list[i] = list[j]
            list[j] = temp
        else:
            break

    # swap the pivot with the ith element
    temp = list[i]
    list[i] = list[ei]
    list[ei] = temp


    # we have data from si to i-1 which are all less than list[i]
    # we have data from i+1 to ei which are all greater than or equal to list[i]
    quick_sortR(list, si, i-1)
    quick_sortR(list, i+1, ei)

def quick_sort10(list):
    quick_sort10R(list, 0, len(list)-1)

def quick_sort10R(list, si, ei):

    if si >= ei:
        return

    if (ei - si + 1) < 10:
        insertion_sort_portion(list, si, ei)
    
    # determine the median of list[si], list[ei], list[midi]
    # and swap that with list[ei]

    
    #pivoti = random.randint(si, ei)
    # swap list[pivoti] and list[ei]
    # or do median of 3
    
    midi = (si + ei) // 2
    if (list[midi] <= list[si] and list[si] <= list[ei]) or \
       (list[midi] >= list[si] and list[si] >= list[ei]):
        # list[si] is median
        temp = list[si]
        list[si] = list[ei]
        list[ei] = temp
    elif (list[si] <= list[midi] and list[midi] <= list[ei]) or \
         (list[si] >= list[midi] and list[midi] >= list[ei]):
        temp = list[midi]
        list[midi] = list[ei]
        list[ei] = temp

    pivotVal = list[ei]

    i = si
    j = ei-1

    while True:

        while list[i] < pivotVal:
            i += 1

        while j >= si and list[j] >= pivotVal:
            j -= 1

        if i < j:
            # swap the ith and jth elements
            temp = list[i]
            list[i] = list[j]
            list[j] = temp
        else:
            break

    # swap the pivot with the ith element
    temp = list[i]
    list[i] = list[ei]
    list[ei] = temp


    # we have data from si to i-1 which are all less than list[i]
    # we have data from i+1 to ei which are all greater than or equal to list[i]
    quick_sort10R(list, si, i-1)
    quick_sort10R(list, i+1, ei)


def quick_sort30(list):
        quick_sort30R(list, 0, len(list)-1)

def quick_sort30R(list, si, ei):

    if si >= ei:
        return

    if (ei - si + 1) < 30:
        insertion_sort_portion(list, si, ei)
    
    # determine the median of list[si], list[ei], list[midi]
    # and swap that with list[ei]

    
    #pivoti = random.randint(si, ei)
    # swap list[pivoti] and list[ei]
    # or do median of 3
    
    midi = (si + ei) // 2
    if (list[midi] <= list[si] and list[si] <= list[ei]) or \
       (list[midi] >= list[si] and list[si] >= list[ei]):
        # list[si] is median
        temp = list[si]
        list[si] = list[ei]
        list[ei] = temp
    elif (list[si] <= list[midi] and list[midi] <= list[ei]) or \
         (list[si] >= list[midi] and list[midi] >= list[ei]):
        temp = list[midi]
        list[midi] = list[ei]
        list[ei] = temp

    pivotVal = list[ei]

    i = si
    j = ei-1

    while True:

        while list[i] < pivotVal:
            i += 1

        while j >= si and list[j] >= pivotVal:
            j -= 1

        if i < j:
            # swap the ith and jth elements
            temp = list[i]
            list[i] = list[j]
            list[j] = temp
        else:
            break

    # swap the pivot with the ith element
    temp = list[i]
    list[i] = list[ei]
    list[ei] = temp


    # we have data from si to i-1 which are all less than list[i]
    # we have data from i+1 to ei which are all greater than or equal to list[i]
    quick_sort30R(list, si, i-1)
    quick_sort30R(list, i+1, ei)
   
def quick_sort50(list):
    quick_sort50R(list, 0, len(list)-1)

def quick_sort50R(list, si, ei):

    if si >= ei:
        return

    if (ei - si + 1) < 50:
        insertion_sort_portion(list, si, ei)
    
    # determine the median of list[si], list[ei], list[midi]
    # and swap that with list[ei]

    
    #pivoti = random.randint(si, ei)
    # swap list[pivoti] and list[ei]
    # or do median of 3
    
    midi = (si + ei) // 2
    if (list[midi] <= list[si] and list[si] <= list[ei]) or \
       (list[midi] >= list[si] and list[si] >= list[ei]):
        # list[si] is median
        temp = list[si]
        list[si] = list[ei]
        list[ei] = temp
    elif (list[si] <= list[midi] and list[midi] <= list[ei]) or \
         (list[si] >= list[midi] and list[midi] >= list[ei]):
        temp = list[midi]
        list[midi] = list[ei]
        list[ei] = temp

    pivotVal = list[ei]

    i = si
    j = ei-1

    while True:

        while list[i] < pivotVal:
            i += 1

        while j >= si and list[j] >= pivotVal:
            j -= 1

        if i < j:
            # swap the ith and jth elements
            temp = list[i]
            list[i] = list[j]
            list[j] = temp
        else:
            break

    # swap the pivot with the ith element
    temp = list[i]
    list[i] = list[ei]
    list[ei] = temp


    # we have data from si to i-1 which are all less than list[i]
    # we have data from i+1 to ei which are all greater than or equal to list[i]
    quick_sort50R(list, si, i-1)
    quick_sort50R(list, i+1, ei)

data = []
size = 1000
while len(data) < size:
    data.append(random.randint(1, size*10))

print(f'generated a sequence of size {size}')

start = perf_counter()
data.sort()
#sort the data  # e.g. here call merge_sort(data) OR selection_sort(data) OR data.sort()
end = perf_counter()
elapsed_time = end - start
print(f'Time elapsed for python built sort is {elapsed_time} seconds.')

start = perf_counter()
merge_sort(data)
end = perf_counter()
elapsed_time = end - start
print(f'Time elapsed for merge sort is {elapsed_time} seconds.')

start = perf_counter()
selection_sort(data)
end = perf_counter()
elapsed_time = end - start
print(f'Time elapsed for selection sort is {elapsed_time} seconds.')

start = perf_counter()
heap_sort(data)
end = perf_counter()
elapsed_time = end - start
print(f'Time elapsed for heap sort is {elapsed_time} seconds.')

input_sizes = []
python_sort_times = []
merge_sort_times = []
selection_sort_times = []
heap_sort_times = []
qs_sort_times = []
qs10_sort_times = []
qs30_sort_times = []    
qs50_sort_times = []  
for size in range(1000,30000 + 1,1000):
    data = []
    while len(data) < size:
        data.append(random.randint(1, size*10))

    input_sizes.append(size)
    
    # compute elapsed time
    start = perf_counter()
    data.sort()
    end = perf_counter()
    elapsed_time = end - start

    python_sort_times.append(elapsed_time)
    
for size in range(1000,30000 + 1,1000):
    data = []
    while len(data) < size:
        data.append(random.randint(1, size*10))
    
    # compute elapsed time
    start = perf_counter()
    merge_sort(data)
    end = perf_counter()
    elapsed_time = end - start

    merge_sort_times.append(elapsed_time)

for size in range(1000,30000 + 1,1000):
    data = []
    while len(data) < size:
        data.append(random.randint(1, size*10))
    
    # compute elapsed time
    start = perf_counter()
    selection_sort(data)
    end = perf_counter()
    elapsed_time = end - start

    selection_sort_times.append(elapsed_time)

for size in range(1000,30000 + 1,1000):
    data = []
    while len(data) < size:
        data.append(random.randint(1, size*10))
    
    # compute elapsed time
    start = perf_counter()
    heap_sort(data)
    end = perf_counter()
    elapsed_time = end - start

    heap_sort_times.append(elapsed_time)

for size in range(2):
    data = []
    while len(data) < size:
        data.append(random.randint(1, size*10))

    # compute elapsed time
    start = perf_counter()
    quick_sort(data)
    end = perf_counter()
    elapsed_time = end - start

    qs_sort_times.append(elapsed_time)

for size in range(2):
    data = []
    while len(data) < size:
        data.append(random.randint(1, size*10))
    
    # compute elapsed time
    start = perf_counter()
    quick_sort10(data)
    end = perf_counter()
    elapsed_time = end - start

    qs10_sort_times.append(elapsed_time)

for size in range(2):
    data = []
    while len(data) < size:
        data.append(random.randint(1, size*10))
    
    # compute elapsed time
    start = perf_counter()
    quick_sort30(data)
    end = perf_counter()
    elapsed_time = end - start

    qs30_sort_times.append(elapsed_time)

for size in range(2):
    data = []
    while len(data) < size:
        data.append(random.randint(1, size*10))
    
    # compute elapsed time
    start = perf_counter()
    quick_sort50(data)
    end = perf_counter()
    elapsed_time = end - start

    qs50_sort_times.append(elapsed_time)

plt.plot(input_sizes, python_sort_times)#blue
plt.plot(input_sizes, merge_sort_times) #orange
plt.plot(input_sizes, selection_sort_times)#green
plt.plot(input_sizes, heap_sort_times)#red
#plt.plot(input_sizes, qs_sort_times) #q6. green line, blue line
#plt.plot(input_sizes, qs10_sort_times)#q6. orange line
#plt.plot(input_sizes, qs30_sort_times)#q6. green line
#plt.plot(input_sizes, qs50_sort_times) #q6. red line
plt.show()

