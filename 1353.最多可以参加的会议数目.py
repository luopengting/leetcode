# events = [[1,5], [2,3], [1,4], [1,6], [3, 5]]
# events.sort(reverse=True)
# print(events)
# [[3, 5], [2, 3], [1, 6], [1, 5], [1, 4]]
import heapq

class Solution(object):
    def maxEvents(self, events):
        """
        :type events: List[List[int]]
        :rtype: int
        """
        # sort by start time and end time.
        events.sort(reverse=True)
        heap = []
        count = 0
        for current_time in range(1, 100001):
            # find all possible join event,
            while events and events[-1][0] == current_time:
                event = events.pop()
                heapq.heappush(heap, event[1])
            # pick the shortest end time
            while heap:
                end_time = heapq.heappop(heap)
                # if the end time is less than current time `i`
                if end_time >= current_time:
                    count += 1
                    # find one
                    break
            if not events and not heap:
                break
        return count


if __name__ == "__main__":
    solution = Solution()

    events = [[1,2],[2,3],[3,4]]
    res = solution.maxEvents(events)
    assert 3 == res

    events = [[1,4],[4,4],[2,2],[3,4],[1,1]]
    res = solution.maxEvents(events)
    assert 4 == res
