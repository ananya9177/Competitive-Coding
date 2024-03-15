# Next Greater Node In Linked List

You are given the head of a linked list with n nodes.

For each node in the list, find the value of the next greater node. That is, for each node, find the value of the first node that is next to it and has a strictly larger value than it.

Return an integer array answer where answer[i] is the value of the next greater node of the ith node (1-indexed). If the ith node does not have a next greater node, set answer[i] = 0.

 

### Example 1:
![linkedlistnext1](https://github.com/ananya9177/Competitive-Coding/assets/151428838/6d6531d0-51f2-47ee-9e1f-4233223ac92e)

```
Input: head = [2,1,5]
Output: [5,5,0]
```

### Example 2:
![linkedlistnext2](https://github.com/ananya9177/Competitive-Coding/assets/151428838/a19af292-8fdb-4497-83ff-847f06bb04ee)

```
Input: head = [2,7,4,3,5]
Output: [7,0,5,5,0]
```

**Constraints:**

The number of nodes in the list is n.

1 <= n <= 104

1 <= Node.val <= 109
