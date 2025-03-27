from collections import deque

def openLock(deadends,target):
    visited = set(deadends)
    queue = deque(['0000'])
    depth = -1

    if target in visited: return -1

    while(queue):
        size = len(queue)
        depth += 1
        for _ in range(size):
            q = queue.popleft()
            if q in visited: continue
            if q == target: return depth

            visited.add(q)
            queue.extend(get_combinations(q))
        

    return -1


def get_combinations(seq):
    all_seq = []
    for i, char in enumerate(seq):
        val = int(char)
        all_seq.append(seq[:i] + str((val-1)%10) + seq[i+1:])
        all_seq.append(seq[:i] + str((val+1)%10) + seq[i+1:])

    return all_seq

deadends = ["0201","0101","0102","1212","2002"]
target = "0202"
print(openLock(deadends, target))
# print(get_combinations('0000'))