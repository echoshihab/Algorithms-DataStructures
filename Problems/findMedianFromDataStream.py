"""
The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.

For example, for arr = [2,3,4], the median is 3.
For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
Implement the MedianFinder class:

MedianFinder() initializes the MedianFinder object.
void addNum(int num) adds the integer num from the data stream to the data structure.
double findMedian() returns the median of all elements so far. Answers within 10^-5 of the actual answer will be accepted.

 

Constraints:

-10^5 <= num <= 10^5
There will be at least one element in the data structure before calling findMedian.
At most 5 * 104 calls will be made to addNum and findMedian.
"""


import heapq


class MedianFinder:

    def __init__(self):
        # two heaps one for larger values and one  for smaller values as in [1,2,3,4] -> small heap - [1,2], large heap = [3,4]
        # smaller values should be maxheap so that we can quickly get the largest value so that small heap becomes [2,1]
        # larger values should be minheap so that we can quickly get the smallest value so that large heap is [3,4]
        
        self.smallHeap = []
        self.largeHeap = []

    def addNum(self, num: int) -> None:
        
        heapq.heappush(self.smallHeap, -num)

        # make sure every element in small heap <= every element in large
        if self.smallHeap and self.largeHeap and -(self.smallHeap[0]) > self.largeHeap[0]:
            val = heapq.heappop(self.smallHeap)
            heapq.heappush(self.largeHeap, -(val))

        # handle uneven size - 2 or greater
        if len(self.smallHeap) > len(self.largeHeap) + 1:
            val = heapq.heappop(self.smallHeap)
            heapq.heappush(self.largeHeap, -(val))
        if len(self.largeHeap) > len(self.smallHeap) + 1:
            val = heapq.heappop(self.largeHeap)
            heapq.heappush(self.smallHeap, -val)

    def findMedian(self) -> float:
        if len(self.smallHeap) > len(self.largeHeap):
            return -(self.smallHeap[0])
        elif len(self.largeHeap) > len(self.smallHeap):
            return self.largeHeap[0]
        else:
            return (-(self.smallHeap[0]) + self.largeHeap[0])/2      
