class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # if not intervals: return 0
        
        res = 0
        rooms = 0
        
        start = [ start for start, end in intervals ]
        end = [ end for start, end in intervals ]
        start.sort()
        end.sort()
        
        s, e = 0, 0
        while s < len(start) and e < len(end):
            if start[s] < end[e]:
                rooms += 1
                s += 1
            else:
                rooms -= 1
                e += 1
            res = max(res, rooms)
        return res

        
        #####################
        
        
        # first we have to figure out how to read interval data
        #  we can use the end of an interval and see if the beginning of another is before it
        # the min number of meeting rooms is equivalent to finding the max number overlapping intervals
        #  to do this, we can go through the list and count each time the end>begin, compare it with max
        #  likewise, we can also count each time begin>=end, subtract from count
        #  (since if a meeting ends same time another begins, they don't need another room)

        # We have to sort the end times since if we check the ending time based on
        #  the room interval starting time, then we could run into the issue where many
        #  intervals fall between but are not overlapping each other, resulting in a higher
        #  count than is needed. 
        # For example:
        #  1------------------------------100
        #   10--20 30--40  50----80 90--99 
        #   in the above example, we only need 2 rooms but if we check the ending time based on
        #   which room starts, then we will end up with 5 rooms
        #  we would have to extract the starting times and ending times separately
        #  then we would sort them both, and finally go through the whole check if
        #   ending>starting, etc        
        
        # We can store the times inside of a sorted list or min/max-heap

        # sortedlist
        if intervals is None: return None
        
        start = sorted([i[0] for i in intervals])
        end = sorted([i[1] for i in intervals])
        count, maxrooms, s, e = 0, 0, 0, 0
        
        # continue until one of them have no more
        # technicaly, we only need to check s since we will always get to end of start-list before end-list
        while (s<len(intervals) and e<len(intervals)):
            if start[s]<end[e]:
                s+=1
                count+=1
                maxrooms=max(count, maxrooms)
            else:
                e+=1
                count-=1
        
        return maxrooms
        
        
        ##############################
        # do this again, took awhile to get the right answer
        # it was a bit difficult since we had to keep track of both the start and end times
        # since we have to close meetings that are finished
        # return max overlapping meetings at once
        #  if a meeting is overlapping, iterate count and start
        #  if it's not overlapping, reduce count and iterate end
        # time: nlogn, we sort a couple times but then we iterate through all meetings at most twice
        # space: n, we keep a couple arrays for the start and end times
        
        
        if len(intervals) == 0: return 0
        if len(intervals) == 1: return 1
        
        startTimes = sorted([i[0] for i in intervals])
        endTimes = sorted([i[1] for i in intervals])
        n = len(intervals)
        start, end, count, maxRooms = 0, 0, 0, 0
        
        while start < n and end < n:
            if startTimes[start] < endTimes[end]:
                count += 1
                start += 1
                maxRooms = max(maxRooms, count)
            else:
                count -= 1
                end += 1
        return maxRooms