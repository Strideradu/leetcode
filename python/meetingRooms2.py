# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        times = []
        for interval in intervals:
            times.append((interval.start, 1))
            times.append((interval.end, 0))
            
        times.sort()
        available = 0
        rooms = 0
        for time in times:
            if time[1] == 1:
                if available > 0:
                    available -= 1
                elif (available == 0):
                    rooms += 1
            
            if time[1] == 0:
                available += 1
                
        return rooms