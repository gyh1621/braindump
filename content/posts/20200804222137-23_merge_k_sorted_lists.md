+++
title = "23. Merge k Sorted Lists"
author = ["John Doe"]
draft = false
+++

tags
: [MergeSort]({{< relref "20200804222157-mergesort" >}}), [PriorityQueue]({{< relref "20200804222308-priorityqueue" >}})

source
: [leetcode](https://leetcode.com/problems/merge-k-sorted-lists/)


## Edge Cases {#edge-cases}


## Solution 1 - Merge one by one {#solution-1-merge-one-by-one}

start from first list, merge second, merge third...


### Complexity {#complexity}

-   time: O(kN), k is number of list, N is length of final list
-   space: O(1)


## Solution 2 - Priority Queue {#solution-2-priority-queue}

1.  create a priority queue
2.  put first element of every list into queue
3.  Until queue is empty:

    1.  pop an element
    2.  push the element's next one into queue

    so, queue will always have k elements

<!--listend-->

```python
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        head = point = ListNode(0)
        q = PriorityQueue()
        for l in lists:
            if l:
                q.put((l.val, l))
        while not q.empty():
            val, node = q.get()
            point.next = ListNode(val)
            point = point.next
            node = node.next
            if node:
                q.put((node.val, node))
        return head.next
```


### Complexity {#complexity}

-   time: O(log(k)N), k is number of list, N is length of final list
-   space: O(k)


## Solution 3 - Merge Sort {#solution-3-merge-sort}

```java
class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        if (lists == null || lists.length == 0) return null;
        return mergeSort(lists, 0, lists.length - 1);
    }

    private ListNode mergeSort(ListNode[] lists, int start, int end) {
        if (start == end) return lists[start];
        int mid = start + (end - start) / 2;
        ListNode left = mergeSort(lists, start, mid);
        ListNode right = mergeSort(lists, mid + 1, end);
        return merge(left, right);
    }

    private ListNode merge(ListNode left, ListNode right) {
        ListNode result = new ListNode(-1), curr = result;
        while (left != null && right != null) {
            if (left.val < right.val) {
                curr.next = left;
                left = left.next;
            } else {
                curr.next = right;
                right = right.next;
            }
            curr = curr.next;
        }
        curr.next = left == null ? right : left;
        return result.next;
    }
}
```


### Complexity {#complexity}

-   time: O(Nlog(k))
-   space: O(1)
