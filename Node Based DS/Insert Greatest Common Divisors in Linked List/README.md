# Insert Greatest Common Divisors in Linked List

Given the head of a linked list head, in which each node contains an integer value.

Between every pair of adjacent nodes, insert a new node with a value equal to the greatest common divisor of them.

Return the linked list after insertion.

The greatest common divisor of two numbers is the largest positive integer that evenly divides both numbers.

 
### Example 1:
![ex1_copy](https://github.com/ananya9177/PAT-CP/assets/151428838/a42a8406-380e-4979-8e24-02ffda858175)

```
Input: head = [18,6,10,3]
Output: [18,6,6,2,10,1,3]
```
**Explanation:** The 1st diagram denotes the initial linked list and the 2nd diagram denotes the linked list after inserting the new nodes (nodes in blue are the inserted nodes).
- We insert the greatest common divisor of 18 and 6 = 6 between the 1st and the 2nd nodes.
- We insert the greatest common divisor of 6 and 10 = 2 between the 2nd and the 3rd nodes.
- We insert the greatest common divisor of 10 and 3 = 1 between the 3rd and the 4th nodes.
There are no more adjacent nodes, so we return the linked list.


### Example 2:
![ex2_copy1](https://github.com/ananya9177/PAT-CP/assets/151428838/8b68eb01-9c13-4b5e-b3eb-33e4645b7573)

```
Input: head = [7]
Output: [7]
```
**Explanation:** The 1st diagram denotes the initial linked list and the 2nd diagram denotes the linked list after inserting the new nodes.
There are no pairs of adjacent nodes, so we return the initial linked list.
