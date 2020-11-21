+++
title = "973. K Closest Points to Origin"
author = ["John Doe"]
draft = false
+++

Time-stamp: <2020-11-21 01:04:25 gyh"timestamp-wrapper"><span class="timestamp">&lt;2020-08-13 Thu 01:17&gt;</span></span>

tags
: [PriorityQueue]({{< relref "20200804222308-priorityqueue" >}}), [QuickSelect]({{< relref "20200805205651-quickselect" >}})

source
: [leetcode](https://leetcode.com/problems/k-closest-points-to-origin/)


## Edge Cases {#edge-cases}


## Solution 1 - priority queue {#solution-1-priority-queue}

1.  add one by one, reach size greater than K, drop one
    -   time: O(NlgK) + O(NlgK)
    -   space: O(N)

2.  build total, extract K
    -   time: O(N) + O(KlgN)
    -   space: O(N)


## Solution 2 - quick select {#solution-2-quick-select}

use quick select
if left partition's length(include pivot element) < K, keep sorting left part
else sort right part with (k - leftLength)

here leftLength must include pivot element
if problem is to find Kth smallest element, like [215. Kth Largest Element in an Array]({{< relref "20200805205618-215_kth_largest_element_in_an_array" >}}), then compare pivot with K

```java
class Solution {
    public int[][] kClosest(int[][] points, int K) {
        if (points.length <= K) return points;
        sortKClosest(points, 0, points.length - 1, K);
        return Arrays.copyOfRange(points, 0, K);
    }

    private void sortKClosest(int[][] points, int start, int end, int K) {
        int pivot = partition(points, start, end);
        int leftLength = pivot - start + 1;

        if (leftLength > K) sortKClosest(points, start, pivot, K);
        else if (leftLength < K) sortKClosest(points, pivot + 1, end, K - leftLength);

        return;
    }

    private int partition(int[][] points, int start, int end) {
        if (start == end) return start;
        int mid = start + (int) (Math.random() * (end - start + 1));
        swap(points, mid, end);

        double pivotV = disSquare(points[end]);

        int curPos = start;
        for (int i = start; i < end; i++) {
            double curV = disSquare(points[i]);
            if (curV <= pivotV) {
                swap(points, curPos, i);
                curPos++;
            }
        }

        swap(points, curPos, end);

        return curPos;
    }

    private void swap(int[][] points, int p1, int p2) {
        int[] tmp = points[p1];
        points[p1] = points[p2];
        points[p2] = tmp;
    }

    private double disSquare(int[] point) {
        return point[0] * point[0] + point[1] * point[1];
    }
}
```


### Complexity {#complexity}

-   time: O(N) on average
-   space: O(1)
