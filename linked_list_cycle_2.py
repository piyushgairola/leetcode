def solution(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break

    else:   ## else clause will run only if the while loop terminates naturally without encountering a break statement
        return None ## Which means, there is no cycle in the linked list
    
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next

    return slow