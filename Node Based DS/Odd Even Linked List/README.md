# Odd Even Linked List

Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

The first node is considered odd, and the second node is even, and so on.

Note that the relative order inside both the even and odd groups should remain as it was in the input.

You must solve the problem in O(1) extra space complexity and O(n) time complexity.

 

### Example 1:
![oddeven-linked-list](https://github.com/ananya9177/Competitive-Coding/assets/151428838/f01a68aa-b84b-4e36-a22a-9cc204a32589)

```
Input: head = [1,2,3,4,5]
Output: [1,3,5,2,4]
```
### Example 2:
![oddeven2-linked-list](https://github.com/ananya9177/Competitive-Coding/assets/151428838/d31e83d9-dc6a-45dc-b412-d88ba795f00b)

```
Input: head = [2,1,3,5,6,4,7]
Output: [2,3,6,7,1,5,4]
```

**Constraints:**

The number of nodes in the linked list is in the range [0, 104].

-106 <= Node.val <= 106
