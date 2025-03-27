import heapq

def maxPerformace(n,speed,efficiency,k):
    heap = []
    ans = -1
    speed_sum = 0

    for eff, sp in sorted(zip(efficiency,speed), reverse=True):
        if len(heap)<k:
            heapq.heappush(heap, sp)
            speed_sum += sp
        
        else:
            least_speed = heapq.heappushpop(heap, sp)
            speed_sum += (sp - least_speed)

        ans = max(ans, eff*speed_sum)

    return ans % (10**9 + 7)