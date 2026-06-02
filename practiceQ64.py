"""Reverse Even-Indexed Nodes and Append
Given a singly linked list, extract all even-indexed nodes, reverse their order, and append them to the end of the list in one traversal. Return the head of the modified list.

Example

Input

head = [10, 20, 30, 40, 50, 60]
Output

[20, 40, 60, 50, 30, 10]"""

def extractAndAppendSponsoredNodes(head):
    if head is None:
        return None

    D = []

    current = head
    prev = None
    count = 0

    
    while current:
        next_node = current.next

        if count % 2 == 0:
            D.append(current.data)

            if prev is None:      
                head = next_node
            else:
                prev.next = next_node
        else:
            prev = current

        current = next_node
        count += 1

    D.reverse()

    
    if head is None:
        head = None
        tail = None
    else:
        tail = head
        while tail.next:
            tail = tail.next

    
    for value in D:
        new_node = SinglyLinkedListNode(value)

        if head is None:
            head = new_node
            tail = new_node
        else:
            tail.next = new_node
            tail = new_node

    return head


head_count = int(input().strip())

head = SinglyLinkedList()

for _ in range(head_count):
    head_item = int(input().strip())
    head.insert_node(head_item)

result = extractAndAppendSponsoredNodes(head.head)

print_singly_linked_list(result, '\n')
print()