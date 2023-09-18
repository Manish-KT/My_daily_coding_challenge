import heapq

# Input: Number of lists
n = int(input())

# Input: Number of elements in each list (Sorted)
global_list = []

for _ in range(n):
    global_list.append(list(map(int, input().split())))

final_list = []

# Create a min-heap to store tuples of (element, list_index, element_index)
min_heap = []

# Initialize the min-heap with the first element from each list
for i, lst in enumerate(global_list):
    if lst:
        heapq.heappush(min_heap, (lst[0], i, 0))

# Merge the lists using the min-heap
while min_heap:
    val, list_ind, element_ind = heapq.heappop(min_heap)
    final_list.append(val)

    if element_ind + 1 < len(global_list[list_ind]):
        next_tuple = (global_list[list_ind][element_ind + 1], list_ind, element_ind + 1)
        heapq.heappush(min_heap, next_tuple)

print(final_list)
