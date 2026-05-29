"""Remove Consecutive Duplicates from Sorted Linked List
Write a function "deleteDuplicates" that removes consecutive duplicate nodes in-place, retaining only the first node of each code. Return the head of the resulting list.

Example

Input

head = [1, 2, 2, 2, 3, 4, 4, 5]
Output

[1, 2, 3, 4, 5]
Explanation

- Given 1→2→2→2→3→4→4→5. 
- Start at 1 (next is 2, no skip). 
- Move to 2; skip all consecutive 2's so that 2 links directly to 3 (removing two extra 2 nodes). 
- Now list is 1→2→3→4→4→5.
- Move to 3 (next is 4, no skip). 
- At 4, skip the duplicate 4 so it links to 5. 
- The resulting list is 1→2→3→4→5."""



def deleteDuplicates(head):
    if head is None:
        return head

    previous = head
    current = head.next

    while current:

        if previous.data == current.data:
            previous.next = current.next
            current = previous.next

        else:
            previous = current
            current = current.next

    return head
    

head_count = int(input().strip())

head = SinglyLinkedList()

for _ in range(head_count):
    head_item = int(input().strip())
    head.insert_node(head_item)

result = deleteDuplicates(head.head)

print_singly_linked_list(result, '\n')
print()