 # Convert Sorted Array to Binary Search Tree

Given an integer array nums where the elements are sorted in ascending order, convert it to a 
height-balancedb binary search tree.

 

### Example 1:
![btree1](https://github.com/ananya9177/Competitive-Coding/assets/151428838/bf9d1940-e73b-409a-9aba-fadd79b71564)

```
Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
```
**Explanation:**  [0,-10,5,null,-3,null,9] is also accepted:
![Uploading btree2.jpg…]()

### Example 2:
![btree](https://github.com/ananya9177/Competitive-Coding/assets/151428838/3de84fc8-c6c9-4b54-9bc6-b29c2386655f)

```
Input: nums = [1,3]
Output: [3,1]
```
**Explanation:** [1,null,3] and [3,1] are both height-balanced BSTs.



**Constraints:**

1 <= nums.length <= 104

-104 <= nums[i] <= 104

nums is sorted in a strictly increasing order.
