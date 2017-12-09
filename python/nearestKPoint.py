import heapq

def nearestK(points, k):
    pq = []
    for point in points:
        distance = point[0]**2 + point[1]**2
        heapq.heappush(pq, (-distance, point[0], point[1]))
        # heapq always build a min heap, pq[0] is the smallets number
        if len(pq) > k:
            heapq.heappop(pq)
        print('pq', pq)
        print(heapq.nlargest(k, pq))
    print(pq[0])
    return heapq.heappop(pq)