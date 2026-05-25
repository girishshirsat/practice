"""One-Pass Removal of k-th Node from End
Given the head of a singly linked list and an integer k, remove the k-th node from the end in one traversal and return the new head. If k is invalid, return the original list.

Example

Input

head = [5, 6, 7, 8]
k = 3
Output

[6, 7, 8]"""





def removeKthNodeFromEnd(head, k):
    if head is None:
        return head

    length = 0
    curr = head
    while curr:
        length += 1
        curr = curr.next

    target = length - k - 1

    if target < 0 or target >= length:
        return head

    if target == 0:
        return head.next

    curr = head
    for i in range(target - 1):
        curr = curr.next

    curr.next = curr.next.next
    return head



head_count = int(input().strip())

head = SinglyLinkedList()

for _ in range(head_count):
    head_item = int(input().strip())
    head.insert_node(head_item)

k = int(input().strip())

result = removeKthNodeFromEnd(head.head, k)

print_singly_linked_list(result, '\n')
print()