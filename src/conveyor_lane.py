"""
HW03 — Conveyor Lane: Nearly-Sorted Packages

Implement sort_k_sorted(arr, k) -> list
"""
import heapq
def sort_k_sorted(arr, k):
    # TODO:
    # 1) Understand the k-near-sorted guarantee.
    # 2) Re-phrase: use a min-heap of size k+1.
    # 3) Identify inputs/outputs/vars.
    # 4) Break down: push first k+1; then for each next item: push, pop to output; finally drain heap.
    # 5) Pseudocode above.
    # 6) Write code.
    # 7) Debug with small arrays.
    # 8) Explain O(n log k).
    
    n = len(arr)
    if n == 0:
        return []

    if k >= n:
        k = n - 1
    
    output = []
    
    heap = arr[0 : k + 1]
    heapq.heapify(heap)

    for i in range(k + 1, n):
        smallest_item = heapq.heappushpop(heap, arr[i])
        output.append(smallest_item)

    while heap:
        output.append(heapq.heappop(heap))

    return output
