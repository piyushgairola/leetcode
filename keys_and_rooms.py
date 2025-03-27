def canVisitAllRooms(rooms):
    visited = [0]
    stack = [0]

    while(stack):
        room = stack.pop()
        for key in rooms[room]:
            if key not in visited:
                visited.append(key)
                stack.append(key)

    if len(visited)==len(rooms):
        return True
    else:
        return False



if __name__ == '__main__':
    rooms = [[1,3],[3,0,1],[2],[0]]
    print(canVisitAllRooms(rooms))